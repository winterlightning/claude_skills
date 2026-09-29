import author_batch as a
import json
from pathlib import Path
# Each changed design is exported as a fresh authoring run, preserving the first attempt.
for n in (2,7):
 b=a.D[n]['body']
 b=b.replace("self.path('handle-bottom',(13,35),(6,42),(11,44),(18,37))", "self.add_line('handle-bottom',(13,36),(6,43))")
 b=b.replace("self.path('shaft-end',(13,35),(6,42),(11,44),(18,37))", "self.add_line('shaft-end',(13,36),(6,43))")
 b=b.replace("self.path('fist',(12,36),(7,31),(7,27,3,3,True),(15,19),(19,19,3,3,True),(28,28))", "self.path('fist',(15,39),(7,31),(7,27,3,3,True),(14,22),(18,22,3,3,True),(27,31))")
 b=b.replace("self.path('thumb',(22,24),(29,29),(31,34,7,7,True),(29,39),(31,44))", "self.path('thumb',(24,28),(29,33),(29,39,6,6,True),(31,44))")
 b=b.replace("for i,(x,y) in enumerate(((10,25),(15,21))):", "for i,(x,y) in enumerate(((10,26),)):")
 a.D[n]['body']=b
 a.D[n]['change']=a.D[n]['change'].replace('two finger divisions','one clear finger division').replace('wrapping fingers','two broad wrapping fingers')
a.D[5]['body']=a.D[5]['body'].replace("self.path('pen-tail',(38,13),(42,13),(42,20),(38,20))", "self.add_line('pen-tail',(38,16),(42,16))")
a.D[6]['body']='''
        # Six-tooth gear on left; open C-shaped hand grips its upper/lower edges.
        self.path('gear',(14,6),(19,6),(20,11),(25,12),(28,17),(24,21),(24,26),(19,27),(17,31),(12,29),(11,24),(6,22),(7,17),(11,15),(10,10),(14,6),closed=True)
        self.circle('hub',17,19,3)
        self.path('index',(31,14),(29,14),(29,6,4,4,True),(33,6),(42,18,13,13,True),(42,42))
        self.path('inside',(31,14),(35,20,7,7,True),(31,29,9,9,True),(27,29))
        self.path('thumb',(31,33),(25,28),(20,32,3,3,False),(30,42))
        self.relate('connect','index','inside')
'''
for n in (9,10):
 a.D[n]['body']=a.D[n]['body'].replace("for side,x in enumerate((20,33)):\n            self.path(f'eye-{side}',(x,17),(x+4,18),(x+2,22),(x,17),closed=True)", "for side,x in enumerate((22,34)):\n            self.path(f'eye-{side}',(x-4,19),(x+4,19,4,3,True),(x-4,19,4,3,True),closed=True)")
 a.D[n]['change']=a.D[n]['change'].replace('almond eye','oval eye').replace('theatrical mask eye','theatrical mask oval eye')
