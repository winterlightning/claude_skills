create('batch-01-laptop-computers','HRECT_L','''
self.path('body',(8,30),[(8,12),((12,8),4,4,True),(36,8),((40,12),4,4,True),(40,30),(44,40),(4,40),(8,30)],True)
self.add_line('hinge',(8,30),(40,30))
self.relate('connect','body','hinge')
''','One laptop: rounded upright screen and a broad flared keyboard base; extremes (4,8)-(44,40).','Lucide laptop: screen and flared base with shared hinge.','Keyboard keys omitted at 48px.')

create('handcuffs-with-arched-connector','HRECT_L','''
for i,cx in enumerate((12,36)):
    self.path(f'cuff-{i}',(cx-4,18),[(cx,18),(cx+4,18),(cx+4,24),((cx+8,30),8,8,True),((cx-8,30),8,10,True),((cx-4,24),8,8,True),(cx-4,18)],True)
self.path('chain',(12,18),[((24,8),12,10,True),((36,18),12,10,True)])
for i in range(2): self.relate('connect','chain',f'cuff-{i}')
''','Two broad closed cuffs with narrow lock housings and an arched chain; mirrored about x=24.','Original handcuffs: lock housings and enlarged cuff openings.','Double ring thickness omitted.')

for icon_id in ('asymmetric-branched-snowflake','branched-cold-snowflake'):
    create(icon_id,'SQUARE','''
# Six rays, each split at its fork node; all actual endpoint junctions declared.
center=(24,24)
rays=[((24,14),(24,6),[(16,6),(32,6)]),((24,34),(24,42),[(16,42),(32,42)]),
      ((14,18),(6,14),[(6,22),(14,10)]),((34,18),(42,14),[(42,22),(34,10)]),
      ((14,30),(6,34),[(6,26),(14,38)]),((34,30),(42,34),[(42,26),(34,38)])]
roots=[]
for i,(node,end,twigs) in enumerate(rays):
    root=f'ray-{i}'
    self.add_line(root,center,node);roots.append(root)
    branches=[]
    for j,p in enumerate([end,*twigs]):
        name=f'fork-{i}-{j}';self.add_line(name,node,p);branches.append(name)
    for a in [root,*branches]:
        for b in [root,*branches]:
            if a<b:self.relate('connect',a,b)
for a in roots:
    for b in roots:
        if a<b:self.relate('connect',a,b)
''','Six crystalline arms with a fork on every arm, shared center and mirrored branch definitions.','Lucide snowflake: sixfold branching.','Fine secondary ice twigs omitted.')

create('cartoon-cat-face','SQUARE','''
# Mirrored ears, circular lower face, paired eyes and a small central nose.
self.path('face',(6,24),[(8,6),(18,14),(30,14),(40,6),(42,24),((6,24),18,18,True)],True)
for x in (16,32):self.add_dot(f'eye-{x}',(x,24))
self.add_polyline('nose',(22,31),(24,33),(26,31))
''','Pointed ears, broad rounded cheeks, paired eyes and a feline nose; vertical mirror axis x=24.','Lucide cat: pointed ears joined to cheek contour and sparse facial marks.','Whiskers omitted to preserve clear space.')

create('borobudur-stupas','SQUARE','''
# Stepped temple platform supports three bell-shaped stupas, central tower taller.
self.path('temple',(6,42),[(6,36),((10,32),4,4,True),((14,36),4,4,True),(14,28),(18,28),(18,24),((24,18),6,6,True),((30,24),6,6,True),(30,28),(34,28),(34,36),((38,32),4,4,True),((42,36),4,4,True),(42,42),(6,42)],True)
self.add_line('spire',(24,6),(24,18));self.relate('connect','spire','temple')
''','A central spired stupa and two smaller domes rise from a shared stepped temple base.','Original Borobudur reference: dominant central stupa and smaller flanking stupas.','Small side spires omitted because they crowd the platform walls.')

create('afghan-hound-head','VRECT_L','''
# Long asymmetric coat arch; one eye inside the long muzzle, with no smile.
self.path('coat',(8,44),[(8,24),((22,4),14,20,True),((40,24),18,20,True),(40,44)])
self.path('muzzle',(19,16),[(17,31),((27,39),10,8,False),(30,33),(30,44)])
self.add_dot('eye',(27,23))
''','Afghan hound in three-quarter view: a long muzzle framed by a large flowing asymmetric coat arch and one eye.','Original Afghan hound: long hair and elongated muzzle; Lucide dog: minimal face marks.','Nose and hair striations omitted; smallest permitted eye is one 4px dot.')

