import revise4 as r
a=r.a;D=a.DESIGNS;body=r.body
body(15, '''
path('shell',(4,40),[('A',(8,28),20,20,True),('A',(24,20),20,20,True),('A',(40,28),20,20,True),('A',(44,40),20,20,True),('L',(4,40))],True)
path('lettuce',(8,28),[('B',(4,20),(4,27),(4,24)),('B',(12,12),(4,14),(8,12)),('B',(24,8),(14,12),(18,8)),('B',(36,12),(30,8),(34,12)),('B',(44,20),(40,12),(44,14)),('B',(40,28),(44,24),(44,27))])
join('lettuce','shell')
''')
D[15]['omissions']='Tiny lettuce bumps reduced to three broad waves; shell remains the dominant semicircle.'
a.run(15)
