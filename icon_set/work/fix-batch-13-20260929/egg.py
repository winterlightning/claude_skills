import revise3 as r
import sys
a=r.a;body=r.body;D=r.D
body(9, '''
# The ribbon occludes the middle shell; top and bottom retain one egg silhouette.
path('egg-top',(14,17),[('B',(24,4),(16,8),(20,4)),('B',(34,17),(28,4),(32,8))])
path('egg-bottom',(34,33),[('B',(24,44),(34,41),(30,44)),('B',(14,33),(18,44),(14,41))])
path('bow-left',(24,25),[('B',(14,17),(21,20),(18,17)),('B',(8,25),(9,17),(8,19)),('B',(14,33),(8,31),(9,33)),('B',(24,25),(18,33),(21,30))],True)
path('bow-right',(24,25),[('B',(34,17),(27,20),(30,17)),('B',(40,25),(39,17),(40,19)),('B',(34,33),(40,31),(39,33)),('B',(24,25),(30,33),(27,30))],True)
for x in ('egg-top','egg-bottom'):
    for y in ('bow-left','bow-right'):join(x,y)
join('bow-left','bow-right')
''')
D[9]['omissions']='Ribbon knot and tails merged into the broad central bow; shell occluded behind ribbon.'
if __name__=='__main__':a.run(9)
