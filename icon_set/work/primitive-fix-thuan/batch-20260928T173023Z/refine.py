from pathlib import Path
import sys,json,textwrap
sys.path.insert(0,str(Path(__file__).parent))
import author_batch as a
SOURCE_ICON_ID=a.SOURCE_ICON_ID
SOURCE_PATH=a.SOURCE_PATH
AUTHOR='gpt-6'
a.claims=json.loads((a.BATCH/'authored.json').read_text())
for r in a.claims:a.BODIES[r['index']]=textwrap.dedent(Path(r['module']).read_text().split('    def build(self):\n',1)[1])
a.BODIES[1]='''self.circle('ring',24,24,20)
# Tall reference C: tangent-continuous oval curves and a straight shared-node slash.
self.path('c',(30,16),[('C',(17,23),(20,10),(17,15)),('C',(20,31),(17,27),(18,29)),('C',(30,31),(23,34),(27,34))])
self.add_polyline('slash',(18,34),(20,31),(30,16));self.relate('connect','c','slash')
'''
a.NOTES[1]=(a.NOTES[1][0],'Rebuilt the taller C from smooth coherent curves and aligned the diagonal slash to exact shared nodes, with more clearance to the badge.')
a.BODIES[2]='''# Circular return fitted to SQUARE so its arrowhead remains within the declared envelope.
self.path('return',(24,42),[('A',(6,24),18,18,True),('A',(24,6),18,18,True),('A',(42,24),18,18,True),('C',(34,39),(42,30),(39,36))])
self.add_polyline('arrow',(34,31),(34,39),(42,39));self.relate('connect','return','arrow')
self.add_polyline('hands',(24,14),(24,24),(33,24))
'''
a.SHAPES[2]='SQUARE'
a.BODIES[3]=a.BODIES[3].replace('(24,24),(44,4)','(24,24),(42,6)').replace('(16,32),(4,44)','(16,32),(6,42)')
a.BODIES[4]=a.BODIES[4].replace('(16,28)','(16,26)').replace("('L',(38,4)),('L',(44,10))","('L',(36,6)),('L',(42,12))")
a.BODIES[4]=a.BODIES[4].replace("[('L',(8,28)),('A',(4,32),4,4,False),('A',(8,36),4,4,False),('L',(29,36)),('A',(29,44),4,4,True),('L',(4,44))]","[('L',(10,26)),('A',(6,30),4,4,False),('A',(10,34),4,4,False),('L',(29,34)),('A',(29,42),4,4,True),('L',(6,42))]")
a.BODIES[17]=a.BODIES[17].replace('(x,18),(x,25)','(x,21),(x,25)')
a.author([1,2,3,4,17],rev=2);a.sheets()
