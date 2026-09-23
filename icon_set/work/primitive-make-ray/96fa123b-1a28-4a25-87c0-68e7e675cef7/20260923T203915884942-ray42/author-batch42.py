from pathlib import Path
import json,textwrap
AUTHOR='gpt-6'
ROWS=json.loads(Path('/tmp/ray42-203112-unique.json').read_text())
SOURCE_ICON_ID=[r['source_uuid'] for r in ROWS]
SOURCE_PATH=[r['reference_path'] for r in ROWS]
H='''
    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

    def shield(self):
        self.add_bezier('crown-left',(8,12),((15,12),(21,7),(24,4)))
        self.add_bezier('crown-right',(24,4),((27,7),(33,12),(40,12)))
        self.add_line('wall-right',(40,12),(40,23))
        self.add_bezier('base-right',(40,23),((40,33),(33,40),(24,44)))
        self.add_bezier('base-left',(24,44),((15,40),(8,33),(8,23)))
        self.add_line('wall-left',(8,23),(8,12))
        self.add_contour('shield','crown-left','crown-right','wall-right','base-right','base-left','wall-left',closed=True)
'''
D=[]
def add(k,p,refs,o,b):D.append((k,p,refs,o,textwrap.dedent(b).strip()))
add('SQUARE','Rounded settings panel with two horizontal switches, knobs on opposite ends.','toggle-left: capsule and circular knob; shared dimensions for both switches.','No defining parts omitted.', '''
self.box('panel',6,6,42,42)
for n,y,x in [('upper',14,18),('lower',28,30)]:
    self.box(n,14,y,34,y+8,4)
    self.circle(n+'-knob',x,y+4,4)
    self.relate('connect',n,n+'-knob')
''')
add('SQUARE','Notification bell above three shareholder busts, with shared head radii and exact own head-to-shoulder gaps.','bell: flared contour; human_ref/user.svg and full_body_ref.png: circular heads and smooth shoulders.','Omitted tiny bell top loop; retained bell clapper and all three people.', '''
self.add_bezier('bell',(14,18),((19,14),(15,6),(24,6)),((33,6),(29,14),(34,18)))
self.add_line('bell-base',(34,18),(14,18));self.add_contour('bell-outline','bell','bell-base',closed=True)
self.add_arc('clapper',(21,18),(27,18),radius_x=3,sweep=False);self.relate('connect','clapper','bell-outline')
for n,x in [('left',11),('center',24),('right',37)]:
    self.circle(n+'-head',x,26,3)
    self.add_bezier(n+'-torso',(x,37),((x-3,37),(x-5,39),(x-5,42)))
    self.add_bezier(n+'-shoulder',(x,37),((x+3,37),(x+5,39),(x+5,42)))
    self.relate('connect',n+'-torso',n+'-shoulder')
    self.mark_human_figure(n,head=n+'-head',torso=n+'-torso',torso_junction='start')
''')
for q in (3,0):
 add('SQUARE','Television on a trapezoidal stand above a low shelf with two short legs.','tv: rounded screen with clean straight sides; paired stand and shelf legs share x-axis symmetry.','No defining parts omitted.',f'''
self.box('screen',10,6,38,22,2)
self.add_line('stand-left',(19,22),(15,30));self.add_line('stand-right',(29,22),(33,30))
{'self.box("shelf",6,30,42,38,3)' if q else 'self.add_polyline("shelf",(6,30),(42,30),(42,38),(6,38),closed=True)'}
for n in ('stand-left','stand-right'):
    self.relate('connect',n,'screen');self.relate('connect',n,'shelf')
for n,x in [('left',10),('right',38)]:
    self.add_line(n+'-leg',(x,38),(x,42));self.relate('connect',n+'-leg','shelf')
''')
add('VRECT_L','Plain shield with angled upper rim and a softly pointed base.','shield: symmetric tapered sides and coherent base curves.','No parts omitted.', '''
self.add_polyline('upper',(8,22),(8,10),(24,4),(40,10),(40,22))
self.add_bezier('base',(40,22),((40,33),(33,40),(24,44)),((15,40),(8,33),(8,22)))
self.relate('connect','upper','base')
''')
add('VRECT_L','Plain shield with gently arched upper rim and rounded pointed base.','shield: equal side curves; crown deliberately softer than shield 1.','No parts omitted.', '''
self.add_bezier('top',(8,8),((13,6),(19,4),(24,4)),((29,4),(35,6),(40,8)))
self.add_line('right',(40,8),(40,24))
self.add_bezier('bottom',(40,24),((40,34),(32,40),(24,44)),((16,40),(8,34),(8,24)))
self.add_line('left',(8,24),(8,8))
self.add_contour('outline','top','right','bottom','left',closed=True)
''')
add('VRECT_L','Crowned shield with a horizontal upper band and pointed lower body.','shield: mirrored tapered lower silhouette.','No parts omitted.', '''
self.add_polyline('crown',(8,16),(8,8),(14,11),(24,4),(34,11),(40,8),(40,16))
self.add_line('band',(8,16),(40,16))
self.add_bezier('lower',(40,16),((42,29),(35,37),(24,44)),((13,37),(6,29),(8,16)))
self.relate('connect','crown','band');self.relate('connect','band','lower');self.relate('connect','crown','lower')
''')
add('VRECT_L','Crested shield enclosing a check mark.','shield-check: broad clear shield and a simple joined check.','No parts omitted.', '''
self.shield()
self.add_polyline('check',(18,25),(23,30),(31,21))
''')
add('VRECT_L','Crested shield enclosing an exclamation mark.','shield-alert: central vertical stroke and detached round point.','No parts omitted.', '''
self.shield()
self.add_line('exclamation',(24,17),(24,25))
self.add_dot('point',(24,34))
''')
add('SQUARE','Parcel cube behind a smartphone with an approval tick and bottom home mark.','package: three visible faces with a shared center seam; rounded phone contour.','Omitted box seam hidden behind phone; retained tick and home mark.', '''
self.add_polyline('box-top',(6,12),(18,6),(30,12),(18,19),closed=True)
self.add_polyline('box-left',(6,12),(6,27),(18,34),(18,19))
self.relate('connect','box-top','box-left')
self.add_line('box-edge',(30,12),(30,16));self.relate('connect','box-top','box-edge')
self.box('phone',26,21,42,42,3)
self.add_polyline('check',(30,29),(33,32),(38,27))
self.add_line('home',(32,37),(36,37))
''')
add('SQUARE','Fragile parcel with top packing ribbon, wine-glass handling symbol and upward arrow.','package and wine: clear folded tape and bowl/stem construction.','No defining parts omitted.', '''
self.box('box',6,6,42,42,3)
self.add_polyline('tape',(18,6),(18,17),(24,13),(30,17),(30,6));self.relate('connect','tape','box')
self.add_polyline('glass-rim',(15,24),(23,24),(23,29))
self.add_arc('glass-bowl',(23,29),(15,29),radius_x=4)
self.add_line('glass-left',(15,29),(15,24))
self.add_contour('glass','glass-rim-1','glass-rim-2','glass-bowl','glass-left',closed=True)
self.add_line('stem',(19,33),(19,37));self.relate('connect','stem','glass')
self.add_line('foot',(16,37),(22,37));self.relate('connect','stem','foot')
self.add_line('arrow-shaft',(33,36),(33,24));self.add_polyline('arrow-head',(29,28),(33,24),(37,28));self.relate('connect','arrow-shaft','arrow-head')
''')
add('CIRCLE','Circular confirmation badge with a simple check mark, matching the supplied ETA reference.','shield-check: joined two-stroke check; circle made of matching semicircles.','No parts omitted; supplied image contains no vehicle or clock.', '''
self.circle('badge',24,24,20)
self.add_polyline('check',(14,24),(21,31),(33,18))
''')
add('SQUARE','Shoemaker with a circular head, apron and a shoe in the lower right foreground.','human_ref/user.svg and full_body_ref.png: circular head and broad smooth shoulders; no exact shoe match.','Omitted small apron side seam; retained apron, shoulder outline and shoe.', '''
self.circle('head',20,13,7)
self.add_bezier('torso',(20,28),((9,28),(6,31),(6,38)))
self.add_bezier('shoulder-right',(20,28),((31,28),(34,30),(34,34)));self.relate('connect','torso','shoulder-right')
self.add_line('left-side',(6,38),(6,42));self.relate('connect','torso','left-side')
self.add_polyline('apron',(14,28),(14,34),(11,42),(22,42))
self.relate('connect','apron','torso')
self.add_bezier('shoe',(23,42),((23,35),(23,35),(29,37)),((33,39),(32,33),(36,36)),((38,39),(42,37),(42,42)))
self.add_line('sole',(42,42),(23,42));self.relate('connect','sole','shoe')
self.mark_human_figure('shoemaker',head='head',torso='torso',torso_junction='start')
''')
add('SQUARE','Rifle silhouette crosses a concentric target with vertical sight marks.','No useful exact local Lucide rifle match; concentric circles and straight sight axes.','Reduced target to two rings; retained stock, barrel, trigger and crosshair.', '''
self.circle('target',24,24,18)
self.circle('inner',24,24,10)
self.add_polyline('rifle',(6,24),(24,24),(28,23),(42,23))
self.add_polyline('stock',(6,24),(6,32),(18,28),(28,28),(30,23))
self.relate('connect','rifle','stock')
self.add_arc('trigger',(19,28),(23,28),radius_x=2,sweep=False);self.relate('connect','trigger','stock')
self.add_line('sight-top',(24,6),(24,16));self.add_line('sight-bottom',(24,33),(24,42))
self.relate('connect','sight-top','target');self.relate('connect','sight-top','inner');self.relate('connect','sight-bottom','target');self.relate('connect','sight-bottom','inner')
''')
add('SQUARE','Shopping basket beneath three rating stars, with the middle star raised.','No exact useful Lucide rating match; shared star definition and mirrored basket sides.','Reduced basket ribs to two; retained three stars and both handles.', '''
for n,x,y in [('left',11,16),('center',24,11),('right',37,16)]:
    self.add_polyline(n,(x,y-5),(x+2,y-1),(x+5,y-1),(x+3,y+2),(x+4,y+5),(x,y+3),(x-4,y+5),(x-3,y+2),(x-5,y-1),(x-2,y-1),closed=True)
self.add_line('rim',(8,29),(40,29))
self.add_polyline('basket',(10,29),(14,42),(34,42),(38,29));self.relate('connect','basket','rim')
for n,a,b in [('left',(15,29),(19,23)),('right',(33,29),(29,23))]:self.add_line(n+'-handle',a,b);self.relate('connect',n+'-handle','rim')
for x in (20,28):self.add_line('rib-'+str(x),(x,34),(x,38))
''')
add('SQUARE','Dollar coin crossed by a rising diagonal suppression slash.','No exact local Lucide match; circular badge and handwritten dollar curves.','No defining parts omitted.', '''
self.circle('coin',24,25,17)
self.add_bezier('dollar',(29,17),((17,10),(14,26),(24,25)),((36,25),(31,39),(19,33)))
self.add_line('dollar-stem',(24,12),(24,37));self.relate('connect','dollar','dollar-stem')
self.add_line('slash',(6,42),(42,6))
self.relate('connect','slash','coin');self.relate('connect','slash','dollar');self.relate('connect','slash','dollar-stem')
''')
add('SQUARE','Diamond road sign with a curved rightward branch rising from the lower left.','No exact local Lucide match; joined arrow contour within a symmetric diamond.','No parts omitted; arrow direction follows source despite filename.', '''
self.add_polyline('diamond',(24,6),(42,24),(24,42),(6,24),closed=True)
self.add_line('stem',(18,30),(18,26))
self.add_arc('turn',(18,26),(24,20),radius_x=6)
self.add_line('shaft',(24,20),(30,20));self.add_contour('road','stem','turn','shaft')
self.add_polyline('head',(26,16),(30,20),(26,24));self.relate('connect','road','head')
''')
add('SQUARE','Diamond road sign with a straight upward arrow and a lower right branch.','No exact local Lucide match; shared arrow/branch junction.','No parts omitted.', '''
self.add_polyline('diamond',(24,6),(42,24),(24,42),(6,24),closed=True)
self.add_line('shaft',(23,31),(23,17))
self.add_polyline('head',(19,21),(23,17),(27,21));self.relate('connect','shaft','head')
self.add_line('branch',(23,25),(30,32));self.relate('connect','branch','shaft')
''')
add('SQUARE','Open hand with four upright fingers, left thumb and downward motion arrow by the palm.','hand: rounded fingertips and coherent palm; human_ref/user.svg and full_body_ref.png inspected for shared human vocabulary, no detached head in this subject.','Omitted minor palm crease; retained four fingers, thumb and motion arrow.', '''
self.add_bezier('outline',(25,40),((13,40),(8,37),(7,29)),((4,20),(7,19),(11,27)))
self.add_line('thumb-web',(11,27),(15,10))
self.add_arc('index-tip',(15,10),(21,10),radius_x=3)
self.add_line('index-side',(21,10),(18,25))
self.add_line('middle-left',(20,16),(22,9))
self.add_arc('middle-tip',(22,9),(28,9),radius_x=3)
self.add_line('middle-right',(28,9),(25,25))
self.add_line('ring-left',(28,13),(30,12))
self.add_arc('ring-tip',(30,12),(36,14),radius_x=4)
self.add_line('ring-right',(36,14),(33,27))
self.add_arc('little-tip',(35,19),(41,21),radius_x=4)
self.add_line('little-side',(41,21),(39,29))
self.add_bezier('palm',(25,40),((33,41),(36,35),(36,31)))
for a,b in [('outline','thumb-web'),('thumb-web','index-tip'),('index-tip','index-side'),('middle-left','middle-tip'),('middle-tip','middle-right'),('ring-left','ring-tip'),('ring-tip','ring-right'),('little-tip','little-side'),('palm','outline')]:self.relate('connect',a,b)
self.add_bezier('motion',(29,28),((40,28),(42,34),(42,42)))
self.add_polyline('motion-head',(38,38),(42,42),(46,38));self.relate('connect','motion','motion-head')
''')
add('SQUARE','Circular wireless signal crossed by a diagonal slash, with broadcast arcs and a dot.','signal plus concentric wireless arc principles; source is wireless, not bar signal.','Reduced outer ring to two arcs around slash clearance; two wireless arcs and dot retained.', '''
self.add_arc('ring-upper',(13,10),(38,35),radius_x=18,large_arc=True)
self.add_arc('ring-lower',(35,40),(8,13),radius_x=18,large_arc=True)
self.add_bezier('wave-top',(14,19),((21,13),(31,15),(36,21)))
self.add_bezier('wave-bottom',(19,26),((24,21),(29,23),(32,27)))
self.circle('dot',24,34,3)
self.add_line('slash',(6,6),(42,42))
self.relate('connect','slash','wave-top');self.relate('connect','slash','wave-bottom')
''')
for r,(k,plan,refs,o,b) in zip(ROWS,D):
 out=Path(r['out']);r.update(keyshape=k,plan=plan,construction_references=refs,omissions=o)
 src=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {r['source_uuid']!r}
SOURCE_PATH = {r['reference_path']!r}
AUTHOR = {AUTHOR!r}
# Plan: {plan}
# Construction references: {refs}
# Reduction: {o}

class AuthoredIcon(Solo48):
    icon_id = {r['icon_id']!r}
    keyshape = Keyshape.{k}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = {tuple(r['concept'].split())!r}

    def build(self):
'''+textwrap.indent(b,'        ')+'\n'+H
 r['module']=r['icon_id'].replace('-','_')+'_'+r['source_uuid'].replace('-','_')+'.py';(out/r['module']).write_text(src)
Path('/tmp/ray42-203112-unique.json').write_text(json.dumps(ROWS,indent=2));(Path(ROWS[0]['out'])/'author-batch42.py').write_text(Path(__file__).read_text());print('Authored',len(D))
