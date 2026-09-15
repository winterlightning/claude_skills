"""Authored SOLO48 reconstruction plans, expanded into independent icon modules."""
from pathlib import Path
import json,textwrap
W=Path(__file__).parent
SOURCE_ICON_ID=None
SOURCE_PATH='plan.json'
AUTHOR='gpt-6'
R={}
def recipe(name,keyshape,plan,code,refs='Supplied original; shared geometric construction principles'):
 R[name]=(keyshape,plan,textwrap.dedent(code).strip(),refs)
HELPERS='''
        def path(n, start, commands, closed=False):
            here=start; members=[]
            for j,c in enumerate(commands):
                kind,end,*args=c; ident=('body-top' if j==2 else 'body-top-right') if n=='body' and j in (2,3) else f'{n}-{j}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(n,*members,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def box(n,l,t,r,b,rad=3):
            path(n,(l+rad,t), [('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
'''
recipe('air-pollution-fire','VRECT_L','A fire with a rising plume: one coherent flame outline and one separate smoke curve. The damaged source is a lone stroke; reconstruct the named subject.', '''
path('flame',(24,18),[('C',(40,32),(24,25),(40,23)),('A',(8,32),16,12,True),('C',(14,22),(8,27),(10,24)),('C',(24,18),(16,33),(26,29))],True)
path('smoke',(20,10),[('C',(30,4),(14,4),(27,4))])
''','Lucide flame and cloud: coherent curved silhouette; source is incomplete')
recipe('adaptive-headlight','HRECT_L','A lamp face, three equally spaced beams and a coherent curved steering indicator. Keep the right face smooth and the beam rhythm equal.', '''
path('lamp',(28,16),[('A',(28,40),12,12,True),('L',(28,16))],True)
for j in range(3): line(f'beam-{j}',(4,20+10*j),(16,16+10*j))
path('adaptive',(24,8),[('L',(36,8)),('A',(44,16),8,8,True)])
poly('turn-tip',(36,16),(44,16),(44,8));join('adaptive','turn-tip')
''')
recipe('affinity-publisher-logo','SQUARE','One clipped square boundary and a series of truly parallel bands, all with rise/run 2. Reuse exact attachment nodes.', '''
poly('outline',(6,34),(10,26),(15,16),(20,6),(30,6),(42,6),(42,30),(42,42),(32,42),(18,42),(6,42),closed=True)
for j,(a,b) in enumerate([((10,26),(18,42)),((15,16),(28,42)),((20,6),(38,42)),((30,6),(42,30))]):
 line(f'band-{j}',a,b);join('outline',f'band-{j}')
''')
recipe('airship-over-cloud','HRECT_L','A tapered airship with tail fin and attached gondola above a cloud. Keep a flat underside for an exact physical gondola join.', '''
path('airship',(12,8),[('L',(32,8)),('A',(32,18),12,5,True),('L',(12,18)),('L',(12,8))],True)
poly('tail',(12,8),(4,8),(8,13),(4,18),(12,18));join('tail','airship')
poly('gondola',(20,18),(22,26),(30,26),(32,18));join('gondola','airship')
path('cloud',(12,40),[('A',(20,35),8,5,True),('A',(28,40),8,5,True),('L',(12,40))],True)
''','Lucide cloud: broad lobes; supplied airship silhouette')
recipe('angry-bird','VRECT_L','A rounded bird face with paired slanted brows, a broad pointed beak and a swept feather tuft. Bird identity is carried by beak and tuft.', '''
path('head',(18,10),[('C',(8,28),(12,14),(8,18)),('A',(40,28),16,16,False),('C',(30,10),(40,18),(34,14)),('L',(26,4)),('C',(18,10),(12,4),(14,8))],True)
poly('brow-left',(16,20),(24,24));poly('brow-right',(24,24),(32,20));join('brow-left','brow-right')
poly('beak',(16,34),(24,28),(32,34),(24,38),closed=True)
''','Lucide face-angry for brows; supplied bird for beak and feather tuft')
recipe('ant','VRECT_L','Three recognizable body segments linked on a vertical axis. Four leg strokes preserve the prior feedback to remove the middle pair; antennae and remaining legs mirror.', '''
circle('head',24,12,5)
circle('abdomen',24,36,8)
line('thorax',(24,17),(24,28));join('head','thorax');join('thorax','abdomen')
for side in (-1,1):
 x=lambda d:24+side*d
 poly(f'antenna-{side}',(x(4),9),(x(9),4),(x(16),4));join('head',f'antenna-{side}')
 poly(f'front-leg-{side}',(24,22),(x(12),18),(x(16),12));join('thorax',f'front-leg-{side}')
 poly(f'rear-leg-{side}',(24,28),(x(12),34),(x(16),44));join('thorax',f'rear-leg-{side}');join('abdomen',f'rear-leg-{side}')
join('front-leg--1','front-leg-1');join('rear-leg--1','rear-leg-1')
''','Lucide bug: coherent body and mirrored limb attachments; supplied ant and saved feedback')
recipe('anteater','HRECT_L','Long forward snout, sloping shoulders, bushy tail and two clear legs preserve the anteater profile. Eye is included as requested.', '''
path('animal',(4,28),[('C',(12,16),(6,24),(8,20)),('C',(28,8),(17,10),(21,8)),('C',(40,20),(35,8),(40,12)),('L',(44,32)),('C',(32,28),(40,34),(36,32)),('L',(32,40)),('L',(24,40)),('L',(24,28)),('L',(20,28)),('L',(16,40)),('L',(8,40)),('L',(12,26)),('L',(4,28))],True)
dot('eye',(24,18))
''')
recipe('aperture-shutter','CIRCLE','A true circle with six coordinated blades: use exact radius-20 rim points and three opposed blade pairs.', '''
points=[(36,8),(44,24),(36,40),(12,40),(4,24),(12,8)]
for j in range(6):self.add_arc(f'rim-{j}',points[j],points[(j+1)%6],radius_x=20)
self.add_contour('rim',*(f'rim-{j}' for j in range(6)),closed=True)
blades=[((36,8),(20,8),(12,24)),((44,24),(36,8)),((36,40),(44,24)),((12,40),(28,40),(36,24)),((4,24),(12,40)),((12,8),(4,24))]
# Interior hexagon and the outer segment extensions share explicit nodes.
for j,p in enumerate(blades):poly(f'blade-{j}',*p);join('rim',f'blade-{j}')
''','Lucide aperture original and atomic-debug: true circle and regular blade rhythm')
recipe('arched-stone-bridge','HRECT_L','A stone deck over one broad rounded arch and a single water stroke, as requested in saved feedback.', '''
poly('deck',(4,8),(44,8))
path('bridge',(4,8),[('L',(4,30)),('L',(12,30)),('L',(12,26)),('A',(36,26),12,12,True),('L',(36,30)),('L',(44,30)),('L',(44,8))])
join('deck','bridge')
path('water',(4,40),[('A',(24,40),10,3,True),('A',(44,40),10,3,True)])
''','Lucide bridge: readable deck/support structure; saved request for one simple stone arch')
recipe('arched-tap-spraying-water','VRECT_L','An arched faucet with a downward outlet and two spaced falling drops. The spout and stem are one smooth thick outline.', '''
path('tap',(8,44),[('L',(8,20)),('A',(40,20),16,16,True),('L',(40,24)),('L',(30,24)),('L',(30,20)),('A',(18,20),6,6,False),('L',(18,44)),('L',(8,44))],True)
line('drop-0',(30,36),(30,40));line('drop-1',(40,36),(40,40))
''')
# Directional symbols remain solo at the user's explicit request. Use square 45-degree heads.
recipe('arrow-angle-right','SQUARE','A centered chevron with equal arms; kept as SOLO48 by user request.',"poly('chevron',(6,6),(42,24),(6,42))",'Lucide chevron-right: a single coherent two-arm stroke')
recipe('arrow-angle-up','SQUARE','A matched upward chevron with equal arms; kept as SOLO48 by user request.',"poly('chevron',(6,42),(24,6),(42,42))",'Lucide chevron-right: matched direction-independent arm construction')
for name,orient in [('arrow-dot-down','down'),('arrow-dot-up','up'),('arrow-dot-left','left'),('arrow-dot-right','right')]:
 code=f'''
orient={orient!r}
def pt(x,y):
    if orient=='down':return (x,y)
    if orient=='up':return (x,48-y)
    if orient=='left':return (48-y,x)
    return (y,x)
poly('head',pt(8,28),pt(24,44),pt(40,28))
line('shaft',pt(24,28),pt(24,44));join('head','shaft')
for j,y in enumerate((4,16)):line(f'dash-{{j}}',pt(24,y),pt(24,y+4))
'''
 recipe(name,'VRECT_L' if orient in ('up','down') else 'HRECT_L','Two equal short dashes, consistent eight-unit clearances and a 45-degree arrowhead; solo family retained.',code,'Lucide move-horizontal: equal diagonal arrowheads')
