"""Source-complete centerline repairs, batch 6."""
D={}
GLYPHS={}
def plan(n,shape,parts,ref,body):D[n]=(shape,parts,ref,body)
plan(1,'CIRCLE','Circular clock with connected upright minute hand and right-facing hour hand.','clock',"""
circle(self,'frame',16,16,14)
self.add_polyline('hands',(16,9),(16,16),(21,16))
""")
plan(3,'HRECT_L','Two horizontal rounded links with inward-curved returning tips and separate middle connecting bar.','link',"""
for name,mirror in [('left',False),('right',True)]:
 def p(x,y):return (32-x if mirror else x,y)
 sweep=mirror
 self.add_arc(name+'-return-top',p(12,9),p(8,6),radius_x=4,radius_y=3,sweep=sweep)
 self.add_line(name+'-top',p(8,6),p(6,6))
 self.add_arc(name+'-tl',p(6,6),p(2,10),radius_x=4,sweep=sweep)
 self.add_line(name+'-side',p(2,10),p(2,22))
 self.add_arc(name+'-bl',p(2,22),p(6,26),radius_x=4,sweep=sweep)
 self.add_line(name+'-base',p(6,26),p(8,26))
 self.add_arc(name+'-return-base',p(8,26),p(12,23),radius_x=4,radius_y=3,sweep=sweep)
 self.add_contour(name,*[name+'-'+s for s in ('return-top','top','tl','side','bl','base','return-base')])
self.add_line('middle',(10,16),(22,16))
""")
plan(4,'CIRCLE','Outer circular sight, inner circular ring and four short attached cardinal ticks.','crosshair',"""
circle(self,'frame',16,16,14);circle(self,'inner',16,16,5)
for n,a,b in [('left',(11,16),(9,16)),('right',(21,16),(23,16)),('top',(16,11),(16,9)),('base',(16,21),(16,23))]:
 self.add_line(n,a,b);self.relate('connect',n,'inner')
""")
plan(6,'CIRCLE','Two concentric coin circles and a short central vertical currency stroke.','coins',"""
circle(self,'frame',16,16,14)
pts=[(16,9),(23,16),(16,23),(9,16),(16,9)]
for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'inner-{i}',a,b,radius_x=7)
self.add_contour('inner',*[f'inner-{i}' for i in range(4)],closed=True)
self.add_line('mark',(16,15),(16,17))
""")
plan(7,'CIRCLE','Two complete concentric circular outlines with open center.','circle',"""
circle(self,'frame',16,16,14);circle(self,'inner',16,16,7)
""")
plan(15,'SQUARE','Open chicken head outline, attached round comb, two eyes and closed diamond beak.','egg',"""
self.add_line('left',(2,30),(2,22));self.add_arc('head-top',(2,22),(30,22),radius_x=14)
self.add_line('right',(30,22),(30,30));self.add_contour('head','left','head-top','right')
circle(self,'comb',16,5,3);self.relate('connect','comb','head')
self.add_line('eye-left',(11,16),(11,16));self.add_line('eye-right',(21,16),(21,16))
self.add_polyline('beak',(16,20),(24,25),(16,30),(8,25),(16,20))
""")
plan(19,'VRECT_XL','Circular detached head above rounded shoulders, flared dress and inset lower body.','human_ref/full_body_ref.png',"""
circle(self,'head',16,6,4)
self.add_line('shoulder-top',(12,18),(20,18))
self.add_bezier('shoulder-right',(20,18),((23,18),(23,20),(24,22)))
points=((24,22),(28,26),(21,26),(20,30),(12,30),(11,26),(4,26),(8,22))
for i,(a,b) in enumerate(zip(points,points[1:])):self.add_line(f'dress-{i}',a,b)
self.add_bezier('shoulder-left',(8,22),((9,20),(9,18),(12,18)))
self.add_contour('body','shoulder-top','shoulder-right',*[f'dress-{i}' for i in range(7)],'shoulder-left',closed=True)
""")
# Framed text marks reuse the shared catalog, uniformly sized and grid fitted.
import json,xml.etree.ElementTree as ET
from pathlib import Path
from svgpathtools import parse_path
from icon_set.scripts.sub_ink32 import _snap
from icon_set.scripts.migrate_sub_profiles import primitive_calls
catalog={g['icon_id']:g for g in json.loads((Path(__file__).resolve().parents[3]/'icon_set/typeface/glyphs.json').read_text())['glyphs']}
def glyph_body(gid,height,cx,cy):
 g=catalog[gid];l,t,r,b=g['bounds'];s=height/(b-t) if b!=t else height/(r-l)
 paths=[parse_path(p).scaled(s).translated(complex(cx-(l+r)*s/2,cy-(t+b)*s/2)) for p in g['paths']]
 paths=_snap(paths,preserve_arcs=False,width=32)
 root=ET.Element('svg',xmlns='http://www.w3.org/2000/svg',viewBox='0 0 32 32')
 for p in paths:ET.SubElement(root,'path',d=p.d())
 return '\n'.join(primitive_calls(ET.tostring(root,encoding='unicode'),text=True))
plan(8,'CIRCLE','Circular frame around the shared digit-zero glyph, proportionally fitted to the interior.','circle',"circle(self,'frame',16,16,14)\n"+glyph_body('digit-0',14,16,16))
GLYPHS[8]=('digit-0',)
# Prefix names from separate glyph conversion to preserve independent primitives.
p=glyph_body('symbol-plus',2,11,11).replace("'p","'plus-p")
m=glyph_body('symbol-hyphen',2,21,21).replace("'p","'minus-p")
plan(50,'CIRCLE','Circular frame, shared upper-left plus and lower-right minus, with rising diagonal slash.','circle',"circle(self,'frame',16,16,14)\n"+p+'\n'+m+"\nself.add_line('slash',(11,21),(21,11))")
GLYPHS[50]=('symbol-plus','symbol-hyphen')
from text_designs import TEXT
for n,spec in TEXT.items():plan(n,'SQUARE','Shared typeface '+', '.join(spec['glyphs'])+' at 32px ink height and natural width.','shared typeface',spec['body'])
