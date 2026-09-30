import json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
REPO=ROOT.parents[2]
sys.path.insert(0,str(REPO))
from icon_set.scripts.primitive_fix import load_icon,run_module,render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
rows=json.loads((ROOT/'batch.json').read_text())
for row in rows:
    if len(sys.argv)>1 and row['icon_id'] not in sys.argv[1:]:continue
    run=REPO/row['run'];module=run_module(run)
    try:
        icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
        (run/(row['icon_id']+'.svg')).write_text(svg)
        (run/'validation.txt').write_text(report.describe())
        render_previews(svg,row['icon_id'],48,run)
        qa=gate(module)
        record={'validation_status':report.status,'errors':list(report.errors),'warnings':list(report.warnings),'build_gate':qa}
        (run/'checks.json').write_text(json.dumps(record,indent=2))
        print(row['icon_id'],json.dumps(record),flush=True)
    except Exception as e: print(row['icon_id'],type(e).__name__,str(e),flush=True)
for start in range(0,len(rows),5):
    sheet=Image.new('RGB',(850,5*205),'#e8e8e8');d=ImageDraw.Draw(sheet)
    for j,row in enumerate(rows[start:start+5]):
        run=REPO/row['run'];y=j*205
        d.text((8,y+3),str(start+j+1)+' '+row['icon_id'],fill='black')
        for k,name in enumerate(['reference.png','before.png','preview-light-384.png','preview-dark-384.png']):
            p=run/name
            if p.exists():sheet.paste(Image.open(p).convert('RGB').resize((144,144)),(k*190+8,y+25))
        for k,theme in enumerate(['light','dark']):
            p=run/f'preview-{theme}-48.png'
            if p.exists():sheet.paste(Image.open(p).convert('RGB'),(k*65+700,y+145))
    sheet.save(ROOT/f'after-{start//5+1}.png')
