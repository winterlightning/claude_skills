import author as a
import json
entries=json.loads((a.BATCH/'drafts.json').read_text())
a.D[1]['body']=a.D[1]['body'].replace("self.path('flyer-head',(30,24),(31,32,5,5,True),(29,32))", "self.circle('flyer-head',35,26,3)").replace("(43,31),(37,31,3,3,False),(37,37)","(43,37),(37,37,3,3,False)")
a.D[2]['body']=a.D[2]['body'].replace("(7,15,4,4,False),(18,25)","(7,15,4,4,False),(15,22)")
a.D[8]['body']=a.D[8]['body'].replace("(6,14),(42,14)","(6,16),(42,16)").replace("(x,10)","(x,11)").replace("'head',24,22,3","'head',24,24,3").replace("(16,36),(32,36,8,3,True)","(16,38),(32,38,8,3,True)").replace('y25 to shoulder apex y33','y27 to shoulder apex y35')
a.D[11]['body']='''
        # Rounded foot outline and a separate open-wrist hand pressing the sole.
        self.path('foot',(6,11),(6,32),(15,41,9,9,False),(23,38))
        self.path('toes',(6,11),(14,11,4,4,True),(14,12),(20,12,3,3,True),(20,13),(26,13,3,3,True),(26,15),(32,15,3,3,True),(32,19))
        for i,(x,y) in enumerate(((14,12),(20,13),(26,15))):
            self.add_line(f'toe-seam-{i}',(x,y),(x,y+3))
            self.relate('connect','toes',f'toe-seam-{i}')
        self.path('thumb',(31,32),(23,25),(18,30,4,4,False),(29,44))
        self.path('hand-back',(40,44),(42,34),(40,27,12,12,False),(35,22),(29,19),(26,23,3,3,False),(31,27),(31,32))
        self.relate('connect','thumb','hand-back')
'''
a.D[11]['omissions']='Omitted the small sole crease so it does not merge into the massaging thumb.'
a.D[14]['body']=a.D[14]['body'].replace("(34,16),(34,7),(44,4),(44,14)","(34,12),(34,6),(44,3),(44,10)").replace("'note-left',31,17,2","'note-left',31,13,2").replace("'note-right',41,15,2","'note-right',41,11,2")
a.D[17]['body']=a.D[17]['body'].replace("(6,38),(10,42,4,4,False),(31,42),(35,38,4,4,False)","(6,40),(10,44,4,4,False),(31,44),(35,40,4,4,False)").replace("'portrait-head',18,27,3","'portrait-head',18,25,3").replace("(11,38),(25,38,7,3,True)","(11,38),(25,38,7,2,True)").replace('Portrait head ends y30 and shoulders apex y35: compact enclosed portrait, flagged for optical review.','Portrait head ends y28 and shoulder apex y36: exact 4px ink clearance.')
for n in (1,2,8,11,14,17):entries[n-1]=a.make(n,'r2')
(a.BATCH/'selected.json').write_text(json.dumps(entries,indent=2))
a.sheet([entries[n-1] for n in (1,2,8)],'refined-1.png')
a.sheet([entries[n-1] for n in (11,14,17)],'refined-2.png')