recipe('arrow-dot-corner-down-right','SQUARE','Equal diagonal dashes feed one right-angle arrowhead with matching arms; keep as solo.', '''
line('dash-0',(6,6),(10,10));line('dash-1',(16,16),(20,20));line('shaft',(26,26),(42,42))
poly('head',(24,42),(42,42),(42,24));join('shaft','head')
''')
recipe('arrow-left-right','HRECT_L','One centered shaft and matched 45-degree heads; matched heads preserve clear direction.', '''
poly('left',(20,8),(4,24),(20,40));poly('right',(28,8),(44,24),(28,40));line('shaft',(4,24),(44,24));join('shaft','left');join('shaft','right')
''','Lucide move-horizontal: one shaft and matching heads')
recipe('arrow-rectangle-left-84253ba9','HRECT_L','A coherent tag-shaped arrow sign and centered inset chevron, retained as a solo subject by explicit request.', '''
path('sign',(18,8),[('L',(40,8)),('A',(44,12),4,4,True),('L',(44,36)),('A',(40,40),4,4,True),('L',(18,40)),('L',(4,24)),('L',(18,8))],True)
poly('chevron',(31,17),(24,24),(31,31))
''')
recipe('arrange-number','VRECT_L','Sorting arrow beside a clear 1-over-9 pair; consistent line terminals and a round 9 counter, kept as solo.', '''
poly('arrow',(8,32),(14,40),(20,32));line('shaft',(14,4),(14,40));join('shaft','arrow')
poly('one',(32,8),(36,4),(36,17))
circle('nine',35,31,5);path('tail',(40,31),[('L',(40,36)),('A',(32,44),8,8,True)]);join('nine','tail')
''','Lucide arrow-down-0-1: numeric sorting layout')
recipe('arrow-up-celsius','SQUARE','A readable rising arrow next to the Celsius C and degree dot; preserve upward meaning and restore the missing temperature notation.', '''
poly('arrow',(6,18),(14,6),(22,18));line('shaft',(14,6),(14,42));join('arrow','shaft')
path('celsius',(42,26),[('A',(30,34),12,8,False),('A',(42,42),12,8,False)])
dot('degree',(36,12))
''')
recipe('bbc-iplayer-logo','CIRCLE','A smooth outlined play mark with a single rounded right tip. Preserve the supplied triangular logo component and solo family; no missing lettering invented.', '''
path('play',(12,8),[('L',(40,22)),('A',(40,26),3,3,True),('L',(12,40)),('L',(12,8))],True)
''')

