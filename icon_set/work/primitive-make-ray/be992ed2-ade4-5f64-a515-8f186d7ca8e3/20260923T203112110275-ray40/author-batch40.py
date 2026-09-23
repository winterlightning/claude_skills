from pathlib import Path
import json,textwrap
AUTHOR='gpt-6'
ROWS=json.loads(Path('/tmp/ray40-unique-202357-intake.json').read_text())
SOURCE_ICON_ID=[r['source_uuid'] for r in ROWS]
SOURCE_PATH=[r['reference_path'] for r in ROWS]
H='''
    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self, n, l, t, r, b, q=3):
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
add('VRECT_M','Door-hanger tag with a large open hook and a minus sign. Hook radii share the vertical axis.','No exact Lucide hanger match; door-closed informed the simple sign treatment.','No defining parts omitted.', '''
self.add_arc('outer-hook',(10,18),(38,18),radius_x=14)
self.add_line('right',(38,18),(38,40))
self.add_arc('bottom-right',(38,40),(34,44),radius_x=4)
self.add_line('bottom',(34,44),(14,44))
self.add_arc('bottom-left',(14,44),(10,40),radius_x=4)
self.add_line('left',(10,40),(10,30))
self.add_bezier('hook-return',(10,30),((10,24),(30,27),(30,18)))
self.add_arc('inner-hook',(30,18),(18,18),radius_x=6,sweep=False)
self.add_line('mouth',(18,18),(10,18))
self.add_contour('tag','outer-hook','right','bottom-right','bottom','bottom-left','left','hook-return','inner-hook','mouth',closed=True)
self.add_line('minus',(20,35),(28,35))
''')
add('SQUARE','Overlapping front and rear tiles with a clockwise rotation arc above the rear tile.','rotate-cw: coherent curved arrow; rounded tile geometry.','No defining parts omitted.', '''
self.box('front',6,14,26,34)
self.add_polyline('rear',(26,26),(42,26),(42,42),(16,42),(16,34))
self.relate('connect','front','rear')
self.add_arc('rotation',(30,6),(42,18),radius_x=12)
self.add_polyline('start-head',(34,6),(30,6),(34,10))
self.add_polyline('end-head',(36,14),(42,18),(42,10))
self.relate('connect','rotation','start-head');self.relate('connect','rotation','end-head')
''')
for j in range(3):
 key='SQUARE' if j<2 else 'HRECT_L'
 add(key,'Closed quadrilateral with two diagonally opposed quarter-circle corners; both radii share one parameter.','No exact Lucide match; elementary tangent quarter-circle construction.','No parts omitted.',f'''
l,t,r,b,q = {('(6,6,42,42,14)' if j<2 else '(4,8,44,40,14)')}
self.add_line('top',(l+q,t),(r,t))
self.add_line('right',(r,t),(r,b-q))
self.add_arc('round-bottom-right',(r,b-q),(r-q,b),radius_x=q)
self.add_line('bottom',(r-q,b),(l,b))
self.add_line('left',(l,b),(l,t+q))
self.add_arc('round-top-left',(l,t+q),(l+q,t),radius_x=q)
self.add_contour('outline','top','right','round-bottom-right','bottom','left','round-top-left',closed=True)
''')
add('SQUARE','Dashed rounded square using four matching quarter-circle corners and four centered short dashes.','square-dashed: equal repeated corner geometry and separated marks.','Reduced dash count to maintain 8-unit centerline gaps.', '''
for n,a,b in [('tl',(6,14),(14,6)),('tr',(34,6),(42,14)),('br',(42,34),(34,42)),('bl',(14,42),(6,34))]:
    self.add_arc(n,a,b,radius_x=8)
