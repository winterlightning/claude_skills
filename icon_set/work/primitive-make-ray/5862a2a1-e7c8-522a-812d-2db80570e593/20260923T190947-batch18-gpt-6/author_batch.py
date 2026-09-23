"""Batch 18 standalone authoring; only writes the four new result folders."""
from pathlib import Path
import json, importlib.util
import cairosvg
from PIL import Image, ImageDraw
SOURCE_ICON_ID = '5862a2a1-e7c8-522a-812d-2db80570e593'
SOURCE_PATH = 'icon_set/work/todo-references/gift heart_5862a2a1-e7c8-522a-812d-2db80570e593.svg'
AUTHOR = 'gpt-6'
BASE=Path(__file__).parent
ROWS=json.loads((BASE/'batch-inputs.json').read_text())
DESIGNS=[
('VRECT_L','A ribbon-tied gift box with a heart hanging over its front.','gift',
 'Lucide gift: joined lid/body structure and mirrored bow loops; supplied reference adds the heart.',
 'Small corner fillets reduced to round joins; complete bow, ribbon, box and heart retained.', '''
        # Plan: bilateral bow above the lid; central ribbon ends at the heart.
        # VRECT_L visible extrema (6,2)-(42,46), centerlines (8,4)-(40,44).
        axis=24
        self.add_bezier('bow-left',(axis,16),((19,4),(12,1),(12,7)),((12,12),(18,14),(axis,16)))
        self.add_bezier('bow-right',(axis,16),((29,4),(36,1),(36,7)),((36,12),(30,14),(axis,16)))
        self.add_polyline('lid',(8,16),(40,16),(40,24),(8,24),closed=True)
        self.add_polyline('box-left',(10,24),(10,40),(18,40))
        self.add_polyline('box-right',(38,24),(38,40),(30,40))
        self.add_line('ribbon',(24,16),(24,30))
        self.add_bezier('heart',(24,30),((13,23),(9,34),(24,44)),((39,34),(35,23),(24,30)))
        self.add_contour('heart-outline','heart',closed=True)
        for part in ('bow-left','bow-right','box-left','box-right','ribbon'):
            self.relate('connect',part,'lid')
        self.relate('connect','bow-left','bow-right')
        self.relate('connect','ribbon','heart-outline')
'''),
('SQUARE','A sun shines above a pair of sunglasses.','glasses',
 'Lucide glasses: paired lens geometry, connecting bridge and rising arms. Source keeps a sun above.',
 'Sun rays reduced to three; lens corners simplified while retaining two lenses, bridge and arms.', '''
        # Plan: repeated lens bowls mirrored about x=24; sun centered above them.
        # SQUARE visible extrema (4,4)-(44,44), centerlines (6,6)-(42,42).
        for side in (-1,1):
            cx=24+side*11
            self.add_line(f'lens-top-{side}',(cx-7,28),(cx+7,28))
            self.add_arc(f'lens-bowl-{side}',(cx+7,28),(cx-7,28),radius_x=7,radius_y=14)
            self.add_contour(f'lens-{side}',f'lens-top-{side}',f'lens-bowl-{side}',closed=True)
            self.add_line(f'arm-{side}',(cx+side*7,28),(cx+side*2,22))
            self.relate('connect',f'arm-{side}',f'lens-{side}')
        self.add_line('bridge',(20,28),(28,28))
        self.relate('connect','bridge','lens--1')
        self.relate('connect','bridge','lens-1')
        self.add_arc('sun-top',(20,14),(28,14),radius_x=4)
        self.add_arc('sun-bottom',(28,14),(20,14),radius_x=4)
        self.add_contour('sun','sun-top','sun-bottom',closed=True)
        self.add_dot('ray-top',(24,6))
        self.add_dot('ray-left',(12,12))
        self.add_dot('ray-right',(36,12))
'''),
('VRECT_L','An arched gravestone with a cross stands on a rectangular plinth.','none',
 'No useful exact Lucide match used; semicircular arch and shared cross junction built from elementary geometry.',
 'Only tiny plinth corner fillets omitted; arch, cross and base retained.', '''
        # Plan: symmetric arch and plinth around x=24; cross has one shared center.
        # VRECT_L visible extrema (6,2)-(42,46), centerlines (8,4)-(40,44).
        self.add_line('stone-left',(10,36),(10,18))
        self.add_arc('stone-arch',(10,18),(38,18),radius_x=14)
        self.add_line('stone-right',(38,18),(38,36))
        self.add_contour('stone','stone-left','stone-arch','stone-right')
        self.add_polyline('plinth',(8,36),(40,36),(40,44),(8,44),closed=True)
        self.relate('connect','stone','plinth')
        center=(24,20)
        for name,point in [('top',(24,12)),('bottom',(24,28)),('left',(20,20)),('right',(28,20))]:
            self.add_line('cross-'+name,center,point)
        self.relate('connect','cross-top','cross-bottom','cross-left','cross-right')
'''),
('SQUARE','A square artboard is surrounded by eight detached crop marks.','frame',
 'Lucide frame: shared horizontal and vertical levels; source requires detached crop marks instead of crossing rails.',
 'Artboard reduced relative to the crop marks to maintain four-unit ink clearance.', '''
        # Plan: square plus a mirrored four-corner series of two crop strokes.
        # SQUARE visible extrema (4,4)-(44,44), centerlines (6,6)-(42,42).
        lo,hi=16,32
        self.add_polyline('artboard',(lo,lo),(hi,lo),(hi,hi),(lo,hi),closed=True)
        for x in (lo,hi):
            for y in (lo,hi):
                a,b=(6,8) if y==lo else (40,42)
                self.add_line(f'vertical-{x}-{y}',(x,a),(x,b))
                a,b=(6,8) if x==lo else (40,42)
                self.add_line(f'horizontal-{x}-{y}',(a,y),(b,y))
''')]

