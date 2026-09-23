"""Author the supplied batch 53 files as standalone SOLO48 candidates."""
from pathlib import Path
import importlib.util,json,textwrap
SOURCE_ICON_ID='c301d7dd-6085-4b9d-94b3-1ce712942ed5'
SOURCE_PATH='icon_set/work/todo-references/underground_c301d7dd-6085-4b9d-94b3-1ce712942ed5.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ENTRIES=json.loads((ROOT/'batch-inputs.json').read_text())
# Reuse only the generic geometry/export machinery, never a previous icon drawing.
utility=Path('icon_set/work/primitive-make-ray/08acfc76-564e-418d-abde-1f5766d10cdc/20260923T210601-batch48/author_batch.py')
spec=importlib.util.spec_from_file_location('local_geometry_export',utility)
u=importlib.util.module_from_spec(spec);spec.loader.exec_module(u)
HELPERS=u.HELPERS.split('    def portrait(')[0]+'''
    def person(self,name,cx,cy,r,bottom):
        # Shared human reference: exact detached head gap at the shoulder apex.
        self.circle(name+'-head',cx,cy,r)
        top=cy+r+8;w=6
        self.add_arc(name+'-shoulder-left',(cx-w,top+6),(cx,top),radius_x=w)
        self.add_arc(name+'-shoulder-right',(cx,top),(cx+w,top+6),radius_x=w)
        self.add_line(name+'-right',(cx+w,top+6),(cx+w,bottom))
        self.add_line(name+'-bottom-right',(cx+w,bottom),(cx,bottom))
        self.add_line(name+'-bottom-left',(cx,bottom),(cx-w,bottom))
        self.add_line(name+'-left',(cx-w,bottom),(cx-w,top+6))
        self.add_contour(name+'-body',name+'-shoulder-left',name+'-shoulder-right',name+'-right',name+'-bottom-right',name+'-bottom-left',name+'-left',closed=True)

    def dollar(self,cx,cy):
        self.add_bezier('dollar',(cx+3,cy-6),((cx-3,cy-9),(cx-6,cy-3),(cx,cy)),((cx+6,cy+3),(cx+3,cy+9),(cx-3,cy+6)))
        self.add_polyline('dollar-stem',(cx,cy-9),(cx,cy),(cx,cy+9))
        self.relate('connect','dollar','dollar-stem')
'''

