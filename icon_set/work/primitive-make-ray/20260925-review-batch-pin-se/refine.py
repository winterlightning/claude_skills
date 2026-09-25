from pathlib import Path
import json
B=Path(__file__).parent;rows=json.loads((B/'inputs.json').read_text())
for i in [2,3,6]:
 p=Path(rows[i]['module']);s=p.read_text();(p.parent/'attempt-01.py.txt').write_text(s);(p.parent/'attempt-01-validation.txt').write_text((p.parent/'validation.txt').read_text())
 if i==2:
  s=s.replace('right=[(29,11),(29,18),(42,26),(42,34),(29,28),(29,33),(35,36),(35,42),(24,38)]','right=[(29,11),(29,17),(42,23),(42,33),(29,27),(29,32),(35,34),(35,42),(24,38)]')
 if i==3:
  s=s[:s.index('    def build(self):')]+'''    def build(self):
        # Shared cap attachment nodes, round jaw, touching avatar shoulders.
        self.add_polyline('board',(8,10),(24,4),(40,10),(32,13),(24,16),(16,13),(8,10))
        self.add_polyline('cap-band',(16,13),(16,24),(24,24),(32,24),(32,13))
        self.relate('connect','board','cap-band')
        self.add_arc('jaw',(32,24),(16,24),radius_x=8)
        self.relate('connect','jaw','cap-band')
        self.add_line('tassel',(8,10),(8,24));self.relate('connect','board','tassel')
        self.path('shoulders',(8,44),[('A',(24,36),16,8,True),('A',(40,44),16,8,True)])
        self.relate('connect','jaw','shoulders')
'''
 if i==6:
  s=s.replace('Keyshape.SQUARE','Keyshape.HRECT_L');s=s[:s.index('    def build(self):')]+'''    def build(self):
        # Four long fingers share eight-unit widths; thumb is a separate lobe
        # in the perimeter, without the prior self-overlapping thumb loop.
        first=12;step=8;r=4;heights=(14,12,14,20)
        cmds=[]
        for i,y in enumerate(heights):
            x=first+i*step;cmds += [('L',(x,y)),('A',(x+step,y),r,r,True)]
        cmds += [('L',(44,28)),('A',(32,40),12,12,True),('L',(24,40)),('C',(12,36),(19,40),(15,39)),('L',(4,28)),('A',(8,24),4,4,True),('L',(12,28))]
        self.path('hand',(12,28),cmds,True)
        for i in range(3):
            x=first+(i+1)*step;y=max(heights[i],heights[i+1]);self.add_line(f'crease-{i}',(x,y),(x,29));self.relate('connect','hand',f'crease-{i}')
'''
 p.write_text(s)
