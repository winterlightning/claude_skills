from pathlib import Path
import json,textwrap
AUTHOR='gpt-6'
ROWS=json.loads(Path('/tmp/ray44-203915-unique.json').read_text())
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
'''
D=[]
def add(k,p,refs,o,b):D.append((k,p,refs,o,textwrap.dedent(b).strip()))
add('VRECT_L','Circular smartwatch face with paired upper and lower strap loops.','watch: dominant circular face with symmetric strap attachments.','No parts omitted; source has an empty watch face.', '''
self.circle('face',24,24,16)
for n,pts in [('upper',((16,10),(16,4),(32,4),(32,10))),('lower',((16,38),(16,44),(32,44),(32,38)))]:
    self.add_polyline(n,*pts);self.relate('connect',n,'face')
''')
add('SQUARE','Sleeping person in bed with two hand-authored Z marks overhead.','bed: simple bedding silhouette; human_ref/user.svg and full_body_ref.png: circular head and smooth shoulder construction.','Omitted minor pillow crease; retained pillow, blanket and both Zs.', '''
self.circle('head',16,25,6)
self.add_bezier('torso',(16,39),((18,39),(21,41),(24,42)))
self.mark_human_figure('sleeper',head='head',torso='torso',torso_junction='start')
self.add_polyline('pillow',(15,34),(6,34),(6,42),(24,42));self.relate('connect','pillow','torso')
self.add_bezier('blanket-top',(24,42),((26,31),(26,30),(31,30)),((36,30),(42,28),(42,35)))
self.add_polyline('blanket-base',(42,35),(42,42),(24,42));self.relate('connect','blanket-top','blanket-base');self.relate('connect','blanket-top','torso')
for n,x,y in [('small',23,15),('large',33,6)]:self.add_polyline(n,(x,y),(x+6,y),(x,y+6),(x+6,y+6))
''')
add('VRECT_L','Snow globe with a pine tree inside and a broad pedestal below.','tree-pine: tiered triangular silhouette; circular globe and symmetric base.','Reduced tree to two tiers; retained trunk and base.', '''
self.circle('globe',24,20,16)
self.add_polyline('base',(10,36),(38,36),(40,44),(8,44),closed=True)
self.relate('connect','base','globe')
self.add_polyline('tree',(24,11),(19,20),(22,20),(17,28),(31,28),(26,20),(29,20),closed=True)
self.add_line('trunk',(24,28),(24,32));self.relate('connect','trunk','tree')
''')
add('SQUARE','Solar panel and sun beside a charging column marked with a lightning bolt.','sun: circular center and radial rays; simple panel grid and rounded charging enclosure.','Reduced sun to four cardinal rays; retained four panel cells and charging bolt.', '''
self.box('charger',30,6,42,42,3)
self.add_polyline('bolt',(37,15),(34,22),(38,22),(35,29))
self.circle('sun',15,14,4)
for n,a,b in [('north',(15,6),(15,7)),('west',(6,14),(7,14)),('east',(23,14),(24,14)),('south',(15,22),(15,23))]:self.add_line(n,a,b)
self.add_polyline('panel',(8,30),(22,30),(25,42),(6,42),closed=True)
self.add_line('column',(15,30),(15,42));self.add_line('row',(7,36),(23,36))
self.relate('connect','column','panel');self.relate('connect','row','panel');self.relate('connect','row','column')
''')
for direction in ('down','up'):
 add('SQUARE',f'{direction.title()}ward arrow over three equally spaced horizontal sort rows.','arrow-down: equal arrow wings and shared shaft endpoint.','No defining parts omitted.',f'''
self.add_line('shaft',(24,6),(24,18))
self.add_polyline('head',*{('((16,10),(24,18),(32,10))' if direction=='down' else '((16,14),(24,6),(32,14))')})
self.relate('connect','shaft','head')
for i in range(3):
    y=26+8*i;self.add_line('row-'+str(i),(6,y),(42,y))
''')
for code in ('SE','SW'):
 add('VRECT_L',f'Compass dial with four ticks and a pointer above the label {code}.','compass: circular dial and geometric pointer; letters authored as strokes.','No parts omitted; pointer direction follows the supplied reference.',f'''