for n,a,b in [('top',(22,6),(26,6)),('right',(42,22),(42,26)),('bottom',(26,42),(22,42)),('left',(6,26),(6,22))]: self.add_line(n,a,b)
''')
add('VRECT_L','Interstate shield with scalloped top, header rule and road center dashes.','shield: mirrored protective silhouette with a pointed base.','Two center dashes retained; no text added because source contains none.', '''
self.add_bezier('left-top',(24,6),((19,8),(14,8),(11,4)))
self.add_bezier('left-side',(11,4),((8,10),(8,14),(8,19)),((8,31),(15,40),(24,44)))
self.add_bezier('right-side',(24,44),((33,40),(40,31),(40,19)),((40,14),(40,10),(37,4)))
self.add_bezier('right-top',(37,4),((34,8),(29,8),(24,6)))
self.add_contour('shield','left-top','left-side','right-side','right-top',closed=True)
self.add_line('header',(8,15),(40,15));self.relate('connect','header','shield')
self.add_line('dash-top',(24,23),(24,25))
self.add_line('dash-bottom',(24,33),(24,35))
''')
add('SQUARE','Two empty row bars with a rightward insertion chevron on the left.','square-dashed/rounded rectangle construction: repeated equal corner radii.','No defining parts omitted.', '''
for n,y in [('upper',6),('lower',30)]: self.box(n,20,y,42,y+12,3)
self.add_polyline('insert',(6,18),(12,24),(6,30))
''')
add('SQUARE','Selected row crossing a vertical table fragment, with a right arrow pointing into its left edge.','Rounded rectangle and arrow construction; no exact local Lucide subject match.','Reduced open table fragment to upper and lower L-shaped corners.', '''
self.add_polyline('upper',(24,12),(24,6),(42,6))
self.add_polyline('lower',(24,36),(24,42),(42,42))
self.box('row',16,20,42,28,2)
self.add_line('divider',(29,20),(29,28));self.relate('connect','divider','row')
self.add_line('shaft',(6,24),(8,24))
self.add_polyline('arrow',(6,20),(10,24),(6,28));self.relate('connect','shaft','arrow')
''')
add('SQUARE','Rounded RSS badge containing two broadcast quarter-circles and a circular dot.','rss: concentric quarter-circle broadcasts around a bottom-left origin.','No defining parts omitted.', '''
self.add_line('top',(10,6),(14,6))
self.add_arc('outer-curve',(14,6),(42,34),radius_x=28)
self.add_line('right',(42,34),(42,38))
self.add_arc('br',(42,38),(38,42),radius_x=4)
self.add_line('bottom',(38,42),(10,42))
self.add_arc('bl',(10,42),(6,38),radius_x=4)
self.add_line('left',(6,38),(6,10))
self.add_arc('tl',(6,10),(10,6),radius_x=4)
self.add_contour('badge','top','outer-curve','right','br','bottom','bl','left','tl',closed=True)
for n,r in [('large',20),('small',11)]: self.add_arc(n,(14,34-r),(14+r,34),radius_x=r)
self.circle('dot',14,34,2)
''')
add('VRECT_L','Rounded standing stone containing a vertical angular rune with a triangular upper branch.','No exact local Lucide match; coherent curved stone outline and joined rune strokes.','No defining parts omitted.', '''
self.add_bezier('stone',(12,44),((8,44),(8,42),(8,38)),((9,27),(9,18),(12,12)),((15,4),(21,4),(24,4)),((32,4),(37,10),(38,18)),((39,27),(40,36),(40,40)),((40,44),(36,44),(32,44)),((25,44),(18,44),(12,44)))
self.add_polyline('rune',(19,34),(19,14),(29,22),(19,28),(29,35))
''')
add('VRECT_M','Indian rupee sign with two horizontal rules, rounded bowl and diagonal leg.','indian-rupee: two bars crossing a single rounded bowl plus diagonal leg.','No defining parts omitted.', '''
self.add_line('top',(10,4),(38,4))
self.add_arc('bowl-top',(18,4),(30,16),radius_x=12)
self.add_arc('bowl-bottom',(30,16),(18,28),radius_x=12)
self.add_line('return',(18,28),(10,28))
self.add_line('leg',(10,28),(30,44))
self.add_contour('bowl-leg','bowl-top','bowl-bottom','return','leg')
self.add_line('bar-left',(10,16),(30,16));self.add_line('bar-right',(30,16),(38,16))
self.relate('connect','top','bowl-leg');self.relate('connect','bar-left','bowl-leg');self.relate('connect','bar-right','bowl-leg');self.relate('connect','bar-left','bar-right')
''')
add('SQUARE','Right-pointing evacuation arrow with three flowing flame trails underneath.','rotate-cw: joined arrowhead principles; no useful local flame-trail match.','Reduced bottom flame outline to one smooth tongue; three trails retained.', '''
self.add_polyline('arrow',(6,16),(34,16),(26,8),(28,6),(42,20),(28,34),(26,32),(34,24),(25,24))
self.add_bezier('trail-top',(6,25),((12,27),(18,26),(25,24)));self.relate('connect','arrow','trail-top')
self.add_bezier('trail-mid',(6,34),((12,27),(19,36),(26,29)))
self.add_bezier('trail-bottom',(6,42),((10,33),(17,41),(22,36)),((20,43),(12,42),(6,42)))
''')
add('CIRCLE','Circular Sass logo with an open upper script loop and lower S loop, hand-authored as smooth cubics.','No useful exact local Lucide logo match. Supplied Sass reference owns the calligraphic path.','Simplified small loop curvature to integer knots; retained both script loops.', '''
self.circle('badge',24,24,20)
self.add_bezier('script',(23,21),((31,25),(39,14),(31,12)),((25,10),(14,18),(14,22)),((14,26),(27,27),(24,34)),((22,40),(12,36),(17,32)),((22,28),(30,27),(31,31)),((32,33),(31,35),(30,35)))
''')
add('SQUARE','Bear head below a rising financial arrow; ears and muzzle mirror around x=26.','No exact local Lucide bear match; smooth lobes and coherent financial arrow.','Omitted tiny muzzle crease while retaining split muzzle and two ears.', '''
self.add_polyline('trend',(6,23),(18,11),(30,13),(42,6))
self.add_polyline('arrow',(34,6),(42,6),(42,14));self.relate('connect','trend','arrow')
self.add_bezier('bear',(16,25),((12,18),(20,17),(22,23)),((25,22),(29,22),(32,23)),((35,17),(41,19),(38,26)),((45,37),(38,42),(27,42)),((16,42),(10,37),(16,25)))
self.add_bezier('muzzle',(22,40),((22,28),(32,28),(32,40)),((29,42),(25,42),(22,40)))
self.add_polyline('nose',(27,36),(27,39),(24,41));self.relate('connect','nose','muzzle')
''')
add('HRECT_L','Charging bull silhouette with a curved horn and upward trend arrow behind its back.','No useful exact local Lucide bull match; supplied reference controls asymmetric animal pose.','Omitted minor rear-leg crease; retained horn, head, body, legs, tail and trend.', '''
self.add_bezier('back',(8,26),((14,20),(16,14),(23,18)),((29,20),(31,23),(38,24)),((43,25),(40,29),(40,31)))
self.add_polyline('legs',(40,31),(40,40),(34,40),(36,33),(32,31),(24,31),(18,40),(12,40),(16,33))
self.add_bezier('head',(16,33),((19,24),(12,25),(11,31)),((9,38),(5,34),(6,30)))
self.add_bezier('horn',(6,30),((10,27),(8,20),(4,18)),((7,23),(4,28),(6,30)))
self.add_line('face',(6,30),(8,26))
self.add_contour('animal','back','legs-1','legs-2','legs-3','legs-4','legs-5','legs-6','legs-7','legs-8','head','face',closed=True)
self.relate('connect','horn','animal')
self.add_polyline('tail',(40,30),(44,35),(44,40));self.relate('connect','tail','animal')
self.add_line('trend',(29,18),(40,8));self.add_polyline('arrow',(32,8),(40,8),(40,16));self.relate('connect','trend','arrow')
''')
add('VRECT_L','Money flower: dollar coin atop stem with paired leaves.','sprout: paired leaf contours and shared stem; circular coin and handwritten dollar.','No defining parts omitted.', '''
self.circle('coin',24,14,10)
self.add_bezier('dollar',(27,10),((19,7),(19,15),(24,14)),((30,13),(30,21),(21,18)))
self.add_line('dollar-stem',(24,7),(24,21));self.relate('connect','dollar','dollar-stem')
self.add_line('stem',(24,24),(24,44));self.relate('connect','coin','stem')
for n,s in [('left',-1),('right',1)]:
    def p(x,y):return (24+s*x,y)
    self.add_bezier(n,p(16,28),(p(6,27),p(4,34),p(8,36)),(p(14,38),p(16,33),p(16,28)))
    self.add_line(n+'-branch',p(8,36),(24,44));self.relate('connect',n,n+'-branch');self.relate('connect','stem',n+'-branch')
