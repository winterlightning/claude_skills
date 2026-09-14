from pathlib import Path
import sys,json,ast,textwrap
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
SOURCE_ICON_ID=None
SOURCE_PATH='icon_set/work/narrow-tall-repair/targets.json'
AUTHOR='gpt-6'
W=Path(__file__).parent;rows=json.loads((W/'results.json').read_text());by={r['root']:r for r in rows}
def edit(k,changes,note=None):
 r=by[k];p=ROOT/r['file'];s=p.read_text()
 for a,b in changes:
  assert a in s,(k,a);s=s.replace(a,b)
 p.write_text(s)
 if note:r['note']=note

def build(k,body,note,shape=None):
 r=by[k];p=ROOT/r['file'];s=p.read_text();s=s[:s.index('    def build')]
 if shape:
  import re
  s=re.sub(r'keyshape = Keyshape.\w+',f'keyshape = Keyshape.{shape}',s)
 p.write_text(s+'    def build(self) -> None:\n'+textwrap.indent(textwrap.dedent(body).strip(),'        ')+'\n');r['note']=note

def coords(k,xs={},ys={},changes=(),note=None):
 r=by[k];p=ROOT/r['file'];t=ast.parse(p.read_text())
 class T(ast.NodeTransformer):
  def visit_Tuple(self,n):
   if len(n.elts)==2 and all(isinstance(v,ast.Constant) and type(v.value) in (int,float) for v in n.elts):
    n.elts[0].value=xs.get(n.elts[0].value,n.elts[0].value);n.elts[1].value=ys.get(n.elts[1].value,n.elts[1].value)
   return self.generic_visit(n)
 p.write_text(ast.unparse(ast.fix_missing_locations(T().visit(t)))+'\n');edit(k,changes,note)