recipe('adaptive-headlight','HRECT_L','A smooth headlamp, three equal beams and a curved upper direction indicator. The lamp face is reduced to leave genuine separation from the indicator.', """
path('lamp',(30,22),[('A',(30,40),14,9,True),('L',(30,22))],True)
for j in range(3):line(f'beam-{j}',(4,20+10*j),(17,16+10*j))
path('turn',(24,8),[('L',(36,8)),('A',(44,16),8,8,True)])
poly('tip',(38,14),(44,16),(44,8));join('turn','tip')
""")
recipe('aperture-shutter','CIRCLE','One exact radius-20 circular rim. Six blades share opposed integer geometry; all diagonal runs have slope 2, without kinks at former inner vertices.', """
rim=[(40,12),(40,36),(24,44),(8,36),(8,12),(24,4)]
for j in range(6):self.add_arc(f'rim-{j}',rim[j],rim[(j+1)%6],radius_x=20)
self.add_contour('rim',*(f'rim-{j}' for j in range(6)),closed=True)
blades=[[(40,12),(28,12),(20,12)],[(40,36),(34,24),(28,12)],[(24,44),(28,36),(34,24)],[(8,36),(20,36),(28,36)],[(8,12),(14,24),(20,36)],[(24,4),(20,12),(14,24)]]
for j,p in enumerate(blades):poly(f'blade-{j}',*p);join('rim',f'blade-{j}')
for j in range(6):join(f'blade-{j}',f'blade-{(j+1)%6}')
""",'Lucide aperture original and atomic-debug: exact circular rim and repeated blades')
recipe('angry-bird','CIRCLE','A rounded bird with swept crest, paired angry brows and a projecting beak; beak is part of the silhouette rather than a crowded interior hole.', """
path('bird',(16,10),[('L',(24,4)),('L',(28,8)),('C',(36,20),(33,10),(36,14)),('L',(44,24)),('L',(36,28)),('C',(22,42),(36,36),(30,42)),('C',(7,26),(12,42),(7,36)),('C',(16,10),(7,18),(10,12))],True)
poly('brows',(16,23),(23,26),(27,22))
""",'Lucide face-angry for brow direction; supplied bird crest and beak identity')
recipe('baby-head','CIRCLE','A true circular baby face with no ears and a single curved hair stroke, matching the saved feedback. Shared horizontal eye axis and a simple smile.', """
circle('head',24,24,20)
path('hair',(24,4),[('C',(20,14),(30,4),(30,14))]);join('head','hair')
dot('eye-left',(16,24));dot('eye-right',(32,24))
self.add_arc('smile',(20,33),(28,33),radius_x=6,radius_y=3,sweep=False)
""",'Lucide user-round for circular face; saved explicit circular baby-head feedback')
recipe('award-flower-rosette','VRECT_L','Four equal circular flower lobes, a centered ring and two symmetric ribbon tails. The flower owns equal lobe radii and exact repeated joins.', """
path('flower',(16,12),[('A',(32,12),8,8,True),('A',(32,28),8,8,True),('A',(16,28),8,8,True),('A',(16,12),8,8,True)],True)
circle('center',24,20,3)
poly('ribbon',(16,28),(12,44),(24,38),(36,44),(32,28));join('flower','ribbon')
""",'Lucide award: medal and paired ribbon; source flower outline reduced to four equal lobes')
recipe('azadi-tower','HRECT_L','A broad flaring monument with one tall pointed arch, restoring the source proportions and avoiding a crowded nested arch.', """
path('tower',(14,8),[('L',(34,8)),('C',(44,40),(34,22),(39,35)),('L',(32,40)),('C',(24,20),(32,30),(28,24)),('C',(16,40),(20,24),(16,30)),('L',(4,40)),('C',(14,8),(9,35),(14,22))],True)
""")
recipe('artillery-field-gun','HRECT_L','Long angled barrel on a large wheel with two stable carriage feet. The barrel keeps consistent parallel walls and a visible muzzle.', """
poly('barrel',(10,20),(40,8),(44,16),(14,28),closed=True)
circle('wheel',20,30,10)
poly('trail',(20,40),(4,40));line('axle',(30,30),(42,40));join('wheel','trail');join('wheel','axle');join('barrel','wheel')
""")
recipe('artillery-gun-outriggers','HRECT_L','A long diagonal cannon barrel on a central wheel with separated left and right outriggers. Shared axis keeps the barrel walls parallel.', """
poly('barrel',(18,18),(38,8),(42,16),(22,26),closed=True)
circle('wheel',20,30,10)
poly('outriggers',(4,40),(20,36),(44,40));join('wheel','outriggers');join('barrel','wheel')
""")
recipe('automatic-rifle','HRECT_L','A recognizable horizontal rifle with a long muzzle, rear stock, magazine and grip. Reduce mechanical detail to preserve silhouette.', """
poly('rifle',(4,22),(12,22),(18,16),(32,16),(32,24),(44,24),(44,32),(32,32),(34,40),(24,40),(22,32),(16,32),(8,38),(4,38),closed=True)
line('sight',(32,16),(32,8));join('rifle','sight')
""")
recipe('baby-walker','HRECT_L','A broad walker tray, hanging seat and rounded base with two wheels. Shared left/right frame posts support the tray.', """
box('tray',4,8,44,16,3)
path('seat',(16,16),[('L',(16,20)),('A',(32,20),8,8,False),('L',(32,16))]);join('tray','seat')
for side,x in [('left',8),('right',40)]:
 line('post-'+side,(x,16),(x,32));join('tray','post-'+side)
poly('base',(8,32),(40,32));join('base','post-left');join('base','post-right')
for j,x in enumerate((12,36)):
 circle(f'wheel-{j}',x,37,3)
 line(f'wheel-link-{j}',(x,32),(x,34));join('base',f'wheel-link-{j}');join(f'wheel-{j}',f'wheel-link-{j}')
""")
recipe('balancing-stick-pose','HRECT_L','One horizontal torso, forward arm and rear raised leg with a supporting leg at the hip. Circular head lies along the upper-torso axis with exactly four units of detached ink gap.', """
circle('head',12,20,4)
line('torso',(24,20),(34,20));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
path('raised-arm',(24,20),[('L',(24,12)),('A',(20,8),4,4,False),('L',(4,8))]);join('torso','raised-arm')
line('rear-leg',(34,20),(44,20));line('support-leg',(34,20),(28,40));join('torso','rear-leg');join('torso','support-leg');join('rear-leg','support-leg')
""",'Shared full_body_ref.png: coherent torso/limbs and exact detached head gap; source balance pose')
recipe('acro-yoga-folded-balance','SQUARE','Two people in a folded supporting balance; shared hand/foot contacts form the acro pose while each head is paired with its actual torso.', """
circle('lower-head',10,36,4)
line('lower-torso',(22,36),(34,36));self.mark_human_figure('base-person',head='lower-head',torso='lower-torso',torso_junction='start')
poly('lower-legs',(34,36),(42,30),(42,42));join('lower-legs','lower-torso')
poly('base-arm',(22,36),(22,22),(30,22));join('base-arm','lower-torso')
circle('upper-head',36,10,4)
line('upper-torso',(24,10),(12,10));self.mark_human_figure('flyer',head='upper-head',torso='upper-torso',torso_junction='start')
poly('folded-legs',(12,10),(6,18),(18,22));join('folded-legs','upper-torso')
poly('flyer-arm',(24,10),(22,22),(30,22));join('flyer-arm','upper-torso');join('flyer-arm','base-arm')
""",'Shared full_body_ref.png and supplied two-person folded balance')
recipe('beading-wire-with-beads','HRECT_L','One continuous U-shaped wire carries three consistent rounded beads. The strand joins each bead at its midpoint and remains clear between beads.', """
box('left-bead',4,8,16,20,4);box('bottom-bead',18,28,30,40,4);box('right-bead',32,8,44,20,4)
path('wire-left',(10,20),[('L',(10,26)),('A',(18,34),8,8,False)]);join('wire-left','left-bead');join('wire-left','bottom-bead')
path('wire-right',(30,34),[('A',(38,26),8,8,False),('L',(38,20))]);join('wire-right','bottom-bead');join('wire-right','right-bead')
""")
recipe('beaded-loop-with-heart-charm','SQUARE','A regular beaded loop with a diagonally aligned heart charm at lower right. The heart uses smooth lobes and coherent sides with a deliberate attachment.', """
for j,p in enumerate([(18,6),(10,10),(6,18),(10,26),(18,30),(26,26),(30,18),(26,10)]):dot(f'bead-{j}',p)
path('heart',(32,30),[('A',(40,30),4,4,True),('C',(42,42),(44,32),(42,38)),('C',(30,40),(38,42),(32,44)),('A',(32,30),5,5,True)],True)
line('link',(26,26),(32,30));join('link','heart');join('link','bead-5')
""")
recipe('artillery-field-gun','HRECT_L','A long constant-width sloping barrel touches the top of a wheel at one exact node. The wheel remains clear inside, with two carriage supports.', """
poly('barrel',(10,16),(34,8),(37,17),(13,25),closed=True)
circle('wheel',13,33,7);join('wheel','barrel')
line('rear-trail',(20,33),(44,40));join('wheel','rear-trail')
line('left-foot',(4,40),(13,40));join('wheel','left-foot')
""")
recipe('artillery-gun-outriggers','HRECT_L','A cannon barrel and wheel meet at the wheel top, with open space around its spokes and two outward carriage legs.', """
poly('barrel',(18,18),(36,8),(40,16),(22,26),closed=True)
circle('wheel',22,33,7);join('barrel','wheel')
line('left-leg',(15,33),(4,40));line('right-leg',(29,33),(44,40));join('wheel','left-leg');join('wheel','right-leg')
""")
recipe('arched-stone-bridge','HRECT_L','A broad stone bridge with one clear rounded arch and a single smooth water wave. Give the deck and arch genuine space.', """
line('deck',(4,8),(44,8))
path('bridge',(4,8),[('L',(4,27)),('L',(14,27)),('L',(14,26)),('A',(34,26),10,10,True),('L',(34,27)),('L',(44,27)),('L',(44,8))]);join('deck','bridge')
path('water',(4,38),[('A',(24,38),10,2,True),('A',(44,38),10,2,False)])
""",'Lucide bridge and supplied stone bridge; simplified single arch requested in feedback')
recipe('beaded-loop-with-heart-charm','SQUARE','A consistent bead loop and a heart turned toward its attachment. Smooth lobes and a coherent pointed lower-right tip preserve the requested charm angle.', """
for j,p in enumerate([(18,6),(10,10),(6,18),(10,26),(18,30),(26,26),(30,18),(26,10)]):dot(f'bead-{j}',p)
path('heart',(32,30),[('C',(40,30),(32,24),(40,24)),('C',(42,42),(40,33),(42,38)),('C',(30,40),(38,42),(33,40)),('C',(32,30),(24,40),(24,32))],True)
line('link',(26,26),(32,30));join('link','heart');join('link','bead-5')
""")
# Portraits are still SOLO48. Headwear owns its silhouette; circular jaw meets shoulder ink.
BODY='''
top=bottom+4
path('body',(8,44),[('L',(8,42)),('A',(18,top),10,42-top,True),('L',(24,top)),('L',(30,top)),('A',(40,42),10,42-top,True),('L',(40,44))])
join('face','body')
'''
BOB='''
path('hair',(8,26),[('L',(8,16)),('A',(24,4),16,12,True),('A',(40,16),16,12,True),('L',(40,26))])
path('fringe',(16,16),[('C',(24,8),(20,16),(24,12)),('C',(32,16),(24,12),(28,16))])
self.add_arc('face',(32,16),(16,16),radius_x=8);join('face','fringe')
# Fringe meets the crown at an actual common point through this short part line.
line('part',(24,4),(24,8));join('part','hair');join('part','fringe')
bottom=24
'''
recipe('arabian-man','VRECT_L','A broad draped headcloth frames a circular jaw; the robe has smooth open shoulders and one central seam.', """
path('cloth',(8,26),[('L',(8,16)),('A',(40,16),16,12,True),('L',(40,26))])
poly('band',(8,16),(16,16),(32,16),(40,16));join('cloth','band')
self.add_arc('face',(32,16),(16,16),radius_x=8);join('face','band');bottom=24
"""+BODY+"line('robe-front',(24,top),(24,44));join('robe-front','body')",'Shared human user.svg and Lucide user-round; supplied headcloth and robe')
recipe('avatar-jockey-man','VRECT_L','A round riding helmet with a short forward peak and circular jaw, above a smooth jersey with a diagonal racing stripe.', """
path('helmet',(14,14),[('A',(34,14),10,10,True),('L',(40,14))])
self.add_arc('face',(34,14),(14,14),radius_x=10);line('brim',(14,14),(34,14));join('face','brim');join('helmet','brim');join('helmet','face');bottom=24
"""+BODY+"line('jersey',(18,top),(32,44));join('jersey','body')",'Human user.svg and Lucide user-round; original riding cap')
recipe('avatar-muslim-man-outfit','VRECT_L','A simple flat kufi cap above a circular jaw and a buttoned tunic. Clothing carries the identity; no facial attributes are invented.', """
poly('cap',(14,14),(14,4),(34,4),(34,14),closed=True)
self.add_arc('face',(34,14),(14,14),radius_x=10);join('face','cap');bottom=24
"""+BODY+"dot('button',(24,39))",'Human user.svg, Lucide user-round and supplied cap/tunic')
recipe('avatar-woman-store-clerk','VRECT_L','A circular face with a short bob and a readable apron within open rounded shoulders; preserve the source hair and apron.',BOB+BODY+"poly('apron',(18,top),(18,44),(30,44),(30,top));join('apron','body')",'Human user.svg, Lucide shirt and supplied bob/apron')
recipe('avatar-woman-store-clerk-3','VRECT_L','A circular face with bobbed hair and two apron straps, with an open lower edge so the torso stays light.',BOB+BODY+"\nfor j,x in enumerate((18,30)):\n line(f'apron-strap-{j}',(x,top),(x,44));join('body',f'apron-strap-{j}')",'Human user.svg, Lucide shirt and supplied bob/apron')
recipe('avatar-korean-woman','VRECT_L','A center-parted bob frames a circular jaw. The crossed garment neckline keeps the supplied hanbok-style clothing readable.',BOB+BODY+"poly('collar',(18,top),(28,42),(34,36));join('collar','body')",'Human user.svg and supplied hairstyle/crossover garment; no facial ethnicity inference')
recipe('avatar-pajamas-woman','VRECT_L','A center-parted bob with a circular jaw above a rounded pajama top and one clear button.',BOB+BODY+"\nfor y in (40,):dot(f'button-{y}',(24,y))",'Human user.svg and supplied bob/pajama top')
recipe('bartainder','HRECT_L','A bartender holds a stemmed cocktail in one bent arm. The circular head follows the vertical torso axis with exactly four units of detached ink clearance.', """
circle('head',12,14,6)
line('torso',(12,28),(12,40));self.mark_human_figure('bartender',head='head',torso='torso',torso_junction='start')
poly('left-arm',(12,28),(4,36),(4,40));poly('serving-arm',(12,28),(24,36),(36,36));join('torso','left-arm');join('torso','serving-arm');join('left-arm','serving-arm')
poly('glass',(28,16),(44,16),(36,28),closed=True);line('stem',(36,28),(36,36));join('glass','stem');join('stem','serving-arm')
""",'Shared full_body_ref.png for limbs and exact detached head; supplied bartender subject')

