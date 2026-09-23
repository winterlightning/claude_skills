"""Batch 21 standalone authored candidates; preserves source identity per module."""
from pathlib import Path
import json, importlib.util
import cairosvg
from PIL import Image,ImageDraw
SOURCE_ICON_ID='bf6cf58a-c4bd-55e5-b5c2-806c4c390311'
SOURCE_PATH='icon_set/work/todo-references/insurance card_bf6cf58a-c4bd-55e5-b5c2-806c4c390311.svg'
AUTHOR='gpt-6'
BASE=Path(__file__).parent
ROWS=json.loads((BASE/'batch-inputs.json').read_text())
HELPERS='''
    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)
'''
DESIGNS=[
('HRECT_L','An insurance identity card combines a shield and a portrait.','id-card and human_ref/user.svg','The small text rule is omitted to preserve spacing around the shield and person.', '''
        # Plan: rounded card; shield at left; circular head and broad shoulders at right.
        # Human construction: icon_set/references/human_ref/user.svg.
        self.rect('card',4,8,40,32)
        self.add_polyline('shield',(12,18),(16,16),(20,18),(20,26),(16,30),(12,26),closed=True)
        self.circle('head',32,19,3)
        # Head ends y=22; shoulder crest y=30: centerline gap 8, ink gap 4.
        self.add_arc('shoulders',(28,32),(36,32),radius_x=4,radius_y=2)
'''),
('SQUARE','A coin sits below a medical cross on a rising balance beam, indicating cheap insurance.','scale','Dollar strokes and plus outline retained; minor source curves simplified.', '''
        # Plan: tilted beam and triangular fulcrum; left coin lower than right cross.
        self.circle('coin',14,18,8)
        self.add_bezier('dollar',(17,14),((10,12),(10,18),(14,18)),((19,18),(18,23),(11,22)))
        self.add_line('dollar-stem',(14,11),(14,25))
        self.relate('connect','dollar','dollar-stem')
        self.add_polyline('medical-cross',(30,6),(38,6),(38,10),(42,10),(42,18),(38,18),(38,22),(30,22),(30,18),(26,18),(26,10),(30,10),closed=True)
        self.add_polyline('beam',(6,38),(24,33),(42,28))
        self.add_polyline('fulcrum',(24,33),(16,42),(32,42),closed=True)
        self.relate('connect','beam','fulcrum')
'''),
('SQUARE','A coin sits above a medical cross on a descending balance beam, indicating expensive insurance.','scale','Dollar strokes and plus outline retained; minor source curves simplified.', '''
        # Plan: price coin higher on left; medical cross lower on right; tilted beam.
        self.circle('coin',14,14,8)
        self.add_bezier('dollar',(17,10),((10,8),(10,14),(14,14)),((19,14),(18,19),(11,18)))
        self.add_line('dollar-stem',(14,7),(14,21))
        self.relate('connect','dollar','dollar-stem')
        self.add_polyline('medical-cross',(30,10),(38,10),(38,14),(42,14),(42,22),(38,22),(38,26),(30,26),(30,22),(26,22),(26,14),(30,14),closed=True)
        self.add_polyline('beam',(6,28),(24,33),(42,38))
        self.add_polyline('fulcrum',(24,33),(16,42),(32,42),closed=True)
        self.relate('connect','beam','fulcrum')
'''),
('VRECT_L','An iPod-like player has a triangular play control above a circular button.','tablet','None: enclosure, separator, play triangle and circular button retained.', '''
        # Plan: upright rounded rectangle split into display and lower button band.
        self.rect('body',8,4,32,40)
        self.add_line('separator',(8,28),(40,28))
        self.relate('connect','body','separator')
        self.add_polyline('play',(18,12),(28,18),(18,24),closed=True)
        self.circle('button',24,36,3)
'''),
('VRECT_L','A circular Kanda Matsuri emblem contains three inward-pointing heart forms and hanging strokes.','heart','Heart lobes simplified; all three heart forms, their stems and lower hanging strokes retained.', '''
        # Plan: round medallion and three oriented heart shapes; paired lower strokes.
        self.circle('medallion',24,20,16)
        self.add_line('top-stem',(24,4),(24,11))
        self.add_bezier('heart-top',(24,11),((14,5),(14,15),(24,19)),((34,15),(34,5),(24,11)))
        self.add_bezier('heart-left',(20,23),((8,13),(10,24),(15,25)),((10,33),(21,34),(20,23)))
        self.add_bezier('heart-right',(28,23),((40,13),(38,24),(33,25)),((38,33),(27,34),(28,23)))
        self.add_line('stem-left',(10,28),(15,25))
        self.add_line('stem-right',(38,28),(33,25))
        self.relate('connect','top-stem','medallion')
        self.relate('connect','top-stem','heart-top')
        self.relate('connect','stem-left','heart-left')
        self.relate('connect','stem-right','heart-right')
        self.add_line('tassel-left',(8,38),(12,44))
        self.add_line('tassel-right',(40,38),(36,44))
        self.add_dot('tassel-center',(24,44))
'''),
('SQUARE','An empty manga action bubble has a scalloped burst outline and external emphasis rays.','none','Eight outline cusps and six emphasis marks retained; tiny curvature variations simplified.', '''
        # Plan: mirrored scalloped outline, four diagonal rays and two axial rays.
        pts=[(24,16),(32,12),(36,20),(42,24),(36,28),(32,36),(24,32),(16,36),(12,28),(6,24),(12,20),(16,12)]
        self.add_polyline('burst',*pts,closed=True)
        self.add_line('ray-top',(24,6),(24,8))
        self.add_line('ray-bottom',(24,40),(24,42))
        for x,dx in [(8,2),(40,-2)]:
            self.add_line(f'ray-top-{x}',(x,6),(x+dx,8))
            self.add_line(f'ray-bottom-{x}',(x,42),(x+dx,40))
'''),
('SQUARE','Three joined keyboard keys show up, left and right arrows.','none','Rounded source corners reduced to round joins; all three key outlines and arrows retained.', '''
        # Plan: three equal directional cells in a T arrangement, sharing the top joint.
        self.add_polyline('keys',(16,6),(32,6),(32,24),(42,24),(42,42),(26,42),(26,24),(22,24),(22,42),(6,42),(6,24),(16,24),closed=True)
        for name,points in [('up',[(24,20),(24,12)]),('left',[(18,33),(10,33)]),('right',[(30,33),(38,33)])]:
            self.add_polyline(name,*points)
        self.add_polyline('up-tip',(20,16),(24,12),(28,16))
        self.add_polyline('left-tip',(14,29),(10,33),(14,37))
        self.add_polyline('right-tip',(34,29),(38,33),(34,37))
        for n in ('up','left','right'):self.relate('connect',n,n+'-tip')
'''),
('HRECT_M','The letters K and R separated by a plus sign represent kiss and ride.','none','None: K, plus and R retained as hand-authored lettering.', '''
        # Plan: monoline letterforms on shared cap and baseline; plus at midheight.
        self.add_polyline('k-stem',(4,10),(4,24),(4,38))
        self.add_polyline('k-arms',(16,10),(4,24),(16,38))
        self.relate('connect','k-stem','k-arms')
        self.add_line('plus-h',(20,24),(28,24))
        self.add_line('plus-v',(24,18),(24,30))
        self.relate('connect','plus-h','plus-v')
        self.add_polyline('r-stem',(34,38),(34,10),(38,10))
        self.add_arc('r-bowl',(38,10),(38,26),radius_x=6,radius_y=8)
        self.add_line('r-bar',(38,26),(34,26))
        self.add_line('r-leg',(38,26),(44,38))
        self.relate('connect','r-stem','r-bowl')
        self.relate('connect','r-stem','r-bar')
        self.relate('connect','r-bowl','r-bar','r-leg')
'''),
('SQUARE','A four-pane kitchen window rests on a projecting sill.','panels-top-left','None: all four panes and projecting sill retained.', '''
        # Plan: equal panes share central mullion; sill is an 8-unit-high band.
        self.add_polyline('window',(10,34),(10,6),(38,6),(38,34))
        self.add_line('mullion',(24,6),(24,34))
        self.add_line('transom',(10,20),(38,20))
        self.add_polyline('sill',(6,34),(42,34),(42,42),(6,42),closed=True)
        self.relate('connect','window','mullion')
        self.relate('connect','window','transom')
        self.relate('connect','window','sill')
        self.relate('connect','mullion','transom')
        self.relate('connect','mullion','sill')
'''),
('CIRCLE','Two sperm cells and a detached oval are shown in a circular laboratory view.','none','None: enclosing circle, two cell heads with tails and lower oval retained.', '''
        # Plan: round observation field; diagonal ovals and flowing tails inside.
        self.circle('field',24,24,20)
        self.add_bezier('head-left',(16,19),((12,17),(17,10),(20,12)),((24,14),(20,21),(16,19)))
        self.add_bezier('tail-left',(16,19),((11,21),(16,26),(11,29)))
        self.add_bezier('head-right',(30,24),((26,22),(31,15),(34,17)),((38,19),(34,26),(30,24)))
        self.add_bezier('tail-right',(30,24),((25,28),(32,30),(26,35)))
        self.add_bezier('oval',(17,35),((13,33),(18,28),(20,30)),((23,32),(20,37),(17,35)))
        self.relate('connect','head-left','tail-left')
        self.relate('connect','head-right','tail-right')
''')]
def author():
    from icon_set.model.keyshapes import Keyshape
    from icon_set.model.profiles import Profile
    for m,(key,subject,ref,omit,body) in zip(ROWS,DESIGNS):
        out=Path(m['result_dir']);uid=m['source_uuid'];iid=m['icon_id'];module=iid.replace('-','_')+'_'+uid.replace('-','_')+'.py'
        bounds=Keyshape[key].bounds_for(Profile.SOLO48)
        source=f'''"""{subject}\nConstruction reference: {ref}.\n"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {uid!r}
SOURCE_PATH = {m['reference_path']!r}
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = {iid!r}
    keyshape = Keyshape.{key}
    # Visible ink extremes: {bounds}.
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
