"""Standalone batch 25 generation and local validation."""
from pathlib import Path
import json, importlib.util
import cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID='eb0b6680-3f5b-40fd-9a39-04012841c110'
SOURCE_PATH='icon_set/work/todo-references/message key_eb0b6680-3f5b-40fd-9a39-04012841c110.svg'
AUTHOR='gpt-6'
BASE=Path(__file__).parent
ROWS=json.loads((BASE/'batch-inputs.json').read_text())
exec((BASE/'helpers.txt').read_text())
PHONE='''
        # Shared symbol plan: upright phone, lower band, individually authored content.
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')
'''
MIC='''
        # Plan: upper globe with two meridians, lower capsule microphone and U support.
        self.add_arc('globe-top',(8,20),(40,20),radius_x=16)
        self.add_arc('globe-left',(10,28),(8,20),radius_x=16,sweep=True)
        self.add_arc('globe-right',(40,20),(38,28),radius_x=16,sweep=True)
        self.add_contour('globe','globe-left','globe-top','globe-right')
        self.add_line('equator',(8,EQUATOR),(40,EQUATOR))
        self.add_bezier('meridian-left',(18,5),((15,9),(15,14),(15,20)))
        self.add_bezier('meridian-right',(30,5),((33,9),(33,14),(33,20)))
        self.rect('microphone',20,24,8,12,r=4)
        self.add_polyline('stand',(24,40),(24,44),(32,44))
        self.add_line('base-left',(16,44),(24,44))
        self.relate('connect','stand','base-left')
        self.add_line('support-left',(12,30),(12,32))
        self.add_arc('support-bowl',(12,32),(36,32),radius_x=12,radius_y=8,sweep=False)
        self.add_line('support-right',(36,32),(36,30))
        self.add_contour('support','support-left','support-bowl','support-right')
        self.relate('connect','support','stand')
'''
DESIGNS=[
('SQUARE','A key sits inside a message bubble.','key-round','Two close key teeth reduced to one to preserve spacing.', '''
        # Plan: speech enclosure with lower-left tail; ring, shaft and tooth inside.
        self.add_polyline('bubble',(6,6),(42,6),(42,34),(24,34),(14,42),(14,34),(6,34),closed=True)
        self.circle('key-ring',19,20,4)
        self.add_polyline('key-shaft',(23,20),(34,20),(34,16))
        self.relate('connect','key-ring','key-shaft')
'''),
('VRECT_L','A globe above a microphone represents international podcasting.','mic and globe','Small reference capsule and globe curves simplified; all principal parts retained.',MIC.replace('EQUATOR','20')),
('VRECT_L','An international podcast microphone sits below a globe with an elevated latitude line.','mic and globe','Small reference capsule and globe curves simplified; elevated latitude line retained.',MIC.replace('EQUATOR','16')),
('SQUARE','A four-point migration star has a right chevron and four outward corner arrows.','none','Arrow stems omitted; four outward tips and central chevron retained.', '''
        # Plan: cardinal star around (24,24), central direction and mirrored corner tips.
        self.add_polyline('star',(24,6),(29,19),(42,24),(29,29),(24,42),(19,29),(6,24),(19,19),closed=True)
        self.add_polyline('center-chevron',(23,21),(26,24),(23,27))
        for sx in (-1,1):
            for sy in (-1,1):
                self.add_polyline(f'corner-{sx}-{sy}',(24+sx*10,24+sy*12),(24+sx*15,24+sy*15),(24+sx*12,24+sy*10))
'''),
('VRECT_L','A mobile phone displays a capital A.','smartphone','None: letter, enclosure and lower band retained.',PHONE+'''
        # Capital A: common apex and crossbar intersections.
        self.add_polyline('a',(16,28),(24,12),(32,28))
        self.add_line('crossbar',(20,20),(28,20))
        self.relate('connect','a','crossbar')
'''),
('VRECT_L','A mobile phone displays a notification bell.','smartphone','None: bell crown, dome and bottom edge retained.',PHONE+'''
        # Bell dome is a semicircle with tangent vertical sides.
        self.add_line('bell-left',(18,28),(18,22))
        self.add_arc('bell-dome',(18,22),(30,22),radius_x=6)
        self.add_line('bell-right',(30,22),(30,28))
        self.add_line('bell-base',(30,28),(18,28))
        self.add_contour('bell','bell-left','bell-dome','bell-right','bell-base',closed=True)
        self.add_line('crown',(24,12),(24,16))
        self.relate('connect','bell','crown')
'''),
('VRECT_L','A mobile phone displays a check mark.','smartphone','None: check, enclosure and lower band retained.',PHONE+'''
        self.add_polyline('check',(16,22),(22,28),(32,16))
'''),
('VRECT_L','A mobile phone displays a circled plus sign.','smartphone','None: plus and its circle retained.',PHONE+'''
        # Nested content symbol with centered plus.
        self.circle('add-circle',24,20,8)
        self.add_line('plus-h',(20,20),(28,20))
        self.add_line('plus-v',(24,16),(24,24))
        self.relate('connect','plus-h','plus-v')
'''),
('VRECT_L','A mobile phone displays a euro sign.','smartphone','The source single euro crossbar is retained.',PHONE+'''
        # Open circular C and a horizontal currency crossbar.
        self.add_bezier('euro-curve',(30,14),((18,6),(14,32),(30,28)))
        self.add_line('euro-bar',(16,21),(26,21))
        self.relate('connect','euro-curve','euro-bar')
'''),
('VRECT_L','A mobile phone displays an eye with a central pupil.','smartphone and eye','Tiny pupil enlarged to the profile stroke-width dot.',PHONE+'''
        # Mirrored lens-shaped lids surrounding a central pupil.
        self.add_bezier('eye',(16,20),((21,10),(27,10),(32,20)),((27,30),(21,30),(16,20)))
        self.add_contour('eye-outline','eye',closed=True)
        self.add_dot('pupil',(24,20))
'''),
('VRECT_L','A mobile phone displays a capital F.','smartphone','None: F, enclosure and lower band retained.',PHONE+'''
        # Shared F stem with top and middle arms, open on the right.
        self.add_polyline('f',(18,28),(18,12),(30,12))
        self.add_line('f-middle',(18,20),(28,20))
        self.relate('connect','f','f-middle')
'''),
('VRECT_L','A mobile phone displays a fingerprint.','smartphone','Fingerprint reduced to outer arch, central whorl and two lower ridge tails.',PHONE+'''
        # Smooth nested ridge curves; intentional asymmetry follows fingertip flow.
        self.add_arc('outer-ridge',(16,20),(32,20),radius_x=8)
        self.add_bezier('inner-ridge',(16,27),((24,24),(17,16),(24,16)),((30,16),(25,25),(32,29)))
        self.add_bezier('left-tail',(24,22),((24,26),(21,28),(20,30)))
        self.add_bezier('right-tail',(25,28),((26,30),(27,31),(28,32)))
''')]
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