recipe('ant','VRECT_L','A clear head and broad abdomen linked by a thorax; two mirrored pairs of legs retain the requested removal of the middle pair.', """
circle('head',24,12,5);circle('abdomen',24,36,8)
line('thorax',(24,17),(24,28));join('head','thorax');join('thorax','abdomen')
for side in (-1,1):
 x=lambda d:24+side*d
 poly(f'antenna-{side}',(x(4),9),(x(9),4),(x(16),4));join('head',f'antenna-{side}')
 poly(f'front-leg-{side}',(24,28),(x(12),24),(x(16),16));join('thorax',f'front-leg-{side}');join('abdomen',f'front-leg-{side}')
 line(f'rear-leg-{side}',(x(8),36),(x(16),44));join('abdomen',f'rear-leg-{side}')
join('front-leg--1','front-leg-1')
""",'Lucide bug and supplied ant; saved request for four leg strokes')
recipe('affinity-publisher-logo','SQUARE','A clipped square with three parallel diagonal divisions. Fewer, wider bands keep the recognizable striped publisher mark readable.', """
poly('outline',(6,34),(12,22),(20,6),(30,6),(42,6),(42,30),(42,42),(22,42),(6,42),closed=True)
for j,(a,b) in enumerate([((12,22),(22,42)),((20,6),(38,42)),((30,6),(42,30))]):
 line(f'band-{j}',a,b);join('outline',f'band-{j}')
""")
recipe('aperture-shutter','CIRCLE','An exact circular rim with six straight blades and a broad central opening. Shared integer intersections keep every blade straight through its inner junction.', """
rim=[(40,12),(40,36),(24,44),(8,36),(8,12),(24,4)]
for j in range(6):self.add_arc(f'rim-{j}',rim[j],rim[(j+1)%6],radius_x=20)
self.add_contour('rim',*(f'rim-{j}' for j in range(6)),closed=True)
blades=[[(40,12),(29,14),(18,16)],[(40,36),(34,24),(29,14)],[(24,44),(30,32),(34,24)],[(8,36),(19,34),(30,32)],[(8,12),(14,24),(19,34)],[(24,4),(18,16),(14,24)]]
for j,p in enumerate(blades):poly(f'blade-{j}',*p);join('rim',f'blade-{j}')
for j in range(6):join(f'blade-{j}',f'blade-{(j+1)%6}')
""",'Lucide aperture original and atomic-debug; exact radius-20 rim')
recipe('baby-head','CIRCLE','A circular baby face without ears, one curved hair stroke and an open smile, matching the saved feedback.', """
circle('head',24,24,20)
path('hair',(20,15),[('C',(28,15),(22,13),(26,13))])
dot('eye-left',(16,24));dot('eye-right',(32,24))
self.add_arc('smile',(20,33),(28,33),radius_x=6,radius_y=3,sweep=False)
""")
recipe('baby-walker','HRECT_L','A broad tray and hanging seat supported by two curved wheeled legs. Open lower construction keeps the wheels distinct.', """
box('tray',4,8,44,16,3)
path('seat',(16,16),[('L',(16,24)),('A',(32,24),8,5,False),('L',(32,16))]);join('tray','seat')
for j,(x,c) in enumerate(((8,12),(40,36))):
 poly(f'leg-{j}',(x,16),(x,30),(c,34));join('tray',f'leg-{j}')
 circle(f'wheel-{j}',c,37,3);join(f'leg-{j}',f'wheel-{j}')
""")
recipe('azadi-tower','HRECT_L','Broad flaring stone piers frame a tall pointed arch; widened piers avoid narrow interior slivers.', """
path('tower',(14,8),[('L',(34,8)),('C',(44,40),(34,22),(39,35)),('L',(30,40)),('C',(24,22),(30,30),(27,25)),('C',(18,40),(21,25),(18,30)),('L',(4,40)),('C',(14,8),(9,35),(14,22))],True)
""")
recipe('artillery-field-gun','HRECT_L','A sloping parallel-sided barrel on a circular wheel and two outward carriage supports.', """
poly('barrel',(10,16),(34,8),(37,17),(13,25),closed=True)
circle('wheel',13,33,7);join('wheel','barrel')
line('rear-trail',(20,33),(44,40));join('wheel','rear-trail')
line('left-foot',(6,33),(4,40));join('wheel','left-foot')
""")
recipe('arrange-number','VRECT_L','A sorting arrow beside a clear 1-over-9 pair. The nine uses a continuous round loop and descending stem.', """
poly('arrow',(8,32),(14,40),(20,32));line('shaft',(14,4),(14,40));join('shaft','arrow')
poly('one',(32,8),(36,4),(36,17))
path('nine',(40,31),[('A',(30,31),5,5,False),('A',(40,31),5,5,False),('L',(40,36)),('A',(32,44),8,8,True)])
""",'Lucide arrow-down-0-1 and supplied sorting symbol')
recipe('airship-over-cloud','HRECT_L','A tapered airship above a broad cloud with an attached gondola and an open forked tail.', """
path('airship',(12,8),[('L',(30,8)),('A',(30,20),14,6,True),('L',(12,20)),('L',(12,8))],True)
poly('tail',(4,8),(12,14),(4,20));join('tail','airship')
poly('gondola',(20,20),(22,28),(30,28),(32,20));join('gondola','airship')
path('cloud',(12,40),[('A',(28,40),8,4,True)])
""",'Lucide cloud and supplied airship; retain the natural sky scene as solo')
recipe('anteater','HRECT_L','An elongated low snout, domed back, large trailing tail and two broad legs preserve the anteater silhouette.', """
path('animal',(4,24),[('C',(16,14),(8,21),(12,17)),('C',(28,8),(20,10),(23,8)),('C',(40,20),(35,8),(40,12)),('L',(44,32)),('C',(34,28),(40,34),(37,31)),('L',(34,40)),('L',(26,40)),('L',(26,28)),('L',(18,28)),('L',(16,40)),('L',(6,40)),('L',(10,24)),('L',(4,24))],True)
dot('eye',(24,18))
""")
recipe('automatic-rifle','HRECT_L','A long horizontal rifle barrel projects from a stock and receiver with a broad magazine. The raised carrying handle is open and simple.', """
poly('body',(4,20),(12,20),(12,16),(32,16),(32,24),(28,24),(28,40),(20,40),(18,28),(12,28),(4,36),closed=True)
line('barrel',(32,20),(44,20));join('barrel','body')
poly('handle',(16,16),(20,8),(28,8),(32,16));join('handle','body')
""")