''')
add('SQUARE','Apple with a short curved stem and three downward gravity arrows.','apple: mirrored lobes, full shoulders and indented base; arrow construction.','No defining parts omitted.', '''
self.add_bezier('apple',(24,13),((13,6),(8,14),(10,23)),((12,32),(19,32),(24,29)),((29,32),(36,32),(38,23)),((40,14),(35,6),(24,13)))
self.add_bezier('stem',(24,13),((24,9),(26,6),(29,6)));self.relate('connect','stem','apple')
for n,x,y in [('left',10,38),('center',24,42),('right',38,38)]:
    self.add_line(n+'-shaft',(x,y-8),(x,y));self.add_polyline(n+'-head',(x-4,y-4),(x,y),(x+4,y-4));self.relate('connect',n+'-shaft',n+'-head')
''')
add('HRECT_L','Scooter under a pitched shelter roof; two wheels, seat, body and steering column.','bike: shared wheel radii and baseline; no useful scooter shelter match.','Omitted tiny seat seam; preserved shelter, seat, scooter body, handle and both wheels.', '''
self.add_polyline('roof',(4,18),(24,8),(44,18))
for n,x in [('rear-wheel',13),('front-wheel',36)]:self.circle(n,x,36,4)
self.add_line('deck',(8,32),(40,32))
self.add_bezier('body',(8,32),((8,24),(21,24),(21,32)))
self.relate('connect','body','deck')
self.add_polyline('seat',(10,25),(9,22),(20,22),(21,25))
self.add_polyline('steering',(29,22),(33,22),(36,32));self.relate('connect','steering','deck')
self.add_arc('front-fender',(29,32),(43,32),radius_x=7)
self.relate('connect','front-fender','deck')
for n in ('rear-wheel','front-wheel'):self.relate('connect',n,'deck')
''')
for row,(k,p,refs,o,b) in zip(ROWS,D):
 out=Path(row['out']);row.update(keyshape=k,plan=p,construction_references=refs,omissions=o)
 src=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = {row['source_uuid']!r}
SOURCE_PATH = {row['reference_path']!r}
AUTHOR = {AUTHOR!r}
# Plan: {p}
# Reference: {refs}
# Reduction: {o}

class AuthoredIcon(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{k}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = {tuple(row['concept'].split())!r}

    def build(self):
'''+textwrap.indent(b,'        ')+'\n'+H
 row['module']=row['icon_id'].replace('-','_')+'_'+row['source_uuid'].replace('-','_')+'.py';(out/row['module']).write_text(src)
Path('/tmp/ray40-unique-202357-intake.json').write_text(json.dumps(ROWS,indent=2));(Path(ROWS[0]['out'])/'author-batch40.py').write_text(Path(__file__).read_text());print('Authored',len(D))
