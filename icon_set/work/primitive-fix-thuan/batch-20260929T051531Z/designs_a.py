author(2,'''
# Broad side lobes and a taller central lobe share the same base, preserving the pumpkin's ribbed form.
self.path('left-lobe',(18,14),('C',(4,28),(7,10),(4,18)),('C',(18,42),(4,38),(9,44)))
self.path('right-lobe',(30,14),('C',(44,28),(41,10),(44,18)),('C',(30,42),(44,38),(39,44)))
self.path('center-lobe',(24,12),('C',(36,28),(33,12),(36,18)),('C',(24,44),(36,39),(31,44)),('C',(12,28),(17,44),(12,39)),('C',(24,12),(12,18),(15,12)),closed=True)
self.add_line('rib',(24,12),(24,44))
self.path('stem',(22,12),('L',(22,9)),('A',(28,4),6,6,True),('A',(26,12),12,12,False))
self.relate('connect','center-lobe','rib')
''','SQUARE','The rejected pumpkin was a squat three-loop knot and its stem was reduced to a hook. The reference has an elongated central rib, broad side lobes and a shaped stem.',
 'Restore three rounded pumpkin lobes, a central vertical rib and a short curved outlined stem; mirror paired side lobes around x24.',
 'No useful local Lucide pumpkin match. Supplied reference establishes lobes and stem; shared smooth arc construction.',
 exception_reason='Natural joined pumpkin ribs and the compact stem retain closer spacing than MIC; complete ribbed silhouette is accepted under the user-authorized visual exception.')
author(3,'''
# Three equal-height outlined parallelogram bars alternate slant; brackets have the reference vertical stagger.
self.add_polyline('left-bracket',(12,19),(4,27),(12,35))
self.add_polyline('right-bracket',(36,7),(44,15),(36,23))
self.add_polyline('bar-top',(15,9),(31,9),(35,14),(19,14),closed=True)
self.add_polyline('bar-middle',(16,21),(32,21),(28,26),(12,26),closed=True)
self.add_polyline('bar-bottom',(16,33),(32,33),(36,38),(20,38),closed=True)
''','HRECT_L','The rejected emblem replaced three long outlined parallelograms with short dashes and aligned brackets incorrectly. Feedback asks to recover the original emblem.',
 'Restore three outlined skewed bars with alternating slant and staggered outer chevrons, preserving the source logo arrangement.',
 'No useful Lucide logo match; supplied PureScript emblem controls the composition.',
 exception_reason='The emblem requires narrow outlined bands and compact staggered brackets; 4px strokes retain visible bar openings under user-authorized logo exception.')
author(6,'''
self.path('body',(10,22),('L',(38,22)),('A',(42,26),4,4,True),('L',(42,40)),('A',(38,44),4,4,True),('L',(10,44)),('A',(6,40),4,4,True),('L',(6,26)),('A',(10,22),4,4,True),closed=True)
self.path('shackle',(14,22),('L',(14,14)),('A',(34,14),10,10,True),('L',(34,22)))
self.path('road-left',(14,43),('L',(21,28)))
self.path('road-right',(34,43),('L',(27,28)))
self.add_line('road-dash-upper',(24,31),(24,32))
self.add_line('road-dash-lower',(24,38),(24,39))
self.relate('connect','body','shackle')
''','VRECT_L','The rejected lock contained an arch-like block instead of a perspective road and omitted both center dashes.',
 'Rounded padlock with a broad shackle, converging road edges and two centered road markings; shared vertical axis keeps road and lock aligned.',
 'Lucide lock: rounded shackle and rectangular body; reference defines perspective road.',
 exception_reason='Two visible road dashes inside a perspective road require compact interior gaps; the complete symbol is readable at48px with4px strokes under the authorized exception.')
author(12,'''
self.path('header',(8,6),('L',(40,6)),('A',(40,14),4,4,True),('L',(8,14)),('A',(8,6),4,4,True),closed=True)
# Front cloth fold overlays the lower fold. One shared right edge avoids doubled outline.
self.path('front-fold',(15,14),('C',(13,32),(15,21),(14,27)),('L',(40,32)),('L',(39,14)))
self.path('lower-fold',(17,32),('L',(14,44)),('L',(41,44)),('L',(40,32)))
self.add_line('pull-cord',(7,14),(7,33))
self.circle('pull-weight',7,37,4)
self.relate('connect','header','front-fold');self.relate('connect','front-fold','lower-fold');self.relate('connect','header','pull-cord');self.relate('connect','pull-cord','pull-weight')
''','VRECT_L','The rejected Roman shade had a disconnected lower strip and an oversized pull weight; overlapping fabric panels were lost.',
 'Long rounded headrail, two broad overlapping fabric folds with curved left drape, and a fine pull cord with round weight.',
 'Lucide blinds: suspended pull cord and repeated horizontal structure; original defines overlapping Roman folds.',
 exception_reason='Outlined headrail, compact fold overlap and small pull weight preserve Roman-shade structure in48px; user-authorized spacing and envelope exception.')
author(13,'''
self.circle('symbol-ring',21,23,15)
self.add_line('male-stem',(32,12),(43,3));self.add_polyline('male-arrow',(35,3),(43,3),(43,11))
self.add_line('female-stem',(21,38),(21,45));self.add_line('female-cross',(15,42),(27,42))
self.path('heart',(21,19),('A',(13,20),4,4,False),('C',(21,30),(13,24),(17,27)),('C',(29,20),(25,27),(29,24)),('A',(21,19),4,4,False),closed=True)
self.relate('connect','symbol-ring','female-stem');self.relate('connect','male-stem','male-arrow');self.relate('connect','female-stem','female-cross')
''','SQUARE','The rejected symbol used a heart as the whole outline and omitted the enclosing circle. The reference has a heart inside a circle with male arrow and female cross.',
 'Restore circular gender-symbol ring around an independent heart, with a northeast arrow and lower cross.',
 'Lucide heart: paired lobes and tapered point; supplied reference owns combined symbol structure.',
 exception_reason='Nested heart and gender ring require compact internal spacing and extended directional marks. All defining parts remain clear under the user-authorized visual exception.')
