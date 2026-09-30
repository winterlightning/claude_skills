# Batch-local source plans; per-reference SOURCE_ICON_ID and SOURCE_PATH are written into every emitted module.
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=None
D={}
D['piping-nozzle-above-icing-dollop']=('SQUARE','Rejected dollop was flattened and nozzle reduced to a line. Restore a fuller rounded icing mound and an outlined taper.', '''
        self.add_polyline('nozzle',(30,6),(42,10),(30,22),(22,16),closed=True)
        path('icing',(6,36),[('C',(14,29),(6,32),(10,29)),('C',(20,26),(15,26),(18,26)),('C',(27,32),(20,30),(23,31)),('C',(32,37),(30,33),(32,35)),('C',(19,42),(32,41),(25,42)),('C',(6,36),(10,42),(6,41))],True)
''')
D['paint-spray-gun-bottle']=('SQUARE','Rejected sprayer has a single floating dash and squat reservoir. Restore a diverging spray pair, clearer feed tube and more natural gun grip.', '''
        box('housing',6,6,26,18,3)
        self.add_polyline('grip',(10,18),(6,34),(14,34),(18,18));join('grip','housing')
        self.add_polyline('feed',(26,18),(26,26),(34,26),(34,30));join('feed','housing')
        box('reservoir',26,30,42,42,4);join('feed','reservoir')
        self.add_line('spray-upper',(36,8),(42,6))
        self.add_line('spray-lower',(36,18),(42,20))
''')
D['pomegranate-crown-inner-stem']=('VRECT_L','Rejected oval fruit has three bare crown rays. Restore the pointed calyx as part of the fruit silhouette and an asymmetric branching inner stem.', '''
        path('fruit',(16,18),[('C',(8,28),(10,21),(8,23)),('A',(24,44),16,16,False),('A',(40,28),16,16,False),('C',(32,18),(40,23),(38,21)),('L',(34,10)),('L',(28,12)),('L',(24,4)),('L',(20,12)),('L',(14,10)),('L',(16,18))],True)
        self.add_polyline('stem',(24,23),(24,29),(24,35))
        self.add_line('branch-left',(24,29),(18,26));join('stem','branch-left')
        self.add_line('branch-right',(24,29),(29,24));join('stem','branch-right');join('branch-left','branch-right')
''')
D['pomelo-with-single-leaf']=('VRECT_L','Rejected fruit is a squat bowl beneath a tall stalk. Restore a full pear-like citrus body and a short stalk with a single pointed leaf.', '''
        path('fruit',(20,18),[('C',(40,30),(27,18),(40,23)),('C',(24,44),(40,39),(31,44)),('C',(8,30),(15,44),(8,38)),('C',(20,18),(8,24),(14,21))],True)
        self.add_line('stem',(20,18),(20,9));join('stem','fruit')
        path('leaf',(20,9),[('C',(40,4),(22,4),(31,4)),('C',(20,9),(36,14),(27,15))],True);join('stem','leaf')
''')
D['scored-bread-loaf']=('HRECT_M','Rejected loaf looks like a tall square bread slice. Restore a broad rounded loaf and curved oblique score marks; retain two scores for clearance.', '''
        path('loaf',(4,24),[('C',(16,11),(4,17),(8,12)),('C',(28,10),(20,10),(24,10)),('C',(44,24),(39,10),(44,17)),('C',(24,38),(44,36),(35,38)),('C',(4,24),(13,38),(4,36))],True)
        path('score-left',(16,11),[('C',(22,23),(20,14),(21,19))]);join('score-left','loaf')
        path('score-right',(28,10),[('C',(34,22),(32,14),(33,18))]);join('score-right','loaf')
''')
D['scissors-cutting-film']=('SQUARE','Rejected scissor handles are tiny and film appears as two brackets. Enlarge handles, keep crossing blades, and close the separated film frames to make the cut readable.', '''
        circle('loop-top',11,14,5);circle('loop-bottom',11,34,5)
        self.add_line('blade-down',(14,18),(30,34));join('loop-top','blade-down')
        self.add_line('blade-up',(14,30),(30,14));join('loop-bottom','blade-up');join('blade-up','blade-down')
        box('film-top',30,6,42,18,0);join('blade-up','film-top')
        box('film-bottom',30,30,42,42,0);join('blade-down','film-bottom')
''')
D['standing-cow-profile']=('HRECT_L','Rejected cow has a dog-like angular muzzle and blocky feet. Restore rounded hanging muzzle, sloped hock and a small ear while preserving the long back.', '''
        path('cow',(8,40),[('L',(8,22)),('A',(16,14),8,8,True),('L',(30,14)),('L',(32,8)),('L',(36,12)),('C',(44,23),(39,16),(44,19)),('A',(40,27),4,4,True),('L',(35,26)),('C',(31,31),(33,27),(32,30)),('L',(31,40)),('L',(23,40)),('L',(23,31)),('L',(16,31)),('L',(12,37)),('L',(14,40)),('L',(8,40))],True)
        path('tail',(8,22),[('C',(4,32),(6,23),(4,28))]);join('tail','cow')
''')
D['strapped-suitcase-above-a-conveyor']=('SQUARE','Rejected case has sharp corners and merges into its conveyor. Round suitcase and handle, separate belt below, and preserve two straps.', '''
        box('case',8,14,42,30,3)
        path('handle',(18,14),[('L',(18,10)),('A',(22,6),4,4,True),('L',(28,6)),('A',(32,10),4,4,True),('L',(32,14))]);join('handle','case')
        for x in (18,32):self.add_line(f'strap-{x}',(x,14),(x,30));join(f'strap-{x}','case')
        path('belt',(42,34),[('L',(10,34)),('A',(10,42),4,4,False),('L',(42,42))])
''')
D['tapered-bucket-with-a-side-handle']=('SQUARE','Rejected bucket looks like a mug with a rigid side loop. Restore broad tapered pail and a swinging handle attached to a visible pivot.', '''
        path('rim',(6,12),[('A',(38,12),16,6,True),('A',(6,12),16,6,True)],True)
        path('body',(6,12),[('L',(10,36)),('C',(22,42),(10,40),(16,42)),('C',(34,36),(28,42),(34,40)),('L',(38,12))]);join('body','rim')
        circle('pivot',23,27,2)
        path('handle',(25,27),[('L',(38,32)),('A',(42,28),4,4,False),('L',(36,22))]);join('handle','pivot');join('handle','body')
''')
D['tall-rain-boot-with-heel']=('VRECT_L','Rejected boot has square cuff and oversized stepped heel. Round the cuff and toe, add a natural curved ankle and a smaller integrated heel.', '''
        path('boot',(26,4),[('L',(38,4)),('A',(40,6),2,2,True),('L',(39,26)),('L',(40,40)),('A',(36,44),4,4,True),('L',(30,44)),('L',(30,39)),('C',(17,42),(26,41),(21,42)),('L',(8,42)),('L',(8,36)),('A',(16,28),8,8,True),('C',(24,17),(23,28),(24,23)),('L',(24,6)),('A',(26,4),2,2,True)],True)
''')
D['teardrop-pendant-round-loop']=('VRECT_M','Rejected pendant is squat and its tiny loop floats separately. Enlarge the loop and join it to a taller pointed pendant.', '''
        circle('loop',24,9,5)
        path('pendant',(24,14),[('C',(38,32),(29,18),(38,26)),('A',(24,44),14,12,True),('A',(10,32),14,12,True),('C',(24,14),(10,26),(19,18))],True);join('loop','pendant')
''')
D['tapping-finger-with-contact-arc']=('SQUARE','Rejected hand has a stubby index finger and a single short halo. Lengthen the upright finger and carry the outer contact arc farther around it; keep the open wrist.', '''
        path('contact-left',(6,28),[('A',(24,6),18,22,True),('A',(42,28),18,22,True)])
        path('hand',(16,42),[('L',(9,35)),('A',(15,29),5,5,True),('L',(20,34)),('L',(20,22)),('A',(28,22),4,4,True),('L',(28,36)),('L',(34,36)),('L',(34,42))])
''')
D['tea-leaves-beside-pearl-cluster']=('SQUARE','Rejected leaf pair is symmetric and pearls are solid dots below it. Restore asymmetric leaves on a diagonal stem and three large outlined pearls beside them.', '''
        path('leaf-left',(12,25),[('C',(10,6),(4,19),(6,11)),('C',(12,25),(17,15),(17,19))],True)
        path('leaf-right',(12,25),[('C',(33,8),(17,15),(29,16)),('C',(12,25),(33,24),(24,27))],True);join('leaf-left','leaf-right')
        self.add_line('stem',(12,25),(6,37));join('stem','leaf-left');join('stem','leaf-right')
        circle('pearl-upper',36,29,6)
        circle('pearl-left',22,36,6)
        circle('pearl-right',38,40,2)
''')
D['square-neck-pinafore-dress']=('VRECT_L','Rejected pinafore has wide sloping shoulders and an hourglass bodice. Restore upright shoulder straps, squared neckline and a straight-sided bodice above the flared skirt.', '''
        self.add_polyline('bodice',(12,4),(20,4),(20,13),(28,13),(28,4),(36,4),(33,24),(15,24),closed=True)
        path('skirt',(15,24),[('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(33,24))]);join('skirt','bodice')
''')
D['three-sugar-cubes-above-deep-spoon']=('SQUARE','Rejected spoon is a long angular trough and cubes are oversized. Restore a rounded deep bowl at left with a narrow handle, under a compact three-cube stack.', '''
        self.add_polyline('cubes',(6,22),(6,14),(14,14),(14,6),(22,6),(22,14),(30,14),(30,22),(6,22),closed=True)
        self.add_line('top-base',(14,14),(22,14));join('top-base','cubes')
        self.add_line('divider',(18,14),(18,22));join('divider','cubes');join('divider','top-base')
        path('bowl',(6,34),[('A',(28,34),11,4,True),('A',(6,34),11,8,True)],True)
        self.add_line('handle',(28,34),(42,34));join('handle','bowl')
''')
