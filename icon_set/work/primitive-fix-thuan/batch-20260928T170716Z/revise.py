from pathlib import Path
import sys,json
sys.path.insert(0,str(Path(__file__).parent))
import author_batch as a
SOURCE_ICON_ID=a.SOURCE_ICON_ID
SOURCE_PATH=a.SOURCE_PATH
AUTHOR='gpt-6'
a.claims=json.loads((a.BATCH/'authored.json').read_text())
a.BODIES[6]=a.BODIES[6].replace('(22,10),(26,10)','(22,12),(26,12)')
for i in [7,9]:a.BODIES[i]=a.BODIES[i].replace('(24,30)','(24,28)')
a.BODIES[8]=a.BODIES[8].replace("24,18,5","24,16,5").replace('(19,18)','(19,16)').replace('(29,18)','(29,16)').replace('(17,26),(19,22),(19,24)','(17,24),(19,20),(19,22)').replace('(31,26),(29,22),(29,24)','(31,24),(29,20),(29,22)').replace('(24,31),8,5','(24,29),8,7').replace('(32,36),8,5','(32,36),8,7')
a.BODIES[11]=a.BODIES[11].replace('b=42,footer=34','b=44,footer=32')
a.BODIES[12]=a.BODIES[12].replace('24,18,5','24,16,5').replace('y23 to shoulder apex y31','y21 to shoulder apex y29').replace('(24,31),8,5','(24,29),8,7').replace('(32,36),8,5','(32,36),8,7')
a.BODIES[14]=a.BODIES[14].replace('(19,10),(24,19)','(19,10),(24,16)')
a.BODIES[15]='''self.monitor()
# AB replaces crowded ABC; two legible letters have a 4u ink gap at their nearest ends.
self.add_polyline('a',(10,27),(16,11),(22,27))
self.add_line('a-bar',(12,22),(20,22));self.relate('connect','a','a-bar')
self.path('b',(30,11),[('L',(33,11)),('A',(33,19),4,4,True),('A',(33,27),4,4,True),('L',(30,27)),('L',(30,19)),('L',(30,11))],True)
self.add_line('b-middle',(30,19),(33,19));self.relate('connect','b','b-middle')
'''
a.BODIES[17]=a.BODIES[17].replace('(11,23)','(10,22)')
a.author([6,7,8,9,11,12,14,15,17],rev=2);a.sheets()