def author():
    for m,(key,subject,ref,principle,omit,body) in zip(ROWS,DESIGNS):
        out=Path(m['result_dir']);uid=m['source_uuid'];iid=m['icon_id']
        module=iid.replace('-','_')+'_'+uid.replace('-','_')+'.py'
        source=f'''"""{subject}\n{principle}\n"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {m['reference_path']!r}
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = {iid!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = {tuple(m['concept'].split())!r}
    def build(self):
'''+body
        (out/module).write_text(source)
        m.update(module=module,keyshape=key,subject=subject,lucide_reference=ref,construction_reference=principle,omissions=omit)
    (BASE/'batch-inputs.json').write_text(json.dumps(ROWS,indent=2))

def export():
    sheet=Image.new('RGB',(780,4*220),'white');d=ImageDraw.Draw(sheet)
    for i,m in enumerate(ROWS):
        out=Path(m['result_dir']);iid=m['icon_id']
        spec=importlib.util.spec_from_file_location('batch18_'+str(i),out/m['module']);mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
        icon=mod.Drawing();report=icon.validate_icon();m['validation_status']=report.status
        (out/'validation.txt').write_text(report.describe());svg=icon.to_svg();(out/(iid+'.svg')).write_text(svg)
        for size in (48,192):
            for theme in ('light','dark'):
                cairosvg.svg2png(bytestring=svg.encode(),write_to=str(out/f'{theme}-{size}.png'),output_width=size,output_height=size,background_color='#000000' if theme=='dark' else '#ffffff',negate_colors=theme=='dark')
        y=i*220
        im=Image.open(out/'reference.png');sheet.paste(im.resize((192,192)),(0,y),im.resize((192,192)))
        for j,theme in enumerate(('light','dark')):
            sheet.paste(Image.open(out/f'{theme}-192.png'),(200+j*200,y))
            sheet.paste(Image.open(out/f'{theme}-48.png'),(610+j*60,y+50))
        d.text((610,y+115),m['concept'],fill='black');d.text((610,y+140),report.status,fill='black')
        print(m['concept'],report.describe())
    sheet.save(BASE/'batch-review.png');(BASE/'batch-inputs.json').write_text(json.dumps(ROWS,indent=2))
if __name__=='__main__':
    import sys
    if '--export-only' not in sys.argv:author()
    export()
