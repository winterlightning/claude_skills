"""Validate and render local runs without changing shared catalogs."""
import sys,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
HERE=Path(__file__).parent
rows=json.loads((HERE/'batch.json').read_text())
sheet=Image.new('RGB',(1120,len(rows)*145),'#ddd');draw=ImageDraw.Draw(sheet)
for i,row in enumerate(rows):
    run=Path(row['run']);module=Path(row['module']);icon=load_icon(module)
    svg=icon.to_svg();report=icon.validate_icon()
    (run/f'{icon.icon_id}.svg').write_text(svg);(run/'validation.txt').write_text(report.describe())
    render_previews(svg,icon.icon_id,48,run)
    g=gate(module);(run/'gate.json').write_text(json.dumps(g,indent=2)+'\n')
    print(i,report.status,g['status'],g['errors'][:2],g['warnings'][:2],flush=True)
    draw.text((5,i*145+8),f'{i}: '+row['key'],fill='black')
    for j,p in enumerate([run/'reference.png',run/'preview-light-384.png',run/'preview-dark-384.png']):
        b=Image.open(p).convert('RGBA').resize((128,128));sheet.paste(b,(570+j*160,i*145+10),b)
    for j,theme in enumerate(['light','dark']):sheet.paste(Image.open(run/f'preview-{theme}-48.png'),(1050,i*145+15+j*65))
sheet.save(HERE/'refined.png')