a.D[11]['body']=a.D[11]['body'].replace("self.path('handle',(17,22),(20,31),(27,31),(24,23))", "self.path('handle-left',(17,22),(19,29))\n        self.path('handle-right',(24,23),(26,29))").replace("self.relate('connect','horn','handle')","self.relate('connect','horn','handle-left')")
a.D[12]['body']=a.D[12]['body'].replace("(17,26),(22,25),(22,29)","(17,28),(19,28),(19,29)").replace("self.path('handle-end',(20,42),(24,44,3,3,False),(27,42))", "self.path('handle-end',(20,42),(27,42,4,3,False))")
a.D[13]['body']='''
        # Long nose and folded wing; the plane ends where the thumb covers it.
        self.path('plane',(6,6),(42,10),(35,19),(6,6),closed=True)
        self.path('fold',(18,12),(35,19),(33,30))
        self.path('underside',(12,14),(12,18,4,4,False),(21,26))
        self.path('thumb',(29,32),(27,24),(21,26,3,3,False),(23,36),(26,42))
        self.path('palm',(33,30),(35,42))
        self.path('fingers',(17,24),(13,23),(9,27,3,3,False),(16,34))
        self.path('lower-finger',(12,31),(10,35,3,3,False),(18,42))
        self.relate('connect','plane','fold')
'''
a.D[15]['body']='''
        # Smooth S-shaped snake neck, a loop on the left, and a clearly draped tail.
        self.path('snake',(34,10),(29,6,5,5,False),(25,6),(21,10,4,4,False),(21,13),(27,19),(30,25,8,8,True),(27,30),(20,28),(16,24,6,6,False),(10,25,5,5,False),(9,30),(13,38),(11,44))
        self.path('snake-back',(34,10),(31,15),(35,21,9,9,True),(32,30),(27,34),(19,33),(17,30),(16,29),(15,30),(18,39),(15,43),(11,44))
        self.add_line('tongue',(34,10),(40,11))
        self.add_line('wrist-top',(6,34),(10,34))
        self.path('hand',(20,37),(27,39),(38,34),(42,37,3,3,True),(29,44),(21,44))
        self.add_line('wrist-bottom',(6,43),(11,43))
        self.relate('connect','snake','tongue')
'''
a.D[16]['body']=a.D[16]['body'].replace("self.add_line('wrist-back',(42,31),(42,42))", "self.path('wrist-back',(42,12),(40,21),(40,31),(42,42))")
a.D[17]['body']='''
        # Two true concentric radio corners; phone and enclosing hand beneath.
        self.path('phone',(25,44),(14,44),(11,41,3,3,True),(11,21),(14,18,3,3,True),(27,18),(30,21,3,3,True),(30,29))
        self.add_line('bezel',(11,36),(22,36))
        self.path('thumb',(34,36),(28,30),(23,34,3,3,False),(28,40),(30,44))
        self.path('back',(30,26),(39,35,9,9,True),(39,39),(42,44))
        for side in (-1,1):
            x=lambda v:24+side*v
            self.path(f'wave-outer-{side}',(x(20),14),(x(10),4,10,10,side==-1))
            self.path(f'wave-inner-{side}',(x(14),14),(x(10),10,4,4,side==-1))
        self.relate('connect','phone','bezel')
'''
a.D[18]['body']=a.D[18]['body'].replace("self.add_line('currency-stem',(30,10),(30,13))", "self.add_line('currency-stem',(30,11),(30,13))").replace("(31,23,3,3,True),(26,23)","(31,22,2,2,True),(27,22)").replace("(14,38),(24,38)","(14,38),(21,38)")
a.D[19]['body']=a.D[19]['body'].replace("(x,23),(x,26)","(x,23),(x,24)")
a.D[20]['body']='''
        # Tall bag with a real loop opening; outlet tube terminates at the hand's back.
        self.path('bag',(19,10),(30,10),(33,13,3,3,True),(33,22),(30,25,3,3,True),(19,25),(16,22,3,3,True),(16,13),(19,10,3,3,True),closed=True)
        self.path('hanger',(21,10),(21,4),(28,4),(28,10))
        self.add_line('fluid',(23,17),(26,17))
        self.path('tube',(25,25),(25,28),(21,32,4,4,True))
        self.path('thumb',(8,35),(15,32),(21,32),(24,35,3,3,True),(21,38),(17,38))
        self.path('palm',(8,44),(15,42),(26,44),(32,41),(39,35),(35,31,3,3,False),(25,38))
        self.relate('connect','bag','hanger')
        self.relate('connect','bag','tube')
        self.relate('connect','tube','thumb')
'''
changes=(2,5,6,7,9,10,11,12,13,15,16,17,18,19,20)
entries=json.loads((a.BATCH/'drafts.json').read_text())
for n in changes: entries[n-1]=a.make(n,'r2')
(a.BATCH/'revised.json').write_text(json.dumps(entries,indent=2))
for p in range(0,len(entries),5):a.sheet(entries[p:p+5],f'revised-{p//5+1}.png')
