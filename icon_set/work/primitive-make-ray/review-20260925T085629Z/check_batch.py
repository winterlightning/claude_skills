from pathlib import Path
import sys,json,io
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
import cairosvg
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent
rows=json.loads((root/('extra-runs.json' if '--extra' in sys.argv else 'runs.json')).read_text())
for row in rows:
    out=Path(row['run']); module=Path(row['module'])
    icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
    (out/f'{icon.icon_id}.svg').write_text(svg)
    (out/'validation.txt').write_text(report.describe())
    render_previews(svg,icon.icon_id,48,out)
    for size in (48,192):
        cairosvg.svg2png(url=str(out/'reference.svg'),write_to=str(out/f'reference-{size}.png'),output_width=size,output_height=size)
    result=gate(module)
    (out/'gate.json').write_text(json.dumps(result,indent=2))
    print(icon.icon_id,report.status,result['status'],flush=True)
    for v in list(report.errors)+list(report.warnings)+result['errors']+result['warnings']:print(' ',v[:600],flush=True)
for page in range((len(rows)+6)//7):
    group=rows[page*7:(page+1)*7];im=Image.new('RGB',(850,len(group)*185),'#e5e5e5');draw=ImageDraw.Draw(im)
    for i,row in enumerate(group):
        out=Path(row['run']);draw.text((4,i*185+2),row['key'],fill='black')
        for x,name,size in [(5,'reference-192.png',150),(170,'preview-light-384.png',150),(330,'preview-light-48.png',48),(420,'preview-dark-384.png',150),(580,'preview-dark-48.png',48)]:
            a=Image.open(out/name).convert('RGBA');a=a.resize((size,size));im.paste(a,(x,i*185+25),a)
    im.save(root/f"{'extra-' if '--extra' in sys.argv else ''}candidate-{page}.png")
