from pathlib import Path
import json
rows=json.loads((Path(__file__).parent/'inputs.json').read_text())
for i in [0,1,5,6]:
 p=Path(rows[i]['module']);s=p.read_text();(p.parent/'attempt-03.py.txt').write_text(s);(p.parent/'attempt-03-validation.txt').write_text((p.parent/'validation.txt').read_text())
 if i==0:
  a=s.index("        self.path('plane'");b=s.index('\n',a)
  s=s[:a]+"        self.path('plane',(4,24),[('L',(10,24)),('L',(14,28)),('L',(23,24)),('L',(11,10)),('L',(21,8)),('L',(33,20)),('L',(36,19)),('C',(44,24),(40,18),(44,21)),('C',(38,29),(44,27),(42,28)),('L',(34,30)),('L',(29,40)),('L',(19,40)),('L',(24,30)),('L',(13,35)),('C',(8,32),(11,36),(9,35)),('L',(4,24))],True)"+s[b:]
 if i==1:
  s=s.replace('(24,16)','(24,17)').replace('(29,16),(33,20)','(29,17),(33,21)').replace('(15,20),(19,16)','(15,21),(19,17)')
 if i==5:
  # Keep the complete ABC; enlarge B's two counters, restore A's true junctions.
  s=s.replace('Keyshape.HRECT_L','Keyshape.VRECT_L')
  a=s.index('    def monitor(self):');b=s.index('    def banknote',a)
  s=s[:a]+'''    def monitor(self):
        self.rounded('screen',8,4,32,32,3)
        self.add_line('stand',(24,36),(24,44))
        self.add_polyline('foot',(16,44),(24,44),(32,44))
        self.relate('connect','screen','stand');self.relate('connect','stand','foot')

'''+s[b:]
  a=s.index('    def build(self):');s=s[:a]+'''    def build(self):
        self.monitor()
        self.add_polyline('a',(12,28),(14,20),(16,12),(18,20),(20,28))
        self.add_line('a-bar',(14,20),(18,20));self.relate('connect','a','a-bar')
        self.add_polyline('b-stem',(24,12),(24,20),(24,28))
        self.add_line('b-top',(24,12),(28,12))
        self.add_arc('b-upper',(28,12),(28,20),radius_x=4)
        self.add_line('b-middle',(28,20),(24,20))
        self.add_arc('b-lower',(28,20),(28,28),radius_x=4)
        self.add_line('b-bottom',(28,28),(24,28))
        for n in ('b-top','b-middle','b-bottom'):self.relate('connect','b-stem',n)
        for a,b in [('b-top','b-upper'),('b-upper','b-middle'),('b-middle','b-lower'),('b-lower','b-bottom')]:self.relate('connect',a,b)
        self.add_arc('c',(36,14),(36,26),radius_x=6,large_arc=True,sweep=False)
'''
 if i==6:
  # Tall monitor makes room for the two eight-unit division gaps and stand.
  s=s.replace('Keyshape.SQUARE','Keyshape.VRECT_L')
  a=s.index('    def monitor(self):');b=s.index('    def banknote',a)
  s=s[:a]+'''    def monitor(self):
        self.add_polyline('screen',(8,4),(40,4),(40,36),(24,36),(8,36),closed=True)
        self.add_line('stand',(24,36),(24,44))
        self.add_polyline('foot',(16,44),(24,44),(32,44))
        self.relate('connect','screen','stand');self.relate('connect','stand','foot')

'''+s[b:]
  a=s.index('    def build(self):');s=s[:a]+'''    def build(self):
        self.monitor()
        self.add_polyline('plus-h',(16,27),(19,27),(22,27))
        self.add_polyline('plus-v',(19,24),(19,27),(19,30))
        self.relate('connect','plus-h','plus-v')
        self.add_line('divide-bar',(28,20),(32,20))
        for i,y in enumerate((12,28)):self.add_dot('divide-dot-'+str(i),(30,y))
'''
 p.write_text(s)
