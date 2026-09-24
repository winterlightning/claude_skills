"""Fresh revised SOLO48 candidates for round 2 batch 2; folder-only."""
from pathlib import Path
import json,importlib.util,textwrap
SOURCE_ICON_ID='8e659963-5f68-4c80-963b-528218ccf29f'
SOURCE_PATH='icon_set/work/todo-references/award wall_8e659963-5f68-4c80-963b-528218ccf29f.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ENTRIES=json.loads((ROOT/'batch-inputs.json').read_text())
s=importlib.util.spec_from_file_location('export_utility',Path('icon_set/work/primitive-make-ray/08acfc76-564e-418d-abde-1f5766d10cdc/20260923T210601-batch48/author_batch.py'))
u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
HELPERS=u.HELPERS.split('    def portrait(')[0]+'''
    def browser(self):
        self.rounded('window',8,4,40,44,4,breaks={2:[(40,12)],6:[(8,12)]})
        self.add_line('header',(8,12),(40,12));self.relate('connect','header','window')

    def dollar(self,x,y):
        self.add_bezier('dollar',(x+4,y-6),((x+2,y-7),(x+1,y-7),(x,y-7)),((x-7,y-7),(x-7,y),(x,y)),((x+7,y),(x+7,y+7),(x,y+7)),((x-1,y+7),(x-2,y+7),(x-4,y+6)))
        self.add_line('stem-top',(x,y-8),(x,y-7));self.relate('connect','dollar','stem-top')
        self.add_line('stem-bottom',(x,y+7),(x,y+8));self.relate('connect','dollar','stem-bottom')

    def euro(self,x):
        self.add_bezier('euro',(x+3,22),((x-2,19),(x-8,21),(x-8,28)),((x-8,35),(x-2,37),(x+3,34)))
        self.add_polyline('crossbar',(x-11,28),(x-8,28),(x,28));self.relate('connect','euro','crossbar')
'''
SPECS={}
def put(n,key,subject,refs,omissions,body):SPECS[n]=(key,subject,refs,omissions,body)

