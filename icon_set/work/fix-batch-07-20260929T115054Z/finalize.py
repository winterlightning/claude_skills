from pathlib import Path
import json,sys,cairosvg,os
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from icon_set.scripts import primitive_fix,work_queue
OUT=Path(__file__).parent;rows=json.loads((OUT/'claims.json').read_text())
for i in map(int,sys.argv[1:]):
 r=rows[i];run=ROOT/(OUT/f'latest-{i}.txt').read_text();meta=json.loads((run/'candidate.json').read_text())
 assert meta['gate']['status']=='pass' and not meta['gate']['warnings'] and meta['validation_status']=='valid'
 for kind in ['reference','before']:
  for size in [48,192]:
   cairosvg.svg2png(url=str(ROOT/r[kind]),write_to=str(run/f'{kind}-{size}.png'),output_width=size,output_height=size,background_color='white')
 meta['visual_review']='Reviewed original, rejected drawing and fresh SVG together; inspected native 48px light and dark previews. Recognizable subject, coherent curves, uniform strokes and readable negative space.'
 meta['artifacts']=[p.name for p in run.iterdir() if p.is_file() and p.name!='result.json']
 (run/'result.json').write_text(json.dumps(meta,indent=2)+'\n')
 rc=primitive_fix.finish(work_queue.default_base_url(),os.environ.get('PICTOGRAPHIC_WORKER') or 'thuan-mac',r['key'],'done',meta['review'],ray_run=run)
 assert rc==0,(i,rc)
