"""Validate and export only the current standalone batch modules."""
from pathlib import Path
import json
import importlib.util
import traceback
import cairosvg
from PIL import Image, ImageDraw

AUTHOR='gpt-6'
SOURCE_ICON_ID='8e659963-5f68-4c80-963b-528218ccf29f'
SOURCE_PATH='icon_set/work/todo-references/award wall_8e659963-5f68-4c80-963b-528218ccf29f.svg'
ROOT=Path(__file__).parent
rows=json.loads((ROOT/'batch-inputs.json').read_text())
sheet=Image.new('RGB',(1100,len(rows)*190),'#dddddd')
draw=ImageDraw.Draw(sheet)
for index,row in enumerate(rows):
    out=Path(row['out'])
    notes=json.loads((out/'design-notes.json').read_text())
    try:
        spec=importlib.util.spec_from_file_location('candidate_'+str(index),out/notes['module'])
        module=importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        icon=module.Drawing()
        report=icon.validate_icon()
        (out/'validation.txt').write_text(report.describe()+'\n')
        (out/'validation-status.json').write_text(json.dumps(dict(status=report.status,errors=len(report.errors),warnings=len(report.warnings)),indent=2))
        svg=icon.to_svg()
        (out/(row['icon_id']+'.svg')).write_text(svg)
        for theme,ink,bg in [('light','#111111','#ffffff'),('dark','#eeeeee','#171717')]:
            # Bind currentColor for preview only; preserve the canonical SVG untouched.
            preview=svg.replace('fill="none"',f'color="{ink}" fill="none"',1)
            for size in (48,192):
                cairosvg.svg2png(bytestring=preview.encode(),write_to=str(out/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
        print(row['concept'],report.status,len(report.errors),'errors',len(report.warnings),'warnings',flush=True)
        if report.status!='valid':
            print(report.describe(),flush=True)
    except Exception:
        (out/'error.txt').write_text(traceback.format_exc())
        print(row['concept'],traceback.format_exc(),flush=True)
        continue
    y=index*190
    draw.text((5,y+8),row['concept'],fill='black')
    draw.text((5,y+30),report.status,fill='black')
    ref=Image.open(out/'reference.png')
    sheet.paste(ref,(200,y+10),ref)
    for x,theme in [(400,'light'),(700,'dark')]:
        large=Image.open(out/f'{theme}-192.png').resize((168,168))
        sheet.paste(large,(x,y+4))
        sheet.paste(Image.open(out/f'{theme}-48.png'),(x+190,y+55))
sheet.save(ROOT/'batch-review.png')