self.circle('dial',24,20,16)
for n,a,b in [('north',(24,4),(24,7)),('south',(24,33),(24,36)),('west',(8,20),(11,20)),('east',(37,20),(40,20))]:
    self.add_line(n,a,b);self.relate('connect',n,'dial')
self.add_polyline('pointer',(19,20),(29,14),(25,26),(23,22),closed=True)
self.add_bezier('s',(20,39),((11,35),(11,42),(17,41)),((23,40),(22,46),(13,43)))
{('self.add_polyline("e",(34,38),(26,38),(26,44),(34,44));self.add_line("e-bar",(26,41),(32,41));self.relate("connect","e","e-bar")' if code=='SE' else 'self.add_polyline("w",(25,38),(28,44),(32,38),(36,44),(39,38))')}
''')
add('SQUARE','Large angular spasm bolt with three short motion rays on its left.','No useful exact local Lucide match; coherent polygon and detached motion strokes.','No parts omitted.', '''
self.add_polyline('bolt',(26,6),(38,6),(30,20),(42,20),(20,42),(24,28),(16,28),closed=True)
for n,a,b in [('upper',(6,16),(8,18)),('middle',(6,26),(8,26)),('lower',(6,36),(8,34))]:self.add_line(n,a,b)
''')
add('SQUARE','Outer ear and inner fold beside a short sound waveform.','ear: continuous outer helix and rounded lower lobe.','Reduced inner fold to one hooked curve; retained waveform.', '''
self.add_arc('outer-top',(18,16),(42,16),radius_x=12,radius_y=10)
self.add_bezier('outer-side',(42,16),((42,29),(34,27),(34,34)))
self.add_arc('lobe',(34,34),(18,34),radius_x=8)
self.add_contour('outer','outer-top','outer-side','lobe')
self.add_bezier('inner',(23,18),((26,10),(35,13),(36,19)))
self.add_bezier('fold',(23,18),((33,16),(34,27),(28,28)),((26,29),(29,33),(23,33)))
self.relate('connect','inner','fold')
self.add_polyline('sound',(6,24),(9,24),(12,28),(16,20),(19,25),(22,25))
''')
add('SQUARE','Open spellbook with a star on its left page and a lower cover edge.','book-open: mirrored page contours with a central gutter.','No defining parts omitted.', '''
self.add_bezier('top-left',(6,10),((6,6),(20,4),(24,12)))
self.add_bezier('top-right',(24,12),((28,4),(42,6),(42,10)))
self.add_polyline('outer',(42,10),(42,42),(6,42),(6,10))
self.add_line('spine',(24,12),(24,39))
self.add_bezier('pages',(6,37),((14,37),(19,35),(24,39)),((29,35),(34,37),(42,37)))
for a,b in [('top-left','top-right'),('top-left','outer'),('top-right','outer'),('spine','top-left'),('spine','top-right'),('spine','pages'),('pages','outer')]:self.relate('connect',a,b)
self.add_polyline('star',(15,17),(17,22),(22,22),(18,25),(19,30),(15,27),(11,30),(12,25),(8,22),(13,22),closed=True)
''')
add('SQUARE','Round plate with a three-tined fork inside and a short diagonal utensil handle outside.','utensils: equal tines and a rounded fork bowl; supplied image has no separate spoon bowl.','No defining parts omitted.', '''
self.circle('plate',23,23,17)
self.add_line('tine-left',(17,15),(17,23));self.add_arc('bowl',(17,23),(29,23),radius_x=6,sweep=False)
self.add_line('tine-right',(29,23),(29,15));self.add_contour('fork','tine-left','bowl','tine-right')
self.add_line('center-tine',(23,15),(23,29));self.add_line('handle',(23,29),(23,33))
self.relate('connect','center-tine','fork');self.relate('connect','handle','fork');self.relate('connect','center-tine','handle')
self.add_line('outer-handle',(35,35),(42,42));self.relate('connect','outer-handle','plate')
''')
add('SQUARE','Curling stone, diagonal broom and small curling stone marker.','No useful exact local Lucide match; coherent stone dome, handle and diagonal broom.','Omitted small stone side seam; retained handle, broom head and round marker.', '''
self.add_arc('stone-top',(6,28),(26,28),radius_x=10,radius_y=6)
self.add_line('stone-mid',(6,28),(26,28));self.relate('connect','stone-top','stone-mid')
self.add_bezier('stone-side',(6,28),((6,35),(8,36),(10,36)))
self.relate('connect','stone-side','stone-top');self.relate('connect','stone-side','stone-mid')
self.add_polyline('handle',(13,22),(13,17),(21,17));self.relate('connect','handle','stone-top')
self.add_line('broom-shaft',(42,6),(23,40))
self.add_bezier('broom-head',(23,40),((21,44),(13,42),(13,38)),((13,32),(19,34),(27,35)))
self.relate('connect','broom-shaft','broom-head')
self.circle('marker',36,39,3)
''')
add('CIRCLE','Spotify circular logo with three progressively shorter curved broadcast lines.','No exact local Lucide logo match; supplied reference owns the three nested curves.','No defining parts omitted.', '''
self.circle('badge',24,24,20)
self.add_bezier('upper',(14,18),((20,14),(28,14),(34,18)))
self.add_bezier('middle',(17,27),((22,23),(26,23),(31,27)))
self.add_bezier('lower',(20,35),((22,32),(26,32),(28,35)))
''')
add('SQUARE','Spreadsheet grid with lower-right analytics chart cutout and a rising curve.','Rounded grid construction; coherent chart axes and smooth S-shaped data trend.','Reduced grid to two columns and two rows; retained chart cutout.', '''
self.add_polyline('table',(6,42),(6,6),(42,6),(42,24),(24,24),(24,42),closed=True)
self.add_line('header',(6,15),(42,15));self.add_line('row',(6,24),(24,24));self.add_line('column',(24,15),(24,24))
for n in ('header','row','column'):self.relate('connect',n,'table')
self.relate('connect','header','column');self.relate('connect','row','column')
self.add_polyline('axes',(30,30),(30,42),(42,42))
self.add_bezier('curve',(30,38),((37,38),(35,32),(42,32)));self.relate('connect','axes','curve')
''')
add('SQUARE','Rounded square enclosing a hand-drawn ampersand with crossed lower loop.','No exact local Lucide ampersand match; smooth handwritten loops and canonical rounded frame.','No defining parts omitted.', '''
self.box('frame',6,6,42,42,4)
self.add_bezier('ampersand',(31,33),((27,29),(17,20),(18,17)),((19,11),(29,12),(28,18)),((27,22),(16,23),(15,28)),((13,36),(28,38),(32,25)))
''')
for mode in ('down-right','down','left','right'):
 p={'down-right':'Diagonal arrow points down-right inside a rounded square, matching the supplied artwork rather than its down-left filename.','down':'Vertical downward arrow in a rounded square; supplied artwork is not diagonal.','left':'Leftward arrow in a rounded square.','right':'Rightward arrow in a rounded square.'}[mode]
 body={'down-right':"self.add_line('shaft',(15,15),(33,33))\nself.add_polyline('head',(23,33),(33,33),(33,23))",'down':"self.add_line('shaft',(24,15),(24,33))\nself.add_polyline('head',(16,25),(24,33),(32,25))",'left':"self.add_line('shaft',(33,24),(15,24))\nself.add_polyline('head',(23,16),(15,24),(23,32))",'right':"self.add_line('shaft',(15,24),(33,24))\nself.add_polyline('head',(25,16),(33,24),(25,32))"}[mode]
 add('SQUARE',p,'square-arrow-right: consistent rounded frame and joined arrow shaft/head.','No defining parts omitted.',"self.box('frame',6,6,42,42,4)\n"+body+"\nself.relate('connect','shaft','head')")
for r,(k,plan,refs,o,b) in zip(ROWS,D):
 out=Path(r['out']);r.update(keyshape=k,plan=plan,construction_references=refs,omissions=o)
 src=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {r['source_uuid']!r}
SOURCE_PATH = {r['reference_path']!r}
AUTHOR = {AUTHOR!r}
# Plan: {plan}
# References: {refs}
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
Path('/tmp/ray44-203915-unique.json').write_text(json.dumps(ROWS,indent=2));(Path(ROWS[0]['out'])/'author-batch44.py').write_text(Path(__file__).read_text());print('Authored',len(D))
