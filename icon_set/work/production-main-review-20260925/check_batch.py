"""Validate and render work-folder modules, without registration or publication."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys
import cairosvg
from PIL import Image, ImageDraw

ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from icon_set.validation.library_qa import inspect_icon, public_row

BATCH=Path(__file__).resolve().parent
ROWS=json.loads((BATCH/'config.json').read_text())

def run(indices):
    for n,row in enumerate(ROWS,1):
        if indices and n not in indices:continue
        out=ROOT/row['out'];path=ROOT/row['module']
        spec=importlib.util.spec_from_file_location('_fresh_'+str(n),path)
        module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        icon=module.Drawing(); report=icon.validate_icon();qa=inspect_icon(icon)
        (out/'validation.txt').write_text(report.describe()+'\n')
        (out/'qa.json').write_text(json.dumps(public_row(qa),indent=2)+'\n')
        (out/(icon.icon_id+'.svg')).write_text(icon.to_svg())
        (out/(icon.icon_id+'.metadata.json')).write_text((out/'input.metadata.json').read_text())
        for theme,bg,fg in [('light','#ffffff','#111827'),('dark','#101827','#f8fafc')]:
            for size in (48,192):
                cairosvg.svg2png(bytestring=icon.to_svg().replace('currentColor',fg).encode(),write_to=str(out/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color=bg)
        print(n,icon.icon_id,qa['status'],len(qa['errors']),len(qa['warnings']),flush=True)
    for page in range(6):
        sheet=Image.new('RGB',(1260,840),'#e8edf4');draw=ImageDraw.Draw(sheet)
        for j,row in enumerate(ROWS[page*6:page*6+6]):
            x=(j%2)*630;y=(j//2)*280;out=ROOT/row['out']
            if not (out/'light-192.png').exists():continue
            qa=json.loads((out/'qa.json').read_text());draw.text((x+12,y+8),f'{page*6+j+1}. '+row['concept']+' — '+qa['status'],fill='black')
            for k,name in enumerate(['reference.png','light-192.png','dark-192.png']):
                im=Image.open(out/name).convert('RGBA');bg=Image.new('RGBA',im.size,'white');bg.alpha_composite(im);sheet.paste(bg.convert('RGB'),(x+8+k*206,y+30))
            for k,name in enumerate(['light-48.png','dark-48.png']):sheet.paste(Image.open(out/name).convert('RGB'),(x+250+k*85,y+228))
        sheet.save(BATCH/f'review-{page+1}.png')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('indices',nargs='*',type=int);args=parser.parse_args();run(args.indices)