put(2,'VRECT_L','A suitcase below a floating weighing dial.','gauge: circular dial and diagonal needle; luggage: joined top handle.','Both decorative suitcase stripes omitted to preserve the case opening.','''
self.circle('dial',24,12,8)
self.add_line('needle',(24,12),(26,10))
self.rounded('case',8,36,40,44,3,breaks={0:[(20,36),(28,36)]})
self.add_polyline('handle',(20,36),(20,28),(28,28),(28,36));self.relate('connect','handle','case')
self.add_polyline('ground',(8,44),(11,44),(37,44),(40,44));self.relate('connect','ground','case')
''')
put(3,'SQUARE','A band saw frame with a toothed wheel and base.','cog: repeated radial teeth and central hole; source determines the nested machine frame.','Tooth count reduced to six broad teeth; ledge shortened where occluded by the wheel.','''
self.add_polyline('frame-left',(8,34),(8,12))
self.add_arc('frame-tl',(8,12),(14,6),radius_x=6)
self.add_line('frame-top',(14,6),(34,6))
self.add_arc('frame-tr',(34,6),(40,12),radius_x=6)
self.add_line('frame-right',(40,12),(40,18))
self.add_contour('frame','frame-left-1','frame-tl','frame-top','frame-tr','frame-right')
self.contours=[c for c in self.contours if c.contour_id!='frame-left']
self.add_polyline('inner',(16,34),(16,14),(32,14),(32,18))
self.rounded('base',6,34,42,42,3,breaks={0:[(16,34)]})
self.relate('connect','inner','base')
self.add_polyline('wheel',(27,18),(33,18),(35,23),(40,22),(42,28),(38,32),(40,37),(34,40),(30,36),(25,38),(21,33),(24,29),(22,24),(27,23),closed=True)
self.circle('hub',31,29,3)
self.add_line('ledge',(16,26),(22,26));self.relate('connect','ledge','inner')
''')
put(4,'HRECT_M','An empty horizontal battery with a projecting positive terminal.','battery: rounded body and right terminal.','None.','''
self.rounded('body',4,10,36,38,4,breaks={2:[(36,18),(36,30)]})
self.add_line('terminal-top',(36,18),(41,18))
self.add_arc('terminal-tr',(41,18),(44,21),radius_x=3)
self.add_line('terminal-right',(44,21),(44,27))
self.add_arc('terminal-br',(44,27),(41,30),radius_x=3)
self.add_line('terminal-bottom',(41,30),(36,30))
self.add_contour('terminal','terminal-top','terminal-tr','terminal-right','terminal-br','terminal-bottom')
self.relate('connect','terminal','body')
''')
put(5,'SQUARE','Two vertical adjustment sliders beside a Bitcoin B.','sliders-vertical: shared vertical axes; bitcoin: joined double lobes.','One Bitcoin stem per end rather than the pair of fine ticks; both sliders and both B lobes retained.','''
for name,x,y in [('low',10,30),('high',22,18)]:
    self.add_polyline(name+'-box',(x-4,y-4),(x,y-4),(x+4,y-4),(x+4,y+4),(x,y+4),(x-4,y+4),closed=True)
    self.add_line(name+'-top',(x,8),(x,y-4));self.add_line(name+'-bottom',(x,y+4),(x,40))
    self.relate('connect',name+'-box',name+'-top');self.relate('connect',name+'-box',name+'-bottom')
self.add_polyline('b-stem',(32,6),(32,10),(32,24),(32,38),(32,42))
self.add_arc('b-upper',(32,10),(32,24),radius_x=10,radius_y=7)
self.add_arc('b-lower',(32,24),(32,38),radius_x=10,radius_y=7)
self.relate('connect','b-stem','b-upper');self.relate('connect','b-stem','b-lower')
''')
put(6,'SQUARE','A bomb with a short fuse and a foreground explosion.','bomb: round body, short neck and curved fuse.','Explosion reduced to five broad points; shell is interrupted where hidden by the burst.','''
self.add_arc('shell-left',(14,39),(14,15),radius_x=8,radius_y=12)
self.add_polyline('neck',(14,15),(16,11),(21,11),(24,11),(24,17))
self.add_bezier('shell-right',(24,17),((28,19),(29,22),(29,24)))
self.relate('connect','shell-left','neck');self.relate('connect','shell-right','neck')
self.add_bezier('fuse',(21,11),((21,8),(23,6),(26,6)),((32,6),(32,12),(39,12)))
self.relate('connect','fuse','neck')
self.add_polyline('burst',(29,24),(33,30),(42,27),(37,34),(42,40),(33,38),(28,42),(27,35),(19,32),(27,30),closed=True)
self.relate('connect','shell-right','burst')
''')
put(7,'HRECT_L','A row of library books with rounded feet and spine bands.','library: repeat spacing; source supplies open tops and rounded spine feet.','Four books reduced to three equal books to keep the required spacing; two bands per spine retained.','''
for i,x in enumerate((4,20,36)):
    nodes=[(x,8),(x,16),(x,28),(x,36)]
    members=[]
    for j,(a,b) in enumerate(zip(nodes,nodes[1:])):
        name=f'book-{i}-left-{j}';self.add_line(name,a,b);members.append(name)
    name=f'book-{i}-foot';self.add_arc(name,(x,36),(x+8,36),radius_x=4,sweep=False);members.append(name)
    for j,(ya,yb) in enumerate(((36,28),(28,16),(16,8))):
        name=f'book-{i}-right-{j}';self.add_line(name,(x+8,ya),(x+8,yb));members.append(name)
    self.add_contour(f'book-{i}',*members)
    for y in (16,28):
        name=f'book-{i}-band-{y}';self.add_line(name,(x,y),(x+8,y));self.relate('connect',name,f'book-{i}')
''')
put(8,'VRECT_L','A book carrying a circular head over curved arms and a torso.','book-user: book cover and pages; human_ref/user.svg and full_body_ref.png: circular head and coherent human strokes.','None; book, head, raised arms and torso retained.','''
self.rounded('book',8,4,40,44,4,breaks={2:[(40,36)],6:[(8,36)]})
self.add_line('pages',(8,36),(40,36));self.relate('connect','pages','book')
self.circle('head',24,15,3)
self.add_arc('arm-left',(16,25),(24,28),radius_x=8,radius_y=3,sweep=False)
self.add_arc('arm-right',(24,28),(32,25),radius_x=8,radius_y=3,sweep=False)
self.add_contour('arms','arm-left','arm-right')
self.add_polyline('torso',(24,26),(24,28),(24,30));self.relate('connect','arms','torso')
self.mark_human_figure('person',head='head',torso='torso-1',torso_junction='start')
# Head bottom18, torso start26 => exact8 centerline /4 ink; front-facing axis x24.
''')
put(10,'SQUARE','A curled bird profile with a separate upper-right leaf.','bird: coherent curved silhouette; supplied Bower reference owns the curl, beak and leaf.','Short mouth divider omitted; tail represented by one broad curve.','''
self.add_bezier('curl',(20,25),((29,25),(29,18),(27,14)),((25,9),(22,6),(18,6)))
self.add_bezier('back',(18,6),((11,6),(6,16),(6,25)),((6,34),(12,39),(20,39)))
self.add_bezier('wing',(20,39),((26,39),(28,36),(29,33)))
self.add_contour('bird','curl','back','wing')
self.add_bezier('beak',(28,24),((33,24),(38,24),(42,24)),((42,30),(36,33),(29,33)))
self.add_bezier('tail',(29,33),((31,36),(33,38),(35,40)),((29,42),(24,42),(20,39)))
self.relate('connect','bird','tail');self.relate('connect','beak','tail');self.relate('connect','bird','beak')
self.add_arc('leaf-a',(42,6),(34,14),radius_x=8)
self.add_arc('leaf-b',(34,14),(42,6),radius_x=8)
self.add_contour('leaf','leaf-a','leaf-b',closed=True)
''')
put(13,'SQUARE','An open male symbol with two floating circles and a triangle.','mars: open round body and attached diagonal arrow.','None; unequal circles, triangle, ring and arrow retained.','''
self.add_arc('ring-top',(14,16),(24,6),radius_x=10)
self.add_arc('ring-right',(24,6),(34,16),radius_x=10)
self.add_arc('ring-bottom',(34,16),(24,26),radius_x=10)
self.add_contour('open-ring','ring-top','ring-right','ring-bottom')
self.add_line('shaft',(34,16),(42,8))
self.add_polyline('arrowhead',(34,8),(42,8),(42,16));self.relate('connect','shaft','open-ring');self.relate('connect','shaft','arrowhead')
self.circle('small-circle',9,28,3)
self.circle('large-circle',22,22,4)
self.add_polyline('triangle',(16,34),(24,42),(8,42),closed=True)
''')
put(14,'SQUARE','A briefcase with an attached handle and dollar sign.','briefcase: rounded case and genuine handle joins; dollar-sign: smooth currency lobes.','None.','''
self.rounded('case',6,14,42,42,4,breaks={0:[(16,14),(32,14)]})
self.add_polyline('handle',(16,14),(16,6),(32,6),(32,14));self.relate('connect','handle','case')
self.dollar(24,28)
''')
put(15,'HRECT_M','A broken tab with an X on its separated right fragment.','No useful broken-tab match; source fracture layout, with coherent rounded exterior corners.','None.','''
self.add_polyline('left-main',(8,10),(14,10),(8,24),(14,38),(8,38))
self.add_arc('left-bl',(8,38),(4,34),radius_x=4)
self.add_line('left-wall',(4,34),(4,14))
self.add_arc('left-tl',(4,14),(8,10),radius_x=4)
self.relate('connect','left-main','left-bl');self.relate('connect','left-main','left-tl')
self.relate('connect','left-wall','left-bl');self.relate('connect','left-wall','left-tl')
self.add_line('right-top',(24,10),(40,10))
self.add_arc('right-tr',(40,10),(44,14),radius_x=4)
self.add_line('right-wall',(44,14),(44,34))
self.add_arc('right-br',(44,34),(40,38),radius_x=4)
self.add_polyline('fracture',(40,38),(24,38),(18,24),(24,10))
self.add_contour('fragment','right-top','right-tr','right-wall','right-br','fracture-1','fracture-2','fracture-3',closed=True)
self.contours=[c for c in self.contours if c.contour_id!='fracture']
self.add_polyline('cross-a',(29,21),(32,24),(35,27))
self.add_polyline('cross-b',(29,27),(32,24),(35,21));self.relate('connect','cross-a','cross-b')
''')
put(16,'VRECT_L','A browser window with a right-aligned dollar sign.','panels-top-left: rounded frame and connected header; dollar-sign: joined currency curves.','Tiny title-bar marks omitted because the eight-unit header cannot contain detached details.','''
self.browser();self.dollar(28,28)
''')
for n,x,alignment in [(17,29,'right-aligned'),(18,26,'centered')]:
    put(n,'VRECT_L',f'A browser window with a {alignment} single-bar euro sign.','panels-top-left: rounded frame and joined header; euro: open currency contour and crossbar.','Tiny title-bar marks omitted because the eight-unit header cannot contain detached details.',f"self.browser();self.euro({x})")
