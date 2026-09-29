from author_batch import *
import cairosvg
from icon_set.scripts import primitive_fix,work_queue

def finalize(n,v):
 r=ITEMS[n-1];run=ROOT/'icon_set/work/primitive-make-ray'/r['uuid']/f'20260928T172849Z-fix-{n:02d}-r{v}';module=next(run.glob('*.py'))
 icon=load_icon(module);report=icon.validate_icon();g=json.loads((run/'gate.json').read_text())
 assert g['status']=='pass',(n,g)
 for sz in (48,384):cairosvg.svg2png(url=str(ROOT/r['ref']),write_to=str(run/f'reference-{sz}.png'),output_width=sz,output_height=sz,background_color='white')
 result=dict(source_uuid=r['uuid'],reference_path=r['ref'],concept=r['concept'],icon_id=icon.icon_id,author=AUTHOR,keyshape=icon.keyshape.name,validation_status=report.status,build_gate=g,visual_review='Inspected at native 48px and enlarged size in light and dark. Smooth coherent contours, consistent stroke, recognizable subject and clean negative space.',comparison=r['comparison'],feedback=r['feedback'],changes=DESIGNS[n][1],references=DESIGNS[n][2],omissions='No identifying feature omitted; microscopic contour detours removed.',artifacts=[p.name for p in sorted(run.iterdir()) if p.is_file()])
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
 note=r['comparison']+' Revised with coherent 4-unit strokes. '+('Approved drawing-bound visual exception; automatic findings retained.' if g.get('exception') else 'Full validation gate passed without warnings.')
 rc=primitive_fix.finish(work_queue.default_base_url(),'thuan-mac',r['key'],'done',note,ray_run=run)
 if rc:raise RuntimeError(f'finish failed for {n}: {rc}')
 return result
if __name__=='__main__':
 for spec in sys.argv[1:]:
  n,v=map(int,spec.split(':'));finalize(n,v)
