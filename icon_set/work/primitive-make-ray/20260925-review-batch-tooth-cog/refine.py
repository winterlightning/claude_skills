from pathlib import Path
import json
B=Path(__file__).parent;rows=json.loads((B/'inputs.json').read_text())
for i in [1,2,3,7,8]:
 p=Path(rows[i]['module']);s=p.read_text();(p.parent/'attempt-01.py.txt').write_text(s);(p.parent/'attempt-01-validation.txt').write_text((p.parent/'validation.txt').read_text())
 if i==1:
  s=s.replace('Keyshape.CIRCLE','Keyshape.HRECT_M');s=s[:s.index('    def build(self):')]+'''    def build(self):
        self.path('pod',(18,10),[('L',(22,10)),('C',(44,26),(32,10),(44,20)),('C',(38,38),(44,32),(44,38)),('L',(18,38)),('A',(18,10),14,14,True)],True)
        self.path('windshield',(22,10),[('C',(32,26),(22,20),(26,26)),('L',(44,26))]);self.relate('connect','pod','windshield')
        self.add_line('mark-top',(14,20),(17,20));self.add_line('mark-bottom',(14,28),(16,28))
'''
 if i==2:s=s.replace('(8,18),(24,4),(40,18)','(8,16),(24,4),(40,16)')
 if i==3:
  s=s.replace("('C',(16,16),(8,26),(12,16)),('L',(30,21)),('C',(40,32),(36,22),(40,28))","('C',(16,14),(8,26),(12,14)),('L',(30,18)),('C',(40,32),(36,20),(40,28))")
  s=s.replace("self.path('cap',(16,16),[('L',(19,9)),('C',(33,14),(21,3),(35,7)),('L',(30,21))])","self.path('cap',(16,14),[('L',(19,7)),('C',(28,7),(21,3),(25,6)),('C',(33,11),(31,8),(34,8)),('L',(30,18))])").replace("(28,8),(30,4)","(28,7),(30,4)")
 if i==7:
  s=s[:s.index('    def build(self):')]+'''    def build(self):
        self.circle('head',24,13,7)
        self.add_line('cap-band',(17,13),(31,13));self.relate('connect','head','cap-band')
        self.path('body-left',(6,42),[('L',(6,32)),('A',(14,24),8,8,True)])
        self.add_line('body-top-left',(14,24),(24,24));self.add_line('body-top-middle',(24,24),(27,24));self.add_line('body-top-right',(27,24),(34,24))
        self.path('body-right',(34,24),[('A',(42,32),8,8,True),('L',(42,42))])
        self.relate('connect','body-left','body-top-left');self.relate('connect','body-top-left','body-top-middle');self.relate('connect','body-top-middle','body-top-right');self.relate('connect','body-top-right','body-right')
        for part in ['body-top-left','body-top-middle','body-top-right']:self.relate('connect','head',part)
        self.add_line('fastening',(27,24),(27,42));self.relate('connect','fastening','body-top-middle');self.relate('connect','fastening','body-top-right')
        self.add_polyline('cross-h',(15,35),(17,35),(19,35));self.add_polyline('cross-v',(17,33),(17,35),(17,37));self.relate('connect','cross-h','cross-v')
'''
 if i==8:
  # Lower cap height restores room for the bow while keeping the closed bust.
  s=s.replace("self.circle('head',24,14,10)","self.circle('head',24,12,8)")
 p.write_text(s)