put(19,'VRECT_L','A browser with a navigation column and two stacked content cards.','panels-top-left: shared header/sidebar nodes and rounded frame.','Three tiny header controls omitted; five navigation ticks reduced to two.','''
self.rounded('window',8,4,40,44,4,breaks={2:[(40,12)],4:[(20,44)],6:[(8,12)]})
self.add_polyline('header',(8,12),(20,12),(40,12));self.relate('connect','header','window')
self.add_line('sidebar',(20,12),(20,44));self.relate('connect','sidebar','header');self.relate('connect','sidebar','window')
for i,y in enumerate((22,36)):self.add_line(f'nav-{i}',(13,y),(15,y))
for i,y in enumerate((20,32)):
    self.add_polyline(f'card-{i}',(28,y),(36,y),(36,y+8),(28,y+8),closed=True)
''')
put(20,'VRECT_L','A browser containing a circular user head above open shoulders.','panels-top-left: rounded window and header; human_ref/user.svg: circular head and smooth open shoulder bust.','Tiny title-bar marks omitted to preserve the clear header band.','''
self.browser()
self.circle('head',24,23,3)
self.add_arc('shoulder-left',(17,35),(24,34),radius_x=7,radius_y=1)
self.add_arc('shoulder-right',(24,34),(31,35),radius_x=7,radius_y=1)
self.add_contour('shoulders','shoulder-left','shoulder-right')
# Circular head bottom26; shoulder apex34 => exact8 centerline /4 ink gap.
''')

def export(e):u.export(e)
def main():
    for e in ENTRIES:
        if e['action']=='already-valid':print(e['position'],'already valid',e['concept']);continue
        key,subject,refs,omissions,body=SPECS[e['position']]
        d=Path(e['result_dir']);name=e['icon_id'].replace('-','_')+'_'+e['source_uuid'].replace('-','_')+'.py'
        header=f'''"""{subject}
Plan: {refs}
Reduction: {omissions}
Author geometry backwards from the exact {key} envelope.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
SOURCE_ICON_ID={e['source_uuid']!r}
SOURCE_PATH={e['reference_path']!r}
AUTHOR={AUTHOR!r}
class Drawing(Solo48):
    icon_id={e['icon_id']!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords={tuple(e['concept'].split())!r}
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
'''
        (d/name).write_text(header+textwrap.indent(textwrap.dedent(body).strip()+'\n','        ')+HELPERS)
        (d/'plan.json').write_text(json.dumps(dict(subject=subject,keyshape=key,construction_reference=refs,omissions=omissions,python=name),indent=2)+'\n')
        export(e)
if __name__=='__main__':main()
