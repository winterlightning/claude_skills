import importlib.util
import json
from pathlib import Path
import cairosvg
from PIL import Image, ImageOps, ImageDraw

AUTHOR = 'gpt-6'
SOURCE_ICON_ID = '5c963504-9db5-4ed1-bcfa-7f38ac3f5fb1'
SOURCE_PATH = 'icon_set/work/todo-references/chat medical cross left_5c963504-9db5-4ed1-bcfa-7f38ac3f5fb1.svg'
ROOT = Path(__file__).parent
rows = json.loads((ROOT / 'batch-work.json').read_text())

ring = '''        # Circle symbol owns its centre and radius; independent inner content.
        cx, cy, r = 24, 24, 20
        self.add_arc('ring-top', (cx-r,cy), (cx+r,cy), radius_x=r)
        self.add_arc('ring-bottom', (cx+r,cy), (cx-r,cy), radius_x=r)
        self.add_contour('ring', 'ring-top', 'ring-bottom', closed=True)
'''
designs = [
('SQUARE', '''        # Rounded speech enclosure, lower-left tail, and outlined medical cross.
        self.add_line('top', (10,6), (38,6))
        self.add_arc('tr', (38,6), (42,10), radius_x=4)
        self.add_line('right', (42,10), (42,34))
        self.add_arc('br', (42,34), (38,38), radius_x=4)
        tail = [(38,38),(18,38),(14,42),(14,38),(10,38)]
        for i,(a,b) in enumerate(zip(tail,tail[1:]),1): self.add_line(f'tail-{i}',a,b)
        self.add_arc('bl', (10,38), (6,34), radius_x=4)
        self.add_line('left', (6,34), (6,10))
        self.add_arc('tl', (6,10), (10,6), radius_x=4)
        self.add_contour('bubble', 'top','tr','right','br', 'tail-1','tail-2','tail-3','tail-4','bl','left','tl', closed=True)
        cx, cy, outer, stem = 24, 22, 7, 4
        pts = [(-stem,-outer),(stem,-outer),(stem,-stem),(outer,-stem),(outer,stem),(stem,stem),(stem,outer),(-stem,outer),(-stem,stem),(-outer,stem),(-outer,-stem),(-stem,-stem)]
        self.add_polyline('medical-cross', *((cx+x,cy+y) for x,y in pts), closed=True)
''', 'Square speech panel with lower-left tail and outlined medical cross.', 'message-circle-plus', 'Tail direction and outlined cross retained; no omissions.'),
('VRECT_L', '''        # Bound page and folded lower-right corner; repeated binding and checklist rows.
        self.add_polyline('page', (8,12),(40,12),(40,36),(32,44),(8,44), closed=True)
        self.add_polyline('fold', (32,44),(32,36),(40,36))
        self.relate('connect','page','fold')
        for i,x in enumerate((16,24,32)):
            self.add_line(f'binding-{i}', (x,4), (x,12))
            self.relate('connect', 'page', f'binding-{i}')
        for i,y in enumerate((22,34)):
            self.add_polyline(f'check-{i}', (16,y),(18,y+2),(22,y-2))
            if i == 0: self.add_line(f'entry-{i}', (30,y),(32,y))
''', 'A top-bound checklist with two checked rows and a folded corner.', 'clipboard-list', 'Reduced four binding strokes to three and omitted the second text stroke to leave room beside the folded corner; both checks retained.'),
('CIRCLE',ring+'''        # Symmetric dome with a shared top attachment and extended baseline.
        self.add_arc('dome-left',(16,24),(24,16),radius_x=8)
        self.add_arc('dome-right',(24,16),(32,24),radius_x=8)
        self.add_line('wall-right',(32,24),(32,30))
        self.add_line('base',(32,30),(16,30))
        self.add_line('wall-left',(16,30),(16,24))
        self.add_contour('bell','dome-left','dome-right','wall-right','base','wall-left',closed=True)
        self.add_line('finial',(24,13),(24,16))
        self.relate('connect','bell','finial')
        for side,x,end in [('left',16,14),('right',32,34)]:
            self.add_line('lip-'+side,(x,30),(end,30))
            self.relate('connect','bell','lip-'+side)
''','A dome bell within a circular button.','bell','All defining parts retained.'),
('CIRCLE',ring+'''        # Previous-track control: separate stop bar and left-pointing triangle.
        self.add_line('stop-bar',(14,18),(14,30))
        self.add_polyline('previous',(22,24),(31,16),(31,32),closed=True)
''','A circular previous-track control with bar and left triangle.','circle-play','All defining parts retained.'),
('CIRCLE',ring+'''        # Basket quadrilateral with handle continuing the right slope; paired wheel dots.
        self.add_polyline('basket',(15,19),(31,19),(28,27),(18,27),closed=True)
        self.add_line('handle',(31,19),(32,16))
        self.relate('connect','basket','handle')
        for i,x in enumerate((20,28)):
            self.add_dot(f'wheel-{i}',(x,35))
''','A shopping cart basket and two wheels within a circle.','shopping-cart','All defining parts retained; wheels remain dots as in reference.'),
('CIRCLE',ring+'''        # Open C currency mark and rising slash crossing at its endpoints.
        self.add_arc('c-upper',(29,14),(15,24),radius_x=10,radius_y=10,sweep=False)
        self.add_arc('c-lower',(15,24),(29,34),radius_x=10,radius_y=10,sweep=False)
        self.add_contour('currency-c','c-upper','c-lower')
        self.add_line('slash',(18,33),(29,14))
        self.relate('connect','currency-c','slash')
''','A slashed C currency symbol within a circle.','circle-play','No useful local match for the currency glyph; circle-play informs only enclosure.'),
]
for direction in ('down','right','up','west'):
    designs.append(('CIRCLE',ring+f'''        # One concave arrowhead; rotations preserve the paired shoulders.
        direction = {direction!r}
        points = [(-8,-7),(0,-2),(8,-7),(0,10)]
        def orient(x,y):
            if direction == 'up': return (-x,-y)
            if direction == 'right': return (y,-x)
            if direction == 'west': return (-y,x)
            return (x,y)
        self.add_polyline('cursor', *((24+a,24+b) for a,b in (orient(x,y) for x,y in points)), closed=True)
''',f'A concave {direction}-pointing cursor within a circle.','circle-play','All defining parts retained; intentional directional asymmetry.'))
designs.extend([
('CIRCLE','''        # Eight short tangent dashes use shared cardinal and diagonal definitions, rotated by quarter-turns.
        # Dash count reduced to maintain the required clearance between independent arcs.
        for i in range(4):
            def turn(x,y):
                for _ in range(i): x,y=-y,x
                return (24+x,24+y)
            self.add_line(f'cardinal-{i}',turn(-3,-19),turn(3,-19))
            self.add_line(f'diagonal-{i}',turn(12,-16),turn(16,-12))
''','A dashed circular outline.','circle-dashed','Reduced dash count to eight for required separation; straight short tangent strokes follow the circular arrangement.'),
('CIRCLE',ring+'''        # Kip currency letter with central junction and a horizontal crossing bar.
        self.add_line('stem-upper',(19,14),(19,24))
        self.add_line('stem-lower',(19,24),(19,34))
        self.add_line('arm-upper',(19,24),(30,15))
        self.add_line('arm-lower',(19,24),(30,33))
        self.add_line('bar-left',(14,24),(19,24))
        self.add_line('bar-right',(19,24),(33,24))
        members=['stem-upper','stem-lower','arm-upper','arm-lower','bar-left','bar-right']
        for i,a in enumerate(members):
            for b in members[i+1:]: self.relate('connect',a,b)
''','A Lao kip currency mark within a circle.','circle-play','No useful local match for the currency glyph; circle-play informs only enclosure.')
])

