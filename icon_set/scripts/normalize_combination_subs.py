"""Refresh every inventoried non-text sub export without changing original models."""
import hashlib,json
from pathlib import Path
from .sub_ink32 import normalize_ink32

if __package__:
    from .workspace import development_dist
else:
    from workspace import development_dist

ROOT=Path(__file__).resolve().parents[2]

def run():
    inventory=json.loads((ROOT/'icon_set/work/combination-sub-review/inventory.json').read_text())
    folder=ROOT/'icon_set/assets/combination-sub32';public=development_dist(ROOT) / 'gallery/combination-sub32'
    folder.mkdir(exist_ok=True);public.mkdir(exist_ok=True)
    manifest_path=ROOT/'icon_set/data/combination-sub32.json'
    manifest=json.loads(manifest_path.read_text());results={}
    repair_path=ROOT/'icon_set/data/sub-text-repairs.json'
    repairs=json.loads(repair_path.read_text()) if repair_path.exists() else {}
    icon_repairs=ROOT/'icon_set/data/sub-icon-repairs.json'
    if icon_repairs.exists():repairs.update(json.loads(icon_repairs.read_text()))
    # Compute the whole batch before replacing any exports.
    for key,a in inventory['assets'].items():
        # Text uses height-only fitting with a free-width integer grid.
        source=ROOT/a['source_path'];document=source.read_text();repair=repairs.get(key)
        if repair:
            normalized=(ROOT/repair['repair_svg']).read_text();metrics=repair['ink32']
        else:normalized,metrics=normalize_ink32(document,text=a['family']=='text')
        family,icon=key.split('/',1);name=family+'--'+icon+'.svg'
        record=dict(icon=icon,family=family,source_svg=a['source_path'],svg=str((folder/name).relative_to(ROOT)),export_url='combination-sub32/'+name,source_sha256=hashlib.sha256(document.encode()).hexdigest(),ink32=metrics)
        if repair:record.update(repair_svg=repair['repair_svg'],sizing_kind='symbol' if repair['symbol'] else 'text',repair_text=repair['text'])
        results[key]=(record,normalized)
    for key,(record,document) in results.items():
        (ROOT/record['svg']).write_text(document);(public/Path(record['svg']).name).write_text(document)
        manifest[record['icon']]=record
    manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
    # Pair inputs use the exact same derived SVGs and measured centerline bounds.
    pairs_path=ROOT/'icon_set/data/combination-pairs.json';pairs=json.loads(pairs_path.read_text())
    for row in pairs['rows']:
        for item in row['subs']:
            key=item['family']+'/'+item['icon']
            if key not in results:continue
            record,document=results[key];item.setdefault('source_bounds',item['bounds'])
            item.update(record,document=document,sha256=hashlib.sha256(document.encode()).hexdigest(),bounds=record['ink32']['bounds'],canvas=32,export_size=32,sub32_status='ink32_normalized',sub32_reason='Grid-snapped derived geometry; visual review required. Text uses height-only fitting.')
    pairs_path.write_text(json.dumps(pairs));(development_dist(ROOT) / 'gallery/experiment-combination.json').write_text(json.dumps(pairs))
    catalog_path=development_dist(ROOT) / 'gallery/combinations.json';catalog=json.loads(catalog_path.read_text())
    for row in catalog['rows']:
        row['sub_exports']=[manifest[g['icon_id']] for g in catalog['references'][row['sub_id']]['generated'] if g['icon_id'] in manifest and not g['key'].startswith('text/')]
    catalog_path.write_text(json.dumps(catalog,separators=(',',':'))+'\n')
    report={'count':len(results),'rule':'Icons: 1-unit grid, maximum ink dimension 32, stroke 4. Text: ink height 32, free width, 1-unit grid.','icons':{k:v[0]['ink32'] for k,v in results.items()}}
    (ROOT/'icon_set/work/combination-sub-review/normalization.json').write_text(json.dumps(report,indent=2)+'\n')
    from .deduplicate_subs import run as deduplicate_subs
    deduplicate_subs()
    print('Normalized',len(results),'combination artworks.')
if __name__=='__main__':run()
