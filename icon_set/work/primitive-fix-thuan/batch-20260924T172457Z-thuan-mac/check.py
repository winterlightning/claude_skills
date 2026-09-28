import json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts.primitive_fix import load_icon,run_module,render_previews
from icon_set.scripts.build_gate import gate
ROOT=Path(__file__).resolve().parent
rows=json.loads((ROOT/'batch.json').read_text())
for row in rows:
 
 if not row['result_dir']:continue
 run=Path(row['result_dir'])
 if not list(run.glob('*.py')) or len(sys.argv)>1 and row['icon_id'] not in sys.argv[1:]:continue
 try:
  f=run_module(run);icon=load_icon(f);report=icon.validate_icon();g=gate(f)
  svg=icon.to_svg();(run/(row['icon_id']+'.svg')).write_text(svg)
  render_previews(svg,row['icon_id'],48,run)
  (run/'validation.txt').write_text(report.describe()+'\nBUILD GATE\n'+json.dumps(g,indent=2))
  (run/'checks.json').write_text(json.dumps(dict(validation_status=report.status,errors=report.errors,warnings=report.warnings,build_gate=g),indent=2))
  print(row['icon_id'],report.status,g,flush=True)
 except Exception as e: print(row['icon_id'],'ERROR',repr(e),flush=True)
