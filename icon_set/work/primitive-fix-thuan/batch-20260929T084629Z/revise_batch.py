"""Fresh revision attempts after native light/dark review; exact sources retained."""
import author_batch as a
AUTHOR=a.AUTHOR
SOURCE_ICON_ID=None
SOURCE_PATH=None

def revise(i, body, plan=None, version='02'):
 global SOURCE_ICON_ID,SOURCE_PATH
 shape,comparison,oldplan,_=a.SPECS[i]
 a.SPECS[i]=(shape,comparison,plan or oldplan,body)
 a.author(i,version)
 SOURCE_ICON_ID=a.SOURCE_ICON_ID;SOURCE_PATH=a.SOURCE_PATH

revise(5,a.SPECS[5][3].replace("line('central-arm',(24,34),(24,44))",''),
 'Rounded crown and four spacious curled arm runs; omit the crowded fifth visible curl to keep the octopus readable at 48px.')
revise(6,a.SPECS[6][3].replace("(15,22)","(18,22)").replace("(12,34)","(15,34)").replace("(36,34)","(33,34)").replace("(33,22)","(30,22)"))
revise(9,"""
ellipse('glass',24,15,11)
arc('cradle',(8,22),(40,22),16,16,False)
line('stem',(24,38),(24,44))
line('base',(14,44),(34,44))
self.relate('connect','stem','base')
""")
revise(10,a.SPECS[10][3].replace("12,9","10,7").replace("24,8,3","24,6,2"))
revise(19,a.SPECS[19][3].replace("(36,23)","(36,28)"))
revise(20,"""
# The torso is vertical at its upper junction, aligning the circular head.
ellipse('head',33,9,5)
line('torso',(33,22),(33,27))
line('lower-torso',(33,27),(28,32))
poly('forward-arm',(33,22),(40,24),(44,18))
poly('carrying-arm',(33,22),(25,18),(13,18))
poly('back-leg',(28,32),(26,38),(31,44))
poly('front-leg',(28,32),(37,31),(41,40),(44,40))
path('bag',(8,23),[('L',(4,29)),('A',(4,39),10,10,False),('A',(20,39),8,5,False),('A',(20,29),10,10,False),('L',(16,23)),('L',(8,23))],True)
poly('tie',(8,23),(7,18),(17,18),(16,23))
path('dollar',(15,28),[('L',(10,28)),('A',(10,33),2,3,False),('L',(14,34)),('A',(14,39),2,3),('L',(9,39))])
line('dollar-stem',(12,26),(12,41))
self.mark_human_figure('runner',head='head',torso='torso',torso_junction='start')
""",'Larger tied sack with an explicit dollar; bent opposing strides and carrying arm. Circular head bottom is 14; upper torso starts at 22, exactly 4 units of visible gap.')
