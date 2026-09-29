from pathlib import Path
import json, textwrap, sys, io, hashlib
import cairosvg
from PIL import Image, ImageDraw
from icon_set.scripts.primitive_fix import load_icon, render_previews
from icon_set.scripts import build_gate
ROOT=Path('icon_set/work/primitive-fix-thuan/batch-20260929T033507Z')
AUTHOR='gpt-6'
rows=json.loads((ROOT/('runs.json' if (ROOT/'runs.json').exists() else 'inputs.json')).read_text())
# Each design is newly authored from the inspected reference and rejected drawing.
notes=[
('The rejected head is crossed by two generic parallel slashes; the reference has a forehead wrap with a folded end.', 'Move the bandage to the upper head and restore its folded return, leaving the lower face open.'),
('The rejected pain wisps are thick detached blobs and the head is squat.', 'Restore a tall left-facing head, continuous nose/chin/neck, and two slender coherent wavy pain strokes.'),
('The rejected headphones replace the face with a small smile-shaped opening and turn the cigarette into a hooked tick.', 'Restore the circular face, separate overhead band, two earcups and a straight diagonal cigarette.'),
('The rejected face rim is broken and its mouth is tiny.', 'Restore a complete round face with two recognizable heart eyes and a broad smile.'),
('The rejected lamp looks like a horizontal pan with a ring on a pole.', 'Restore a pointed flame above a deep bowl, round side handle and flared pedestal.'),
('The rejected parent overlaps the arch and the nodes are cramped.', 'Separate the parent square above a broad rounded branch with three equally sized child squares.'),
('The rejected drawing removes all three rectangular list nodes.', 'Restore three outlined rectangular nodes connected to a right-hand bracket.'),
('The rejected headphones have no earcups and the player is a plain rounded block.', 'Restore two earcups, an overhead arch and a player with screen division and circular control.'),
('The rejected cluster has three hexagons without separate central holes.', 'Restore three larger hexagonal nuts with clear circular bores in the same staggered arrangement.'),
('The rejected bag loses its taper and the hanging triangle merges into its flat top.', 'Restore a suspended tapered bag with rounded bottom and a distinct triangular hanger.'),
('The rejected walker is upright, the pack is an unrelated square, and its head is bisected.', 'Restore a leaning walking pose, slanted backpack, circular head and headlamp with two forward rays.'),
('The rejected backpack has an angular cross silhouette and an oversized buckle.', 'Restore the rounded tall body, overhanging top flap, central fastening tab and side pockets.'),
('The rejected hippo resembles a robot and places its only dots in the muzzle.', 'Restore round ears, domed head, wide rounded muzzle, separate eyes and nostrils.'),
('The rejected leaves are smooth generic ovals and berries are detached dots.', 'Restore pointed toothed holly leaves and a joined cluster of three outlined berries.'),
('The rejected house is joined to the projector by a funnel and the play symbol is a blob.', 'Float a house with a clear triangular play sign above a lens and rounded projector base, with outward projection rays.'),
('The rejected projector loses its base and the cube crowds its internal edges.', 'Restore the cube above a round lens on a low rounded base, with separate projection rays.'),
('The rejected dipper becomes a rectangular tool and its handle bends sideways.', 'Restore three rounded diagonal dipper ridges, a straight rising handle and a pointed falling drop.'),
('The rejected chain links are tall parentheses with a short floating dash.', 'Restore two horizontally arranged open circular links and a longer joining bar through their mouths.'),
('The rejected blind omits the round pull end and has an oversized header and heavy side posts.', 'Restore a shallow header, three evenly spaced horizontal slats, light guide structure and left cord with circular pull.'),
('The rejected blind omits the round pull end and has an oversized header and heavy side posts.', 'Restore a shallow header, three evenly spaced horizontal slats, light guide structure and right cord with circular pull.'),
]
helpers='''
    def circle(self, n, x, y, r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def rect(self,n,x,y,w,h,r=0):
        if not r:
            self.add_polyline(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            return
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        for j in range(8):
            a,b=pts[j],pts[(j+1)%8]
            if j%2:self.add_arc(n+str(j),a,b,radius_x=r)
            else:self.add_line(n+str(j),a,b)
        self.add_contour(n,*(n+str(j) for j in range(8)),closed=True)
    def curve(self,n,start,*segments):
        self.add_bezier(n,start,*segments)
'''
designs=[]
def add(keyshape, code, refs='No useful exact Lucide match; constructed from the original reference with smooth geometric contours.'):
 designs.append((keyshape,textwrap.dedent(code).strip(),refs))
