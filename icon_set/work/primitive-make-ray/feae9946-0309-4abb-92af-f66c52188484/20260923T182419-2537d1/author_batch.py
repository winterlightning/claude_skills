from pathlib import Path
import json, importlib.util, shutil
import cairosvg
from PIL import Image, ImageOps, ImageDraw

AUTHOR = 'gpt-6'
SOURCE_ICON_ID = 'feae9946-0309-4abb-92af-f66c52188484'
SOURCE_PATH = 'icon_set/work/todo-references/column insert_feae9946-0309-4abb-92af-f66c52188484.svg'
ROOT = Path(__file__).parent
rows = json.loads((ROOT/'batch-work.json').read_text())
helpers = '''
    def circle(self, name, cx, cy, radius):
        self.add_arc(name+'-top',(cx-radius,cy),(cx+radius,cy),radius_x=radius)
        self.add_arc(name+'-bottom',(cx+radius,cy),(cx-radius,cy),radius_x=radius)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def box(self, name, left, top, right, bottom, radius):
        # Shared corner radius and a bottom-centre attachment node.
        mid=(left+right)//2
        pts=[(left+radius,top),(right-radius,top),(right,top+radius),
             (right,bottom-radius),(right-radius,bottom),(mid,bottom),
             (left+radius,bottom),(left,bottom-radius),(left,top+radius),(left+radius,top)]
        members=[]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):
            key=f'{name}-{i}';members.append(key)
            if i in (1,3,6,8): self.add_arc(key,a,b,radius_x=radius)
            else: self.add_line(key,a,b)
        self.add_contour(name,*members,closed=True)
'''
designs=[
('SQUARE', '''        # Two matching column definitions flank the central downward insertion chevron.
        for name,left in [('left-column',6),('right-column',30)]:
            self.box(name,left,20,left+12,42,3)
        self.add_polyline('insert',(18,6),(24,12),(30,6))
''','Two separate columns with a downward insertion chevron between them.','columns-2','No defining parts omitted; columns share dimensions and rounding.'),
('SQUARE', '''        # A single rounded speech panel with a lower-left triangular tail.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,30))
        self.add_arc('br',(42,30),(38,34),radius_x=4)
        tail=[(38,34),(24,34),(14,42),(14,34),(10,34)]
        for i,(a,b) in enumerate(zip(tail,tail[1:])):self.add_line(f'tail-{i}',a,b)
        self.add_arc('bl',(10,34),(6,30),radius_x=4)
        self.add_line('left',(6,30),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('bubble','top','tr','right','br','tail-0','tail-1','tail-2','tail-3','bl','left','tl',closed=True)
''','An empty rounded comment box with a lower-left speech tail.','message-square','No omissions; deliberate lower-left tail asymmetry preserved.'),
('HRECT_M', '''        # East: outlined E inside a circular badge, followed by a concave right arrow.
        self.circle('badge',16,24,12)
        self.add_polyline('letter-e',(20,16),(12,16),(12,24),(12,32),(20,32))
        self.add_line('middle-bar',(12,24),(20,24))
        self.relate('connect','letter-e','middle-bar')
        self.add_polyline('east-arrow',(34,10),(44,24),(34,38),(38,24),closed=True)
''','A circular east badge containing E beside a right-pointing compass arrow.','navigation','No omissions. Letter, enclosing circle and separate directional arrow are all essential; keep spacing failures if they cannot fit.'),
('VRECT_L', '''        # Symmetric shield: sloped roof, vertical flanks, elliptical lower quarters.
        roof=[(8,24),(8,8),(24,4),(40,8),(40,24)]
        for i,(a,b) in enumerate(zip(roof,roof[1:]),1):self.add_line(f'roof-{i}',a,b)
        self.add_arc('lower-right',(40,24),(24,44),radius_x=16,radius_y=20)
        self.add_arc('lower-left',(24,44),(8,24),radius_x=16,radius_y=20)
        self.add_contour('shield','roof-1','roof-2','roof-3','roof-4','lower-right','lower-left',closed=True)
        self.box('screen',17,16,31,26,2)
        self.add_line('neck',(24,26),(24,34))
        self.add_polyline('foot',(20,34),(24,34),(28,34))
        self.relate('connect','screen','neck')
        self.relate('connect','neck','foot')
''','A computer display and stand enclosed by a protective shield.','shield, monitor','Lower screen bezel separator omitted and tapered stand reduced to one neck stroke to preserve the nested monitor and shield.'),
('SQUARE', '''        # Large rounded display with an 8-unit bottom bezel and tapered pedestal.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right-1',(42,10),(42,26))
        self.add_line('right-2',(42,26),(42,30))
        self.add_arc('br',(42,30),(38,34),radius_x=4)
        bottom=[(38,34),(29,34),(19,34),(10,34)]
        for i,(a,b) in enumerate(zip(bottom,bottom[1:])):self.add_line(f'bottom-{i}',a,b)
        self.add_arc('bl',(10,34),(6,30),radius_x=4)
        self.add_line('left-1',(6,30),(6,26))
        self.add_line('left-2',(6,26),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('display','top','tr','right-1','right-2','br','bottom-0','bottom-1','bottom-2','bl','left-1','left-2','tl',closed=True)
        self.add_line('bezel',(6,26),(42,26))
        self.relate('connect','display','bezel')
        for name,x1,x2 in [('left',19,17),('right',29,31)]:
            self.add_line('pedestal-'+name,(x1,34),(x2,42))
            self.relate('connect','display','pedestal-'+name)
        self.add_polyline('foot',(14,42),(17,42),(31,42),(34,42))
        self.relate('connect','foot','pedestal-left')
        self.relate('connect','foot','pedestal-right')
''','A desktop computer monitor with a bottom bezel and tapered stand.','monitor','No omissions; mirrored pedestal and rounded display retained.'),
]
for radius in (10,11,9):
    designs.append(('CIRCLE',f'''        # Concentric definition owns both radii and the common centre.
        for name,radius in [('outer',20),('inner',{radius})]:
            self.circle(name,24,24,radius)
''','Two concentric circular outlines.','circle-dot',f'Inner radius reduced to {radius} to maintain certified ink clearance. Both complete rings retained. Source stroke weight replaced by the required 4-unit stroke.'))
designs.append(('SQUARE', '''        # Human-reference vocabulary: rounded continuous hand silhouette; no detached head.
        # Paired raised outer fingers, two curled middle knuckles, thumb and three energy bolts.
        self.add_arc('index-cap',(8,18),(16,18),radius_x=4)
        self.add_line('index-inner',(16,18),(16,30))
        self.add_arc('middle-knuckle',(16,30),(24,30),radius_x=4)
        self.add_arc('ring-knuckle',(24,30),(32,30),radius_x=4)
        self.add_line('little-inner',(32,30),(32,18))
        self.add_arc('little-cap',(32,18),(40,18),radius_x=4)
        self.add_line('right-palm',(40,18),(40,26))
        self.add_arc('palm-right',(40,26),(24,42),radius_x=16)
        self.add_arc('palm-left',(24,42),(8,26),radius_x=16)
        self.add_line('left-palm',(8,26),(8,18))
        self.add_contour('hand','index-cap','index-inner','middle-knuckle','ring-knuckle','little-inner','little-cap','right-palm','palm-right','palm-left','left-palm',closed=True)
        self.add_line('thumb-top-1',(32,34),(24,34))
        self.add_arc('thumb-tip',(24,34),(24,42),radius_x=4,sweep=False)
        self.add_contour('thumb','thumb-top-1','thumb-tip')
        self.relate('connect','thumb','hand')
        self.add_line('finger-fold',(24,30),(24,34))
        self.relate('connect','finger-fold','hand')
        self.relate('connect','finger-fold','thumb')
        for name,points in [('left-bolt',[(6,8),(12,12),(6,12)]),('top-bolt',[(26,6),(22,10),(28,10),(24,14)]),('right-bolt',[(42,8),(36,12),(42,12)])]:
            self.add_polyline(name,*points)
''','A rock-concert horns hand gesture surrounded by three lightning marks.','hand-metal','All identifying parts retained; fine palm crease simplified to the thumb contour. Human references inspected: user.svg and full_body_ref.png; no isolated hand there, so hand-metal informs finger construction. No detached head/body gap applies.'))

