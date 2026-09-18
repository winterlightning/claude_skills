"""Link pair choices to their independent sub models, including review drafts.

Draft artwork is staged outside release sub32; its validation state is explicit.
Original source IDs and many-to-one profile references remain unchanged.
"""
import hashlib
import json
from pathlib import Path
from icon_set.model.icons.registry import create
from icon_set.validation.envelope import centerline_bounds, visible_bounds
from icon_set.scripts.workspace import development_dist

ROOT=Path(__file__).resolve().parents[2]


def stage_catalog(catalog, root=ROOT):
    data=root/'icon_set/data'
    path=data/'sub-profile-aliases.json'
    if not path.exists():return
    mapping=json.loads(path.read_text())
    models=json.loads((data/'canonical-sub32.json').read_text())
    for row in catalog['rows']:
        choices=[];exports=[];seen=set()
        for old in row.get('sub_generated',catalog['references'][row['sub_id']]['generated']):
            uid=mapping.get(old['icon_id']);record=models.get(uid)
            if not record or record.get('family')!='sub':
                key=old['key'];choice=old
            else:
                key='sub/'+uid
                choice=dict(icon_id=uid,key=key,preview_url=record['export_url'],model_validation=record.get('model_validation','not-run'))
            if key in seen:continue
            seen.add(key);choices.append(choice)
            if record:exports.append(record)
        row['sub_generated']=choices
        if exports:row['sub_exports']=exports


def run(root=ROOT):
    data=root/'icon_set/data';gallery=development_dist(root) / 'gallery'
    path=data/'sub-profile-migration.json'
    if not path.exists():return
    migration=json.loads(path.read_text())['icons']
    aliases=json.loads((data/'sub-deduplication.json').read_text())['aliases']
    qa_path=root/'icon_set/work/sub-profile-migration/qa.json'
    qa=json.loads(qa_path.read_text()) if qa_path.exists() else {}
    folder=root/'icon_set/assets/sub-profiles';folder.mkdir(exist_ok=True)
    public=gallery/'sub-profiles';public.mkdir(exist_ok=True)
    published={}
    for manifest_path in (development_dist(root) / 'sub32/manifest.json', development_dist(root) / 'failed/sub32/manifest.json'):
        if manifest_path.exists():
            for item in json.loads(manifest_path.read_text()).get('icons',[]):
                published[item['icon_id']]=item
    models={};mapping={} 
    for original,entry in migration.items():
        uid=entry['model_key'].split('/',1)[1];icon=create(uid)
        document=icon.to_svg();bounds=list(centerline_bounds(icon.draw().primitives));ink=list(visible_bounds(icon.draw().primitives, radius=icon.STROKE_WIDTH / 2))
        name=uid+'.svg';file=folder/name;file.write_text(document);(public/name).write_text(document)
        digest=hashlib.sha256(document.encode()).hexdigest()
        status=qa.get(uid,{}).get('status','not-run') if qa.get(uid,{}).get('svg_sha256')==digest else 'stale-validation'
        built=published.get(uid,{})
        if built.get('svg_sha256')==digest:
            status='pass' if built.get('validation',{}).get('status') in ('valid','human-selected') else built.get('status',status)
        from icon_set.model.icons.sub._text_base import canvas_dimensions
        width,height=canvas_dimensions(icon)
        record=dict(icon=uid,family='sub',model_key='sub/'+uid,python_source=entry['python_source'],
                    source_svg=entry['reference_export'],svg=str(file.relative_to(root)),export_url='sub-profiles/'+name,
                    document=document,sha256=hashlib.sha256(document.encode()).hexdigest(),bounds=bounds,canvas=32,export_size=32,
                    canvas_width=width,sizing_kind='text' if getattr(icon,'sizing_mode',None)=='text-height32' else 'symbol',
                    sub32_status='native_sub32' if status=='pass' else 'needs_review',
                    sub32_reason='' if status=='pass' else 'Independent Python model; geometry QA requires review. See model_validation.',
                    model_validation=status,profile_sources=entry['sources'],
                    ink32=dict(bounds=bounds,ink_bounds=ink,ink_width=ink[2]-ink[0],ink_height=ink[3]-ink[1],canvas=32,canvas_width=width,stroke=icon.STROKE_WIDTH,grid=1))
        models[uid]=record;mapping[original]=uid;mapping[uid]=uid
        for prior_key in entry.get("previous_model_keys", []):
            mapping[prior_key.split("/", 1)[1]]=uid
    for alias,canonical in aliases.items():
        if canonical in mapping:mapping[alias]=mapping[canonical]
    pairs_path=data/'combination-pairs.json';pairs=json.loads(pairs_path.read_text());changed=0
    for row in pairs['rows']:
        items=[];seen=set()
        for old in row['subs']:
            uid=mapping.get(old['icon'])
            if uid is None:raise ValueError('Sub outside migrated inventory: '+old['icon'])
            if uid in seen:continue
            seen.add(uid);items.append(models[uid])
        if row['subs']!=items:changed+=1
        row['subs']=items
    payload=json.dumps(pairs);pairs_path.write_text(payload);(gallery/'experiment-combination.json').write_text(payload)
    catalog_path=gallery/'combinations.json'
    if catalog_path.exists():
        catalog=json.loads(catalog_path.read_text())
        for row in catalog['rows']:
            choices=[];exports=[];seen=set()
            for old in catalog['references'][row['sub_id']]['generated']:
                uid=mapping.get(old['icon_id']);key='sub/'+uid if uid else old['key']
                if key in seen:continue
                seen.add(key)
                if uid:
                    record=models[uid];choices.append(dict(icon_id=uid,key=key,preview_url=record['export_url'],model_validation=record['model_validation']))
                    exports.append({k:v for k,v in record.items() if k!='document'})
                else:choices.append(old)
            row['sub_generated']=choices;row['sub_exports']=exports
        catalog_path.write_text(json.dumps(catalog,separators=(',',':'))+'\n')
    compact={uid:{k:v for k,v in r.items() if k!='document'} for uid,r in models.items()}
    (data/'canonical-sub32.json').write_text(json.dumps(compact,indent=2)+'\n')
    (data/'sub-profile-aliases.json').write_text(json.dumps(mapping,indent=2)+'\n')
    print('Activated',len(models),'sub profile models;',changed,'pair rows refreshed',flush=True)
    return compact

if __name__=='__main__':run()