add('CIRCLE','''
self.circle('head',24,24,20)
self.add_line('wrap-upper',(6,16),(33,6))
self.add_polyline('wrap-lower',(4,25),(23,18),(23,21),(44,21))
''')
add('VRECT_L','''
self.curve('head',(17,13),((9,16),(9,22),(6,28)))
self.add_polyline('face',(6,28),(12,28),(12,33))
self.curve('chin',(12,33),((12,37),(16,37),(20,37)))
self.add_line('front-neck',(20,37),(20,44))
self.curve('back',(36,44),((36,39),(35,37),(38,34)),((44,29),(43,20),(37,15)))
for x in (22,30):
 self.curve('pain-'+str(x),(x,4),((x-4,7),(x+4,9),(x,12)))
''')
add('CIRCLE','''
self.curve('headband',(5,23),((5,-2),(43,-2),(43,23)))
self.curve('face',(12,18),((15,10),(33,10),(36,18)),((40,25),(38,32),(33,37)),((29,42),(19,42),(15,38)),((8,33),(8,24),(12,18)))
self.rect('ear-left',4,20,7,12,3)
self.rect('ear-right',37,20,7,12,3)
self.curve('smile',(19,31),((22,34),(27,34),(30,31)))
self.add_polyline('cigarette',(32,32),(42,41),(39,44),(29,35),closed=True)
''','Lucide headphones: continuous overhead arch and rounded earcups; user.svg: circular head vocabulary.')
add('CIRCLE','''
self.circle('face',24,24,20)
for n,x in [('left',15),('right',33)]:
 self.curve(n+'-heart',(x,16),((x-4,11),(x-9,17),(x-4,21)),((x-2,23),(x,25),(x,25)),((x,25),(x+2,23),(x+4,21)),((x+9,17),(x+4,11),(x,16)))
self.curve('smile',(14,31),((17,40),(31,40),(34,31)))
''','Lucide heart: paired rounded lobes and tapered point; complete circular face from source.')
add('VRECT_L','''
self.curve('flame',(24,4),((24,10),(30,11),(30,17)),((30,24),(18,24),(18,17)),((18,12),(23,10),(24,4)))
self.add_line('wick',(24,23),(24,27))
self.curve('bowl',(6,27),((10,43),(30,43),(34,27)))
self.add_line('rim',(6,27),(34,27))
self.curve('handle',(34,25),((38,17),(46,23),(43,29)),((41,33),(36,33),(33,32)))
self.add_polyline('foot',(20,39),(15,44),(31,44),(26,39))
''','Lucide flame: pointed tip and rounded teardrop body; source owns bowl, handle and pedestal.')
add('SQUARE','''
self.rect('parent',19,4,10,10)
for x in (4,19,34):self.rect('child-'+str(x),x,34,10,10)
self.add_line('trunk',(24,14),(24,34))
self.curve('branch',(9,34),((9,24),(15,23),(24,23)),((33,23),(39,24),(39,34)))
''')
add('SQUARE','''
for y in (6,20,34):
 self.rect('node-'+str(y),6,y,23,8)
 self.add_line('link-'+str(y),(29,y+4),(42,y+4))
self.add_polyline('bracket',(42,4),(42,38))
''')
add('SQUARE','''
self.curve('band',(5,27),((5,-3),(43,-3),(43,27)))
self.rect('left-cup',4,24,6,10,3)
self.rect('right-cup',38,24,6,10,3)
self.rect('player',15,17,18,27,4)
self.add_line('screen-rule',(15,25),(33,25))
self.circle('control',24,34,3)
''','Lucide headphones: arch tangent to earcups and matching earcup radii.')
add('SQUARE','''
for n,x,y in [('upper',14,13),('lower',14,35),('right',36,24)]:
 self.add_polyline(n,(x-5,y-8),(x+5,y-8),(x+10,y),(x+5,y+8),(x-5,y+8),(x-10,y),closed=True)
 self.circle(n+'-bore',x,y,3)
''')
add('VRECT_M','''
self.add_polyline('hanger',(24,4),(18,14),(30,14),closed=True)
self.add_polyline('straps',(21,14),(18,20),(30,20),(27,14))
self.curve('bag',(18,20),((15,24),(14,27),(14,32)),((14,40),(17,44),(24,44)),((31,44),(34,40),(34,32)),((34,27),(33,24),(30,20)))
''')
add('VRECT_L','''
# Shared human full-body construction. r=4 head; neck (22,22) gives 5-12-13 distance from center (27,10), hence exact 4px ink gap.
self.circle('head',27,10,5)
self.add_line('headband',(22,9),(32,9))
self.add_line('lamp-ray-upper',(37,7),(43,4))
self.add_line('lamp-ray-lower',(37,13),(43,16))
self.add_line('torso',(22,22),(17,32))
self.add_polyline('arm',(22,22),(27,29),(34,31))
self.add_polyline('front-leg',(17,32),(25,36),(25,44))
self.add_polyline('rear-leg',(17,32),(14,39),(8,44))
self.add_polyline('backpack',(16,18),(12,16),(7,26),(13,30))
self.mark_human_figure('hiker',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: round head, single torso and bent limbs; intentional lean preserves hiking motion.')
add('VRECT_L','''
self.rect('body',12,6,24,38,6)
self.rect('top-flap',10,4,28,14,4)
self.rect('tab',20,14,8,11,3)
self.curve('left-pocket',(12,28),((3,27),(4,29),(4,34)),((4,39),(5,40),(12,40)))
self.curve('right-pocket',(36,28),((45,27),(44,29),(44,34)),((44,39),(43,40),(36,40)))
self.add_line('pocket-seam',(19,34),(29,34))
''')
add('VRECT_L','''
self.circle('ear-left',10,9,5)
self.circle('ear-right',38,9,5)
self.curve('head',(10,28),((4,5),(44,5),(38,28)))
self.curve('muzzle',(24,25),((15,24),(5,26),(5,34)),((5,46),(19,44),(24,42)),((29,44),(43,46),(43,34)),((43,26),(33,24),(24,25)))
for x in (17,31):
 self.add_dot('eye-'+str(x),(x,20))
 self.add_dot('nostril-'+str(x),(x,33))
''')
add('SQUARE','''
# Two pointed serrated leaves, mirrored only in their shared overall structure.
self.add_polyline('leaf-left',(20,29),(11,27),(10,22),(5,18),(5,6),(16,7),(20,12),(23,13),(24,24))
self.add_polyline('leaf-right',(28,29),(37,27),(38,22),(43,18),(43,6),(32,7),(28,12),(25,13),(24,24))
self.add_line('vein-left',(11,13),(19,23))
self.add_line('vein-right',(37,13),(29,23))
self.circle('berry-top',24,30,5)
self.circle('berry-left',18,39,5)
self.circle('berry-right',30,39,5)
''')
add('VRECT_L','''
self.add_polyline('roof',(8,14),(24,4),(40,14))
self.add_polyline('house',(11,12),(11,27),(37,27),(37,12))
self.add_polyline('play',(21,13),(29,18),(21,23),closed=True)
self.add_line('ray-left',(5,28),(12,34))
self.add_line('ray-right',(43,28),(36,34))
self.circle('lens',24,36,5)
self.rect('base',10,40,28,5,2)
''')
add('VRECT_L','''
self.add_polyline('cube',(24,4),(37,11),(37,24),(24,31),(11,24),(11,11),closed=True)
self.add_polyline('cube-top',(11,11),(24,18),(37,11))
self.add_line('cube-front',(24,18),(24,31))
self.add_line('ray-left',(4,28),(11,35))
self.add_line('ray-right',(44,28),(37,35))
self.circle('lens',24,38,5)
self.rect('base',10,42,28,4,2)
''')
add('SQUARE','''
# One diagonal shaft and three rounded ribs normal to it.
self.add_polyline('shaft',(24,23),(41,6),(44,9),(27,26))
for n,dx,dy in [('top',0,0),('middle',-4,4),('bottom',-8,8)]:
 self.curve(n,(18+dx,20+dy),((14+dx,16+dy),(10+dx,20+dy),(14+dx,24+dy)),((14+dx,24+dy),(21+dx,31+dy),(21+dx,31+dy)),((25+dx,35+dy),(29+dx,31+dy),(25+dx,27+dy)),((25+dx,27+dy),(18+dx,20+dy),(18+dx,20+dy)))
self.curve('drop',(9,36),((7,39),(5,40),(5,42)),((5,47),(13,47),(13,42)),((13,40),(11,39),(9,36)))
''')
add('HRECT_M','''
self.curve('left-link',(19,17),((6,4),(-3,23),(7,32)),((11,36),(16,35),(19,31)))
self.curve('right-link',(29,17),((42,4),(51,23),(41,32)),((37,36),(32,35),(29,31)))
self.add_line('connection',(15,24),(33,24))
''')
for left in (True,False):
 add('SQUARE',f'''
self.rect('header',6,5,36,7,1)
for y in (20,28,36):self.add_line('slat-'+str(y),(7,y),(41,y))
self.add_line('guide',(37 if {left!r} else 11,12),(37 if {left!r} else 11,36))
self.add_line('cord',(10 if {left!r} else 38,12),(10 if {left!r} else 38,40))
self.circle('pull',10 if {left!r} else 38,43,3)
''')

# Visual review corrections, kept as a new standalone run for each input.
def revise(i, code):
 old=designs[i-1]
 designs[i-1]=(old[0],textwrap.dedent(code).strip(),old[2])
revise(2,"""
self.curve('head',(17,17),((10,20),(9,24),(6,29)))
self.add_polyline('face',(6,29),(12,29),(12,34))
self.curve('chin',(12,34),((12,37),(16,37),(20,37)))
self.add_line('front-neck',(20,37),(20,44))
self.curve('back',(36,44),((36,39),(35,37),(38,34)),((44,29),(43,21),(37,17)))
for x in (22,30):
 self.curve('pain-'+str(x),(x,3),((x-4,7),(x+4,10),(x,14)))
""")
revise(3,"""
self.curve('headband',(5,24),((5,-2),(43,-2),(43,24)))
self.circle('face',24,26,14)
self.rect('ear-left',4,21,6,12,3)
self.rect('ear-right',38,21,6,12,3)
self.curve('smile',(19,31),((22,34),(27,34),(30,31)))
self.add_line('cigarette',(30,33),(41,43))
""")
revise(4,"""
self.circle('face',24,24,20)
for n,x in [('left',16),('right',32)]:
 self.curve(n+'-heart',(x,17),((x-3,12),(x-8,17),(x-4,21)),((x-2,23),(x,25),(x,25)),((x,25),(x+2,23),(x+4,21)),((x+8,17),(x+3,12),(x,17)))
self.curve('smile',(14,32),((18,40),(30,40),(34,32)))
""")
revise(9,"""
for n,x,y in [('upper',14,12),('lower',14,36),('right',35,24)]:
 self.add_polyline(n,(x-5,y-8),(x+5,y-8),(x+9,y),(x+5,y+8),(x-5,y+8),(x-9,y),closed=True)
 self.circle(n+'-bore',x,y,3)
""")
revise(10,"""
self.add_polyline('hanger',(24,4),(18,14),(30,14),closed=True)
self.add_polyline('straps',(21,14),(18,20),(30,20),(27,14))
self.curve('shoulder-left',(18,20),((15,24),(14,25),(14,28)))
self.add_line('left-side',(14,28),(14,34))
self.add_arc('bottom',(14,34),(34,34),radius_x=10,sweep=False)
self.add_line('right-side',(34,34),(34,28))
self.curve('shoulder-right',(34,28),((34,25),(33,24),(30,20)))
self.add_contour('bag','shoulder-left','left-side','bottom','right-side','shoulder-right')
""")
revise(11,designs[10][1].replace("self.add_line('headband',(22,9),(32,9))", "self.add_line('lamp',(31,8),(33,8))"))
revise(12,"""
self.curve('body',(12,18),((12,18),(12,35),(12,38)),((12,42),(14,44),(18,44)),((18,44),(30,44),(30,44)),((34,44),(36,42),(36,38)),((36,35),(36,18),(36,18)))
self.curve('top-flap',(20,18),((20,18),(14,18),(14,18)),((11,18),(10,17),(10,14)),((10,14),(10,8),(10,8)),((10,5),(11,4),(14,4)),((14,4),(34,4),(34,4)),((37,4),(38,5),(38,8)),((38,8),(38,14),(38,14)),((38,17),(37,18),(34,18)),((34,18),(28,18),(28,18)))
self.rect('tab',20,14,8,11,3)
self.curve('left-pocket',(12,28),((3,27),(4,29),(4,34)),((4,39),(5,40),(12,40)))
self.curve('right-pocket',(36,28),((45,27),(44,29),(44,34)),((44,39),(43,40),(36,40)))
self.add_line('pocket-seam',(19,34),(29,34))
""")
revise(14,"""
self.add_polyline('leaf-left',(20,27),(11,25),(10,20),(5,17),(5,5),(15,6),(18,10),(21,12),(20,23))
self.add_polyline('leaf-right',(28,27),(37,25),(38,20),(43,17),(43,5),(33,6),(30,10),(27,12),(28,23))
self.add_line('vein-left',(11,12),(17,20))
self.add_line('vein-right',(37,12),(31,20))
self.circle('berry-top',24,29,5)
self.circle('berry-left',18,39,5)
self.circle('berry-right',30,39,5)
""")
revise(15,"""
self.add_polyline('roof',(8,13),(24,3),(40,13))
self.add_polyline('house',(11,11),(11,25),(37,25),(37,11))
self.add_polyline('play',(21,11),(29,16),(21,21),closed=True)
self.add_line('ray-left',(4,29),(10,34))
self.add_line('ray-right',(44,29),(38,34))
self.circle('lens',24,35,4)
self.rect('base',10,40,28,6,3)
""")
revise(16,"""
self.add_polyline('cube',(24,3),(37,10),(37,23),(24,30),(11,23),(11,10),closed=True)
self.add_polyline('cube-top',(11,10),(24,17),(37,10))
self.add_line('cube-front',(24,17),(24,30))
self.add_line('ray-left',(4,29),(10,34))
self.add_line('ray-right',(44,29),(38,34))
self.circle('lens',24,37,3)
self.rect('base',10,42,28,4,2)
""")
revise(17,"""
self.add_line('shaft',(23,24),(42,5))
for n,a,b in [('top',(17,18),(30,31)),('middle',(12,23),(25,36)),('bottom',(7,28),(20,41))]:
 self.add_line(n,a,b)
self.curve('drip',(6,38),((5,40),(3,42),(3,43)),((3,47),(9,47),(9,43)),((9,42),(7,40),(6,38)))
""")
revise(18,"""
self.add_arc('left-link',(20,16),(20,32),radius_x=10,large_arc=True,sweep=False)
self.add_arc('right-link',(28,16),(28,32),radius_x=10,large_arc=True,sweep=True)
self.add_line('connection',(15,24),(33,24))
""")

revise(1,designs[0][1].replace("(33,6)","(32,6)").replace("(4,25)","(4,24)").replace("(44,21)","(43,21)"))
revise(16,designs[15][1].replace("self.circle('lens',24,37,3)","self.circle('lens',24,36,4)").replace("self.rect('base',10,42,28,4,2)","self.rect('base',10,40,28,6,3)"))
revise(17,designs[16][1].replace("(23,24),(42,5)","(13,34),(42,5)"))

revise(16,"""
self.add_polyline('cube',(24,3),(35,9),(35,19),(24,25),(13,19),(13,9),closed=True)
self.add_polyline('cube-top',(13,9),(24,15),(35,9))
self.add_line('cube-front',(24,15),(24,25))
self.add_line('ray-left',(4,29),(10,34))
self.add_line('ray-right',(44,29),(38,34))
self.circle('lens',24,35,4)
self.rect('base',10,40,28,6,3)
""")

if __name__=='__main__':
 selected=list(map(int,sys.argv[1:])) or list(range(1,21))
 for index in selected:
  row=rows[index-1]; keyshape,code,refs=designs[index-1]
  reference=Path(row['reference']); SOURCE_ICON_ID=reference.stem[-36:]; SOURCE_PATH=str(reference)
  concept=reference.stem[:-37]
  from datetime import datetime,timezone
  stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
  run=Path('icon_set/work/primitive-make-ray')/SOURCE_ICON_ID/(stamp+'-meaning-fix')
  run.mkdir(parents=True)
  meta={'concept':concept,'source_uuid':SOURCE_ICON_ID,'reference_path':SOURCE_PATH}
  (run/(row['id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
  (run/'review-before.md').write_text(f"Subject: {concept}.\n\nOriginal/current comparison: {notes[index-1][0]}\n\nFeedback: {row['feedback']}\n\nRevision: {notes[index-1][1]}\n\nConstruction references: {refs}\n")
  filename=row['id'].replace('-','_')+'_'+SOURCE_ICON_ID.replace('-','_')+'.py'
  module=run/filename
  source=f'''from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = {SOURCE_ICON_ID!r}
SOURCE_PATH = {SOURCE_PATH!r}
AUTHOR = {AUTHOR!r}
# Symbol plan: {notes[index-1][1]}
# Construction references: {refs}
class Drawing(Solo48):
    icon_id = {row['id']!r}
    keyshape = Keyshape.{keyshape}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ({concept!r},)
{helpers}
    def build(self):
{textwrap.indent(code,'        ')}
'''
  module.write_text(source)
  icon=load_icon(module);report=icon.validate_icon();svg=icon.to_svg()
  (run/(row['id']+'.svg')).write_text(svg)
  (run/'validation.txt').write_text(report.describe())
  render_previews(svg,row['id'],48,run)
  for label,p in [('reference',reference),('before',Path(row['before']))]:
   cairosvg.svg2png(url=str(p),write_to=str(run/(label+'.png')),output_width=192,output_height=192)
  row.update({'run':str(run),'module':str(module),'svg':str(run/(row['id']+'.svg')),'comparison':notes[index-1][0],'change':notes[index-1][1],'references':refs})
  print(index,row['id'],report.status,len(report.errors),len(report.warnings),flush=True)
 (ROOT/'runs.json').write_text(json.dumps(rows,indent=2))