coords('canyon-buttes-with-sun',ys={10:11},note='Square envelope; moved the sun down one unit without changing its radius or the buttes.')
coords('chiron-astrological-symbol',ys={2:4,46:44},changes=[('radius_x=13, radius_y=11','radius_x=16, radius_y=10')],note='Widened the key bow and inset the stem and bow ends on VRECT_L.')
coords('diamond-drop-earring',xs={11:8,37:40},ys={2:4,12:14,20:22,28:30,46:44},note='Broadened the diamond at its facet and inset the stud and drop ends; retained the facet.')
coords('mercury-astrological-symbol',xs={11:8,37:40},ys={2:4,46:44},changes=[('radius_x=13, radius_y=10','radius_x=16, radius_y=8')],note='Widened the crescent horns with shared radii and inset the top and cross ends.')
coords('minoan-palace',ys={43:42},note='Square envelope; ended all four columns at the shared base instead of below it.')
coords('sheep-head',changes=[('radius_x=14, radius_y=14','radius_x=14, radius_y=13'),('radius_x=14, radius_y=24','radius_x=14, radius_y=23')],note='Square envelope; canonical elliptical crown and chin reach exact integer extremes.')
coords('snow-capped-mountain-with-sun',ys={10:9},note='Square envelope; moved the sun up one unit and retained the snowline and mountain.')
coords('titanic-belfast-museum',ys={35:34},note='Square envelope; opened the plinth band to eight units, moving all attached walls with it.')
coords('penguin-face',changes=[('radius_x=16, radius_y=16','radius_x=16, radius_y=15')],note='Square envelope; corrected paired dome radii to exact quarter ellipses and certified eye spacing.')
coords('sloth-face',xs={14:17,34:31},ys={30:29},note='Square envelope; moved both eyes inward together, retaining the attached eye masks.')
coords('turreted-chateau-hotel',xs={14:12},note='Square envelope; widened the gap between the left turret divider and the main gable.')
coords('azadi-tower',xs={14:15,34:33},note='Square envelope; widened the two lower legs by shifting the inner foot corners toward the axis.')
coords('salamander',ys={15:16},note='Square envelope; moved the head station down one unit to fit the crown and open eye clearance.')
# A single shared bow profile controls all four quarters.
build('clam-shell','''
# SQUARE centerlines (6,6)-(42,42). Asymmetric shell with shared
# upper/lower radii, one valve crease and a short hinge.
axis_y, apex_x, left_x, right_x = 24, 14, 6, 42
for name,a,b,rx in [
 ('top-left',(left_x,axis_y),(apex_x,6),8),
 ('top-right',(apex_x,6),(right_x,axis_y),28),
 ('bottom-right',(right_x,axis_y),(apex_x,42),28),
 ('bottom-left',(apex_x,42),(left_x,axis_y),8)]:
    self.add_arc(name,a,b,radius_x=rx,radius_y=18)
self.add_contour('shell','top-left','top-right','bottom-right','bottom-left',closed=True)
self.add_polyline('valve',(apex_x,6),(34,axis_y),(apex_x,42))
self.add_line('hinge',(left_x,axis_y),(24,axis_y))
self.relate('connect','valve','shell')
self.relate('connect','hinge','shell')
''','Canonical quarter ellipses remove off-grid extremes; valve creases now attach at exact shell nodes.')
build('corded-computer-mouse','''
# VRECT_L (8,4)-(40,44). Shared capsule axis and elliptical cap radii;
# button seam and cable meet the same cap endpoints.
x, left, right, upper, lower, rx, ry = 24, 8, 40, 24, 32, 16, 12
self.add_arc('ne',(x,12),(right,upper),radius_x=rx,radius_y=ry)
self.add_line('right',(right,upper),(right,lower))
self.add_arc('se',(right,lower),(x,44),radius_x=rx,radius_y=ry)
self.add_arc('sw',(x,44),(left,lower),radius_x=rx,radius_y=ry)
self.add_line('left',(left,lower),(left,upper))
self.add_arc('nw',(left,upper),(x,12),radius_x=rx,radius_y=ry)
self.add_contour('body','ne','right','se','sw','left','nw',closed=True)
self.add_line('cord',(x,4),(x,12))
self.add_polyline('buttons',(left,upper),(x,upper),(right,upper))
self.add_line('divider',(x,12),(x,upper))
for part in ('cord','buttons','divider'):self.relate('connect','body',part)
self.relate('connect','buttons','divider')
''','Broadened the capsule with matched elliptical caps, inset the ends and retained the cable and two buttons.')
build('necktie','''
# SQUARE (6,6)-(42,42). Diagonal tie; paired edges reflect about
# x+y=48. Shared neck corners join the trapezoid knot to the blade.
a,b=(24,14),(34,24)
self.add_polyline('knot',(30,6),(42,18),b,a,closed=True)
self.add_polyline('blade',a,(8,28),(6,42),(20,40),b)
self.relate('connect','knot','blade')
''','Re-authored diagonally to preserve a narrow tie blade and trapezoid knot without stretching it sideways.','SQUARE')
build('oval-jewel-earring','''
# VRECT_L (8,4)-(40,44). Shared axis, open hook above a broad oval jewel.
x=24
self.add_arc('hook-top',(14,10),(34,10),radius_x=10,radius_y=6)
self.add_arc('hook-return',(x,16),(14,10),radius_x=10,radius_y=6)
self.add_contour('hook','hook-return','hook-top')
self.add_line('post',(x,16),(x,20))
self.add_arc('jewel-right',(x,20),(x,44),radius_x=16,radius_y=12)
self.add_arc('jewel-left',(x,44),(x,20),radius_x=16,radius_y=12)
self.add_contour('jewel','jewel-right','jewel-left',closed=True)
self.relate('connect','hook','post')
self.relate('connect','post','jewel')
''','Enlarged the oval jewel and inset the open hook; retained the hook, post and jewel.')
build('teardrop-earring','''
# VRECT_L (8,4)-(40,44). Shared axis, circular hook and paired
# smooth shoulders tangent to the lower elliptical bowl.
x=24
self.add_arc('hook',(18,10),(30,10),radius_x=6)
self.add_arc('hook-return',(30,10),(x,16),radius_x=6)
self.add_line('post',(x,16),(x,20))
self.add_contour('earwire','hook','hook-return','post')
self.add_bezier('drop-left',(x,20),((16,24),(8,28),(8,32)))
self.add_arc('drop-bottom',(8,32),(40,32),radius_x=16,radius_y=12,sweep=False)
self.add_bezier('drop-right',(40,32),((40,28),(32,24),(x,20)))
self.add_contour('pendant','drop-left','drop-bottom','drop-right',closed=True)
self.relate('connect','earwire','pendant')
''','Broadened the drop with mirrored curved shoulders and an elliptical bowl; kept the open hook.')
build('three-bead-drop-earring','''
# SQUARE (6,6)-(42,42). Diagonal chain preserves three round beads;
# a shared circular definition and two true attachment nodes control links.
for name,cx,cy in [('stud',9,9),('drop',39,39)]:
    self.add_arc(name+'-right',(cx,cy-3),(cx,cy+3),radius_x=3)
    self.add_arc(name+'-left',(cx,cy+3),(cx,cy-3),radius_x=3)
    self.add_contour(name,name+'-right',name+'-left',closed=True)
points=((16,18),(30,16),(32,30),(18,32),(16,18))
for i,(a,b) in enumerate(zip(points,points[1:])):self.add_arc(f'main-{i}',a,b,radius_x=10)
self.add_contour('main',*[f'main-{i}' for i in range(4)],closed=True)
self.add_line('upper-link',(9,12),(16,18))
self.add_line('lower-link',(32,30),(39,36))
for a,b in [('stud','upper-link'),('main','upper-link'),('main','lower-link'),('drop','lower-link')]:self.relate('connect',a,b)
''','Re-authored the three-bead chain diagonally to preserve circular beads and avoid an oversized middle bead.','SQUARE')
coords('venus-astrological-symbol',ys={2:4,28:30,46:44},changes=[('radius_x=13)','radius_x=16, radius_y=13)')],note='Broadened the ring to a gentle oval and inset the stem, preserving the centered cross.')
build('walking-cane','''
# SQUARE (6,6)-(42,42). Tilt the shaft while keeping a compact hook.
# Circular crown, short tangent bend, then a straight shaft on a 3:2 slope.
self.add_arc('hook',(22,16),(42,16),radius_x=10)
self.add_bezier('bend',(42,16),((42,18),(39,20),(36,22)))
self.add_line('shaft',(36,22),(6,42))
self.add_contour('cane','hook','bend','shaft')
''','Re-authored diagonally with a compact circular handle and smooth tangent transition to the straight shaft.','SQUARE')
build('usb-cable-connector','''
# VRECT_L (8,4)-(40,44). Broad rounded grip and stepped USB tip;
# one shared cable attachment joins a tangent quarter-circle bend.
cx=28
self.add_polyline('tip',(18,20),(18,4),(38,4),(38,20))
self.add_polyline('top',(16,20),(18,20),(38,20),(40,20))
self.add_line('right',(40,20),(40,24))
self.add_arc('se',(40,24),(cx,36),radius_x=12)
self.add_arc('sw',(cx,36),(16,24),radius_x=12)
self.add_line('left',(16,24),(16,20))
# Flatten the top polyline into the surrounding contour.
self.contours.clear()
self.add_contour('tip','tip-1','tip-2','tip-3')
self.add_contour('body','top-1','top-2','top-3','right','se','sw','left',closed=True)
self.add_dot('tip-mark',(cx,12))
self.add_arc('cable-bend',(cx,36),(20,44),radius_x=8)
self.add_line('cable-end',(20,44),(8,44))
self.add_contour('cable','cable-bend','cable-end')
self.relate('connect','tip','body')
self.relate('connect','body','cable')
''','Opened the plug for its contact mark, widened the grip and shortened the tangent cable bend.')
build('usb-flash-drive','''
# VRECT_L (8,4)-(40,44). Shared axis and six-unit lower corners.
# A 24-unit plug holds two equal contacts eight units apart.
self.add_polyline('plug',(12,20),(12,4),(36,4),(36,20))
self.add_polyline('top',(8,20),(12,20),(36,20),(40,20))
self.add_line('right',(40,20),(40,38))
self.add_arc('se',(40,38),(34,44),radius_x=6)
self.add_line('bottom',(34,44),(14,44))
self.add_arc('sw',(14,44),(8,38),radius_x=6)
self.add_line('left',(8,38),(8,20))
self.contours.clear()
self.add_contour('plug','plug-1','plug-2','plug-3')
self.add_contour('body','top-1','top-2','top-3','right','se','bottom','sw','left',closed=True)
self.relate('connect','body','plug')
for side,x in [('left',20),('right',28)]:self.add_dot('pin-'+side,(x,12))
''','Broadened the plug and body, retaining two contacts with eight-unit spacing and rounded lower corners.')
build('vintage-studio-microphone','''
# VRECT_L (8,4)-(40,44). Capsule and broad foot share x=24.
# Two grille rows replace three crowded rows; paired half-bars repeat.
cx,left,right=24,14,34
self.add_arc('nw',(left,14),(cx,4),radius_x=10)
self.add_arc('ne',(cx,4),(right,14),radius_x=10)
self.add_line('right',(right,14),(right,22))
self.add_arc('se',(right,22),(cx,32),radius_x=10)
self.add_arc('sw',(cx,32),(left,22),radius_x=10)
self.add_line('left',(left,22),(left,14))
self.add_contour('capsule','nw','ne','right','se','sw','left',closed=True)
for y in (14,22):
    for side,a,b in [('left',left,20),('right',28,right)]:
        name=f'grille-{side}-{y}'
        self.add_line(name,(a,y),(b,y))
        self.relate('connect','capsule',name)
self.add_line('stem',(cx,32),(cx,44))
self.add_polyline('base',(8,44),(cx,44),(40,44))
self.relate('connect','capsule','stem')
self.relate('connect','stem','base')
''','Widened the foot and capsule; replaced three crowded grille rows with two equally spaced rows.')
(W/'results.json').write_text(json.dumps(rows,indent=2))
