from edit_batch import revise
revise(43,'Simplify the portrait to a dot head and shoulder curve; separate both oval locket halves at one clean hinge.',keyshape='HRECT_L',body="""
oval('back',11,24,7,16)
oval('front',31,24,13,16)
join('back','front')
dot('portrait-head',(31,18))
path('portrait-shoulders',(29,29),[('A',(33,29),2,1,True)])
""")
revise(215,'Shorten and widen both wings; give the landing wheel clear space below the broad horizontal fuselage.',keyshape='SQUARE',body="""
path('plane',(6,14),[('L',(14,16)),('L',(18,16)),('L',(14,6)),('L',(24,6)),('L',(32,16)),('L',(38,16)),('A',(38,24),4,4,True),('L',(32,24)),('L',(24,32)),('L',(14,32)),('L',(18,24)),('L',(14,24)),('L',(6,26)),('L',(10,20)),('L',(6,14))],True)
line('strut',(38,24),(39,36))
join('strut','plane')
oval('wheel',39,39,3,3)
join('wheel','strut')
""")
