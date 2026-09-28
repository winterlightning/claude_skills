import sys,json,io
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from icon_set.scripts.primitive_fix import load_icon,render_previews
from icon_set.scripts.build_gate import gate
import cairosvg
from PIL import Image,ImageDraw
ROOT=Path(__file__).parent
entries=json.loads((ROOT/'entries.json').read_text())
rows=[]
for e in entries:
    run=Path(e['run']);mods=list(run.glob('*.py'))
    if not mods or (len(sys.argv)>1 and e['icon_id'] not in sys.argv[1:]):continue
    icon=load_icon(mods[0]);report=icon.validate_icon();g=gate(mods[0])
    svg=icon.to_svg();(run/(e['icon_id']+'.svg')).write_text(svg)
    (run/'validation.txt').write_text(report.describe()+'\n'+json.dumps(g,indent=2))
    (run/'checks.json').write_text(json.dumps(dict(validation=report.status,errors=report.errors,warnings=report.warnings,gate=g),indent=2))
    render_previews(svg,e['icon_id'],48,run)
    cairosvg.svg2png(url=e['reference_path'],write_to=str(run/'reference.png'),output_width=192,output_height=192)
    print(e['icon_id'],report.status,g['status'],flush=True)
    for msg in list(report.errors)+list(report.warnings)+g['errors']+g['warnings']:print(' ',msg,flush=True)
    rows.append(e)
sheet=Image.new('RGB',(640,len(rows)*150),'white');d=ImageDraw.Draw(sheet)
for n,e in enumerate(rows):
    y=n*150;run=Path(e['run']);d.text((5,y+2),e['icon_id'],fill='black')
    for x,theme in [(10,'light'),(320,'dark')]:
        bg='white' if theme=='light' else '#171717';d.rectangle((x,y+20,x+300,y+148),fill=bg)
        for xx,size in [(x+12,48),(x+110,120)]:
            svg=(run/(e['icon_id']+'.svg')).read_text().replace('currentColor','#111111' if theme=='light' else '#eeeeee')
            a=Image.open(io.BytesIO(cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size)))
            sheet.paste(a,(xx,y+25),a)
sheet.save(ROOT/'review.png')
