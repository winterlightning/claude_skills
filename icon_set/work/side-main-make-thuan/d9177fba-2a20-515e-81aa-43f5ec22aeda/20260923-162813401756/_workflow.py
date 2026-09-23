"""Local-only batch authoring and export utility. Never registers or builds icons."""
SOURCE_ICON_ID = "d9177fba-2a20-515e-81aa-43f5ec22aeda"
SOURCE_PATH = "pictographic-primitives/work/task list to do_d9177fba-2a20-515e-81aa-43f5ec22aeda.svg"
AUTHOR = "gpt-6"
import json, importlib.util, textwrap, traceback
from pathlib import Path
import cairosvg
from PIL import Image, ImageDraw
ROOT = Path(__file__).parent
DIRS = [Path(s) for s in json.loads((ROOT/'batch-dirs.json').read_text())]
HELPERS = """
def circle(icon, name, cx, cy, r):
    icon.add_arc(name+'-top', (cx-r,cy), (cx+r,cy), radius_x=r)
    icon.add_arc(name+'-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
    icon.add_contour(name, name+'-top', name+'-bottom', closed=True)

def rounded_rect(icon, name, x0,y0,x1,y1,r):
    points=[(x0+r,y0),(x1-r,y0),(x1,y0+r),(x1,y1-r),(x1-r,y1),(x0+r,y1),(x0,y1-r),(x0,y0+r)]
    members=[]
    for j,a in enumerate(points):
        b=points[(j+1)%8]; part=name+'-'+str(j)
        if j%2: icon.add_arc(part,a,b,radius_x=r)
        else: icon.add_line(part,a,b)
        members.append(part)
    icon.add_contour(name,*members,closed=True)

def monitor(icon, x0=6,y0=6,x1=42,y1=34,foot=42):
    # Split bottom wall at the exact stand attachment.
    r=3; cx=24
    icon.add_line('screen-top',(x0+r,y0),(x1-r,y0))
    icon.add_arc('screen-tr',(x1-r,y0),(x1,y0+r),radius_x=r)
    icon.add_line('screen-right',(x1,y0+r),(x1,y1-r))
    icon.add_arc('screen-br',(x1,y1-r),(x1-r,y1),radius_x=r)
    icon.add_line('screen-bottom-r',(x1-r,y1),(cx,y1))
    icon.add_line('screen-bottom-l',(cx,y1),(x0+r,y1))
    icon.add_arc('screen-bl',(x0+r,y1),(x0,y1-r),radius_x=r)
    icon.add_line('screen-left',(x0,y1-r),(x0,y0+r))
    icon.add_arc('screen-tl',(x0,y0+r),(x0+r,y0),radius_x=r)
    icon.add_contour('screen','screen-top','screen-tr','screen-right','screen-br','screen-bottom-r','screen-bottom-l','screen-bl','screen-left','screen-tl',closed=True)
    icon.add_line('stand',(cx,y1),(cx,foot))
    icon.add_line('foot-left',(16,foot),(cx,foot));icon.add_line('foot-right',(cx,foot),(32,foot))
    icon.add_contour('foot','foot-left','foot-right')
    for part in ['screen-bottom-r','screen-bottom-l','foot-left','foot-right']: icon.relate('connect','stand',part)
"""

def author(index,icon_id,keyshape,description,plan,body,omissions,refs):
    d=DIRS[index-1]; m=json.loads((d/'retrieval.metadata.json').read_text())
    filename=icon_id.replace('-','_')+'_'+m['source_uuid'].replace('-','_')+'.py'
    header=f'"""{description}\n\nSymbol plan: {plan}\n"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\n\nSOURCE_ICON_ID = {m["source_uuid"]!r}\nSOURCE_PATH = {m["reference_path"]!r}\nAUTHOR = "gpt-6"\n'
    cls=f'\nclass AuthoredIcon(Solo48):\n    icon_id = {icon_id!r}\n    keyshape = Keyshape.{keyshape}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = {m["category"]!r}\n    aliases = ()\n    keywords = {tuple(icon_id.split("-"))!r}\n\n    def build(self):\n'+textwrap.indent(textwrap.dedent(body).strip()+'\n','        ')
    (d/filename).write_text(header+HELPERS+cls)
    (d/(icon_id+'.metadata.json')).write_text(json.dumps(m,indent=2))
    info=dict(source_uuid=m['source_uuid'],source_path=m['reference_path'],icon_id=icon_id,author='gpt-6',keyshape=keyshape,description=description,symbol_plan=plan,omissions=omissions,references=refs,python=filename)
    (d/'candidate.json').write_text(json.dumps(info,indent=2))
    return export(index)

def export(index):
    d=DIRS[index-1]; info=json.loads((d/'candidate.json').read_text()); fn=d/info['python']
    try:
        spec=importlib.util.spec_from_file_location('candidate_'+str(index),fn); module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
        icon=module.AuthoredIcon(); report=icon.validate_icon(); info['validation_status']=report.status
        (d/'validation.txt').write_text(report.describe()); svg=icon.to_svg();(d/(icon.icon_id+'.svg')).write_text(svg)
        for theme in ('light','dark'):
            for size in (48,288):
                cairosvg.svg2png(bytestring=svg.encode(),write_to=str(d/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color='white' if theme=='light' else '#171717',negate_colors=(theme=='dark'))
        print(index,icon.icon_id,report.describe(),flush=True)
    except Exception:
        info['validation_status']='error'; info['error']=traceback.format_exc();(d/'validation.txt').write_text(info['error']);print(index,info['error'],flush=True)
    (d/'candidate.json').write_text(json.dumps(info,indent=2)); return info

def sheet():
    im=Image.new('RGB',(1440,800),'#eeeeee');dr=ImageDraw.Draw(im)
    for i,d in enumerate(DIRS):
        x=(i%5)*288;y=(i//5)*400;info=json.loads((d/'candidate.json').read_text())
        dr.text((x+8,y+4),str(i+1)+'. '+info['icon_id'][:34],fill='black')
        for j,theme in enumerate(('light','dark')):
            f=d/f'{theme}-288.png'
            if f.exists(): im.paste(Image.open(f).convert('RGB').resize((144,144)),(x+j*144,y+28))
            f=d/f'{theme}-48.png'
            if f.exists(): im.paste(Image.open(f).convert('RGB'),(x+48+j*144,y+188))
        im.paste(Image.open(d/'reference.png').convert('RGB').resize((120,120)),(x+84,y+256))
        dr.text((x+8,y+240),info['validation_status'],fill='black')
    im.save(ROOT/'batch-review.png')