for row,(key,body,subject,refs,omissions) in zip(rows,designs):
    d=Path(row['directory']);icon_id=row['icon_id']
    if (d/'result.json').exists(): continue
    attempt=d/'attempt-1'
    filename=icon_id.replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py'
    if (d/filename).exists() and not attempt.exists():
        attempt.mkdir()
        for f in [filename,'validation.txt',icon_id+'.svg','light-48.png','dark-48.png']:
            if (d/f).exists():shutil.copyfile(d/f,attempt/f)
    source=f'''"""{subject}
Plan: {omissions}
Lucide construction references: {refs}.
Keyshape {key}: {'radial ink radius 22 about (24,24)' if key=='CIRCLE' else '(4,4)-(44,44) ink' if key=='SQUARE' else '(6,2)-(42,46) ink' if key=='VRECT_L' else '(2,8)-(46,40) ink'}.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape

SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {icon_id!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}
{helpers}
    def build(self):
{body}
'''
    (d/filename).write_text(source)
    spec=importlib.util.spec_from_file_location('drawing_'+row['source_uuid'].replace('-',''),d/filename)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    try:
        icon=mod.Drawing();report=icon.validate_icon();(d/'validation.txt').write_text(report.describe())
        svg=icon.to_svg();(d/(icon_id+'.svg')).write_text(svg)
        for size in (48,240):
            light=d/f'light-{size}.png'
            cairosvg.svg2png(bytestring=svg.encode(),write_to=str(light),output_width=size,output_height=size,background_color='white')
            ImageOps.invert(Image.open(light).convert('RGB')).save(d/f'dark-{size}.png')
        row.update(validation_status=report.status,error_count=len(report.errors),warning_count=len(report.warnings))
        print(icon_id,report.describe())
    except Exception as exc:
        (d/'error.txt').write_text(repr(exc));row.update(validation_status='error',error=repr(exc));print(icon_id,repr(exc))
    row.update(keyshape=key,subject=subject,lucide_references=refs.split(', '),omissions=omissions,python_file=filename)
(ROOT/'batch-work.json').write_text(json.dumps(rows,indent=2))
s=Image.new('RGB',(720,900),'#dddddd');draw=ImageDraw.Draw(s)
for i,row in enumerate(rows):
    x=i%3*240;y=i//3*300;d=Path(row['directory'])
    for j,theme in enumerate(('light','dark')):
        p=d/f'{theme}-240.png'
        if not p.exists():continue
        im=Image.open(p);im.thumbnail((120,120));s.paste(im,(x+j*120,y));s.paste(Image.open(d/f'{theme}-48.png'),(x+j*120+36,y+136))
    draw.text((x+4,y+202),row['concept'],fill='black');draw.text((x+4,y+222),row['validation_status'],fill='black')
s.save(ROOT/'review-sheet.png')
