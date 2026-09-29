from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
root=Path(__file__).parent
rows=json.loads((root/'batch.json').read_text())
for i,m in enumerate(rows,1):
    if len(sys.argv)>1 and i not in {int(x) for x in sys.argv[1:]}:continue
    rd=Path(m['result_dir']);module=Path(m['module'])
    try:
        icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
        (rd/(m['icon_id']+'.svg')).write_text(svg)
        render_previews(svg,m['icon_id'],48,rd)
        (rd/'validation.txt').write_text(report.describe())
        g=gate(module);(rd/'gate.json').write_text(json.dumps(g,indent=2))
        print(i,m['icon_id'],report.status,g['status'],flush=True)
        for e in report.errors+report.warnings:print(' ',e,flush=True)
        for e in g['errors']+g['warnings']:print(' G',e,flush=True)
    except Exception as e: print(i,'ERROR',type(e).__name__,str(e),flush=True)
for page in range(2):
    sheet=Image.new('RGB',(1050,1000),'#eee');d=ImageDraw.Draw(sheet)
    for j,m in enumerate(rows[page*10:(page+1)*10]):
        x=j%2*525;y=j//2*200;rd=Path(m['result_dir']);d.text((x+8,y+5),f'{page*10+j+1}. {m["icon_id"]}',fill='black')
        for k,name in enumerate(['reference.png','preview-light-384.png','preview-dark-384.png']):
            p=rd/name
            if p.exists():sheet.paste(Image.open(p).convert('RGB').resize((144,144)),(x+8+k*165,y+25))
        for k,theme in enumerate(['light','dark']):
            p=rd/f'preview-{theme}-48.png'
            if p.exists():sheet.paste(Image.open(p).convert('RGB'),(x+420+k*50,y+148))
    sheet.save(root/f'candidate-{page+1}.png')
