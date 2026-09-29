from pathlib import Path
import json
root=Path(__file__).parent
rows=json.loads((root/'batch.json').read_text())
AUTHOR='gpt-6'
SOURCE_ICON_ID=[m['source_uuid'] for m in rows]
SOURCE_PATH=[m['reference_path'] for m in rows]
drawings={
1:('SQUARE','wifi; router','Feedback names Wi-Fi. The rejected router has only two tall semicircles and a filled-looking chassis. Restore three broad, shallow signal waves, antenna and a rounded open chassis.', '''
        for n,a,z,c1,c2 in [('outer-left',(8,9),(24,3),(13,5),(18,3)),('outer-right',(24,3),(40,9),(30,3),(35,5)),('middle-left',(14,16),(24,11),(17,13),(20,11)),('middle-right',(24,11),(34,16),(28,11),(31,13)),('inner',(20,23),(28,23),(22,20),(26,20))]:
            self.add_bezier(n,a,(c1,c2,z))
        self.add_contour('outer','outer-left','outer-right')
        self.add_contour('middle','middle-left','middle-right')
        path('case',(8,32),[('L',(24,32)),('L',(40,32)),('A',(44,36),4,True),('L',(44,38)),('A',(40,42),4,True),('L',(36,42)),('L',(12,42)),('L',(8,42)),('A',(4,38),4,True),('L',(4,36)),('A',(8,32),4,True)],True)
        line('antenna',(24,28),(24,32));join('antenna','case')
        for n,a,b in [('left-foot',(12,42),(10,44)),('right-foot',(36,42),(38,44))]:line(n,a,b);join(n,'case')
'''),
2:('HRECT_M','headset','The rejected headset is a tall rounded rectangle with a sharp nose notch. Restore the broad, low goggle silhouette, gently domed top and smooth paired eye lobes.', '''
        path('goggles',(4,23),[('C',(12,14),(4,17),(6,14)),('C',(36,14),(19,13),(29,13)),('C',(44,23),(42,14),(44,17)),('C',(36,34),(44,30),(41,34)),('C',(24,28),(30,34),(29,28)),('C',(12,34),(19,28),(18,34)),('C',(4,23),(7,34),(4,30))],True)
'''),
3:('SQUARE','smartphone','Feedback names the phone. The rejected phone is much too narrow compared with the reference. Widen the portrait device, retain equal corner radii, and balance the two vibration strokes.', '''
        box('phone',10,4,38,44,3)
        for n,x in [('left',4),('right',44)]:line(n+'-vibration',(x,12),(x,36))
'''),
4:('SQUARE','monitor; human_ref/user.svg','Feedback names the monitor. The rejected screen is almost square and its figure is a dot above a narrow arch. Rebuild a broader screen and outlined circular head over smooth broad shoulders, with a centered stand.', '''
        path('screen',(8,4),[('L',(40,4)),('A',(44,8),4,True),('L',(44,32)),('A',(40,36),4,True),('L',(24,36)),('L',(8,36)),('A',(4,32),4,True),('L',(4,8)),('A',(8,4),4,True)],True)
        line('stand',(24,36),(24,44));join('stand','screen')
        poly('base',(16,44),(24,44),(32,44));join('base','stand')
        circle('head',24,14,3)
        path('shoulders',(16,29),[('E',(24,25),8,4,True),('E',(32,29),8,4,True)])
        # Shared human user.svg: circular head; broad shoulders. 25-(14+3)=8 centerline =4 ink gap.
'''),
5:('VRECT_L','sprout','The rejected flytrap reads as a chunky crown on a zigzag stalk. Restore its rounded trap bowl, three clearly separated teeth, gently curved stem and a distinct pointed leaf.', '''
        path('trap',(20,4),[('C',(8,15),(13,5),(8,9)),('C',(14,25),(8,19),(10,22)),('C',(30,29),(20,31),(25,32)),('C',(39,17),(35,27),(38,22)),('L',(30,21)),('L',(33,12)),('L',(24,17)),('L',(27,8)),('L',(18,12)),('L',(20,4))],True)
        path('stem',(14,25),[('C',(14,34),(10,28),(11,30)),('C',(20,40),(17,38),(19,38)),('L',(20,44))]);join('stem','trap')
        path('leaf',(20,40),[('C',(38,34),(24,30),(31,31)),('C',(20,40),(34,44),(26,44))],True);join('leaf','stem')
'''),
6:('SQUARE','sandwich','Feedback names the burger. The rejected burger has a narrow stacked-bead silhouette and obscures the drink. Restore a wide domed bun, a visible filling band and a lower bun beside the tapered cup and long straw.', '''
        path('cup',(23,20),[('L',(24,14)),('L',(16,14)),('L',(4,14)),('L',(7,41)),('C',(10,44),(7,43),(8,44)),('L',(16,44))])
        poly('straw',(13,29),(16,14),(18,4),(26,4));join('straw','cup')
        path('burger',(22,31),[('A',(28,25),6,True),('L',(38,25)),('A',(44,31),6,True),('L',(44,37)),('A',(38,43),6,True),('L',(28,43)),('A',(22,37),6,True),('L',(22,31))],True)
        for n,y in [('bun-edge',31),('filling-edge',37)]:line(n,(22,y),(44,y));join(n,'burger')
'''),
7:('SQUARE','camera','Feedback names the strap. The rejected semicircular strap makes the camera resemble a handbag. Restore the long triangular carry strap, raised viewfinder housing, offset lens and shutter mark.', '''
        path('body',(8,21),[('L',(9,21)),('L',(14,21)),('L',(18,17)),('L',(28,17)),('L',(32,21)),('L',(39,21)),('L',(40,21)),('A',(44,25),4,True),('L',(44,40)),('A',(40,44),4,True),('L',(8,44)),('A',(4,40),4,True),('L',(4,25)),('A',(8,21),4,True)],True)
        poly('strap',(9,21),(24,4),(39,21));join('strap','body')
        circle('lens',28,32,6);self.add_dot('shutter',(11,29))
'''),
8:('HRECT_M','toggle-left','The rejected capsule is tall and nearly oval, and the two strokes are too long. Restore the wide pill shape and shorter equal bars toward the left.', '''
        path('capsule',(14,14),[('L',(34,14)),('A',(44,24),10,True),('A',(34,34),10,True),('L',(14,34)),('A',(4,24),10,True),('A',(14,14),10,True)],True)
        for i in range(2):line('bar-'+str(i),(15+8*i,21),(15+8*i,27))
'''),
9:('HRECT_M','toggle-left','The alternate rejected capsule is also too tall and its bars dominate. Restore the source wide capsule with two equal compact left-side strokes.', '''
        path('capsule',(14,14),[('L',(34,14)),('A',(44,24),10,True),('A',(34,34),10,True),('L',(14,34)),('A',(4,24),10,True),('A',(14,14),10,True)],True)
        for i in range(2):line('bar-'+str(i),(15+8*i,21),(15+8*i,27))
'''),
10:('SQUARE','clock-arrow-up','Rejected arrival clock uses an oval orbit and very short hands. Restore a circular return arrow with its upper-left opening and longer perpendicular clock hands.', '''
        path('orbit',(12,11),[('C',(24,6),(15,8),(19,6)),('A',(42,24),18,True),('A',(24,42),18,True),('A',(6,24),18,True)])
        poly('head',(2,29),(6,24),(11,29));join('orbit','head')
        poly('hands',(24,15),(24,25),(32,25))
'''),
11:('SQUARE','box','The rejected cube is squashed into a layered hexagon with heavy node joints. Restore three visible cube faces and three equal endpoint nodes with distinct connecting stems.', '''
        poly('cube-outline',(24,17),(34,23),(34,31),(24,37),(14,31),(14,23),(24,17))
        poly('cube-y',(14,23),(24,29),(34,23));line('cube-center',(24,29),(24,37))
        join('cube-outline','cube-y');join('cube-outline','cube-center');join('cube-y','cube-center')
        for n,x,y,a,b in [('top',24,8,(24,12),(24,17)),('left',8,40,(8,36),(14,31)),('right',40,40,(40,36),(34,31))]:
            circle(n+'-node',x,y,4);line(n+'-stem',a,b);join(n+'-node',n+'-stem');join(n+'-stem','cube-outline')
'''),
12:('HRECT_L','No useful local Lucide bay/waves match','Rejected shoreline is a square step and its waves are thick short blobs. Restore the smooth inlet, broad curved basin and two longer gentle wave lines.', '''
        path('coast',(4,12),[('A',(8,8),4,True),('L',(18,8)),('C',(32,22),(28,8),(22,22)),('L',(40,22)),('L',(40,28)),('C',(28,40),(40,35),(36,40)),('L',(20,40)),('C',(4,26),(10,40),(4,35)),('L',(4,12))],True)
        path('right-shore',(40,22),[('L',(40,14)),('C',(44,8),(40,10),(41,8))]);join('right-shore','coast')
        path('wave-top',(10,21),[('C',(20,21),(14,17),(16,25))])
        path('wave-bottom',(15,31),[('C',(25,31),(19,27),(21,35)),('C',(35,31),(29,27),(31,35))])
'''),
13:('SQUARE','utensils-crossed','Rejected fork is too heavy and its spoon bowl is small. Restore three distinct fork tines, a larger tilted oval spoon bowl, and balanced crossing handles.', '''
        path('fork',(4,12),[('L',(12,20)),('C',(20,20),(14,22),(18,22)),('C',(20,12),(22,18),(22,14)),('L',(12,4))])
        line('middle-tine',(8,8),(20,20));join('middle-tine','fork')
        poly('fork-handle',(20,20),(24,24),(42,42));join('fork-handle','fork');join('fork-handle','middle-tine')
        path('spoon',(28,20),[('C',(29,7),(24,16),(25,11)),('C',(42,6),(33,3),(39,3)),('C',(41,19),(45,9),(45,15)),('C',(28,20),(37,23),(32,24))],True)
        poly('spoon-handle',(28,20),(24,24),(6,42));join('spoon-handle','spoon');join('spoon-handle','fork-handle')
'''),
14:('SQUARE','No useful local Lucide logo match','Rejected logo changes the relative circle sizes and positions. Restore the dominant upper-left circle and the three progressively placed smaller circles to its right and below.', '''
        for n,x,y,r in [('main',15,15,11),('small',41,18,3),('middle',31,29,4),('lower',30,42,4)]:circle(n,x,y,r)
'''),
15:('SQUARE','headphones','Rejected headband is a narrow ellipse above oversized cups. Restore the broad semicircular arch and proportional rounded earcups, with equal radii and a shared center axis.', '''
        path('headband',(6,30),[('L',(6,24)),('A',(24,6),18,True),('A',(42,24),18,True),('L',(42,30))])
        for n,l,r in [('left',6,16),('right',32,42)]:box(n+'-cup',l,26,r,42,4);join(n+'-cup','headband')
'''),
16:('HRECT_M','fish','Rejected fish changes the reference to an open crossed tail and an eye dot. Restore the closed triangular tail and curved gill inside a natural horizontal fish body.', '''
        path('body',(12,24),[('C',(28,10),(16,16),(22,10)),('C',(44,24),(34,10),(40,16)),('C',(28,38),(40,32),(34,38)),('C',(12,24),(22,38),(16,32))],True)
        poly('tail',(12,24),(4,14),(4,34),closed=True);join('tail','body')
        path('gill',(33,19),[('C',(33,29),(31,22),(31,26))])
'''),
17:('VRECT_L','house; dollar-sign','Rejected dollar has squared bends and dominates the house. Restore a smooth compact S with a fine vertical stem inside the upright house silhouette.', '''
        path('house',(8,20),[('L',(24,4)),('L',(40,20)),('L',(40,40)),('A',(36,44),4,True),('L',(12,44)),('A',(8,40),4,True),('L',(8,20))],True)
        path('dollar',(30,21),[('C',(24,19),(28,19),(27,19)),('C',(18,23),(20,19),(18,20)),('C',(24,27),(18,26),(21,27)),('C',(30,31),(27,27),(30,28)),('C',(24,35),(30,34),(27,35)),('C',(18,33),(21,35),(20,35))])
        poly('stem',(24,16),(24,19),(24,27),(24,35),(24,38));join('stem','dollar')
'''),
18:('VRECT_M','hourglass','Rejected hourglass is a wide rigid block with a heavy central X and a short sand dash. Restore slender vertical rims, smooth tapering glass walls and a longer horizontal sand level.', '''
        for n,y in [('top',4),('bottom',44)]:poly(n+'-rim',(10,y),(14,y),(34,y),(38,y))
        path('glass-left',(14,4),[('L',(14,12)),('C',(24,24),(14,18),(20,21)),('C',(34,36),(28,27),(34,30)),('L',(34,44))])
        path('glass-right',(34,4),[('L',(34,12)),('C',(24,24),(34,18),(28,21)),('C',(14,36),(20,27),(14,30)),('L',(14,44))])
        for g in ('glass-left','glass-right'):
            join(g,'top-rim');join(g,'bottom-rim')
        join('glass-left','glass-right')
        line('sand',(19,13),(29,13))
'''),
19:('CIRCLE','power','Rejected power symbol has a flattened lower loop. Rebuild its circular ring on a shared center with equal mirrored endpoints and a centered vertical stroke.', '''
        path('ring',(12,8),[('A',(4,24),20,False),('A',(24,44),20,False),('A',(44,24),20,False),('A',(36,8),20,False)])
        line('stem',(24,4),(24,24))
'''),
20:('SQUARE','No useful local Lucide PyUp logo match','Feedback explicitly says the logo is narrow. Widen both the outer hexagonal spiral and inner hexagon, preserving the open lower-right break and left vertical return.', '''
        poly('outer',(26,44),(44,34),(44,14),(24,4),(4,14),(4,34),(14,40),(14,29))
        poly('inner',(14,29),(14,19),(24,14),(34,19),(34,29),(24,34),closed=True)
        join('outer','inner')
''')}
helpers='''
    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            ident=f'{n}-{i}';k,end,*a=c
            if k=='L':self.add_line(ident,start,end)
            elif k=='A':self.add_arc(ident,start,end,radius_x=a[0],sweep=a[1])
            elif k=='E':self.add_arc(ident,start,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif k=='C':self.add_bezier(ident,start,(a[0],a[1],end))
            ids.append(ident);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,True),('A',(x,y+r),r,True),('A',(x-r,y),r,True),('A',(x,y-r),r,True)],True)
    def box(self,n,l,t,r,b,q):
        self.path(n,(l+q,t),[('L',(r-q,t)),('A',(r,t+q),q,True),('L',(r,b-q)),('A',(r-q,b),q,True),('L',(l+q,b)),('A',(l,b-q),q,True),('L',(l,t+q)),('A',(l+q,t),q,True)],True)
'''
for i,m in enumerate(rows,1):
    key,ref,note,body=drawings[i];rd=Path(m['result_dir']);m.update(comparison=note,lucide=ref,keyshape=key,author=AUTHOR)
    (rd/'comparison.md').write_text(f'# Reference/current comparison\n\n{note}\n\nReviewer feedback: {m["feedback"]}\n\nConstruction reference: {ref}. Inspected original and atomic-debug where present. Preserve semantic silhouette and arrangement.\n')
    mod=rd/(m['icon_id'].replace('-','_')+'_'+m['source_uuid'].replace('-','_')+'.py')
    mod.write_text(f'''"""{note}
Symbol plan: shared dimensions and symmetry for paired parts; coherent contours and explicit real junctions.
Construction reference: {ref}.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID={m['source_uuid']!r}
SOURCE_PATH={m['reference_path']!r}
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id={m['icon_id']!r}
    keyshape=Keyshape.{key}
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords={tuple(m['concept'].split())!r}
    def build(self):
        path=self.path;circle=self.circle;box=self.box;line=self.add_line;poly=self.add_polyline
        join=lambda a,b:self.relate('connect',a,b)
{body}
{helpers}
''')
    m['module']=str(mod)
(root/'batch.json').write_text(json.dumps(rows,indent=2))