create('bowling-pins-row','HRECT_L','''
# One continuous pin definition repeated on 16-unit centers; no touching loops.
for i,cx in enumerate((8,24,40)):
    self.path(f'pin-{i}',(cx-3,11),[((cx+3,11),3,3,True),(cx+2,18),(cx+2,22),
        ((cx+4,30),4,8,True),(cx+3,38),((cx+1,40),2,2,True),(cx-1,40),
        ((cx-3,38),2,2,True),(cx-4,30),((cx-2,22),4,8,True),(cx-2,18),(cx-3,11)],True)
''','Three continuous bowling-pin outlines: rounded crown, narrow neck, lower belly, flat base; shared shape and spacing.','Original three bowling pins: continuous pin silhouettes; no useful local Lucide bowling-pin match.','Neck stripes omitted; neck width is the anticipated blocking constraint.')

for icon_id in ('boxer-avatar','boxer'):
    create(icon_id,'HRECT_L','''
# Raised boxing gloves flank the guarded figure. One glove definition mirrored.
self.circle('head',24,14,6)
self.add_line('torso',(24,28),(24,40))
self.mark_human_figure('boxer',head='head',torso='torso',torso_junction='start')
for i,cx in enumerate((10,38)):
    self.path(f'glove-{i}',(cx-6,29),[((cx+6,29),6,6,True),(cx+6,32),(cx+6,36),(cx+4,40),(cx-4,40),(cx-6,36),(cx-6,32),(cx-6,29)],True)
    node=(cx+6,32) if i==0 else (cx-6,32)
    self.add_line(f'arm-{i}',(24,28),node)
    self.relate('connect',f'arm-{i}',f'glove-{i}')
    self.relate('connect',f'arm-{i}','torso')
self.relate('connect','arm-0','arm-1')
''','Boxer in a guard pose with large padded gloves and narrow wrist cuffs; mirrored gloves share dimensions.','Shared human_ref/full_body_ref.png: detached circular head and round-ended limbs; Lucide hand-fist: one continuous fist silhouette.','Headguard omitted in favor of the conventional boxing-glove cue; head-to-torso ink gap is exactly 4px.')

create('person-holding-smartphone','SQUARE','''
# Detached circular head follows upper torso axis at x=16; exact gap: 26-(12+6)=8.
self.circle('head',16,12,6)
self.add_line('torso',(16,26),(16,42))
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
self.path('back',(16,26),[((6,36),10,10,False),(6,42)])
self.relate('connect','torso','back')
self.box('phone',30,14,12,20,2)
self.path('arm',(16,26),[(24,42),(40,42),(40,34)])
self.relate('connect','arm','torso');self.relate('connect','arm','back');self.relate('connect','arm','phone')
''','A person with a clearly separate upright smartphone supported by a bent arm.','Shared human_ref/user.svg and full_body_ref.png: circular head, round shoulder and limb construction.','Screen details omitted; detached head has an exact 4px ink gap.')

create('cloud-display-globe','VRECT_L','''
# Glass dome on a pedestal, containing one three-lobed cloud.
self.path('globe',(12,36),[((8,20),4,16,True),((24,4),16,16,True),((40,20),16,16,True),((36,36),4,16,True)])
self.box('base',10,36,28,8,4)
self.relate('connect','globe','base')
self.path('cloud',(21,27),[((21,19),4,4,True),((27,19),3,3,True),((27,27),4,4,True),(21,27)],True)
''','Cloud displayed inside a glass globe with a distinct rounded pedestal.','Original sphere: globe and pedestal; Lucide cloud: continuous lobes and flat cloud base.','Minor cloud lobes reduced.')

create('contactless-card-payment-dollar','SQUARE','''
# Payment card in the lower right; radiating arcs at upper left show NFC.
self.box('card',18,30,24,12,2)
self.path('signal-outer',(6,24),[((24,6),18,18,False)])
self.path('signal-inner',(6,15),[((15,6),9,9,False)])
''','A payment card with contactless radio waves instead of an ambiguous touching hand.','Lucide nfc: concentric wireless arcs; original contactless payment: card and wireless cue.','Dollar and holding hand omitted so the contactless payment concept remains clear.')

create('crested-penguin','VRECT_L','''
# Side view preserves a bird beak and long flipper without antenna-like symmetry.
self.path('body',(32,24),[(32,32),((24,44),8,12,True),((8,32),16,12,True),((16,21),8,11,True),(16,15),((25,6),9,9,True),((34,15),9,9,True),(40,20),(32,24)],True)
self.add_dot('eye',(25,16))
self.add_line('flipper',(23,27),(19,34))
self.add_line('crest',(25,6),(14,4));self.relate('connect','body','crest')
self.add_line('foot',(24,44),(34,44));self.relate('connect','body','foot')
''','Crested penguin in side profile: upright pear body, projecting beak, long flipper, swept crest and flat foot.','Original penguin: upright body, crest, beak and flipper; deliberate profile asymmetry prioritizes a conventional bird reading.','Far eye, far flipper and belly patch omitted.')

