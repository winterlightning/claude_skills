import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.model.icons.registry import create
from icon_set.scripts.workspace import build_dist
W=Path(__file__).parent
root=build_dist()
manifest=json.loads((root/'solo48/manifest.json').read_text())
rows={r['icon_id']:r for r in manifest['icons']}
results={}
for id in json.loads((W/'icon-ids.json').read_text()):
 assert id in rows,id+' missing from manifest'
 svg=root/'solo48'/f'{id}.svg'
 assert svg.is_file(),str(svg)
 x=create(id)
 assert svg.read_text()==x.to_svg(),id+' export differs from original'
 results[id]={'manifest':rows[id],'svg':str(svg)}
 print(id,'export verified')
(W/'exports.json').write_text(json.dumps(results,indent=2))
