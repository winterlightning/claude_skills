import author_batch as a
import json
entries=json.loads((a.BATCH/'revised.json').read_text())
a.D[15]['body']='''
        # A clear oval snake head, flowing S-shaped body and draped tail, above an open palm.
        self.path('head',(25,10),(37,10,6,4,True),(25,10,6,4,True),closed=True)
        self.path('body',(31,14),(34,20,8,8,True),(27,28,7,7,True),(18,25),(10,29,5,5,False),(14,41))
        self.add_line('tongue',(37,10),(42,9))
        self.add_line('wrist-top',(6,34),(10,34))
        self.path('palm',(20,35),(27,38),(38,33),(42,36,3,3,True),(29,44),(19,44))
        self.add_line('wrist-bottom',(6,44),(12,44))
        self.relate('connect','head','body')
        self.relate('connect','head','tongue')
'''
a.D[15]['change']='Rebuilt an oval snake head, smooth S-shaped body, coiled bend and hanging tail over an open supporting palm.'
a.D[15]['omissions']='Reduced the snake body to one smooth 4px stroke; omitted tiny eye detail and secondary palm creases.'
a.D[19]['body']='''
        # Dryer with two repeated curved airflow strokes, above a cupped hand.
        self.path('dryer',(8,14),(8,12),(14,6,6,6,True),(34,6),(40,12,6,6,True),(40,14),(8,14),closed=True)
        for i,x in enumerate((19,29)):
            self.path(f'air-{i}',(x,20),(x-1,23,3,3,False),(x,26,3,3,True))
        self.path('thumb',(6,36),(13,32),(24,32),(24,38,3,3,True),(18,38))
        self.path('palm',(6,44),(14,42),(25,44),(31,42,10,10,False),(41,34),(37,30,3,3,False),(27,37))
'''
a.D[19]['change']='Restored the wall-dryer housing, two curved airflow streams, and an open cupped hand.'
a.D[20]['body']='''
        # Tall hanging bag above a receiving hand; unobstructed tubing carries the action.
        self.path('bag',(19,10),(29,10),(32,13,3,3,True),(32,25),(29,28,3,3,True),(19,28),(16,25,3,3,True),(16,13),(19,10,3,3,True),closed=True)
        self.path('hanger',(20,10),(20,4),(28,4),(28,10))
        self.path('tube',(24,28),(24,31),(20,35,4,4,True))
        self.path('thumb',(8,36),(15,33),(20,33),(23,36,3,3,True),(20,39),(16,39))
        self.path('palm',(8,44),(15,43),(26,44),(32,41),(39,35),(35,31,3,3,False),(25,38))
        self.relate('connect','bag','hanger')
        self.relate('connect','bag','tube')
'''
a.D[20]['change']='Restored an elongated hanging IV bag, open hanger loop and curved tubing entering the receiving hand.'
a.D[20]['omissions']='Omitted fluid-level mark to keep the elongated bag clean, as in the original.'
for n in (15,19,20): entries[n-1]=a.make(n,'r3')
(a.BATCH/'selected.json').write_text(json.dumps(entries,indent=2))
a.sheet([entries[n-1] for n in (15,19,20)],'refined-final.png')
