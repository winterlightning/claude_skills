"""Native v2 text subs and side compositions; translations only, never height fitting."""
from __future__ import annotations
import argparse
import hashlib
import json
import xml.etree.ElementTree as ET
from pathlib import Path
from .workspace import REPO_ROOT, build_dist, output_lock
from .experiment_gallery import stage_preview_combinations

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)

def save_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, separators=(',', ':')) + '\n')

def glyph_map():
    result = {}
    for name in ('glyphs.json', 'glyphs-v2.json'):
        for glyph in json.loads((REPO_ROOT/'icon_set/typeface'/name).read_text())['glyphs']:
            if glyph['preferred']:
                result[glyph['character']] = glyph
    return result

def native_text(text, glyphs, tracking=4, line_gap=4):
    """Align native baselines, with exactly tracking units between ink boxes."""
    lines=[]
    for line in text.split('\n'):
        placements=[];cursor=0
        for character in line:
            g=glyphs[character]
            left,top,right,bottom=g['bounds']
            placements.append(dict(character=character,glyph_id=g['icon_id'],x=cursor+2-left,
                                   y=-g['baseline'],bounds=g['bounds'],paths=g['paths']))
            cursor+=right-left+4+tracking
        if not placements:
            raise ValueError('Empty text line')
        top=min(p['bounds'][1]+p['y']-2 for p in placements)
        bottom=max(p['bounds'][3]+p['y']+2 for p in placements)
        lines.append(dict(placements=placements,width=cursor-tracking,top=top,height=bottom-top))
    width=max(line['width'] for line in lines);height=sum(line['height'] for line in lines)+line_gap*(len(lines)-1)
    root=ET.Element(f'{{{NS}}}svg',dict(viewBox=f'0 0 {width:.12g} {height:.12g}',width=f'{width:.12g}',height=f'{height:.12g}',fill='none',stroke='currentColor',**{'stroke-width':'4','stroke-linecap':'round','stroke-linejoin':'round'}))
    ET.SubElement(root,f'{{{NS}}}title').text=text
    output=[];y=0
    for index,line in enumerate(lines):
        for p in line['placements']:
            dx=p['x']+(width-line['width'])/2;dy=p['y']+y-line['top']
            group=ET.SubElement(root,f'{{{NS}}}g',{'transform':f'translate({dx:.12g} {dy:.12g})'})
            for d in p['paths']:ET.SubElement(group,f'{{{NS}}}path',{'d':d})
            output.append(dict(character=p['character'],glyph_id=p['glyph_id'],line=index,scale=1,
                               translate=[dx,dy],ink_bounds=[p['bounds'][0]+dx-2,p['bounds'][1]+dy-2,p['bounds'][2]+dx+2,p['bounds'][3]+dy+2]))
        y+=line['height']+line_gap
    return ET.tostring(root,encoding='unicode')+'\n',width,height,output

def native_records(dist):
    file=Path(dist)/'text-native-v2/manifest.json'
    return json.loads(file.read_text())['icons'] if file.exists() else []

def engine_item(document, icon_id, family):
    """Measure exactly as the ordinary combination snapshot builder does."""
    import sys
    import tempfile
    from svgpathtools import parse_path
    sys.path.insert(0,str(REPO_ROOT/'icon_set/vendor/combination'))
    from box_combine import bbox, parse_segments
    engine_document=document
    if family=='text':
        # The shared engine reads path coordinates, not nested SVG transforms.
        # Bake translations only for its clearance input; restoration uses the
        # untouched source document below, retaining original glyph commands.
        source=ET.fromstring(document);flat=ET.Element(source.tag,source.attrib)
        for group in source:
            if group.tag.rsplit('}',1)[-1]!='g':continue
            dx,dy=map(float,group.get('transform').removeprefix('translate(').removesuffix(')').split())
            for path in group:
                ET.SubElement(flat,f'{{{NS}}}path',{'d':parse_path(path.get('d')).translated(complex(dx,dy)).d()})
        engine_document=ET.tostring(flat,encoding='unicode')
    with tempfile.TemporaryDirectory() as folder:
        file=Path(folder)/'input.svg';file.write_text(engine_document)
        bounds=bbox(parse_segments(file))
    view=list(map(float,ET.fromstring(document).get('viewBox').split()))
    item=dict(icon=icon_id,family=family,document=document,bounds=bounds,
              canvas=max(view[2],max(bounds[2]-bounds[0],bounds[3]-bounds[1])*48/44),
              canvas_width=view[2],canvas_height=view[3],sha256=hashlib.sha256(document.encode()).hexdigest())
    if family=='text':
        item.update(engine_document=engine_document,sizing_mode='typeface-native',sizing_kind='text',native_text=True,model_validation='pass')
    return item

