import author as a
import json
entries=json.loads((a.BATCH/'drafts.json').read_text())
newhands='''
        # Two open-wrist palms; shortened thumb creases stay clear of the outer thumb curve.
        for side in (-1,1):
            x=lambda v:24+side*(24-v)
            self.path(f'hand-outer-{side}',(x(12),44),(x(12),40),(x(6),34),(x(6),27),(x(12),27,3,3,side==-1),(x(12),33),(x(15),36))
            self.path(f'hand-inner-{side}',(x(12),33),(x(18),32,4,4,side==-1),(x(20),37,6,6,side==-1),(x(20),44))
            self.relate('connect',f'hand-outer-{side}',f'hand-inner-{side}')
'''
for n in range(1,9):
 b=a.D[n]['body'].replace(a.HANDS,newhands)
 if n in (1,3,5):b=b.replace('(14,26)','(17,25)').replace('(14,25)','(17,24)').replace('(34,26)','(31,25)').replace('(34,25)','(31,24)')
 if n in (4,7):b=b.replace("'head',24,10,5","'head',24,10,4").replace('(16,29),(32,29,8,6,True)','(17,25),(31,25,7,3,True)').replace('bottom y15 to shoulder apex y23','bottom y14 to shoulder apex y22')
 if n==6:b=b.replace('(16,27)','(17,26)').replace('(32,27)','(31,26)')
 if n==8:b=b.replace('(16,30),(32,30,8,3,True)','(18,29),(30,29,6,2,True)')
 a.D[n]['body']=b
# Remove overlapping middle-bar traversal; put both pinches outside the glyph.
a.D[10]['body']='''
        self.path('coin-upper',(22,8),(40,24,17,17,True),(38,31,17,17,True))
        self.path('coin-lower',(26,41),(8,24,17,17,True),(12,14,17,17,True))
        for side in (0,1):
            pt=lambda x,y:(x,y) if side==0 else (48-x,48-y)
            self.path(f'hand-{side}',pt(4,4),pt(9,9),pt(9,12),pt(15,17),(*pt(11,21),3,3,True),pt(6,16))
            self.path(f'wrist-{side}',pt(12,4),pt(15,9),pt(15,12))
        self.path('bitcoin',(20,15),(26,15),(26,23,4,4,True),(26,31,4,4,True),(20,31),(20,15),closed=True)
        self.add_line('bar',(20,23),(26,23))
        self.add_line('stem-top',(23,13),(23,15))
        self.add_line('stem-bottom',(23,31),(23,33))
        self.relate('connect','bitcoin','bar')
        self.relate('connect','bitcoin','stem-top')
        self.relate('connect','bitcoin','stem-bottom')
'''
a.D[12]['body']='''
        self.path('brush',(7,18),(41,18),(41,26,4,4,True),(7,26),(7,18,4,4,True),closed=True)
        self.path('arm-left',(8,4),(16,18))
        self.path('arm-right',(20,4),(26,10),(31,10),(37,16,6,6,True))
        self.path('thumb',(26,15),(31,20),(28,25,3,3,True))
        for i,x in enumerate((9,15,21,27,33,39)):
            self.add_line(f'bristle-{i}',(x,26),(x,31))
            self.relate('connect','brush',f'bristle-{i}')
        self.path('foam',(6,44),(10,40,4,4,True),(20,40),(26,38,4,4,True),(33,37,5,5,True),(40,41,5,5,True),(44,44,4,4,True),(6,44),closed=True)
'''
a.D[13]['body']=a.D[13]['body'].replace('(27,34),(29,39),(36,37,4,4,False),(34,31)','(26,33),(27,37),(33,36,3,3,False),(32,30)')
a.D[16]['body']=a.D[16]['body'].replace('(39,17)','(37,18)')
for n in (*range(1,9),10,12,13,16):entries[n-1]=a.make(n,'r2')
(a.BATCH/'selected.json').write_text(json.dumps(entries,indent=2))
for p in range(0,len(entries),5):a.sheet(entries[p:p+5],f'refined-{p//5+1}.png')
