from pathlib import Path
import json,sys,subprocess
sys.path.insert(0,str(Path.cwd()))
from icon_set.scripts.primitive_fix import load_icon
batch=Path('icon_set/work/primitive-fix-thuan/batch-20260924-thuan-mac')
rows=json.loads((batch/'runs.json').read_text())
notes=[
'Curved the palm frond and citron stem and smoothed the citron outline while preserving the botanical bundle.',
'Rebuilt the blocky handle with a rounded tilted contour and replaced the squared blade with a broader toothed outline.',
'Restored the long hanging thread, shortened the abdomen and arranged all eight legs in mirrored pairs.',
'Smoothed the skull-to-forehead transition and nose; rebuilt the smile and rounded jaw.',
'Replaced the kinked forehead and rear-neck transition with coherent curves; retained separated throat passages.',
'Smoothed the forehead and nose transition and rebalanced the rounded jaw and neck.',
'Rebuilt the mask as a curved face-covering with a rising strap and shared seam nodes; removed the crowded eye.',
'Restored shoulders above a trapezoidal deck, preserved the exact head-to-shoulder gap and spaced the platter dots.',
'Restored the reference right-facing smooth muzzle and swept quills in place of the jagged star-like silhouette.',
'Rebalanced the almond eye to a flatter horizontal envelope and smoothed all four contour sections.',
'Rebuilt the leaf with flowing curves and a pointed tip, with the cord and vein joining the same tip.',
'Rebuilt the mane, muzzle, belly and tail with natural curves in place of the squared silhouette.',
'Rounded the rear trigger, flared nozzle and grip while keeping the three water strokes evenly separated.',
'Rebuilt the bowl and kidney bean with coherent curves and replaced the cramped steam fragments with smooth wisps.',
'Rounded the roast silhouette and snout, retained the pig ear and opened the steam clearance above a tapered plate.',
'Rounded the scan frame, forehead, chin and rear neck, replacing the stepped facial contour.',
'Rounded the stock shoulder and grip transition while preserving the diagonal barrel and front sight.',
'Restored a semicircular pod rear and flowing nose/window contour in a horizontal envelope.',
'Replaced the squared thumb with a curved diagonal thumb and smoothed the palm transition.',
'Removed the angular inner kink and made the two overlapping loops symmetric with coherent arc flow.'
]
for row,note in zip(rows,notes):
 out=Path(row['run']);icon=load_icon(row['module']);report=icon.validate_icon()
 assert report.status=='valid' and not report.errors and not report.warnings
 meta=json.loads((out/(row['icon_id']+'.metadata.json')).read_text())
 if row['icon_id']=='headphone-wearing-dj-behind-two-turntables':meta['omissions']='Platters reduced to two spaced dots; shoulders restored. Exact head bottom y16 to shoulder top y24 gives 4-unit ink gap.'
 meta.update(revision_note=note,visual_review='Reviewed original and rejected SVG, then native 48px and enlarged previews in light and dark. Smooth contour flow, readable defining silhouette and open negative spaces; directional asymmetry follows the source.',validation_status=report.status,validation_errors=[],validation_warnings=[],artifacts=[p.name for p in out.iterdir() if p.is_file() and p.name!='result.json'])
 (out/(row['icon_id']+'.metadata.json')).write_text(json.dumps(meta,indent=2)+'\n')
 (out/'result.json').write_text(json.dumps(meta,indent=2)+'\n')
 row['note']=note
 # Each finish validates again, uploads before/after evidence and returns this exact claim to Ready.
 cmd=['python3','icon_set/scripts/primitive_fix.py','--worker','thuan-mac','finish','--icon',row['key'],'--run',row['run'],'--outcome','done','--note',note]
 result=subprocess.run(cmd,text=True,capture_output=True)
 (out/'finish.log').write_text(result.stdout+result.stderr)
 print(result.stdout+result.stderr,flush=True)
 if result.returncode:raise SystemExit(result.returncode)
 row['outcome']='done';row['status']='valid, 0 errors, 0 warnings'
(batch/'completed.json').write_text(json.dumps(rows,indent=2)+'\n')
report=['# Bad-stroke fix batch — thuan-mac','', '20 claimed; 20 done and returned to Ready. Every revision is valid with zero errors and zero warnings.','', 'Feedback for every claim: **Bad stroke drawn**. Author: `gpt-6`.','', '[Light/dark reference comparison](review.png)','']
for r in rows:
 out=Path(r['run']).resolve()
 report += [f"## {r['key']}",'',f"Feedback: {r['feedback']}",'',r['note'],'',f"Keyshape: {r['keyshape']}. {r['plan']}",'',f"Construction reference: {r['construction_reference']}",'',f"Omissions: {json.loads((out/'result.json').read_text())['omissions']}",'',f"Validation: **valid · 0 errors · 0 warnings**. Reported outcome: **done → Ready**.",'',f"[RESULT_DIR]({out}) · [SVG]({out / (r['icon_id']+'.svg')}) · [Production finish record]({Path(r['fix_dir']).resolve()/'result.json'})",'']
(batch/'REPORT.md').write_text('\n'.join(report))
print('Completed 20/20; report:',batch/'REPORT.md',flush=True)
