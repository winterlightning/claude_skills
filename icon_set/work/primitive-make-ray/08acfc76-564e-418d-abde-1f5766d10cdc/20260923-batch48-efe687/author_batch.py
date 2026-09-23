"""Standalone batch 48 authoring; never registers or publishes artwork."""
from pathlib import Path
import json, importlib.util, textwrap
import cairosvg

AUTHOR = 'gpt-6'
HERE = Path(__file__).parent
INPUTS = json.loads((HERE / 'batch-inputs.json').read_text())
SOURCE_ICON_ID = tuple(row['source_uuid'] for row in INPUTS)
SOURCE_PATH = tuple(row['reference_path'] for row in INPUTS)

HELPERS = '''
    def circle(self, name, x, y, r):
        self.add_arc(name+'-upper', (x-r,y), (x+r,y), radius_x=r)
        self.add_arc(name+'-lower', (x+r,y), (x-r,y), radius_x=r)
        self.add_contour(name, name+'-upper', name+'-lower', closed=True)

    def box(self, name, left, top, right, bottom, r):
        # One rounded rectangle definition owns all matching corners.
        points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members=[]
        for i,start in enumerate(points):
            end=points[(i+1)%8]; member=f'{name}-{i}'
            if i%2: self.add_arc(member,start,end,radius_x=r)
            else: self.add_line(member,start,end)
            members.append(member)
        self.add_contour(name,*members,closed=True)

    def cross(self, name, x, y, r, diagonal=False):
        ends = [(-r,-r),(r,r),(r,-r),(-r,r)] if diagonal else [(-r,0),(r,0),(0,-r),(0,r)]
        for i,(dx,dy) in enumerate(ends):
            self.add_line(f'{name}-{i}',(x,y),(x+dx,y+dy))
        self.relate('connect',*[f'{name}-{i}' for i in range(4)])

    def bust_body(self):
        # Shared shoulder radii; badge occludes the right shoulder and hem.
        self.add_line('body-left',(6,42),(6,40))
        self.add_arc('shoulder-left',(6,40),(16,30),radius_x=10)
        self.add_line('shoulder-top',(16,30),(24,30))
        self.add_arc('shoulder-right',(24,30),(30,36),radius_x=6)
        self.add_contour('shoulders','body-left','shoulder-left','shoulder-top','shoulder-right')
        self.add_line('hem',(6,42),(36,42))
        self.circle('badge',36,36,6)
        self.relate('connect','hem','body-left')
        self.relate('connect','hem','badge-lower')
        self.relate('connect','shoulder-right','badge-upper','badge-lower')
'''

