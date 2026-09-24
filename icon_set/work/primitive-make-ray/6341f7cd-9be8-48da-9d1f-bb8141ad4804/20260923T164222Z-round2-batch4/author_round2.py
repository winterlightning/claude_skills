"""Standalone round 2 batch 4 originals; previous runs preserved."""
from pathlib import Path
import json,importlib.util,textwrap
SOURCE_ICON_ID='6341f7cd-9be8-48da-9d1f-bb8141ad4804'
SOURCE_PATH='icon_set/work/todo-references/christmas postcard 2_6341f7cd-9be8-48da-9d1f-bb8141ad4804.svg'
AUTHOR='gpt-6'
ROOT=Path(__file__).parent
ENTRIES=json.loads((ROOT/'batch-inputs.json').read_text())
s=importlib.util.spec_from_file_location('utility',Path('icon_set/work/primitive-make-ray/08acfc76-564e-418d-abde-1f5766d10cdc/20260923T210601-batch48/author_batch.py'))
u=importlib.util.module_from_spec(s);s.loader.exec_module(u)
HELPERS=u.HELPERS.split('    def portrait(')[0]
SPECS={}
def put(n,key,subject,refs,omissions,body):SPECS[n]=(key,subject,refs,omissions,body)

put(1,'HRECT_L','A Christmas postcard with a snowflake, divider, stamp and address rules.','snowflake: branched axial strokes; source postcard layout.','Two address rules reduced to one; all four snowflake branches retained.','''
self.rounded('card',4,8,44,40,3)
self.add_line('divider',(27,17),(27,31))
self.add_polyline('flake-v',(16,17),(16,20),(16,24),(16,28),(16,31))
self.add_polyline('flake-h',(9,24),(12,24),(16,24),(20,24),(23,24));self.relate('connect','flake-v','flake-h')
for n,pts,parent in [('north',[(13,18),(16,20),(19,18)],'flake-v'),('south',[(13,30),(16,28),(19,30)],'flake-v'),('west',[(10,21),(12,24),(10,27)],'flake-h'),('east',[(22,21),(20,24),(22,27)],'flake-h')]:
    self.add_polyline(n,*pts);self.relate('connect',n,parent)
self.circle('stamp',36,20,3)
self.add_line('address',(33,32),(38,32))
''')
put(2,'CIRCLE','An Indian rupee sign inside a circular badge.','indian-rupee: two horizontal bars, curved bowl and descending leg.','None.','''
self.circle('ring',24,24,20)
self.add_polyline('top',(17,15),(24,15),(31,15))
self.add_polyline('middle',(17,23),(29,23),(31,23))
self.add_arc('bowl-upper',(24,15),(29,23),radius_x=5,radius_y=8)
self.add_arc('bowl-lower',(29,23),(24,31),radius_x=5,radius_y=8)
self.add_polyline('leg',(24,31),(17,31),(27,35))
self.add_contour('bowl','bowl-upper','bowl-lower')
self.relate('connect','bowl','top');self.relate('connect','bowl','middle');self.relate('connect','bowl','leg')
''')
for n,angry in [(3,True),(4,False)]:
    eyes="""
for side in (-1,1):self.add_line('eye-'+str(side),(24+side*5,23),(24+side*4,24))
""" if angry else """
for side in (-1,1):self.add_dot('eye-'+str(side),(24+side*4,23))
"""
    put(n,'CIRCLE','A skull with '+('slanted eyes' if angry else 'dot eyes')+' inside a circular badge.','skull: domed head and narrowed open jaw; source dictates circular enclosure.','Slanted eye strokes shortened for clearance.' if angry else 'None.',"""
self.circle('ring',24,24,20)
self.add_arc('dome',(13,23),(35,23),radius_x=11)
self.add_bezier('right-cheek',(35,23),((35,28),(32,29),(32,30)))
self.add_line('right-jaw',(32,30),(32,32))
self.add_line('left-jaw',(16,32),(16,30))
self.add_bezier('left-cheek',(16,30),((16,29),(13,28),(13,23)))
self.add_contour('skull','left-jaw','left-cheek','dome','right-cheek','right-jaw')
self.add_line('mouth',(24,32),(24,34))
"""+eyes)
put(5,'HRECT_L','An open cloud canopy above the text CO2.','cloud: coherent lobed canopy; hand-authored C, O and lowered 2.','None; all three text characters retained.','''
self.add_arc('cloud-left',(4,20),(12,12),radius_x=8)
self.add_arc('cloud-top',(12,12),(36,12),radius_x=12,radius_y=4)
self.add_arc('cloud-right',(36,12),(44,20),radius_x=8)
self.add_contour('cloud','cloud-left','cloud-top','cloud-right')
self.add_bezier('c',(11,29),((7,27),(4,29),(4,34)),((4,39),(7,41),(11,39)))
self.rounded('o',20,28,28,40,4)
self.add_bezier('two-top',(37,32),((37,28),(44,28),(44,32)))
self.add_polyline('two-base',(44,32),(37,40),(44,40));self.relate('connect','two-top','two-base')
''')
put(6,'SQUARE','Two coworkers below a disconnected plug and socket joined by an outer cord.','plug: cap and paired prongs; human_ref/user.svg: equivalent circular heads and shoulders.','Socket holes reduced from two to one; closed shoulder bases omitted for clear bust silhouettes.','''
for i,cx in enumerate((13,35)):
    self.circle(f'head-{i}',cx,28,4)
    self.add_arc(f'shoulders-{i}',(cx-7,42),(cx+7,42),radius_x=7,radius_y=2)
# Head bottom32, shoulder apex40: exact8 centerline /4 ink units.
self.rounded('plug',10,6,20,18,3,breaks={2:[(20,8),(20,16)],6:[(10,12)]})
self.rounded('socket',32,6,42,18,3,breaks={2:[(42,12)]})
for i,y in enumerate((8,16)):
    self.add_line(f'pin-{i}',(20,y),(24,y));self.relate('connect',f'pin-{i}','plug')
self.add_dot('socket-hole',(37,12))
self.add_polyline('cord-left',(10,12),(6,12),(6,24),(13,24));self.relate('connect','cord-left','plug');self.relate('connect','cord-left','head-0')
self.add_polyline('cord-right',(42,12),(42,24),(35,24));self.relate('connect','cord-right','socket');self.relate('connect','cord-right','head-1')
''')
put(7,'HRECT_L','A construction crane suspending a code window.','construction: shared truss nodes; source supplies hanging window and three code strokes.','Two truss bays reduced to one; code chevrons and slash retained.','''
self.add_polyline('crane',(4,40),(4,8),(24,8),(36,16),(4,16))
self.add_polyline('truss',(8,16),(16,8),(24,16));self.relate('connect','truss','crane')
self.add_polyline('mast',(12,16),(12,40),(4,40));self.relate('connect','mast','crane')
self.add_polyline('hanger',(28,16),(28,20),(24,24));self.relate('connect','hanger','crane')
self.add_line('hanger-right',(28,20),(32,24));self.relate('connect','hanger-right','hanger')
self.rounded('window',20,24,44,40,3,breaks={0:[(24,24),(32,24)]})
self.relate('connect','hanger','window');self.relate('connect','hanger-right','window')
self.add_polyline('code-left',(27,29),(24,32),(27,35))
self.add_line('slash',(34,28),(30,36))
self.add_polyline('code-right',(38,29),(41,32),(38,35))
''')
for n in (8,9):
    put(n,'SQUARE','Two equal toothed gears on a rising diagonal.','cog: repeated radial teeth and circular hubs, generated from shared quarter geometry.','Eight teeth per gear reduced to four broad teeth to open tooth valleys; both hubs retained.','''
quarter=[(-4,-9),(4,-9),(4,-4),(9,-4)]
for i,(cx,cy) in enumerate(((15,33),(33,15))):
    pts=[]
    for turn in range(4):
        for x,y in quarter:
            for _ in range(turn):x,y=-y,x
            pts.append((cx+x,cy+y))
    self.add_polyline(f'gear-{i}',*pts,closed=True)
    self.circle(f'hub-{i}',cx,cy,3)
''')
put(11,'HRECT_M','A circular east compass badge followed by a right arrow.','compass: circular badge; hand-authored E and concave directional arrow.','None.','''
self.circle('badge',17,24,13)
self.add_polyline('e',(20,16),(13,16),(13,24),(13,32),(20,32))
self.add_line('e-mid',(13,24),(19,24));self.relate('connect','e','e-mid')
self.add_polyline('arrow',(36,10),(44,24),(36,38),(39,24),closed=True)
''')
put(13,'SQUARE','A horns hand gesture with three lightning accents.','hand-metal: rounded raised fingers and folded middle fingers; shared human references supply anatomy principles.','Fine palm crease omitted; thumb contour and all three lightning accents retained.','''
self.add_arc('index-cap',(12,22),(20,22),radius_x=4)
self.add_line('index-inner',(20,22),(20,30))
self.add_arc('middle-knuckle',(20,30),(26,30),radius_x=3)
self.add_arc('ring-knuckle',(26,30),(32,30),radius_x=3)
self.add_line('little-inner',(32,30),(32,22))
self.add_arc('little-cap',(32,22),(40,22),radius_x=4)
self.add_line('right-palm',(40,22),(40,28))
self.add_arc('palm-right',(40,28),(26,42),radius_x=14)
self.add_arc('palm-left',(26,42),(12,28),radius_x=14)
self.add_line('left-palm',(12,28),(12,22))
self.add_contour('hand','index-cap','index-inner','middle-knuckle','ring-knuckle','little-inner','little-cap','right-palm','palm-right','palm-left','left-palm')
self.add_bezier('thumb',(32,34),((28,32),(22,32),(22,35)),((22,38),(27,38),(30,38)))
self.add_line('fold',(26,30),(26,33));self.relate('connect','fold','hand')
for n,pts in [('left-bolt',[(6,10),(11,14),(6,14)]),('top-bolt',[(26,6),(22,10),(28,10),(24,14)]),('right-bolt',[(42,8),(36,12),(42,12)])]:self.add_polyline(n,*pts)
''')
put(14,'VRECT_L','A Polaroid photograph of a couple beneath a heart.','image: coherent photo frame; human_ref/user.svg: paired circular heads and smooth shoulders.','None; both people and the heart retained.','''
self.add_polyline('frame',(8,4),(40,4),(40,36),(40,44),(8,44),(8,36),closed=True)
self.add_polyline('photo-bottom',(8,36),(11,36),(23,36),(25,36),(37,36),(40,36));self.relate('connect','frame','photo-bottom')
for i,cx in enumerate((17,31)):
    self.circle(f'head-{i}',cx,22,3)
    self.add_arc(f'shoulders-{i}',(cx-6,36),(cx+6,36),radius_x=6,radius_y=3)
    self.relate('connect',f'shoulders-{i}','photo-bottom')
# Head bottom25, shoulder apex33: exact8 centerline /4 ink gap.
self.add_bezier('heart',(24,11),((19,6),(16,12),(24,17)),((32,12),(29,6),(24,11)))
''')
put(15,'HRECT_L','A payment terminal with receipt beside a card and insertion arrow.','credit-card: outlined card and stripe; source supplies terminal and receipt.','Six keypad marks reduced to two; receipt serrations reduced to one broad notch.','''
self.rounded('terminal',4,16,28,40,3,breaks={0:[(10,16),(22,16)],2:[(28,24)],6:[(4,24)]})
self.add_polyline('receipt',(10,24),(10,8),(16,12),(22,8),(22,24));self.relate('connect','receipt','terminal')
self.add_polyline('slot',(4,24),(10,24),(22,24),(28,24));self.relate('connect','slot','terminal');self.relate('connect','slot','receipt')
for i,x in enumerate((12,20)):self.add_dot(f'key-{i}',(x,32))
self.rounded('card',36,8,44,24,2,breaks={0:[(40,8)],4:[(40,24)]})
self.add_line('stripe',(40,8),(40,24));self.relate('connect','stripe','card')
self.add_line('shaft',(40,32),(40,40))
self.add_polyline('arrow',(36,36),(40,40),(44,36));self.relate('connect','shaft','arrow')
''')
put(16,'SQUARE','Crossing crop corners with opposing rotation arrows.','crop: shared crossing nodes; rotate-ccw: quarter arcs with compact corner arrowheads.','Chevron arrowheads changed to right-angle arrowheads; both rotation arrows retained.','''
self.add_polyline('crop-left',(18,6),(18,18),(18,30),(30,30),(42,30))
self.add_polyline('crop-right',(6,18),(18,18),(30,18),(30,30),(30,42));self.relate('connect','crop-left','crop-right')
self.add_arc('rotate-top',(42,18),(30,6),radius_x=12,sweep=False)
self.add_polyline('arrow-top',(34,6),(30,6),(30,10));self.relate('connect','rotate-top','arrow-top')
self.add_arc('rotate-bottom',(6,30),(18,42),radius_x=12,sweep=False)
self.add_polyline('arrow-bottom',(14,42),(18,42),(18,38));self.relate('connect','rotate-bottom','arrow-bottom')
''')
put(17,'HRECT_L','The four swept bands of the Crowdin logo.','No useful exact logo match; coherent cubic boundaries preserve the nested broken C arrangement.','None; all four bands retained.','''
self.add_bezier('outer-upper',(44,10),((38,8),(34,8),(28,8)),((16,8),(6,12),(4,20)))
self.add_line('upper-end',(4,20),(12,22))
self.add_bezier('upper-inner',(12,22),((18,10),(32,12),(44,12)))
self.add_contour('upper-band','outer-upper','upper-end','upper-inner')
self.add_bezier('inner-upper',(42,21),((32,19),(25,22),(23,29)))
self.add_line('inner-end',(23,29),(29,30))
self.add_bezier('inner-return',(29,30),((31,24),(36,24),(40,24)))
self.add_line('inner-tip',(40,24),(42,21))
self.add_contour('inner-upper-band','inner-upper','inner-end','inner-return','inner-tip',closed=True)
self.add_line('lower-end',(4,31),(12,32))
self.add_bezier('lower-inner',(12,32),((14,37),(18,39),(24,40)))
self.add_bezier('lower-outer',(24,40),((12,40),(4,38),(4,31)))
self.add_contour('lower-band','lower-end','lower-inner','lower-outer',closed=True)
self.add_line('small-end',(23,38),(29,38))
self.add_bezier('small-inner',(29,38),((31,39),(34,40),(37,40)))
self.add_bezier('small-outer',(37,40),((31,40),(26,40),(23,38)))
self.add_contour('small-band','small-end','small-inner','small-outer',closed=True)
''')
put(18,'CIRCLE','A Megacoin badge containing three equal domed arches.','No useful exact currency logo match; parameterized identical arches within a circle.','None; all three arches retained.','''
self.circle('coin',24,24,20)
for i,x in enumerate((8,20,32)):
    self.add_line(f'arch-{i}-left',(x,28),(x,23))
    self.add_arc(f'arch-{i}-top',(x,23),(x+8,23),radius_x=4)
    self.add_polyline(f'arch-{i}-rest',(x+8,23),(x+8,28),(x,28))
    self.relate('connect',f'arch-{i}-top',f'arch-{i}-left');self.relate('connect',f'arch-{i}-top',f'arch-{i}-rest');self.relate('connect',f'arch-{i}-left',f'arch-{i}-rest')
''')
put(19,'SQUARE','Binary rows 10100 and 01100 above two water wave lines.','waves: repeated smooth lobes; source supplies literal binary strings.','Wave count reduced from three to two lobes per row; all ten digits retained.','''
for row,text in enumerate(('10100','01100')):
    y=6+row*14
    for col,digit in enumerate(text):
        x=6+col*8;n=f'digit-{row}-{col}'
        if digit=='1':self.add_line(n,(x+2,y),(x+2,y+6))
        else:
            self.add_arc(n+'-top',(x,y+3),(x+4,y+3),radius_x=2,radius_y=3)
            self.add_arc(n+'-bottom',(x+4,y+3),(x,y+3),radius_x=2,radius_y=3)
            self.add_contour(n,n+'-top',n+'-bottom',closed=True)
for row,y in enumerate((32,40)):
    for col in range(2):
        x=6+18*col
        self.add_bezier(f'wave-{row}-{col}',(x,y),((x+3,y+2),(x+6,y+2),(x+9,y+2)),((x+12,y+2),(x+15,y+2),(x+18,y)))
    self.add_contour(f'water-{row}',f'wave-{row}-0',f'wave-{row}-1')
''')
put(20,'VRECT_L','An arched gravestone marked RIP on a rectangular plinth.','No useful exact tombstone original; coherent arch and hand-authored RIP letter contours.','None; all three letters retained.','''
self.add_line('stone-left',(10,36),(10,18))
self.add_arc('stone-arch',(10,18),(38,18),radius_x=14)
self.add_line('stone-right',(38,18),(38,36))
self.add_contour('stone','stone-left','stone-arch','stone-right')
self.add_polyline('plinth',(8,36),(10,36),(38,36),(40,36),(40,44),(8,44),closed=True);self.relate('connect','stone','plinth')
for label,x in [('r',16),('p',31)]:
    self.add_polyline(label+'-stem',(x,29),(x,25),(x,19))
    self.add_arc(label+'-bowl',(x,19),(x,25),radius_x=4,radius_y=3)
    self.relate('connect',label+'-stem',label+'-bowl')
self.add_line('r-leg',(16,25),(21,29));self.relate('connect','r-leg','r-stem');self.relate('connect','r-leg','r-bowl')
self.add_line('i',(25,19),(25,29))
''')

def export(e):u.export(e)
def main():
    for e in ENTRIES:
        if e['action']=='already-valid':print(e['position'],'already valid',e['concept']);continue
        key,subject,refs,omissions,body=SPECS[e['position']]
        d=Path(e['result_dir']);name=e['icon_id'].replace('-','_')+'_'+e['source_uuid'].replace('-','_')+'.py'
        header=f'''"""{subject}
Symbol plan: {refs}
Reduction: {omissions}
Keyshape: {key}; model supplies exact ink extremes.
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
        (d/'plan.json').write_text(json.dumps(dict(subject=subject,keyshape=key,construction_reference=refs,omissions=omissions,python=name),indent=2)+'\n');export(e)
if __name__=='__main__':main()
