"""Folder-only authoring for the supplied batch, in input order."""
import json
import textwrap
from pathlib import Path

AUTHOR = 'gpt-6'
SOURCE_ICON_ID = '8e659963-5f68-4c80-963b-528218ccf29f'
SOURCE_PATH = 'icon_set/work/todo-references/award wall_8e659963-5f68-4c80-963b-528218ccf29f.svg'
ROOT = Path(__file__).parent

HELPERS = '''
    def circle(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name, name+'-top', name+'-bottom', closed=True)

    def box(self, name, left, top, right, bottom, radius=4):
        r = radius
        points = [(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),
                  (right-r,bottom),(left+r,bottom),(left,bottom-r),(left,top+r)]
        members = []
        for i, start in enumerate(points):
            end = points[(i+1)%8]
            part = f'{name}-{i}'
            if i%2:
                self.add_arc(part,start,end,radius_x=r)
            else:
                self.add_line(part,start,end)
            members.append(part)
        self.add_contour(name,*members,closed=True)
'''

# Each body is a fresh drawing in final SOLO48 coordinates.
DESIGNS = {
'award wall': ('VRECT_L', 'A blank pointed award pennant suspended from a wall rail.',
 'Upright pennant; shared axis 24 controls the hanger and lower point; rail joins the two side walls.',
 'rectangle-horizontal: a coherent contour with clean corners; preserve the angular pennant tips.', [], '''
axis = 24
self.add_polyline('hanger',(12,12),(axis,4),(36,12))
self.add_polyline('pennant',(12,12),(12,34),(axis,44),(36,34),(36,12))
for i,(a,b) in enumerate([(8,12),(12,36),(36,40)]):
    self.add_line(f'rail-{i}',(a,12),(b,12))
for rail in ('rail-0','rail-1'):
    self.relate('connect',rail,'hanger-1')
    self.relate('connect',rail,'pennant-1')
for rail in ('rail-1','rail-2'):
    self.relate('connect',rail,'hanger-2')
    self.relate('connect',rail,'pennant-4')
'''),
'bacteria magnifying glass': ('SQUARE', 'A magnifying glass enclosing scattered microbial dots.',
 'Circular lens owns a diagonal handle attachment and a triangular group of three dots.',
 'search: a circular lens with one attached diagonal handle.',
 ['Reduced seven tiny microbial specks to three legible dots to preserve clearance.'], '''
cx, cy, radius = 21, 21, 15
join, opposite = (cx+9,cy+12),(cx-9,cy-12)
self.add_arc('lens-a',join,opposite,radius_x=radius)
self.add_arc('lens-b',opposite,join,radius_x=radius)
self.add_contour('lens','lens-a','lens-b',closed=True)
self.add_line('handle',join,(42,42))
for arc in ('lens-a','lens-b'):
    self.relate('connect',arc,'handle')
for i,p in enumerate([(17,17),(25,17),(21,25)]):
    self.add_dot(f'microbe-{i}',p)
'''),
'badge 1': ('SQUARE', 'An empty eight-point award badge with stepped shoulders.',
 'One closed badge contour; four identical quarter-turn groups around the shared center.',
 'badge: repeated radial symmetry; retain the supplied angular shoulders rather than circular scallops.', [], '''
axis = 24
quarter = [(0,-18),(6,-12),(12,-12),(12,-6)]
points=[]
for turn in range(4):
    for x,y in quarter:
        for _ in range(turn):
            x,y=-y,x
        points.append((axis+x,axis+y))
self.add_polyline('badge',*points,closed=True)
'''),
'badge arrow': ('VRECT_L', 'A blank upright badge with a peaked arrow-like top.',
 'One symmetric peaked enclosure; paired lower quarter-circle corners with radius 4.',
 'rectangle-horizontal: tangent quarter-circle transitions at the lower corners.', [], '''
axis=24
self.add_polyline('peak',(8,40),(8,18),(axis,4),(40,18),(40,40))
self.add_arc('lower-right',(40,40),(36,44),radius_x=4)
self.add_line('bottom',(36,44),(12,44))
self.add_arc('lower-left',(12,44),(8,40),radius_x=4)
self.add_contour('outline','peak-1','peak-2','peak-3','peak-4','lower-right','bottom','lower-left',closed=True)
'''),
'baggage weight': ('SQUARE', 'A suitcase on a baseline beneath a floating weighing dial.',
 'Symmetric dial and case around x24; the needle is deliberately diagonal; handle joins the case roof.',
 'search: a round dial; rectangle-horizontal: rounded case corners.',
 ['Reduced the two suitcase stripes to one to reserve room for the handle and dial.'], '''
self.circle('dial',24,14,8)
self.add_line('needle',(24,14),(27,11))
self.add_polyline('handle',(20,32),(20,26),(28,26),(28,32))
self.add_line('roof-left',(16,32),(20,32))
self.add_line('roof-middle',(20,32),(28,32))
self.add_line('roof-right',(28,32),(32,32))
self.add_arc('case-top-right',(32,32),(36,36),radius_x=4)
self.add_line('case-right',(36,36),(36,38))
self.add_arc('case-bottom-right',(36,38),(32,42),radius_x=4)
self.add_line('case-bottom',(32,42),(16,42))
self.add_arc('case-bottom-left',(16,42),(12,38),radius_x=4)
self.add_line('case-left',(12,38),(12,36))
self.add_arc('case-top-left',(12,36),(16,32),radius_x=4)
self.add_contour('case','roof-left','roof-middle','roof-right','case-top-right','case-right','case-bottom-right','case-bottom','case-bottom-left','case-left','case-top-left',closed=True)
for a,b in [('handle-1','roof-left'),('handle-1','roof-middle'),('handle-3','roof-middle'),('handle-3','roof-right')]:
    self.relate('connect',a,b)
self.add_line('stripe',(21,37),(27,37))
self.add_line('ground-left',(6,42),(16,42))
self.add_line('ground-right',(32,42),(42,42))
for a in ('case-bottom','case-bottom-left'):
    self.relate('connect','ground-left',a)
for a in ('case-bottom','case-bottom-right'):
    self.relate('connect','ground-right',a)
'''),
'bathroom mirror': ('VRECT_L', 'A rounded rectangular bathroom mirror on a short central pedestal.',
 'Symmetric mirror outline and pedestal; a single diagonal reflection mark.',
 'rectangle-horizontal: equal-radius corners and tangent straight sides.',
 ['Reduced two close parallel reflection strokes to one.'], '''
self.add_line('top',(14,4),(34,4))
self.add_arc('tr',(34,4),(38,8),radius_x=4)
self.add_line('right',(38,8),(38,32))
self.add_arc('br',(38,32),(34,36),radius_x=4)
self.add_line('bottom-right',(34,36),(24,36))
self.add_line('bottom-left',(24,36),(14,36))
self.add_arc('bl',(14,36),(10,32),radius_x=4)
self.add_line('left',(10,32),(10,8))
self.add_arc('tl',(10,8),(14,4),radius_x=4)
self.add_contour('mirror','top','tr','right','br','bottom-right','bottom-left','bl','left','tl',closed=True)
self.add_line('reflection',(19,24),(27,16))
self.add_line('stem',(24,36),(24,44))
self.add_line('foot-left',(8,44),(24,44))
self.add_line('foot-right',(24,44),(40,44))
for other in ('bottom-right','bottom-left','foot-left','foot-right'):
    self.relate('connect','stem',other)
'''),
'binary': ('HRECT_L', 'The binary digits 010 above 001 in two aligned rows.',
 'Two rows at y14 and y34; column centers 8,24,40; every zero uses the same ellipse.',
 'No useful Lucide match for this exact six-glyph arrangement; shared ellipse geometry and regular spacing.',
 ['Removed the small lead-in serifs on each digit one.'], '''
columns=[8,24,40]
for row, digits in enumerate(('010','001')):
    cy=14+row*20
    for col,digit in enumerate(digits):
        cx=columns[col]
        name=f'digit-{row}-{col}'
        if digit=='0':
            self.circle(name,cx,cy,4,6)
        else:
            self.add_line(name,(cx,cy-6),(cx,cy+6))
'''),
'biology': ('VRECT_L', 'A round laboratory flask containing a pointed leaf.',
 'Symmetric flask with open neck and a centered diagonal leaf lens; neck and shoulders share endpoints.',
 'leaf: pointed leaf silhouette; search: coherent circular lower bowl.',
 ['Omitted the short inner leaf vein so the leaf opening remains legible.'], '''
self.add_line('neck-left',(20,4),(20,16))
self.add_arc('shoulder-left',(20,16),(8,28),radius_x=12,sweep=False)
self.add_arc('bowl',(8,28),(40,28),radius_x=16,sweep=False)
self.add_arc('shoulder-right',(40,28),(28,16),radius_x=12,sweep=False)
self.add_line('neck-right',(28,16),(28,4))
self.add_contour('flask','neck-left','shoulder-left','bowl','shoulder-right','neck-right')
for i,(a,b) in enumerate([(16,20),(20,28),(28,32)]):
    self.add_line(f'rim-{i}',(a,4),(b,4))
for side,ids in [('left',(0,1)),('right',(1,2))]:
    for i in ids:
        self.relate('connect','neck-'+side,f'rim-{i}')
self.add_arc('leaf-upper',(19,33),(29,23),radius_x=10)
self.add_arc('leaf-lower',(29,23),(19,33),radius_x=10)
self.add_contour('leaf','leaf-upper','leaf-lower',closed=True)
'''),
'blind file': ('VRECT_L', 'A document with a clipped upper corner and five braille-like dots.',
 'One file enclosure; a two-column dot series with the lower-right cell intentionally absent.',
 'file: clipped upper corner and coherent rounded lower corners; no added folded-corner line.', [], '''
self.add_line('top',(12,4),(30,4))
self.add_line('clip',(30,4),(40,14))
self.add_line('right',(40,14),(40,40))
self.add_arc('br',(40,40),(36,44),radius_x=4)
self.add_line('bottom',(36,44),(12,44))
self.add_arc('bl',(12,44),(8,40),radius_x=4)
self.add_line('left',(8,40),(8,8))
self.add_arc('tl',(8,8),(12,4),radius_x=4)
self.add_contour('page','top','clip','right','br','bottom','bl','left','tl',closed=True)
for row,count in enumerate((2,2,1)):
    for col in range(count):
        self.add_dot(f'dot-{row}-{col}',(18+col*10,14+row*10))
'''),
'board 1': ('HRECT_L', 'A blank standing board with a horizontal tray and two legs.',
 'Symmetric rounded top; continuous sides split at the tray junction; shared y30 tray.',
 'rectangle-horizontal: matching top corner arcs and straight sides.', [], '''
self.add_line('left-leg',(8,40),(8,30))
self.add_line('left-wall',(8,30),(8,12))
self.add_arc('tl',(8,12),(12,8),radius_x=4)
self.add_line('top',(12,8),(36,8))
self.add_arc('tr',(36,8),(40,12),radius_x=4)
self.add_line('right-wall',(40,12),(40,30))
self.add_line('right-leg',(40,30),(40,40))
self.add_contour('board','left-leg','left-wall','tl','top','tr','right-wall','right-leg')
for i,(a,b) in enumerate([(4,8),(8,40),(40,44)]):
    self.add_line(f'tray-{i}',(a,30),(b,30))
for side,ids in [('left',(0,1)),('right',(1,2))]:
    for part in ('wall','leg'):
        for i in ids:
            self.relate('connect',f'{side}-{part}',f'tray-{i}')
'''),
'bomb explode': ('SQUARE', 'A round fused bomb with an explosion burst over its lower-right side.',
 'Asymmetric composition: open bomb silhouette, attached two-arc fuse, and one angular burst outline.',
 'bomb: round shell and short fuse neck; retain the supplied foreground explosion.', [], '''
self.add_arc('shell-left',(18,42),(18,16),radius_x=12,radius_y=13)
self.add_polyline('neck',(18,16),(18,10),(22,10),(26,10),(26,18))
self.add_arc('shell-right',(26,18),(34,28),radius_x=12)
self.add_contour('shell','shell-left','neck-1','neck-2','neck-3','neck-4','shell-right')
self.add_arc('fuse-rise',(22,10),(30,6),radius_x=8,radius_y=4)
self.add_arc('fuse-fall',(30,6),(42,10),radius_x=12,radius_y=4)
self.add_contour('fuse','fuse-rise','fuse-fall')
for member in ('neck-2','neck-3'):
    self.relate('connect','fuse-rise',member)
self.add_polyline('burst',(30,24),(33,30),(42,26),(37,34),(42,38),(34,38),(32,42),(28,36),(22,40),(25,32),(22,28),(29,29),closed=True)
'''),
}

for row in json.loads((ROOT/'batch-inputs.json').read_text()):
    shape,description,plan,lucide,omissions,body=DESIGNS[row['concept']]
    out=Path(row['out'])
    filename=row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py'
    source=f'''"""{description}
Plan: {plan}
Construction reference: {lucide}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}

class Drawing(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{shape}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}
    # Bounds are supplied by the contract; geometry below is authored to them.
    planned_visible_bounds = Keyshape.{shape}.bounds_for(Profile.SOLO48)
{HELPERS}
    def build(self):
'''+textwrap.indent(textwrap.dedent(body).strip()+'\n','        ')
    (out/filename).write_text(source)
    (out/'design-notes.json').write_text(json.dumps(dict(description=description,plan=plan,keyshape=shape,lucide_reference=lucide,omissions=omissions,module=filename),indent=2)+'\n')
    print(row['concept'],filename)