def engine_pair(main_svg, sub_svg, position, main_id, sub_id, pair_id='native-text',concept='Native text'):
    return dict(id=pair_id,concept=concept,position=position,type='side',native_text=True,
                mains=[engine_item(main_svg,main_id,'solo')],subs=[engine_item(sub_svg,sub_id,'text')])

def compose(main_svg, sub_svg, position, main_id, sub_id):
    from .combination_experiment import render
    row=engine_pair(main_svg,sub_svg,position,main_id,sub_id)
    result=render({'id':row['id']},row=row)
    return result['svg']+'\n',result['canvas'],result['canvas']

def generate(dist, reviews=None):
    from .gallery import copy_originals
    from .combination_catalog import write_catalog
    from .side_components import refresh
    dist=Path(dist);gallery=dist/'gallery';spec=json.loads((REPO_ROOT/'icon_set/data/side-text-v2.json').read_text())
    glyphs=glyph_map();folder=dist/'text-native-v2';folder.mkdir(parents=True,exist_ok=True)
    records=[]
    for item in spec['icons']:
        document,w,h,placements=native_text(item['text'],glyphs,spec['tracking'],spec['line_gap'])
        uid='side-text-v2-'+item['source_id'];file=folder/(uid+'.svg');file.write_text(document)
        record=dict(icon_id=uid,key='text/'+uid,name=item['name'],description=item['text'],text=item['text'],family='text',profile='TEXT_NATIVE_V2',semantic_role='SUB',semantic_kind='text',composition_class='TEXT',canvas_size=max(w,h),canvas_width=w,canvas_height=h,geometry_policy='native-translation-only',tracking=4,line_gap=4,placements=placements,source_ids=item['source_ids'],original_sources=copy_originals([REPO_ROOT/item['source_path']],gallery),python_source=None,preview_url='../text-native-v2/'+file.name,svg_path=file.relative_to(dist).as_posix(),svg_sha256=hashlib.sha256(document.encode()).hexdigest(),author='user-supplied-typeface-v2',tags=['text','typeface v2','side sub'],aliases=[],keywords=[item['text']],category='text',style=dict(stroke_width=4,line_cap='round',line_join='round'),validation=dict(status='valid',errors=[],warnings=[],checks_run=['native glyph paths','translation only','4-unit character ink gap','4-unit stroke'],scope='Native typeface layout, not SUB32 geometric validation.'))
        records.append(record)
    save_json(folder/'manifest.json',dict(family='text',profile='TEXT_NATIVE_V2',icons=records,unresolved=spec['unresolved']))
    iconfile=gallery/'icons.json';catalog=json.loads(iconfile.read_text());keys={r['key'] for r in records}
    catalog['icons']=[r for r in catalog['icons'] if r['key'] not in keys]+records;save_json(iconfile,catalog)
    combinations=json.loads((gallery/'combinations.json').read_text());by_key={r['key']:r for r in catalog['icons']};by_source={s:r for r in records for s in r['source_ids']}
    output=dist/'compositions';output.mkdir(exist_ok=True);done=[];blocked=[];engine_rows=[];engine_results={}
    for pair in combinations['rows']:
        if pair['kind']!='side' or pair['sub_id'] not in by_source:continue
        sub=by_source[pair['sub_id']]
        candidates=[by_key[g['key']] for g in combinations['references'][pair['main_id']]['generated'] if g.get('key') in by_key and by_key[g['key']]['family'] in ('solo','combination_main') and (reviews or {}).get(g['key']) not in ('pending','rejected')]
        candidates=[r for r in candidates if r.get('validation',{}).get('status')=='valid' or r.get('model_validation')=='pass']
        if not candidates:
            blocked.append(dict(id=pair['id'],concept=pair['concept'],reason='No usable generated main icon',main_id=pair['main_id'],sub_source_id=pair['sub_id']));continue
        main=candidates[0];mainfile=(gallery/main['preview_url']).resolve();subfile=folder/(sub['icon_id']+'.svg')
        from .combination_experiment import render
        engine_row=engine_pair(mainfile.read_text(),subfile.read_text(),pair['position'],main['icon_id'],sub['icon_id'],pair['id'],pair['concept'])
        for item, record, path in ((engine_row['mains'][0], main, mainfile), (engine_row['subs'][0], sub, subfile)):
            item.update(family=record['family'], model_key=record['key'], svg=path.relative_to(REPO_ROOT).as_posix(), export_url=record['preview_url'])
        # A layout adjusted by hand on the side pairs page survives this rebuild.
        from .combination_layouts import active, load as load_layouts
        adjusted=active(engine_row,load_layouts().get(pair['id']))
        try:
            result=render({'id':pair['id'],**(adjusted or {})},row=engine_row)
        except ValueError:
            if not adjusted:
                raise
            result=render({'id':pair['id']},row=engine_row)
        document=result['svg']+'\n';w=h=result['canvas']
        engine_row.update(canvas_width=w,canvas_height=h)
        engine_rows.append(engine_row)
        uid='side-text-v2-'+pair['id'];(output/(uid+'.svg')).write_text(document)
        metadata=dict(icon_id=uid,source_pair_id=pair['id'],name=pair['concept'],composition_class='SIDE_COMBINE',geometry_policy='shared-convex-hull-native-text',canvas_width=w,canvas_height=h,position=pair['position'],children=[dict(icon_id=main['icon_id'],svg_sha256=main['svg_sha256']),dict(icon_id=sub['icon_id'],svg_sha256=sub['svg_sha256'])])
        save_json(output/(uid+'.json'),metadata)
        engine_results[pair['id']]=dict(url='../compositions/'+uid+'.svg',result=result)
        print('Combined with shared engine: '+pair['concept'],flush=True)
        done.append(dict(id=pair['id'],concept=pair['concept'],sub_source_id=pair['sub_id'],preview_url='../compositions/'+uid+'.svg',main_key=main['key'],canvas_width=w,canvas_height=h))
    # Feed the same pair snapshots and preview cache used by every side icon.
    for path,key,values in [(REPO_ROOT/'icon_set/data/combination-pairs.json','rows',engine_rows)]:
        data=json.loads(path.read_text());ids={r['id'] for r in values}
        data[key]=[r for r in data[key] if r['id'] not in ids]+values
        save_json(path,data);save_json(gallery/'experiment-combination.json',data)
    cache_path=REPO_ROOT/'icon_set/data/combination-previews.json'
    cache=json.loads(cache_path.read_text());cache.update(engine_results)
    save_json(cache_path,cache);save_json(gallery/'experiment-combination-results.json',dict(results=cache))
    report=dict(generated_subs=len(records),generated_pairs=len(done),pairs=done,blocked=blocked,unresolved=spec['unresolved'])
    save_json(gallery/'side-text-v2.json',report)
    stage_preview_combinations(gallery)
    write_catalog(gallery,json.loads((gallery/'primitives.json').read_text()),catalog['icons'])
    refresh(gallery)
    print(json.dumps({k:v for k,v in report.items() if k!='pairs'},indent=2))
    return report

def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--dist',type=Path,default=build_dist());parser.add_argument('--reviews',type=Path,required=True,help='Review-status JSON fetched from the target gallery /api/reviews')
    args=parser.parse_args(argv)
    with output_lock(args.dist):generate(args.dist,json.loads(args.reviews.read_text()) if args.reviews else {})
    return 0

if __name__=='__main__':raise SystemExit(main())
