author(0,'''
# Side-profile pterosaur, intentionally asymmetric: long beak left, crest above neck, raised wing right.
self.path('flying-pterosaur',(4,32),('L',(18,24)),('L',(14,18)),('L',(4,16)),('C',(26,7),(11,9),(18,9)),('C',(26,25),(19,13),(22,21)),('C',(44,5),(27,17),(37,10)),('C',(40,32),(37,19),(37,24)),('C',(28,36),(35,31),(35,38)),('C',(4,32),(18,32),(15,32)),closed=True)
self.add_line('rear-leg',(38,33),(42,39));self.add_line('front-leg',(32,36),(36,43))
self.relate('connect','flying-pterosaur','rear-leg');self.relate('connect','flying-pterosaur','front-leg')
''','SQUARE','The rejected pteranodon was a symmetric bat-shaped star. The source is an asymmetric side view with a long left-facing beak, backward crest and a swept right wing.',
 'Restore the long pointed beak, curved cranial crest, large swept wing, flowing belly and two small trailing legs; retain the source directional asymmetry.',
 'No useful local Lucide pterosaur match. Source silhouette controls construction; smooth curves preserve wing and neck flow.',
 'Tiny eye and wing rib lines omitted, matching the sparse source.',
 exception_reason='Natural pterosaur proportions need an asymmetric near-full square envelope and sharp beak/wing tips. User-authorized visual exception preserves identity with4px strokes.')
author(1,'''
# One diagonal shotgun body with a short butt, a separate rounded pump and a small trigger guard.
self.path('stock-and-barrel',(8,44),('L',(5,35)),('C',(9,28),(3,32),(5,30)),('L',(38,6)),('L',(43,11)),('L',(18,31)),('L',(12,36)),('L',(14,41)),('A',(8,44),4,4,True),closed=True)
self.path('pump',(23,27),('A',(29,30),5,5,False),('L',(37,24)),('A',(39,17),5,5,False))
self.path('trigger-guard',(13,35),('L',(18,33)),('A',(16,29),4,4,False))
self.relate('connect','stock-and-barrel','pump');self.relate('connect','stock-and-barrel','trigger-guard')
''','SQUARE','The rejected shotgun looked like an angular pistol with a large box below it. The original has a long barrel, curved pump grip and a separate small trigger guard.',
 'Restore long diagonal shotgun proportions, compact rounded butt, rounded fore-end pump and small trigger guard.',
 'Lucide sword: clean diagonal construction; supplied shotgun reference owns barrel and stock proportions.',
 'Mechanical fasteners omitted.',
 exception_reason='The long barrel band, pump attachment and compact trigger opening retain natural narrow gaps under the authorized visual exception; this is a48px pictogram with4px strokes.')
for i in [4,5]:
 author(i,'''
# Frontal portrait with a broad symmetric fan headdress; no invented single side feather.
self.path('headdress',(10,21),('C',(7,13),(3,20),(4,14)),('C',(13,8),(7,8),(9,6)),('C',(20,7),(16,3),(19,4)),('C',(28,7),(21,1),(27,1)),('C',(35,8),(29,4),(32,3)),('C',(41,13),(39,6),(41,8)),('C',(38,21),(44,14),(45,20)))
self.path('head',(15,24),('A',(24,18),9,6,True),('A',(33,24),9,6,True),('L',(33,28)),('A',(15,28),9,9,True),('L',(15,24)),closed=True)
self.add_line('headband',(15,24),(33,24));self.relate('connect','head','headband')
self.path('left-ear',(15,25),('A',(11,31),4,4,False),('L',(15,32)))
self.path('right-ear',(33,25),('A',(37,31),4,4,True),('L',(33,32)))
self.path('shoulders',(8,44),('C',(18,40),(10,42),(15,40)),('L',(24,45)),('L',(30,40)),('C',(40,44),(33,40),(38,42)))
self.add_line('headdress-left-rib',(18,14),(21,18));self.add_line('headdress-right-rib',(30,14),(27,18))
''','SQUARE','The rejected portrait substituted a single side feather for the reference fan headdress and omitted the ears and V collar. Feedback asks to recover the reference portrait.',
 'Restore broad scalloped fan headdress, horizontal headband, round lower face, ears and V-shaped collar with shoulders; paired contours share x24 symmetry.',
 'human_ref/user.svg: circular lower face and broad shoulders. Original reference defines fan headdress, headband and collar.',
 'Facial features omitted as in the original.',
 exception_reason='Fan headdress, headband and ears need compact local gaps in the complete portrait. User authorized a meaning-preserving visual exception with4px strokes; circular lower jaw and balanced shoulders remain clear.')
author(7,'''
# The halo is a separate open arc behind the head. A raised arm belongs to a full robe, not a triangular pedestal.
self.add_arc('halo',(12,16),(41,22),radius_x=17,radius_y=17,sweep=True,large_arc=True)
self.circle('head',27,17,5)
self.path('robe-and-arm',(19,44),('L',(22,30)),('L',(13,30)),('A',(9,26),4,4,True),('L',(9,19)),('A',(15,19),3,3,True),('L',(15,25)),('L',(33,25)),('L',(41,44)))
self.add_line('robe-fold',(20,39),(34,26))
self.relate('connect','robe-and-arm','robe-fold')
''','SQUARE','The rejected holy figure became a raised arm over a triangular block and lost the diagonal robe drape. The source shows an open halo, a round head and a flowing robe.',
 'Open circular halo behind a round head, a bent raised arm and long robe sides with a diagonal draped fold.',
 'human_ref/user.svg and full_body_ref.png: circular head and coherent human silhouette; supplied robed figure establishes halo and drapery.',
 'Open robe base preserved from source.',
 exception_reason='Halo, head and robe form a compact devotional figure. Local spacing and natural robe envelope use the authorized visual exception; no generic pedestal replaces the body.')