# Each entry: chosen envelope, subject/plan, construction reference, omissions, body.
SPECS = [
('SQUARE','Rounded square enclosing a centered X; shared axis and four joined arms.', 'square-x: rounded enclosure and crossing diagonals', [], '''
self.box('frame',6,6,42,42,5)
self.cross('x',24,24,8,True)
'''),
('SQUARE','Rounded square enclosing the horizontal dash visible in the source.', 'square-x: rounded enclosure', [], '''
self.box('frame',6,6,42,42,5)
self.add_line('dash',(16,24),(32,24))
'''),
('SQUARE','Rounded square with a horizontal bar above a small outlined circle.', 'square-x and circle: rounded frame and circular mark', [], '''
self.box('frame',6,6,42,42,5)
self.add_line('bar',(16,16),(32,16))
self.circle('ring',24,31,3)
'''),
('SQUARE','Hand grips a phone while two arrows point inward; four repeated fingers and a curved thumb.', 'smartphone and move-horizontal: rounded phone and arrow strokes', [], '''
self.box('phone',16,6,34,42,4)
# Four finger capsules, sharing the same width and pitch.
for i in range(4):
    self.box(f'finger-{i}',8,16+6*i,22,22+6*i,3)
self.add_bezier('thumb',(34,18),((40,18),(36,30),(42,30)))
self.add_line('wrist',(34,40),(42,42))
self.add_polyline('left-arrow',(6,6),(10,10),(6,14))
self.add_line('left-shaft',(6,10),(10,10))
self.relate('connect','left-arrow','left-shaft')
self.add_polyline('right-arrow',(42,6),(38,10),(42,14))
self.add_line('right-shaft',(38,10),(42,10))
self.relate('connect','right-arrow','right-shaft')
self.relate('connect','thumb','phone-2')
'''),
('VRECT_M','Phone with paired inward-bowing squeeze marks and a bottom separator.', 'smartphone: rounded vertical enclosure', [], '''
self.box('phone',10,4,38,44,4)
self.add_line('footer',(10,36),(38,36))
self.relate('connect','footer','phone-2','phone-6')
for side in (-1,1):
    outer=24+side*8; inner=24+side*12
    self.add_bezier(f'pressure-{side}',(outer,13),((outer-side*7,19),(outer-side*7,23),(outer,29)))
    self.add_bezier(f'echo-{side}',(inner,17),((inner-side*3,20),(inner-side*3,22),(inner,25)))
'''),
('SQUARE','Closed surgical scissors beside a rotated female symbol.', 'circle: round scissor handles; no useful complete Lucide subject match', [], '''
self.circle('handle-left',12,36,6)
self.circle('handle-right',28,36,6)
self.add_polyline('blades',(18,36),(18,24),(20,6),(22,24),(22,36))
self.add_line('blade-joint',(18,28),(22,24))
self.relate('connect','blades','handle-left','handle-right','blade-joint')
self.add_arc('female-bowl',(30,14),(36,32),radius_x=10)
self.add_line('female-stem',(36,16),(42,10))
self.add_polyline('female-cross',(36,6),(40,10),(42,12))
self.relate('connect','female-stem','female-cross')
'''),
('SQUARE','A descending staircase of stacked column cells with two downward curved arrows.', 'No useful Lucide subject match; shared cell widths and repeated arrow construction', [], '''
self.add_polyline('column-top',(6,6),(14,6),(14,22),(6,22),closed=True)
self.add_line('divider-top',(6,14),(14,14))
self.relate('connect','divider-top','column-top')
self.add_polyline('column-middle',(14,22),(22,22),(22,34),(14,34),closed=True)
self.add_line('divider-middle',(14,28),(22,28))
self.relate('connect','divider-middle','column-middle')
self.relate('connect','column-top','column-middle')
self.add_polyline('column-bottom',(22,34),(30,34),(30,42),(22,42),closed=True)
self.relate('connect','column-middle','column-bottom')
for name,x,y in [('first',28,10),('second',36,26)]:
    self.add_arc(name+'-turn',(x,y),(x+6,y+6),radius_x=6)
    self.add_arc(name+'-down',(x+6,y+6),(x,y+12),radius_x=6)
    self.add_contour(name+'-curve',name+'-turn',name+'-down')
    self.add_polyline(name+'-tip',(x+4,y+8),(x,y+12),(x+4,y+16))
    self.relate('connect',name+'-down',name+'-tip')
'''),
('VRECT_L','Three round anthers on radiating filaments above a capsule base.', 'circle: circular anthers; shared mirrored filament placement', [], '''
self.box('base',16,36,32,44,4)
self.circle('anther-center',24,6,2)
for side in (-1,1):
    x=24+side*14
    self.circle(f'anther-{side}',x,10,2)
    self.add_bezier(f'filament-{side}',(x,12),((x,16),(24+side*4,22),(24,30)))
    self.relate('connect',f'anther-{side}',f'filament-{side}')
self.add_line('stem',(24,8),(24,36))
self.relate('connect','stem','anther-center','base')
for side in (-1,1): self.relate('connect','stem',f'filament-{side}')
'''),
('SQUARE','Open book at upper left beside a four-node learning network.', 'book-open and network: central book fold and repeated connected nodes', [], '''
self.add_polyline('book',(6,24),(6,6),(16,11),(26,6),(26,17))
self.add_line('book-bottom',(6,24),(13,28))
self.add_line('fold',(16,11),(16,23))
self.relate('connect','book','book-bottom','fold')
self.circle('hub',23,29,5)
for name,x,y,r in [('top',36,19,3),('right',39,31,3),('bottom',34,39,3)]:
    self.circle(name,x,y,r)
self.add_line('hub-top',(27,26),(33,21))
self.add_line('hub-right',(28,29),(36,31))
self.add_line('hub-bottom',(27,32),(31,37))
self.add_line('top-right',(38,21),(40,28))
self.add_line('right-bottom',(38,34),(36,37))
'''),
('SQUARE','Woman with a shoulder-length bob and circular lower-right relationship badge.', 'human_ref/user.svg: circular jaw and broad curved shoulders', [], '''
self.bust_body()
self.add_arc('jaw',(14,14),(30,14),radius_x=8,sweep=False)
self.add_bezier('fringe',(14,14),((19,14),(23,13),(25,10)),((27,13),(28,14),(30,14)))
self.add_contour('face','jaw','fringe',closed=True)
self.add_arc('hair-top',(10,18),(34,18),radius_x=12)
self.add_bezier('hair-right',(34,18),((34,22),(36,28),(30,28)))
self.add_bezier('hair-left',(14,28),((8,28),(10,22),(10,18)))
self.add_contour('hair','hair-left','hair-top','hair-right')
# Jaw lowest y=22; shoulder top y=30: exactly 4 units of ink gap.
'''),
('SQUARE','Young man with swept hair and circular lower-right relationship badge.', 'human_ref/user.svg: circular face and smooth broad shoulders', [], '''
self.bust_body()
self.circle('head',22,14,8)
self.add_bezier('hairline',(14,14),((17,8),(20,14),(26,10)),((28,10),(29,12),(30,14)))
# Head bottom y=22, own shoulders y=30: exactly 4 units of ink gap.
self.relate('connect','head','hairline')
'''),
('SQUARE','Bald male bust with circular lower-right relationship badge.', 'human_ref/user.svg: round head, broad shoulders, detached 4-unit ink gap', [], '''
self.bust_body()
self.circle('head',22,14,8)
# Head bottom y=22; shoulder centerline y=30; ink gap=30-22-4=4.
'''),
('SQUARE','Girl with long hair and circular lower-right relationship badge.', 'human_ref/user.svg: circular jaw and broad shoulder construction', [], '''
self.bust_body()
self.add_arc('jaw',(14,14),(30,14),radius_x=8,sweep=False)
self.add_bezier('fringe',(14,14),((19,14),(23,13),(25,10)),((27,13),(28,14),(30,14)))
self.add_contour('face','jaw','fringe',closed=True)
self.add_arc('hair-top',(10,18),(34,18),radius_x=12)
self.add_line('hair-left',(10,18),(8,32))
self.add_line('hair-right',(34,18),(36,28))
self.relate('connect','hair-left','hair-top')
self.relate('connect','hair-right','hair-top')
# Jaw bottom y=22; shoulder top y=30 gives the required 4-unit ink gap.
'''),
('CIRCLE','Circular story button surrounded by a broken outer ring.', 'circle: concentric radial geometry', ['Two very short outer dashes consolidated into one dash to retain open gaps.'], '''
self.circle('inner',24,24,11)
self.add_arc('outer-top-right',(24,4),(44,24),radius_x=20)
self.add_arc('outer-bottom',(44,24),(4,24),radius_x=20)
self.add_contour('outer','outer-top-right','outer-bottom')
self.add_arc('dash',(8,12),(12,8),radius_x=20)
'''),
('SQUARE','Round strainer bowl with a diagonal open handle extending down-left.', 'circle: circular bowl; intentional diagonal handle asymmetry', [], '''
# Bowl radius 15 about (27,21); Pythagorean attachment points lie on the rim.
self.add_arc('rim-upper',(15,30),(27,6),radius_x=15)
self.add_arc('rim-right',(27,6),(42,21),radius_x=15)
self.add_arc('rim-lower',(42,21),(18,33),radius_x=15)
self.add_arc('rim-attachment',(18,33),(15,30),radius_x=15)
self.add_contour('rim','rim-upper','rim-right','rim-lower','rim-attachment',closed=True)
self.add_polyline('handle',(15,30),(6,39),(9,42),(18,33))
self.relate('connect','handle','rim-upper','rim-lower','rim-attachment')
'''),
('SQUARE','Standing person beside a map pin and short road line.', 'human_ref/full_body_ref.png and map-pin: outlined head, connected limbs, pointed marker', [], '''
self.circle('head',14,10,4)
self.add_line('torso',(14,22),(14,32))
self.add_polyline('arms',(6,30),(6,26),(14,22),(22,26),(22,30))
self.add_polyline('legs',(10,42),(10,34),(14,32),(18,34),(18,42))
self.relate('connect','torso','arms','legs')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
self.add_arc('pin-top',(26,14),(42,14),radius_x=8)
self.add_polyline('pin-tip',(42,14),(34,28),(26,14))
self.add_contour('pin','pin-top','pin-tip-1','pin-tip-2',closed=True)
self.add_dot('pin-center',(34,14))
self.add_line('road',(28,34),(42,34))
self.add_line('ground',(6,42),(42,42))
self.relate('connect','ground','legs')
# 22-(10+4)-4 = 4 ink units at the actual vertical torso junction.
'''),
('SQUARE','Side-profile head containing plus, minus and multiplication marks.', 'No useful Lucide profile-head match; brain inspected but its lobes do not apply', [], '''
self.add_arc('skull-top',(10,22),(26,6),radius_x=16)
self.add_arc('skull-back',(26,6),(42,22),radius_x=16)
self.add_bezier('back-neck',(42,22),((42,31),(34,31),(34,38)))
self.add_line('neck-right',(34,38),(34,42))
self.add_polyline('face',(10,22),(6,29),(10,30),(10,35))
self.add_arc('chin',(10,35),(14,39),radius_x=4,sweep=False)
self.add_polyline('neck-left',(14,39),(20,39),(20,42))
self.add_contour('profile','neck-left-2') if False else None
self.relate('connect','skull-top','skull-back')
self.relate('connect','skull-back','back-neck')
self.relate('connect','back-neck','neck-right')
self.relate('connect','face','skull-top','chin')
self.relate('connect','chin','neck-left')
self.cross('plus',24,16,3)
self.add_line('minus',(18,28),(23,28))
self.cross('times',33,28,2,True)
'''),
('SQUARE','Rounded speech bubble with a descending right tail and rising slash.', 'message-square: rounded speech enclosure and angular tail', [], '''
self.add_line('top',(11,6),(37,6))
self.add_arc('top-right',(37,6),(42,11),radius_x=5)
self.add_line('right',(42,11),(42,29))
self.add_arc('bottom-right',(42,29),(37,34),radius_x=5)
self.add_polyline('tail',(37,34),(36,34),(36,42),(28,34),(11,34))
self.add_arc('bottom-left',(11,34),(6,29),radius_x=5)
self.add_line('left',(6,29),(6,11))
self.add_arc('top-left',(6,11),(11,6),radius_x=5)
self.add_contour('bubble','top','top-right','right','bottom-right','tail-1','tail-2','tail-3','tail-4','bottom-left','left','top-left',closed=True)
self.add_line('slash',(16,25),(31,14))
'''),
]

