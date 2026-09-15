from edit_batch import *
revise(50,'Remove the pinched inner leaf triangles and leave a generous open suspension above the bowl.',patch=lambda s:remove_named(s,{'leaf-a','leaf-b','leaf-c','leaf-d','pot','rim-right'}).replace("self.add_line('rim-left', (10, 32), (17, 32))","self.add_line('rim-left',(10,32),(38,32))")+"\n    self.add_contour('pot','rim-left','bowl',closed=True)\n    self.relate('connect','pot','left-support')\n    self.relate('connect','pot','right-support')\n")
revise(98,'Enlarge the outer toe ovals and rebalance the lower pad within a taller envelope.',body='''
for name,x,y in [('upper-left',16,9),('upper-right',32,9),('outer-left',12,26),('outer-right',36,26)]:oval(name,x,y,4,5)
oval('pad',24,40,6,4)
''',keyshape='VRECT_L',ref='Lucide paw-print: rounded paired toes and a separate lower pad')
revise(213,'Round all four wing and tail tips with explicit smooth turns.',body='''
path('plane',(34,6),[('A',(42,14),8,8,True),('L',(34,24)),('L',(40,32)),('C',(40,36),(42,34),(42,34)),('L',(36,40)),('C',(32,39),(34,42),(34,42)),('L',(26,30)),('L',(20,36)),('L',(21,39)),('C',(18,42),(22,42),(22,42)),('L',(15,42)),('A',(12,39),3,3,True),('L',(12,36)),('L',(8,35)),('C',(6,32),(6,34),(6,34)),('L',(6,27)),('C',(9,25),(6,24),(6,24)),('L',(14,26)),('L',(20,20)),('L',(9,14)),('C',(8,10),(6,12),(6,12)),('L',(10,8)),('C',(14,7),(12,6),(12,6)),('L',(26,14)),('L',(34,6))],True)
''',ref='Lucide plane: smooth nose and coherent joined wing outline')