SPECS=[
('VRECT_L','An arched underground entrance with an inner doorway.','rectangle-vertical: coherent outer wall; nested arches use shared vertical axes and tangent joins.','None.', '''
self.add_arc('outer-arch',(8,20),(40,20),radius_x=16)
self.add_polyline('outer-walls',(40,20),(40,44),(31,44),(17,44),(8,44),(8,20))
self.relate('connect','outer-arch','outer-walls')
self.add_line('door-left',(17,44),(17,23))
self.add_arc('door-arch',(17,23),(31,23),radius_x=7)
self.add_line('door-right',(31,23),(31,44))
self.add_contour('door','door-left','door-arch','door-right')
self.relate('connect','door','outer-walls')
'''),
('HRECT_M','Two equal horizontal underline strokes.','No more useful Lucide subject match; source defines two straight repeated rules.','None; no U letter is present in the supplied reference.', '''
for name,y in [('upper',10),('lower',38)]:self.add_line(name,(4,y),(44,y))
'''),
('HRECT_L','A balance scale weighing a person against a dollar sign.','scale: mirrored pans and central pedestal; human_ref/user.svg: round head and smooth shoulders.','Small arm/leg outline steps simplified; human, dollar, both pans and pedestal retained.', '''
self.person('person',12,12,4,30)
for name,cx in [('left',12),('right',36)]:
    self.add_polyline(name+'-rim',(cx-8,30),(cx,30),(cx+8,30))
    self.add_arc(name+'-bowl-right',(cx+8,30),(cx,35),radius_x=8,radius_y=5)
    self.add_arc(name+'-bowl-left',(cx,35),(cx-8,30),radius_x=8,radius_y=5)
    self.add_contour(name+'-bowl',name+'-bowl-right',name+'-bowl-left')
    self.relate('connect',name+'-rim',name+'-bowl')
self.relate('connect','person-body','left-rim')
self.add_polyline('pedestal',(18,40),(20,36),(22,32),(26,32),(28,36),(30,40),closed=True)
self.add_bezier('left-link',(12,35),((12,38),(17,36),(20,36)))
self.add_bezier('right-link',(28,36),((31,36),(36,38),(36,35)))
self.relate('connect','left-link','left-bowl');self.relate('connect','left-link','pedestal')
self.relate('connect','right-link','right-bowl');self.relate('connect','right-link','pedestal')
self.dollar(36,18)
'''),
('SQUARE','A person and a dollar coin balanced on a seesaw.','scale: horizontal balance and fulcrum; human_ref/user.svg: circular head and shoulder apex.','Small arm/leg outline steps simplified; coin, dollar and fulcrum retained.', '''
self.person('person',12,10,4,30)
self.add_polyline('beam',(6,32),(24,32),(42,32))
self.add_polyline('fulcrum',(24,32),(18,42),(30,42),closed=True)
self.relate('connect','beam','fulcrum')
self.circle('coin',34,20,8)
self.dollar(34,20)
'''),
('SQUARE','A large P node connected to two smaller nodes.','network: shared endpoints between node outlines and connecting branches.','None; the literal P from the input is retained.', '''
self.circle('main',20,24,14)
self.circle('node-upper',38,10,4)
self.circle('node-lower',38,38,4)
self.add_line('upper-link',(20,10),(34,10))
self.add_line('lower-link',(20,38),(34,38))
self.relate('connect','upper-link','main');self.relate('connect','upper-link','node-upper')
self.relate('connect','lower-link','main');self.relate('connect','lower-link','node-lower')
self.add_polyline('p-stem',(17,31),(17,24),(17,16),(23,16))
self.add_arc('p-bowl',(23,16),(23,24),radius_x=4)
self.add_line('p-return',(23,24),(17,24))
self.relate('connect','p-stem','p-bowl');self.relate('connect','p-stem','p-return');self.relate('connect','p-bowl','p-return')
'''),
('SQUARE','A broadcast user icon above the word LIVE.','radio: nested broadcast arcs; human_ref/user.svg: circular head and smooth shoulder run.','None; all four letters retained as authored strokes.', '''
self.add_arc('signal-outer',(8,26),(40,26),radius_x=18,radius_y=20)
self.add_arc('signal-inner',(15,23),(33,23),radius_x=11,radius_y=12)
self.circle('head',24,20,3)
self.add_arc('shoulders',(18,34),(30,34),radius_x=6,radius_y=3)
self.add_polyline('letter-l',(6,34),(6,42),(12,42))
self.add_line('letter-i',(17,34),(17,42))
self.add_polyline('letter-v',(22,34),(26,42),(30,34))
self.add_polyline('letter-e',(42,34),(35,34),(35,38),(35,42),(42,42))
self.add_line('e-middle',(35,38),(40,38));self.relate('connect','letter-e','e-middle')
'''),
('SQUARE','A user node linked to three surrounding mobility nodes.','network: three repeated connections; human_ref/user.svg: head and shoulder vocabulary.','None; user enclosure and three nodes retained.', '''
self.circle('user-ring',18,24,12)
self.circle('head',18,19,3)
self.add_arc('shoulders',(10,34),(26,34),radius_x=8,radius_y=4)
self.circle('node-upper',38,10,4)
self.circle('node-middle',38,24,4)
self.circle('node-lower',38,38,4)
for name,a,b in [('upper',(18,12),(34,10)),('middle',(30,24),(34,24)),('lower',(18,36),(34,38))]:
    self.add_line('link-'+name,a,b);self.relate('connect','link-'+name,'user-ring');self.relate('connect','link-'+name,'node-'+name)
'''),
('SQUARE','A standing user inside two broadcast arcs.','radio: concentric open arcs; human_ref/user.svg: detached circular head and shoulder apex.','Arm/leg steps reduced to a smooth torso; both signal arcs retained.', '''
self.add_arc('signal-outer',(8,32),(40,32),radius_x=18,radius_y=20)
self.add_arc('signal-inner',(14,29),(34,29),radius_x=12,radius_y=13)
self.person('person',24,22,4,42)
'''),
('SQUARE','A Vaisakhi drum with two beaters and a wheat sprig.','drum: barrel silhouette and hoops; wheat: repeated diagonal stalk branches.','None; drum, both beaters and stalk retained.', '''
self.add_polyline('beater-left',(6,6),(16,12))
self.add_polyline('beater-right',(36,6),(26,12))
self.add_line('drum-top',(12,18),(30,18))
self.add_bezier('drum-right',(30,18),((33,27),(33,35),(30,42)))
self.add_line('drum-bottom',(30,42),(12,42))
self.add_bezier('drum-left',(12,42),((9,35),(9,27),(12,18)))
self.add_contour('drum','drum-top','drum-right','drum-bottom','drum-left',closed=True)
for i,y in enumerate((24,36)):self.add_line(f'hoop-{i}',(11,y),(27,y))
self.add_polyline('wheat-stem',(28,42),(34,36),(38,32),(42,28))
for name,a,b in [('low',(34,36),(40,36)),('middle',(38,32),(38,26)),('high',(42,28),(42,22))]:
    self.add_line('grain-'+name,a,b);self.relate('connect','grain-'+name,'wheat-stem')
'''),
('HRECT_M','The five-letter VALVE wordmark.','No useful local logo original; hand-authored geometric letter strokes preserve the given word.', 'None; all five letters retained.', '''
self.add_polyline('v-first',(4,10),(7,38),(10,10))
self.add_polyline('a-sides',(13,38),(16,10),(19,38))
self.add_line('a-bar',(14,29),(18,29))
self.add_polyline('l',(23,10),(23,38),(28,38))
self.add_polyline('v-second',(31,10),(34,38),(37,10))
self.add_polyline('e',(44,10),(40,10),(40,24),(40,38),(44,38))
self.add_line('e-middle',(40,24),(44,24));self.relate('connect','e','e-middle')
'''),
('SQUARE','A diagonal vector pen nib with an upper-left plus sign.','pen-tool: coherent nib, cap and slit; plus: centered intersecting arms.','None; cap, nib, slit and plus retained.', '''
self.add_polyline('nib',(6,42),(14,18),(26,14),(34,22),(30,34),(6,42))
self.add_polyline('cap',(26,14),(34,6),(42,14),(34,22))
self.relate('connect','cap','nib')
self.add_line('slit',(6,42),(21,27));self.relate('connect','slit','nib')
self.add_polyline('plus-h',(6,12),(12,12),(18,12))
self.add_polyline('plus-v',(12,6),(12,12),(12,18));self.relate('connect','plus-h','plus-v')
'''),
('VRECT_L','A folded velvet sheet with a turned corner and trailing edge.','rectangle-vertical: consistent rounded cloth corners; source defines the fold hierarchy.','None.', '''
self.add_line('sheet-top',(12,4),(36,4))
self.add_arc('sheet-tr',(36,4),(40,8),radius_x=4)
self.add_line('sheet-right',(40,8),(40,22))
self.add_line('fold-diagonal',(40,22),(24,38))
self.add_line('sheet-bottom',(24,38),(12,38))
self.add_arc('sheet-bl',(12,38),(8,34),radius_x=4)
self.add_line('sheet-left',(8,34),(8,8))
self.add_arc('sheet-tl',(8,8),(12,4),radius_x=4)
self.add_contour('sheet','sheet-top','sheet-tr','sheet-right','fold-diagonal','sheet-bottom','sheet-bl','sheet-left','sheet-tl',closed=True)
self.add_polyline('fold',(24,38),(24,26),(28,22),(40,22));self.relate('connect','fold','sheet')
self.add_polyline('trailing-edge',(40,22),(40,44),(24,44));self.relate('connect','trailing-edge','sheet')
'''),
('SQUARE','V and S separated by a rising diagonal slash.','Source lettering reconstructed with straight V and smooth S; no useful exact local Lucide match.','None; both letters and slash retained.', '''
self.add_polyline('v',(6,6),(13,25),(20,6))
self.add_line('slash',(8,42),(40,8))
self.add_bezier('s',(41,28),((33,21),(25,30),(33,33)),((43,36),(43,42),(31,42)))
'''),
('VRECT_M','A vertical coupon with centered top and bottom semicircular notches.','ticket: inward notches and equal rounded corners.','None.', '''
self.add_line('top-left',(14,4),(20,4))
self.add_arc('top-notch',(20,4),(28,4),radius_x=4,sweep=False)
self.add_line('top-right',(28,4),(34,4))
self.add_arc('tr',(34,4),(38,8),radius_x=4)
self.add_line('right',(38,8),(38,40))
self.add_arc('br',(38,40),(34,44),radius_x=4)
self.add_line('bottom-right',(34,44),(28,44))
self.add_arc('bottom-notch',(28,44),(20,44),radius_x=4,sweep=False)
self.add_line('bottom-left',(20,44),(14,44))
self.add_arc('bl',(14,44),(10,40),radius_x=4)
self.add_line('left',(10,40),(10,8))
self.add_arc('tl',(10,8),(14,4),radius_x=4)
self.add_contour('coupon','top-left','top-notch','top-right','tr','right','br','bottom-right','bottom-notch','bottom-left','bl','left','tl',closed=True)
'''),
('VRECT_L','A plain upright rounded rectangle.','rectangle-vertical: equal circular corner radii and straight walls.','None.', '''
self.rounded('rectangle',8,4,40,44,5)
'''),
('SQUARE','A veterinarian with a stethoscope and cat badge.','human_ref/user.svg: circular head and shoulders; stethoscope: tubing and bell; source supplies cat badge.','Fine facial detail omitted; collar, stethoscope and cat retained.', '''
self.circle('head',20,12,6)
self.add_bezier('shoulders',(6,42),((6,28),(10,26),(20,26)),((28,26),(32,29),(32,34)))
self.add_line('body-bottom',(6,42),(28,42));self.relate('connect','body-bottom','shoulders')
self.add_polyline('collar',(16,26),(20,30),(24,26))
self.add_line('stethoscope-tube',(14,27),(14,33))
self.circle('stethoscope-bell',14,36,3);self.relate('connect','stethoscope-tube','stethoscope-bell')
self.circle('badge',33,33,9)
self.add_polyline('cat-ears',(28,32),(28,27),(32,29),(34,29),(38,27),(38,32))
self.add_arc('cat-jaw',(38,32),(28,32),radius_x=5,sweep=True)
self.relate('connect','cat-ears','cat-jaw')
'''),
('HRECT_M','A video camera with a central plus mark.','video: rounded body and tapered lens hood; plus: equal arms.','None; the source shows a plus, not an X.', '''
self.rounded('camera',4,10,32,38,4,breaks={2:[(32,18),(32,30)]})
self.add_polyline('hood',(32,18),(44,12),(44,36),(32,30));self.relate('connect','hood','camera')
self.add_polyline('plus-h',(12,24),(18,24),(24,24))
self.add_polyline('plus-v',(18,18),(18,24),(18,30));self.relate('connect','plus-h','plus-v')
'''),
('SQUARE','Two video panels separated by a dashed cut line and a top marker.','split: paired panels and central division; source supplies the downward triangle.','None; paired footers and three cut marks retained.', '''
for name,l,r in [('left',6,20),('right',28,42)]:
    self.rounded(name,l,16,r,40,3,breaks={2:[(r,32)],6:[(l,32)]})
    self.add_line(name+'-footer',(l,32),(r,32));self.relate('connect',name+'-footer',name)
self.add_polyline('marker',(20,6),(28,6),(24,13),closed=True)
for i,y in enumerate((18,28,38)):self.add_line(f'cut-{i}',(24,y),(24,y+4))
'''),
('HRECT_L','A 360-degree VR band with a small game symbol.','cylinder: curved band silhouette; source supplies 360 text and open-mouth game mark.','None; digits and game symbol retained.', '''
self.add_arc('band-top',(4,24),(44,24),radius_x=20,radius_y=6,sweep=False)
self.add_line('band-right',(44,24),(44,34))
self.add_arc('band-bottom',(44,34),(4,34),radius_x=20,radius_y=6)
self.add_line('band-left',(4,34),(4,24))
self.add_contour('band','band-top','band-right','band-bottom','band-left',closed=True)
self.add_bezier('three',(13,9),((21,5),(21,13),(15,13)),((21,13),(21,21),(13,17)))
self.add_bezier('six',(28,9),((20,5),(20,19),(26,19)),((32,19),(30,11),(23,14)))
self.add_arc('zero-top',(32,13),(40,13),radius_x=4,radius_y=5)
self.add_arc('zero-bottom',(40,13),(32,13),radius_x=4,radius_y=5)
self.add_contour('zero','zero-top','zero-bottom',closed=True)
self.add_arc('game-mouth',(27,31),(27,37),radius_x=4,large_arc=True,sweep=False)
self.add_polyline('game-wedge',(27,37),(24,34),(27,31));self.relate('connect','game-mouth','game-wedge')
'''),
('VRECT_L','A round game flask containing a small stepped city and a floating ball.','cylinder: round vessel vocabulary; source supplies narrow neck, city blocks and ball.','None.', '''
self.add_arc('bowl-left',(18,14),(24,44),radius_x=16,large_arc=False,sweep=False)
self.add_arc('bowl-right',(24,44),(30,14),radius_x=16,large_arc=False,sweep=False)
self.add_polyline('neck',(18,14),(18,8),(30,8),(30,14))
self.relate('connect','neck','bowl-left');self.relate('connect','neck','bowl-right');self.relate('connect','bowl-left','bowl-right')
self.add_line('lip',(14,8),(34,8))
self.circle('ball',34,6,2)
self.add_polyline('city',(16,35),(16,31),(20,31),(20,27),(24,27),(24,23),(28,23),(28,27),(32,27),(32,35),closed=True)
'''),
]

def export(e):u.export(e)

def author_all():
    for e,(key,subject,reference,omissions,body) in zip(ENTRIES,SPECS):
        d=Path(e['result_dir']);slug=e['icon_id'];name=slug.replace('-','_')+'_'+e['source_uuid'].replace('-','_')+'.py'
        if list(d.parent.glob('*/result.json')):print('already done',slug);continue
        header=f'''"""{subject}
Symbol plan: {reference}
Keyshape: {key}; fixed profile envelope is recorded in ink_extremes.
Reduction: {omissions}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={e['source_uuid']!r}
SOURCE_PATH={e['reference_path']!r}
AUTHOR={AUTHOR!r}

class Drawing(Solo48):
    icon_id={slug!r}
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
        (d/'plan.json').write_text(json.dumps(dict(subject=subject,keyshape=key,construction_reference=reference,omissions=omissions,python=name),indent=2)+'\n');export(e)

if __name__=='__main__':author_all()
