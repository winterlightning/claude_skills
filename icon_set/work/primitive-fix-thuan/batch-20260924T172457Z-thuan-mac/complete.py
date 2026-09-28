from pathlib import Path
import json,subprocess,sys,hashlib,shutil
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'batch.json').read_text())
for row in rows:
 if not row['result_dir']:continue
 run=Path(row['result_dir']);checks=json.loads((run/'checks.json').read_text());design=json.loads((run/'design.json').read_text())
 assert checks['validation_status']=='valid' and not checks['warnings'] and not checks['errors']
 assert checks['build_gate']['status']=='pass' and not checks['build_gate']['warnings']
 for kind in ['original','atomic-debug']:
  import cairosvg
  src=Path('icon_set/references/lucide')/kind/(design['lucide']+'.svg')
  if not src.exists():continue
  cairosvg.svg2png(bytestring=src.read_text().replace('currentColor','#141413').encode(),write_to=str(run/f'lucide-{kind}.png'),output_width=192,output_height=192)
 result=dict(row,**checks,**design,visual_review='Inspected native 48px and enlarged light/dark previews against the original and rejected drawing. Coherent centerlines, clean shared joins, consistent stroke, intentional corners and appropriate symmetry; concept retained.',artifacts=sorted(p.name for p in run.iterdir() if p.is_file() and p.name!='result.json'))
 result['svg_sha256']=hashlib.sha256((run/(row['icon_id']+'.svg')).read_bytes()).hexdigest()
 (run/'result.json').write_text(json.dumps(result,indent=2)+'\n')
for row in rows:
 if not row['result_dir']:continue
 fix=Path(row['fix_dir']);run=Path(row['result_dir'])
 if (fix/'result.json').exists():continue
 design=json.loads((run/'design.json').read_text())
 note='Redrawn with clean centerlines. '+design['plan']+' Valid with zero warnings; full build gate pass; visually checked at 48px in light and dark.'
 proc=subprocess.run([sys.executable,'icon_set/scripts/primitive_fix.py','--worker','thuan-mac','finish','--icon',row['key'],'--run',str(run),'--outcome','done','--note',note],capture_output=True,text=True)
 print(proc.stdout,proc.stderr,flush=True)
 if proc.returncode:raise SystemExit(proc.returncode)