for row,(key,body,subject,lucide,notes) in zip(rows,designs):
    d=Path(row['directory']); icon_id=row['icon_id']
    filename=icon_id.replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py'
    source=f'''"""{subject}
Construction: {notes}
Lucide construction reference: {lucide}; coherent arcs and independent enclosed content.
Keyshape {key}: {'radial ink radius 22, centre (24,24)' if key=='CIRCLE' else '(4,4)-(44,44) ink' if key=='SQUARE' else '(6,2)-(42,46) ink'}.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

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

    def build(self):
{body}
'''
    (d/filename).write_text(source)
    spec=importlib.util.spec_from_file_location('drawing_'+row['source_uuid'].replace('-',''),d/filename)
    mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
    icon=mod.Drawing(); report=icon.validate_icon()
    (d/'validation.txt').write_text(report.describe())
    svg=icon.to_svg();(d/(icon_id+'.svg')).write_text(svg)
    for size in (48,240):
        light=d/f'light-{size}.png'
        cairosvg.svg2png(bytestring=svg.encode(),write_to=str(light),output_width=size,output_height=size,background_color='white')
        ImageOps.invert(Image.open(light).convert('RGB')).save(d/f'dark-{size}.png')
    row.update(keyshape=key,subject=subject,lucide_reference=lucide,omissions=notes,python_file=filename,validation_status=report.status)
    print(icon_id,report.status,report.describe())
(ROOT/'batch-work.json').write_text(json.dumps(rows,indent=2))
sheet=Image.new('RGB',(960,960),'#dddddd'); draw=ImageDraw.Draw(sheet)
for i,row in enumerate(rows):
    x=i%4*240;y=i//4*320;d=Path(row['directory'])
    for j,theme in enumerate(('light','dark')):
        im=Image.open(d/f'{theme}-240.png');im.thumbnail((120,120));sheet.paste(im,(x+j*120,y))
        sheet.paste(Image.open(d/f'{theme}-48.png'),(x+j*120+36,y+140))
    draw.text((x+4,y+206),row['concept'],fill='black')
    draw.text((x+4,y+225),row['validation_status'],fill='black')
sheet.save(ROOT/'review-sheet.png')
