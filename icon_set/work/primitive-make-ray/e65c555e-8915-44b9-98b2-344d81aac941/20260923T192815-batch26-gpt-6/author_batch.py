"""Batch 26 standalone authoring and local exports."""
from pathlib import Path
import json,importlib.util
import cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID='e65c555e-8915-44b9-98b2-344d81aac941'
SOURCE_PATH='icon_set/work/todo-references/mobile phone headphone_e65c555e-8915-44b9-98b2-344d81aac941.svg'
AUTHOR='gpt-6'
BASE=Path(__file__).parent
ROWS=json.loads((BASE/'batch-inputs.json').read_text())
exec((BASE/'helpers.txt').read_text())
exec((BASE/'designs.py').read_text())
def author():
    from icon_set.model.keyshapes import Keyshape
    from icon_set.model.profiles import Profile
    for m,(key,subject,ref,omit,body) in zip(ROWS,DESIGNS):
        out=Path(m['result_dir']);uid=m['source_uuid'];iid=m['icon_id'];module=iid.replace('-','_')+'_'+uid.replace('-','_')+'.py';bounds=Keyshape[key].bounds_for(Profile.SOLO48)
        source=f'''"""{subject}\nConstruction reference: {ref}.\n"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {m['reference_path']!r}
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = {iid!r}
    keyshape = Keyshape.{key}
    # Visible ink extrema: {bounds}.
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = {tuple(m['concept'].split())!r}
'''+HELPERS+'\n    def build(self):\n'+body
        (out/module).write_text(source);m.update(module=module,keyshape=key,subject=subject,construction_reference=ref,omissions=omit)
    (BASE/'batch-inputs.json').write_text(json.dumps(ROWS,indent=2))
def export():
    sheet=Image.new('RGB',(800,len(ROWS)*200),'white');d=ImageDraw.Draw(sheet)
    for i,m in enumerate(ROWS):
        out=Path(m['result_dir']);iid=m['icon_id'];spec=importlib.util.spec_from_file_location('drawing'+str(i),out/m['module']);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        icon=mod.Drawing();report=icon.validate_icon();m['validation_status']=report.status
        (out/'validation.txt').write_text(report.describe());svg=icon.to_svg();(out/(iid+'.svg')).write_text(svg)
        for size in (48,192):
            for theme in ('light','dark'):cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color='#000000' if theme=='dark' else '#ffffff',negate_colors=theme=='dark')
        y=i*200;a=Image.open(out/'reference.png');sheet.paste(a,(0,y),a)
        for j,theme in enumerate(('light','dark')):
            sheet.paste(Image.open(out/f'{theme}-192.png'),(185+j*195,y))
            sheet.paste(Image.open(out/f'{theme}-48.png'),(585+j*60,y+20))
        d.text((585,y+90),m['concept'][:28],fill='black');d.text((585,y+115),report.status,fill='black')
        print(m['concept'],report.describe())
    sheet.save(BASE/'batch-review.png');(BASE/'batch-inputs.json').write_text(json.dumps(ROWS,indent=2))
if __name__=='__main__':
    import sys
    if '--export-only' not in sys.argv:author()
    export()
