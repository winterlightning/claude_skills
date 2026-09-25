from pathlib import Path
import json,re,textwrap
ROOT=Path('icon_set/work/primitive-make-ray/review-20260925T060624Z')
rows=json.loads((ROOT/'batch.json').read_text())
AUTHOR='gpt-6'
# Every emitted module records the exact SOURCE_ICON_ID and SOURCE_PATH from its row.
helpers='''
        def path(name, start, commands, closed=False):
            members=[]; here=start
            for index, command in enumerate(commands):
                ident=f'{name}-{index}'; kind,end,*args=command
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident); here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,cx,cy,r):
            path(name,(cx-r,cy),[('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)],True)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line; poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
'''
D={}
def add(i,key,plan,ref,code):D[i]=(key,plan,ref,textwrap.dedent(code))
add(0,'SQUARE','Tilted umbrella canopy and pole above an articulated reclining chair. Tilt and angled back preserve the reference.','umbrella: coherent domed canopy and attached pole', '''
path('canopy',(6,22),[('C',(36,14),(7,7),(27,1)),('L',(6,22))],True)
line('pole',(21,18),(25,34));join('pole','canopy')
poly('seat',(6,34),(34,34),(42,24));join('pole','seat')
line('front-leg',(11,34),(8,42));join('front-leg','seat')
line('back-leg',(34,34),(39,42));join('back-leg','seat')
''')
add(1,'SQUARE','A softly curved heart with three radiating beat strokes at upper left.','heart: rounded lobes and smoothly converging sides', '''
path('heart',(26,22),[('C',(42,23),(33,9),(42,13)),('C',(26,42),(42,30),(34,37)),('C',(10,23),(18,37),(10,30)),('C',(26,22),(10,13),(19,9))],True)
line('beat-left',(6,18),(9,19))
line('beat-diagonal',(10,9),(13,12))
line('beat-top',(19,6),(20,10))
''')
add(2,'SQUARE','Bell has a broad flared skirt, attached top loop and modest clapper, with paired ringing marks.','bell-ring: smooth shoulder-to-skirt transitions', '''
path('bell',(10,32),[('C',(14,18),(13,28),(14,24)),('A',(34,18),10,10,True),('C',(38,32),(34,24),(35,28)),('L',(10,32))],True)
path('loop',(20,9),[('A',(28,9),4,5,True)]);join('loop','bell')
path('clapper',(18,32),[('A',(30,32),6,10,False)]);join('clapper','bell')
for side,x in [('left',6),('right',42)]:
 line('ring-'+side,(x,21),(x,25))
''')
add(3,'VRECT_M','Open upper thigh bends into a horizontal knee and a tapering shin and foot. Smooth anatomical contours replace the angular boot. Human full_body_ref consulted for simple limb flow; no head present.','human_ref/full_body_ref.png: rounded continuous limb construction; no exact Lucide match', '''
path('leg',(24,4),[('L',(24,18)),('C',(22,21),(24,20),(24,21)),('L',(17,22)),('C',(15,28),(14,23),(14,25)),('L',(17,37)),('C',(14,40),(17,39),(15,39)),('C',(10,44),(11,41),(10,41)),('L',(22,44)),('A',(25,41),3,3,False),('L',(25,30)),('L',(31,30)),('C',(38,22),(36,30),(38,27)),('L',(38,4))])
''')
add(4,'SQUARE','An arch rises from a large square anchor through a small top square to a circular end; horizontal handle reaches a left circle.','spline: continuous curve with endpoint nodes', '''
rounded('anchor',6,28,22,42,3)
poly('node',(22,6),(30,6),(30,14),(22,14),(22,6))
circle('handle',9,10,3)
line('handle-bar',(12,10),(22,10));join('handle-bar','handle');join('handle-bar','node')
path('left-curve',(12,28),[('C',(22,10),(12,18),(15,10))]);join('left-curve','anchor');join('left-curve','node');join('left-curve','handle-bar')
path('right-curve',(30,10),[('C',(39,36),(39,10),(39,23))]);join('right-curve','node')
circle('end',39,39,3);join('right-curve','end')
''')
add(5,'SQUARE','Three birds over a stepped telescope and tripod; angled optical barrel and shared tripod joint retain the scene.','telescope: stepped barrel and shared tripod joint', '''
for n,x,y in [('left',8,8),('middle',22,6),('right',36,9)]:
 poly('bird-'+n,(x-2,y),(x,y+2),(x+2,y))
poly('objective',(26,20),(38,16),(42,29),(30,33),(26,20))
poly('barrel',(26,23),(16,26),(19,35),(30,31));join('objective','barrel')
poly('eyepiece',(16,28),(6,31),(8,37),(19,33));join('eyepiece','barrel')
poly('tripod',(16,42),(25,34),(34,42));join('tripod','barrel');join('tripod','objective')
line('center-leg',(25,34),(25,42));join('center-leg','tripod')
''')
add(6,'SQUARE','A broad blank rounded board sits on outward leaning easel legs with a crossbar.','presentation: sparse screen outline with supporting stand', '''
rounded('board',6,6,42,30,3)
for side,a,b,c in [('left',17,14,12),('right',31,34,36)]:
 poly('leg-'+side,(a,30),(b,38),(c,42));join('board','leg-'+side)
line('crossbar',(14,38),(34,38));join('crossbar','leg-left');join('crossbar','leg-right')
''')
add(7,'VRECT_L','Closed book with a clean front cover and curved lower page block; no invented vertical spine stripe.','book: rounded bound edge and lower page block', '''
path('cover',(8,38),[('L',(8,10)),('A',(14,4),6,6,True),('L',(40,4)),('L',(40,32)),('L',(14,32)),('A',(8,38),6,6,False)])
path('pages',(8,38),[('A',(14,44),6,6,False),('L',(40,44)),('C',(40,32),(38,40),(38,36))]);join('cover','pages')
''')
add(8,'HRECT_L','Two mirrored open pages with a central fold and short text lines; shared centre keeps page angles equal.','book-open: matched page contours around one gutter', '''
poly('outline',(4,8),(24,14),(44,8),(44,34),(24,40),(4,34),closed=True)
line('gutter',(24,14),(24,40));join('gutter','outline')
for n,x,s in [('left',13,1),('right',35,-1)]:
 line('text-'+n,(x,23),(x+s*3,24))
''')
add(9,'CIRCLE','Round bowling ball with two generously separated circular finger holes on an upper-right diagonal.','no useful Lucide subject match; concentric circular primitives', '''
circle('ball',24,24,20)
circle('upper-hole',27,15,3)
circle('lower-hole',33,27,3)
''')
add(10,'SQUARE','Flat rounded parcel with an attached rectangular tape tab, preserving the unbroken top edge.','package: attached seam construction; front-view reference retained', '''
rounded('box',6,6,42,42,4)
poly('tape',(18,6),(18,18),(30,18),(30,6));join('tape','box')
''')
for i in [11,13]:
 add(i,'SQUARE','Flat square parcel with rounded corners and one short vertical seam from the top edge.','package: meaningful seams; no invented perspective', '''
rounded('box',6,6,42,42,4)
line('seam',(24,6),(24,18));join('seam','box')
''')
add(12,'SQUARE','Square parcel with a centered hanging ribbon and a symmetrical V-cut end.','package: preserve structural seams', '''
poly('box',(6,6),(42,6),(42,42),(6,42),closed=True)
poly('ribbon',(16,6),(16,23),(24,18),(32,23),(32,6));join('ribbon','box')
''')
add(14,'SQUARE','Front-view box with trapezoidal top, a centered lid seam and an uncluttered front face.','package: junctions share explicit seam nodes', '''
poly('box',(6,16),(13,6),(35,6),(42,16),(42,42),(6,42),closed=True)
line('lid',(6,16),(42,16));join('lid','box')
line('top-seam',(24,6),(24,16));join('top-seam','box');join('top-seam','lid')
''')
add(15,'HRECT_L','Side-view brain with asymmetric smooth lobes and two curved sulci, preserving the wider anatomical shape.','brain: coherent lobes with attached fold strokes', '''
path('brain',(10,20),[('C',(16,8),(10,12),(12,8)),('C',(24,10),(19,8),(22,8)),('C',(36,15),(30,5),(36,9)),('C',(44,24),(41,15),(44,19)),('C',(41,31),(44,28),(42,29)),('C',(33,40),(41,37),(37,40)),('C',(26,36),(30,40),(28,39)),('C',(17,36),(22,40),(19,39)),('C',(4,29),(8,41),(4,36)),('C',(10,20),(4,24),(6,21))],True)
path('upper-fold',(24,10),[('C',(20,22),(21,14),(20,17))]);join('upper-fold','brain')
path('lower-fold',(26,36),[('C',(30,24),(24,31),(26,26))]);join('lower-fold','brain')
''')
add(16,'CIRCLE','Circular brake rotor with a curved upper-left caliper and an open central hub, rather than a filled dot.','no useful Lucide match; concentric rotor and caliper construction', '''
path('rotor',(24,4),[('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(4,24),20,20,True)])
path('caliper',(4,24),[('A',(24,4),20,20,True),('L',(24,12)),('A',(12,24),12,12,False),('L',(4,24))],True);join('caliper','rotor')
circle('hub',24,26,4)
''')
add(17,'SQUARE','Moose side silhouette with long muzzle, joined antlers and two broad legs; curved antler tines retain its distinctive profile.','no useful Lucide match; coherent animal contour and shared antler beam', '''
path('body',(6,42),[('L',(6,29)),('A',(14,21),8,8,True),('L',(27,21)),('C',(35,15),(29,17),(32,15)),('C',(42,24),(40,15),(42,20)),('C',(36,26),(42,28),(39,28)),('L',(33,42)),('L',(25,42)),('L',(25,33)),('A',(22,30),3,3,False),('L',(16,30)),('A',(13,33),3,3,False),('L',(13,42)),('L',(6,42))],True)
path('antler',(6,6),[('L',(6,10)),('A',(10,14),4,4,False),('L',(27,14)),('L',(32,17))]);join('antler','body')
for n,x in [('one',15),('two',24)]:
 line('tine-'+n,(x,6),(x,14));join('tine-'+n,'antler')
''')
add(18,'SQUARE','Sweeping broom with long tapered bristles and a separate two-lobed dust puff; remove the mistaken ring.','brush: flowing silhouette and integrated handle', '''
path('broom',(38,6),[('C',(42,10),(41,5),(43,7)),('C',(28,39),(38,18),(34,31)),('C',(21,42),(26,42),(23,43)),('L',(23,36)),('C',(13,38),(20,40),(16,39)),('L',(15,34)),('C',(8,31),(12,35),(9,33)),('C',(34,9),(21,27),(28,20)),('C',(38,6),(36,7),(36,6))],True)
path('dust',(6,20),[('C',(6,10),(1,17),(2,10)),('C',(14,15),(10,8),(14,10)),('C',(16,24),(20,15),(21,23)),('C',(6,20),(11,27),(7,24))],True)
''')
add(19,'SQUARE','A speech balloon has two separated jagged fracture edges and a bottom-left tail; enclosing halves remain recognizably one bubble.','no useful Lucide match; rounded enclosure corners with deliberate fractured edges', '''
path('left',(19,6),[('L',(10,6)),('A',(6,10),4,4,False),('L',(6,34)),('A',(10,38),4,4,False),('L',(14,38)),('L',(14,42)),('L',(22,36))])
poly('crack-left',(19,6),(24,14),(19,18),(26,28))
join('left','crack-left')
path('right',(31,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,34)),('A',(38,38),4,4,True),('L',(30,38))])
poly('crack-right',(31,6),(34,16),(31,21),(34,28));join('right','crack-right')
''')
for i,r in enumerate(rows):
 key,plan,ref,code=D[i];source=re.search(r'([0-9a-f-]{36})\.svg$',r['ref']).group(1);concept=Path(r['ref']).stem[:-37]
 run=Path('icon_set/work/primitive-make-ray')/source/'20260925T0610-thuan-mac-revision';run.mkdir(parents=True,exist_ok=False)
 meta={'concept':concept,'source_uuid':source,'reference_path':r['ref']};(run/(r['id']+'.metadata.json')).write_text(json.dumps(meta,indent=2))
 module=run/(concept.replace(' ','_').replace('-','_')+'_'+source.replace('-','_')+'.py')
 content=f'"""{plan}"""\nfrom icon_set.model.keyshapes import Keyshape\nfrom icon_set.model.icons.solo._base import Solo48\nSOURCE_ICON_ID = {source!r}\nSOURCE_PATH = {r["ref"]!r}\nAUTHOR = {AUTHOR!r}\n\nclass Revision(Solo48):\n    icon_id = {r["id"]!r}\n    keyshape = Keyshape.{key}\n    semantic_role = "MAIN"\n    semantic_kind = "noun"\n    category = "objects"\n    aliases = ()\n    keywords = ({concept!r},)\n\n    def build(self):\n        # Plan: {plan}\n        # Construction reference: {ref}\n'+helpers+'\n'+textwrap.indent(code.strip(),'        ')+'\n'
 module.write_text(content);r.update(run=str(run),module=str(module),plan=plan,lucide=ref,keyshape=key,source_uuid=source)
(ROOT/'batch.json').write_text(json.dumps(rows,indent=2))