create('owl-wearing-mortarboard','VRECT_L','''
# Owl face: two large open eye disks and a pointed beak under a diamond cap.
self.add_polyline('cap',(8,10),(24,4),(40,10),(24,16),(8,10))
for x in (14,34):self.circle(f'eye-{x}',x,28,5)
self.add_polyline('beak',(21,40),(24,44),(27,40))
self.add_line('tassel',(8,10),(8,16));self.relate('connect','cap','tassel')
''','Owl face with two large circular eyes and a pointed beak beneath its mortarboard.','Lucide graduation-cap: diamond brim and tassel; original study owl: large paired round eyes and small beak.','Body and wing outline omitted to preserve the owl-specific eyes and beak at 48px.')

create('bunny-holding-easter-egg','VRECT_L','''
# Upright bunny with two long ears and an egg cradled against its right side.
self.path('bunny',(8,44),[(8,36),(8,24),(8,8),((16,8),4,4,True),(16,16),(24,16),(24,8),((32,8),4,4,True),(32,26)])
self.add_dot('eye',(18,25))
self.path('egg',(32,26),[((40,36),8,10,True),((32,44),8,8,True),((24,36),8,8,True),((32,26),8,10,True)],True)
self.add_line('paw',(8,36),(24,36))
self.relate('connect','bunny','egg');self.relate('connect','bunny','paw');self.relate('connect','paw','egg')
''','Long-eared rabbit with a rounded Easter egg cradled by one paw.','Lucide rabbit: long ears and spare profile; original Easter bunny: egg held on its right.','Whiskers and egg decoration omitted.')

create('hand-holding-stopwatch','VRECT_L','''
# Wrist is open at left; continuous thumb/palm contour and four rounded fingers at right.
self.path('hand',(8,28),[(16,20),(20,8),((28,8),4,4,True),(28,12),(36,12),
    ((36,20),4,4,True),((36,28),4,4,True),((36,36),4,4,True),((36,44),4,4,True),(8,44)])
for y in (20,28,36):
    self.add_line(f'crease-{y}',(28,y),(36,y));self.relate('connect','hand',f'crease-{y}')
self.circle('stopwatch',20,30,8)
self.add_polyline('watch-hand',(20,25),(20,30),(23,33))
''','Rounded palm, extended thumb, open wrist and stacked curled fingers restore the hand silhouette.','Lucide hand and hand-fist: shared finger joints and rounded knuckles; original coaching hand reference.','Four fingers and stopwatch dial must remain recognizable; this fit tests their spacing.')

create('diagonal-handshake','HRECT_L','''
# Opposed cuffs, curved central thumb and a scalloped lower finger edge.
self.path('outer',(4,16),[(12,8),(22,12),(30,8),(44,18),(38,28),
    ((32,34),5,5,True),((26,38),4,4,True),((18,40),5,5,True),(4,26),(4,16)],True)
self.path('thumb',(30,8),[(20,18),((26,24),5,5,False),(30,20),(38,28)])
self.relate('connect','outer','thumb')
self.add_line('finger-1',(26,28),(32,34));self.relate('connect','outer','finger-1')
self.add_line('finger-2',(20,32),(26,38));self.relate('connect','outer','finger-2')
''','Two hands meet diagonally, with a curved clasping thumb and rounded finger edge.','Lucide handshake: two opposing palms, inset thumb and scalloped fingers.','Fourth finger and second visible thumb require additional room; tested in the repair loop.')

create('hands-gripping-wrists','SQUARE','''
# Four perpendicular hands grasp the next wrist around an open center.
for i in range(4):
    def rot(p):
        x,y=p
        for _ in range(i):x,y=48-y,x
        return x,y
    pts=[(6,6),(24,6),(28,10),(28,18),(20,18),(20,14),(6,14)]
    self.add_polyline(f'hand-{i}',*[rot(p) for p in pts])
''','Four open-ended wrists and hooked palms form a cooperative hand lock around a central opening.','Original hand-lock reference: four hands cyclically gripping wrists; Lucide hand: finger/palm ownership.','Individual finger creases initially omitted; grasp silhouettes must carry the concept.')

create('stacked-hands','SQUARE','''
# A top wrist enters from above; a second palm approaches diagonally from right.
self.path('lower-hand',(14,6),[(14,20),((6,28),8,8,False),((14,36),8,8,False),(16,42)])
self.path('upper-wrist',(28,6),[(28,15),(34,21)])
self.path('top-hand',(42,42),[(34,34),(22,22),((16,28),5,5,False),(24,36),(18,36),(6,42)])
self.add_polyline('fingers',(34,21),(42,29))
self.relate('connect','fingers','upper-wrist')
''','Overlapping palms entered by visible wrists replace the angular central knot.','Original stacked hands: an upper wrist and a diagonally crossing palm; Lucide hand: rounded finger turn.','Finger seams reduced to preserve the overlapping-hand reading.')