recipe('affinity-publisher-logo','SQUARE','A clipped square with three genuinely parallel diagonal divisions and exact boundary joins. Broad bands preserve the striped mark at native size.', """
poly('outline',(6,30),(12,18),(18,6),(30,6),(42,6),(42,24),(42,42),(28,42),(6,42),closed=True)
for j,(a,b) in enumerate([((12,18),(28,42)),((18,6),(42,42)),((30,6),(42,24))]):
 line(f'band-{j}',a,b);join('outline',f'band-{j}')
""")
recipe('arrange-number','VRECT_L','A sorting arrow beside 1 and 9; the circular nine has a long descending stem with a broad terminal curve.', """
poly('arrow',(8,32),(14,40),(20,32));line('shaft',(14,4),(14,40));join('shaft','arrow')
poly('one',(32,8),(36,4),(36,14))
path('nine',(40,27),[('A',(30,27),5,5,False),('A',(40,27),5,5,False),('L',(40,40)),('A',(32,44),8,4,True)])
""",'Lucide arrow-down-0-1 and supplied sorting symbol')
recipe('air-pollution-fire','VRECT_L','One recognizable flame with a pointed rising tongue and a curved inset lick. The partial source is completed into the named fire subject.', """
path('flame',(24,4),[('C',(40,28),(24,16),(40,18)),('A',(8,28),16,16,True),('C',(16,16),(8,22),(12,18)),('C',(20,28),(14,22),(16,26)),('C',(24,4),(26,23),(26,12))],True)
""",'Lucide flame original and atomic-debug; supplied name and incomplete source')
recipe('balancing-stick-pose','HRECT_L','A forward-reaching balance pose with a raised rear leg and one vertical support leg. The downward-facing circular head has exactly four units of clear ink gap at its neck.', """
path('head',(12,24),[('A',(16,28),4,4,True),('A',(12,32),4,4,True),('A',(8,28),4,4,True),('A',(12,24),4,4,True)],True)
line('torso',(12,16),(12,8));self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
poly('back-and-leg',(12,8),(28,16),(44,8));join('torso','back-and-leg')
line('arm',(4,8),(12,8));join('arm','torso');join('arm','back-and-leg')
line('support-leg',(28,16),(28,40));join('support-leg','back-and-leg')
""",'Shared full_body_ref.png and supplied downward-facing balancing pose')
recipe('acro-yoga-folded-balance','SQUARE','A folded upper person balances at the supporting hand of a seated lower person. Each head follows its own neck direction; broad open limb shapes replace the cramped angular loops.', """
circle('lower-head',10,38,4)
line('lower-torso',(22,38),(34,38));self.mark_human_figure('base-person',head='lower-head',torso='lower-torso',torso_junction='start')
path('lower-legs',(34,38),[('L',(38,38)),('A',(42,34),4,4,False),('L',(42,32))]);join('lower-legs','lower-torso')
line('supporting-arm',(22,38),(22,22));join('supporting-arm','lower-torso')
circle('upper-head',34,22,4)
self.add_bezier('upper-torso',(22,22),((14,22),(22,14),(22,6)))
self.mark_human_figure('flyer',head='upper-head',torso='upper-torso',torso_junction='start')
poly('folded-leg',(22,6),(6,14),(6,22));join('folded-leg','upper-torso');join('supporting-arm','upper-torso')
""",'Shared full_body_ref.png and supplied two-person folded acro-yoga pose')

