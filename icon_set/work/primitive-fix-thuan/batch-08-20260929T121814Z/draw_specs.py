# Every authored module receives the exact SOURCE_ICON_ID and SOURCE_PATH from claims.json.
SPECS={}
def spec(i,shape,finding,construction,body):SPECS[i-1]=(shape,finding+' No written reviewer feedback.',construction,body)
spec(1,'SQUARE','The rejected bacterium is upright with rail-like projections; restore the reference diagonal capsule and radial protrusions.','Capsule with coherent semicircular ends and four attached projections; dots retain the two inclusions. No useful exact Lucide match.', '''
        self.path('cell',(13,21),[('L',(21,13)),('A',(35,27),10,10,True),('L',(27,35)),('A',(13,21),10,10,True)],True)
        for i,(a,b) in enumerate([((13,21),(6,16)),((21,13),(16,6)),((35,27),(42,32)),((27,35),(32,42))]):
            self.add_line(f'projection-{i}',a,b);self.relate('connect',f'projection-{i}','cell')
        self.add_dot('inclusion-a',(20,28));self.add_dot('inclusion-b',(28,20))
''')
spec(2,'SQUARE','The rejected hand is squat with short fingers; restore the tall palm and upright joined fingers.','Lucide hand and shared human reference: rounded fingers and coherent palm. Three long fingertips replace four crowded fingers; thumb retained.', '''
        self.path('hand',(18,28),[('L',(18,12)),('A',(26,12),4,4,True),('L',(26,10)),('A',(34,10),4,4,True),('L',(34,14)),('A',(42,14),4,4,True),('L',(42,28)),('A',(28,42),14,14,True),('C',(10,32),(20,42),(13,36)),('L',(6,24)),('C',(14,20),(6,18),(10,16)),('L',(18,28))],True)
        self.add_line('finger-crease-a',(26,12),(26,26));self.add_line('finger-crease-b',(34,14),(34,26))
        self.relate('connect','finger-crease-a','hand');self.relate('connect','finger-crease-b','hand')
''')
spec(3,'SQUARE','The rejected raised hands have abbreviated thumbs and detached stripes; restore extended fingers and a clearer binding across the wrists.','Lucide hand: rounded fingertip and angled thumb. Mirrored hands share dimensions; two binding turns replace three fine lines.', '''
        for side in (0,1):
            x=lambda a:48-a if side else a
            sw=not side
            self.path(f'hand-{side}',(x(12),34),[('C',(x(6),20),(x(8),28),(x(6),24)),('L',(x(6),10)),('A',(x(14),10),4,4,sw),('L',(x(14),22)),('L',(x(20),28)),('L',(x(20),34))])
            self.add_line(f'thumb-{side}',(x(14),22),(x(16),18));self.relate('connect',f'thumb-{side}',f'hand-{side}')
        self.add_polyline('binding-top',(10,34),(12,34),(20,34),(28,34),(36,34),(38,34))
        self.add_line('binding-bottom',(10,42),(38,42))
        self.relate('connect','binding-top','hand-0');self.relate('connect','binding-top','hand-1')
''')
spec(4,'HRECT_M','The rejected offering hand curls almost vertically; restore the reference horizontal palm, forearm and softly raised fingertips.','Lucide hand-helping: coherent horizontal hand outline and inner thumb crease. Natural asymmetry follows the reference.', '''
        self.path('palm',(4,18),[('C',(17,12),(10,18),(11,12)),('C',(28,18),(22,12),(23,18)),('L',(31,18)),('L',(38,12)),('C',(42,10),(40,10),(41,10)),('C',(44,14),(44,10),(44,12)),('C',(42,24),(44,18),(44,22)),('L',(33,34)),('C',(22,38),(29,38),(25,38)),('C',(4,32),(15,38),(10,30))])
        self.path('thumb',(18,26),[('L',(24,26)),('C',(31,18),(28,26),(31,22))]);self.relate('connect','thumb','palm')
''')
spec(5,'SQUARE','The rejected speech outline has lost its tail, and the shopping bag reads as a padlock; restore the speech cue and bag shape.','Lucide message-square: open rounded speech enclosure and tail. Bag and side profile retain the complete source composition; small facial marks omitted.', '''
        self.path('bubble',(32,6),[('L',(10,6)),('A',(6,10),4,4,False),('L',(6,34)),('A',(10,38),4,4,False),('L',(16,39)),('L',(24,42)),('L',(24,39))])
        self.add_polyline('bag',(15,21),(25,21),(25,29),(15,29),closed=True)
        self.path('handle',(15,21),[('A',(25,21),5,6,True)]);self.relate('connect','handle','bag')
        self.path('profile',(42,16),[('C',(38,26),(38,16),(38,22)),('L',(34,31)),('L',(38,31)),('L',(38,38)),('A',(42,42),4,4,False)])
''')
spec(6,'VRECT_L','The rejected vampire lacks its bow tie and has a generic round head; restore the bow tie and pointed ears with a smaller circular face.','Shared human_ref/user.svg: circular face and broad shoulders. Pointed ears and fang stroke identify the vampire; small eyes and hairline omitted. Body touches jaw ink.', '''
        self.circle('head',24,17,13)
        self.add_line('ear-left',(11,17),(8,10));self.relate('connect','ear-left','head')
        self.add_line('ear-right',(37,17),(40,10));self.relate('connect','ear-right','head')
        self.add_polyline('fangs',(20,19),(20,17),(28,17),(28,19))
        self.add_polyline('bow',(8,36),(24,40),(40,36),(40,44),(24,40),(8,44),closed=True)

''')
spec(7,'VRECT_L','The rejected veil frames an undersized shallow face; restore the longer face and continuous draping veil.','Shared human reference: circular jaw. Symmetric domed cap and sloping veil; no face details added beyond the supplied drawing.', '''
        self.path('cap',(10,18),[('A',(24,4),14,14,True),('A',(38,18),14,14,True),('L',(10,18))],True)
        self.path('face',(14,27),[('A',(34,27),10,10,False)])
        self.add_line('veil-left',(14,27),(8,44));self.add_line('veil-right',(34,27),(40,44))
        self.relate('connect','face','veil-left');self.relate('connect','face','veil-right')
''')
spec(8,'CIRCLE','The rejected thermometer has a flattened broad bulb and a heavy interior bar; restore a round bulb and shorter temperature column.','Lucide thermometer: narrow stem above a circular bulb. Symmetric vertical construction; tiny bulb point omitted.', '''
        self.path('outline',(15,13),[('A',(33,13),9,9,True),('L',(33,24)),('C',(36,32),(35,27),(36,29)),('A',(24,44),12,12,True),('A',(12,32),12,12,True),('C',(15,24),(12,29),(13,27)),('L',(15,13))],True)
        self.add_line('column',(24,14),(24,27))

''')
spec(9,'CIRCLE','The rejected ruler is broad and its ticks dominate the interior; shorten the ticks and make the ruled edge read clearly.','Lucide ruler: attached alternating ticks. Four ticks replace six to maintain spacing; fixed SOLO48 envelope limits slenderness.', '''
        self.path('body',(16,8),[('A',(32,8),8,4,True),('L',(32,40)),('A',(16,40),8,4,True),('L',(16,32)),('L',(16,24)),('L',(16,16)),('L',(16,8))],True)
        for i,y in enumerate((16,24,32)):
            self.add_line(f'tick-{i}',(16,y),(23 if i%2==0 else 20,y));self.relate('connect',f'tick-{i}','body')

''')
spec(10,'VRECT_L','The rejected paw toes are dots and the medical cross nearly disappears; restore outlined toes and a larger cross.','Lucide paw-print: repeated rounded toes above broad pad. Three circular toes match source count; mirrored pad.', '''
        for i,(x,y) in enumerate(((24,7),(10,13),(38,13))):self.circle(f'toe-{i}',x,y,3 if i==0 else 2)
        self.path('pad',(14,44),[('A',(8,38),6,6,True),('C',(24,20),(8,30),(14,20)),('C',(40,38),(34,20),(40,30)),('A',(34,44),6,6,True),('L',(14,44))],True)
        self.add_polyline('cross-h',(21,32),(24,32),(27,32));self.add_polyline('cross-v',(24,29),(24,32),(24,35));self.relate('connect','cross-h','cross-v')

''')
spec(11,'VRECT_M','The rejected victory hand has no folded fingers or thumb, so it resembles a fork; restore a palm crease beneath the two raised fingers.','Lucide hand-metal and hand: rounded fingertips and folded-finger crease. Two raised fingers and open wrist preserved.', '''
        self.path('hand',(16,44),[('L',(16,38)),('A',(10,32),6,6,True),('L',(10,8)),('A',(18,8),4,4,True),('L',(22,22)),('L',(26,22)),('L',(30,8)),('A',(38,8),4,4,True),('L',(34,28)),('L',(34,30)),('L',(34,36)),('A',(30,40),4,4,True),('L',(30,44))])
        self.add_polyline('fold',(34,30),(22,30),(22,34));self.relate('connect','fold','hand')
''')
spec(12,'VRECT_L','The rejected pilot cap is a sharp pentagon and the uniform lacks its collar; restore a flatter rounded cap and collar cue.','Shared human reference: circular jaw and touching shoulder construction. Cap follows source flattened crown; fine emblems and sleeve divisions omitted.', '''
        self.path('cap',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(34,16)),('L',(14,16)),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.path('face',(34,16),[('A',(14,16),10,10,True)]);self.relate('connect','face','cap')
        self.path('body',(8,44),[('A',(24,30),16,14,True),('A',(40,44),16,14,True)]);self.relate('connect','face','body')
        self.add_line('uniform-seam',(24,30),(24,44));self.relate('connect','uniform-seam','body')
''')
spec(13,'SQUARE','The rejected visitor has only a head and arrow-like shoulders; restore a visible standing body and legs beside the wheel.','Shared full_body_ref.png: round head and stick figure with exact 4-unit ink gap. Wheel circle and cross spokes retained; tiny cabin rings omitted.', '''
        self.circle('head',10,15,4)
        self.add_line('torso',(10,27),(10,34));self.mark_human_figure('visitor',head='head',torso='torso',torso_junction='start')
        self.add_polyline('arms',(6,31),(10,27),(14,31));self.relate('connect','arms','torso')
        self.add_polyline('legs',(6,42),(10,34),(14,42));self.relate('connect','legs','torso')
        self.circle('wheel',32,16,10)
        self.add_polyline('spoke-v',(32,6),(32,16),(32,26));self.add_polyline('spoke-h',(22,16),(32,16),(42,16))
        for k in ('spoke-v','spoke-h'):self.relate('connect',k,'wheel')
        self.relate('connect','spoke-v','spoke-h')
        self.add_polyline('stand',(24,42),(32,26),(40,42));self.relate('connect','stand','wheel');self.relate('connect','stand','spoke-v')
''')
spec(14,'CIRCLE','The rejected ball has only three broad panels; restore the repeated curved volleyball seams.','Lucide volleyball: curved seam groups meeting in a central junction. Circle radius20 and explicitly shared seam nodes.', '''
        self.circle('ball',24,24,20)
        self.path('main',(24,4),[('C',(20,24),(15,7),(14,18)),('C',(44,24),(28,19),(36,19))])
        self.path('lower',(20,24),[('C',(28,34),(25,27),(28,31)),('C',(24,44),(28,38),(27,41))]);self.relate('connect','main','lower')
        self.relate('connect','main','ball');self.relate('connect','lower','ball')
        self.path('left-panel',(4,24),[('C',(28,34),(10,35),(18,38))]);self.relate('connect','left-panel','ball');self.relate('connect','left-panel','lower')
''')
for i in (15,16):
 spec(i,'CIRCLE','The rejected voicemail loops are elongated ovals; restore the two matching circular reels and shared baseline.','Lucide voicemail: circular loops and tangent baseline. CIRCLE radial envelope preserves the horizontal layout; no details omitted.', '''
        self.circle('left',12,24,8);self.circle('right',36,24,8)
        self.add_line('bridge',(12,32),(36,32));self.relate('connect','bridge','left');self.relate('connect','bridge','right')
''')
spec(17,'SQUARE','The rejected doll became a stick person holding a pin; restore a rounded stuffed body and a pin entering its shoulder.','Source toy silhouette and shared human reference for round limbs. Continuous toy head/body connection; no detached-human gap applies.', '''
        self.circle('head',19,13,7)
        self.path('body',(19,20),[('L',(30,24)),('L',(34,25)),('L',(40,37)),('A',(30,37),5,5,True),('L',(26,29)),('L',(22,37)),('A',(12,37),5,5,True),('L',(14,28)),('L',(19,20))],True);self.relate('connect','head','body')
        self.add_line('arm-left',(14,28),(6,28));self.relate('connect','arm-left','body')
        self.circle('pin-head',39,10,3)
        self.add_line('pin',(39,13),(30,24));self.relate('connect','pin','pin-head');self.relate('connect','pin','body')

''')
spec(18,'CIRCLE','The rejected volleyball has only three sections; restore a second curved seam in each visible panel group.','Lucide volleyball: flowing seam junctions and a round silhouette. Repeated seams rebalanced to retain clear channels.', '''
        self.path('ball',(24,4),[('A',(40,12),20,20,True),('A',(44,24),20,20,True),('A',(24,44),20,20,True),('A',(12,40),20,20,True),('A',(4,24),20,20,True),('A',(24,4),20,20,True)],True)
        self.path('sweep',(24,4),[('C',(20,16),(21,8),(20,12)),('C',(24,24),(20,20),(21,23)),('C',(44,24),(31,28),(39,28))]);self.relate('connect','sweep','ball')
        self.path('lower',(24,24),[('C',(12,40),(15,26),(13,33))]);self.relate('connect','lower','sweep');self.relate('connect','lower','ball')
        self.path('panel-top',(40,12),[('C',(20,16),(33,9),(25,10))]);self.relate('connect','panel-top','ball');self.relate('connect','panel-top','sweep')

''')
spec(19,'SQUARE','The rejected VR profile has a square nose and no rounded chin; restore the sloping nose and curved lower face beneath the visor.','Shared human reference for head, Lucide headset for rounded equipment. Continuous profile and neck; no detached head gap. Left-facing asymmetry follows reference.', '''
        self.path('head',(18,14),[('A',(28,6),10,8,True),('A',(42,20),14,14,True),('L',(42,26)),('A',(32,36),10,10,True),('L',(32,42))])
        self.path('visor',(10,14),[('L',(18,14)),('L',(22,14)),('A',(26,18),4,4,True),('L',(26,20)),('L',(26,22)),('A',(22,26),4,4,True),('L',(14,26)),('L',(10,26)),('A',(6,22),4,4,True),('L',(6,18)),('A',(10,14),4,4,True)],True)
        self.add_line('strap',(26,20),(42,20));self.relate('connect','strap','head');self.relate('connect','strap','visor');self.relate('connect','head','visor')
        self.path('face',(14,26),[('L',(11,34)),('L',(18,34)),('L',(18,36)),('A',(24,42),6,6,False)]);self.relate('connect','face','visor')
''')
spec(20,'HRECT_L','The rejected uniform pockets are chevrons and the collar is a simple notch; restore two actual pocket outlines and a tailored collar.','Lucide shirt: symmetric shoulders and body. Two outlined pockets retain the uniform identity; fine flap seams and button placket omitted.', '''
        self.path('shoulder-left',(16,8),[('C',(4,20),(8,8),(4,12))])
        self.add_line('wall-left',(4,20),(4,40));self.add_line('bottom',(4,40),(44,40));self.add_line('wall-right',(44,40),(44,20))
        self.path('shoulder-right',(44,20),[('C',(32,8),(44,12),(40,8))]);self.add_line('neck',(32,8),(16,8))
        for a,b in [('shoulder-left','wall-left'),('wall-left','bottom'),('bottom','wall-right'),('wall-right','shoulder-right'),('shoulder-right','neck'),('neck','shoulder-left')]:self.relate('connect',a,b)
        self.add_polyline('collar',(16,8),(24,16),(32,8));self.relate('connect','collar','neck');self.relate('connect','collar','shoulder-left');self.relate('connect','collar','shoulder-right')
        for x in (16,32):self.add_polyline(f'pocket-{x}',(x-4,24),(x+4,24),(x+4,32),(x-4,32),closed=True)

''')
