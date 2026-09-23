"""Explicit repairs selected after inspecting first validation and both themes."""
from pathlib import Path
import importlib.util
import json
import shutil
import textwrap

SOURCE_ICON_ID = '0c038416-c2a9-4ae0-ab80-a793e4a0b0c7'
SOURCE_PATH = 'icon_set/work/todo-references/playlist album_0c038416-c2a9-4ae0-ab80-a793e4a0b0c7.svg'
AUTHOR = 'gpt-6'
ROOT = Path(__file__).parent
s=importlib.util.spec_from_file_location('batch',ROOT/'author_batch.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)

BODIES = {
'plug-circle-xmark': '''
self.add_arc('ring-top',(6,24),(42,24),radius_x=18)
self.add_arc('ring-bottom',(24,42),(6,24),radius_x=18)
self.add_contour('ring','ring-bottom','ring-top')
cx=22; radius=6
self.add_polyline('plug-top',(cx-radius,25),(cx-4,25),(cx+4,25),(cx+radius,25))
self.add_line('plug-right',(cx+radius,25),(cx+radius,26))
self.add_arc('bowl-right',(cx+radius,26),(cx,32),radius_x=radius)
self.add_arc('bowl-left',(cx,32),(cx-radius,26),radius_x=radius)
self.add_line('plug-left',(cx-radius,26),(cx-radius,25))
self.add_contour('plug-bowl','plug-right','bowl-right','bowl-left','plug-left')
self.relate('connect','plug-bowl','plug-top')
for i,x in enumerate((cx-4,cx+4)):
    self.add_line(f'prong-{i}',(x,17),(x,25))
    self.relate('connect',f'prong-{i}','plug-top')
self.add_bezier('cable',(22,32),((22,37),(24,38),(24,42)))
self.relate('connect','cable','plug-bowl')
self.relate('connect','cable','ring')
self.add_polyline('cross-down',(34,34),(38,38),(42,42))
self.add_polyline('cross-up',(34,42),(38,38),(42,34))
self.relate('connect','cross-down','cross-up')
''',
'plugin': '''
self.add_line('frame-top',(14,4),(34,4))
self.add_arc('frame-tr',(34,4),(40,10),radius_x=6)
self.add_line('frame-right',(40,10),(40,34))
self.add_arc('frame-br',(40,34),(34,40),radius_x=6)
self.add_line('frame-bottom-1',(34,40),(24,40))
self.add_line('frame-bottom-2',(24,40),(14,40))
self.add_arc('frame-bl',(14,40),(8,34),radius_x=6)
self.add_line('frame-left',(8,34),(8,10))
self.add_arc('frame-tl',(8,10),(14,4),radius_x=6)
self.add_contour('frame','frame-top','frame-tr','frame-right','frame-br','frame-bottom-1','frame-bottom-2','frame-bl','frame-left','frame-tl',closed=True)
self.plug(top=22,bottom=31)
self.add_polyline('cable',(24,31),(24,40),(24,44))
self.relate('connect','cable','plug-bowl')
self.relate('connect','cable','frame')
''',
'police-polygraph': '''
self.rounded('monitor',8,4,40,44,4)
self.add_polyline('trace',(8,16),(15,16),(19,12),(25,20),(29,13),(32,16))
self.relate('connect','trace','monitor')
self.add_line('control-divider',(8,28),(40,28))
self.relate('connect','control-divider','monitor')
for i,x in enumerate((18,30)): self.add_dot(f'control-{i}',(x,36))
''',
'polyester': '''
self.add_polyline('sheet',(30,6),(10,6),(6,10),(6,38),(10,42),(38,42),(42,38),(42,18),(30,6))
self.add_polyline('fold',(30,6),(30,18),(42,18))
self.relate('connect','sheet','fold')
# Reduced repeated weave: three vertical strands and two horizontal strands.
xs=(14,22,30); ys=(26,34)
for i,x in enumerate(xs): self.add_line(f'vertical-{i}',(x,26),(x,34))
for j,y in enumerate(ys):
    self.add_polyline(f'horizontal-{j}',*((x,y) for x in xs))
    for i in range(3): self.relate('connect',f'vertical-{i}',f'horizontal-{j}')
''',
'pregnancy-ultrasound-baby': '''
self.add_line('fan-left',(4,28),(24,8))
self.add_line('fan-right',(24,8),(44,28))
self.add_arc('fan-bottom',(44,28),(4,28),radius_x=20,radius_y=12)
self.add_contour('fan','fan-left','fan-right','fan-bottom',closed=True)
self.add_bezier('fetus',(25,27),((25,24),(28,24),(28,27)),((28,31),(24,32),(20,31)),((16,30),(18,26),(21,27)),((22,28),(24,28),(25,27)))
self.add_contour('baby','fetus',closed=True)
''',
'pregnancy-vagina': '''
axis=24
for side,sign in [('left',1),('right',-1)]:
    def p(x,y): return (axis+sign*(x-axis),y)
    self.add_bezier('body-'+side,p(12,4),(p(15,16),p(8,16),p(8,28)),(p(8,38),p(9,42),p(11,44)))
self.add_bezier('heart-left',(24,27),((19,21),(14,27),(19,32)),((21,34),(22,36),(24,38)))
self.add_bezier('heart-right',(24,38),((26,36),(27,34),(29,32)),((34,27),(29,21),(24,27)))
self.add_contour('heart','heart-left','heart-right',closed=True)
self.add_line('pelvic-line',(24,38),(24,44))
self.relate('connect','heart','pelvic-line')
''',
'prescription-px-square': '''
self.rounded('frame',6,6,42,42,5)
self.add_polyline('r-upright',(16,33),(16,25),(16,15),(24,15))
self.add_arc('r-bowl',(24,15),(24,25),radius_x=5)
self.add_line('r-return',(24,25),(16,25))
self.relate('connect','r-upright','r-bowl')
self.relate('connect','r-upright','r-return')
self.relate('connect','r-bowl','r-return')
self.add_polyline('rx-down',(24,25),(28,29),(32,33))
self.add_polyline('rx-up',(24,33),(28,29),(32,25))
self.relate('connect','rx-down','rx-up')
self.relate('connect','rx-down','r-bowl')
self.relate('connect','rx-down','r-return')
''',
'programming-hold-code-2': '''
axis=24
self.add_polyline('code-left',(12,6),(6,12),(12,18))
self.add_polyline('code-right',(36,6),(42,12),(36,18))
self.add_line('code-slash',(26,6),(22,18))
for side,sign in [('left',1),('right',-1)]:
    def p(x,y): return (axis+sign*(x-axis),y)
    self.add_bezier('hand-'+side,p(12,42),(p(12,38),p(6,36),p(6,33)),(p(6,31),p(6,30),p(6,29)),(p(6,26),p(10,26),p(10,29)))
    self.add_line('finger-'+side,p(10,29),p(10,34))
    self.add_bezier('palm-'+side,p(10,34),(p(10,31),p(12,30),p(14,32)),(p(16,34),p(20,36),p(20,39)),(p(20,40),p(20,41),p(20,42)))
    self.add_contour('cupped-'+side,'hand-'+side,'finger-'+side,'palm-'+side)
''',
}

for e in m.ENTRIES:
    slug=e['icon_id'];d=Path(e['result_dir']);plan=json.loads((d/'plan.json').read_text());p=d/plan['python'];old=p.read_text();new=old
    if slug in BODIES:
        a=old.index('    def build(self):');b=old.index('    def circle(',a)
        new=old[:a]+'    def build(self):\n'+textwrap.indent(textwrap.dedent(BODIES[slug]).strip()+'\n','        ')+'\n'+old[b:]
    if slug=='playlist-album':
        new=new.replace("('note-left',17,32)","('note-left',17,31)").replace('(19,32),(19,18)','(19,31),(19,18)')
    if slug=='preferences':
        new=new.replace('(24,4),(24,12),(24,36),(24,44)', '(25,4),(25,12),(25,20),(25,32),(25,36),(25,44)')
        new=new.replace("'gear',(24,12)","'gear',(25,12)").replace('(29,35),(24,36)', '(29,35),(25,36)').replace("'gear-hub',(24,20),(24,32)","'gear-hub',(25,20),(25,32)")
    if slug in ('plugin','police-polygraph'):
        new=new.replace('keyshape = Keyshape.VRECT_M','keyshape = Keyshape.VRECT_L').replace('keyshape = Keyshape.SQUARE','keyshape = Keyshape.VRECT_L')
        plan['keyshape']='VRECT_L'
    if slug=='plugin': new=new.replace('r=8','r=7')
    if slug=='polyester': plan['omissions']='Three vertical strands retained; horizontal strand count reduced from three to two to leave legal clearance below the fold.'
    if new!=old:
        backup=d/'before-spacing-repair';backup.mkdir(exist_ok=True)
        for f in d.iterdir():
            if f.is_file() and (f==p or f.name=='validation.txt' or f.suffix in ('.svg','.png')):shutil.copy2(f,backup/f.name)
        p.write_text(new);(d/'plan.json').write_text(json.dumps(plan,indent=2)+'\n')
        m.export(e)