recipe('airship-over-cloud','HRECT_L','An elongated airship with a tail fin and a clear gondola above a compact lobed cloud. The staggered sky scene gives both subjects room at 48 pixels.', """
path('airship',(12,8),[('L',(36,8)),('A',(36,20),8,6,True),('L',(12,20)),('L',(12,8))],True)
poly('tail',(4,8),(12,14),(4,20));join('tail','airship')
poly('gondola',(28,20),(28,28),(36,28),(36,20));join('gondola','airship')
path('cloud',(8,32),[('A',(4,36),4,4,False),('A',(8,40),4,4,False),('L',(16,40)),('A',(20,36),4,4,False),('C',(8,32),(20,28),(10,28))],True)
""",'Lucide cloud original and atomic-debug; supplied airship/gondola scene')

def write():
 plans=json.loads((W/'plan.json').read_text())
 for r in plans:
  if r['icon_id'] not in R:continue
  key,plan,code,refs=R[r['icon_id']]
  meta=r['meta'];text=f'''"""{plan}\nReferences: {refs}.\nAuthored directly on SOLO48; original retained for comparison."""\nfrom ...keyshapes import Keyshape\nfrom ._base import Solo48\nSOURCE_ICON_ID = {meta.get('SOURCE_ICON_ID')!r}\nSOURCE_PATH = {meta.get('SOURCE_PATH')!r}\nAUTHOR = 'gpt-6'\n\nclass {r['class_name']}(Solo48):\n    icon_id = {r['new_id']!r}\n    variant_of = {r['icon_id']!r}\n    variant_label = 'Reconstructed solo drawing after rejection'\n    keyshape = Keyshape.{key}\n    semantic_role = 'MAIN'\n    semantic_kind = 'noun'\n    category = {('people/occupations' if r['icon_id']=='bartainder' else next(i['category'] for i in json.loads(Path('icon_set/work/rejected-solo-review-50-sep15/snapshot.json').read_text()) if i['icon_id']==r['icon_id']))!r}\n    aliases = ()\n    keywords = {tuple(r['icon_id'].split('-'))!r}\n\n    def build(self):\n        # Symbol plan: {plan}\n'''+HELPERS+textwrap.indent(code,'        ')+'\n'
  compile(text,r['new_path'],'exec');Path(r['new_path']).write_text(text);r['change']=plan;r['references']=refs
 (W/'plan.json').write_text(json.dumps(plans,indent=2))
 print(len(R),'recipes written')
if __name__=='__main__':write()