def author():
    for row,(keyshape,plan,reference,omissions,body) in zip(INPUTS,SPECS):
        out=Path(row['result_dir'])
        if (out/'result.json').exists(): continue
        module_name=row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')
        src=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}
PLAN = {plan!r}
CONSTRUCTION_REFERENCE = {reference!r}

class Drawing(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}
{HELPERS}
    def build(self):
'''+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n'
        (out/(module_name+'.py')).write_text(src)
        row.update(module=module_name+'.py',keyshape=keyshape,subject=plan,construction_reference=reference,omissions=omissions)
    (HERE/'batch-inputs.json').write_text(json.dumps(INPUTS,indent=2))

def export():
    rows=json.loads((HERE/'batch-inputs.json').read_text())
    for i,row in enumerate(rows):
        out=Path(row['result_dir'])
        if (out/'result.json').exists(): continue
        try:
            spec=importlib.util.spec_from_file_location('candidate_'+str(i),out/row['module'])
            module=importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
            icon=module.Drawing(); report=icon.validate_icon()
            (out/'validation.txt').write_text(report.describe())
            row['validation_status']=report.status
            svg=icon.to_svg(); (out/(row['icon_id']+'.svg')).write_text(svg)
            for theme,bg,negative in [('light','white',False),('dark','#181818',True)]:
                for size in (48,192):
                    cairosvg.svg2png(bytestring=svg.encode(),output_width=size,output_height=size,
                        background_color=bg,negate_colors=negative,write_to=str(out/f'{theme}-{size}.png'))
            print(i+1,row['concept'],report.status,flush=True)
        except Exception as exc:
            row['validation_status']='error'; row['error']=repr(exc)
            (out/'validation.txt').write_text(repr(exc)); print(i+1,repr(exc),flush=True)
    (HERE/'batch-inputs.json').write_text(json.dumps(rows,indent=2))

if __name__=='__main__':
    import sys
    if 'export' not in sys.argv: author()
    export()
