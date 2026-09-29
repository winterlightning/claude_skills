from author_batch import *
# Start from the selected standalone candidates, keeping earlier attempts intact.
records=json.loads((ROOT/'runs.json').read_text())
def body(i):
 t=Path(records[str(i)]['module']).read_text();return t.split('    def build(self):\n',1)[1].split('\n    def circle(',1)[0]
def change(i,old,new):
 b=body(i);assert old in b;SPECS[i]=(SPECS[i][0],SPECS[i][1],b.replace(old,new))
change(2,"(36,32),(29,8),(35,10)","(36,32),(32,20),(29,8),(35,8)")
SPECS[4]=(SPECS[4][0],SPECS[4][1],'''
        # Canopy left, reclining person with distinct raised knees right, low water ripples.
        self.add_arc('canopy',(4,14),(20,14),radius_x=8,radius_y=8)
        self.add_line('canopy-base',(20,14),(4,14))
        self.add_contour('umbrella','canopy','canopy-base',closed=True)
        self.add_line('pole',(12,14),(10,35))
        self.circle('head',28,20,4)
        self.curve('torso',(28,32),((28,34),(28,36),(31,36)))
        self.add_polyline('legs',(31,36),(38,28),(44,35))
        self.relate('connect','torso','legs')
        self.mark_human_figure('recliner',head='head',torso='torso',torso_junction='start')
        self.curve('water',(4,43),((7,46),(10,46),(14,43)),((17,46),(20,46),(24,43)),((27,46),(30,46),(34,43)),((37,46),(40,46),(44,43)))
''')
SPECS[7]=(SPECS[7][0],SPECS[7][1],'''
        # Simplified banknote: rounded rectangular bill and enlarged central denomination.
        self.rect('bill',4,10,40,28,3)
        self.circle('denomination',24,24,5)
''')
b=body(8)+"\n        self.relate('connect','upper-node','right-lobe')\n        self.relate('connect','left-node','upper-lobe')\n        self.relate('connect','right-node','lower-lobe')\n"
SPECS[8]=(SPECS[8][0],SPECS[8][1],b)
change(12,"(15,20),(33,20)","(15,19),(33,19)")
k,n,b=SPECS[12];SPECS[12]=(k,n,b.replace("(24,20),(24,40)","(24,19),(24,40)"))
change(17,"self.add_line('torso',(27,26),(25,33))","self.curve('torso',(27,26),((27,29),(27,31),(25,33)))")
author([2,4,7,8,12,17])
