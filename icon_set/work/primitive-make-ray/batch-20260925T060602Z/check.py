from pathlib import Path
import sys,json,io
sys.path.insert(0,str(Path(__file__).resolve().parents[4]))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
import cairosvg
SOURCE_ICON_ID=None
SOURCE_PATH=None
AUTHOR='gpt-6'
BATCH=Path(__file__).parent
items=json.loads((BATCH/'items.json').read_text())
selected=list(map(int,sys.argv[1:])) or list(range(20))
for i in selected:
    item=items[i];run=Path(item['run']);module=Path(item['module'])
    try:
        icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
        (run/(item['id']+'.svg')).write_text(svg)
        render_previews(svg,item['id'],48,run)
        for size in (48,192):
            cairosvg.svg2png(url=item['reference'],write_to=str(run/f'reference-{size}.png'),output_width=size,output_height=size,background_color='white')
        result=gate(module)
        (run/'validation.txt').write_text(report.describe()+'\n'+json.dumps(result,indent=2))
        (run/'checks.json').write_text(json.dumps({'validation':report.status,'errors':report.errors,'warnings':report.warnings,'gate':result},indent=2))
        print(i,item['id'],report.status,result['status'],flush=True)
        for msg in list(report.errors)+list(report.warnings)+result['errors']+result['warnings']:print(' ',msg,flush=True)
    except Exception as e:print(i,type(e).__name__,str(e),flush=True)
for page in range(2):
    sheet=Image.new('RGB',(1100,1100),'#ddd');d=ImageDraw.Draw(sheet)
    for j,item in enumerate(items[page*10:page*10+10]):
        x=j%2*550;y=j//2*220;run=Path(item['run']);d.text((x+5,y+5),f"{page*10+j}: {item['id']}",fill='black')
        for k,(theme,bg) in enumerate((('light','white'),('dark','#1c1c19'))):
            p=run/f'preview-{theme}-384.png'
            if not p.exists():continue
            im=Image.open(p).convert('RGB');sheet.paste(im.resize((160,160)),(x+10+k*265,y+30))
            sheet.paste(im.resize((48,48)),(x+180+k*265,y+80))
    sheet.save(BATCH/f'revisions-{page}.png')
