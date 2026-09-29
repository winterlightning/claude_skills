import _author_batch as a
import json
from pathlib import Path
def replace(i,old,new):
    assert old in a.DESIGNS[i]['code'],(i,old)
    a.DESIGNS[i]['code']=a.DESIGNS[i]['code'].replace(old,new)
replace(1,"('L',(33,42))","('L',(30,42))")
replace(1,"('C',(10,31),(9,40),(8,35))","('C',(9,31),(7,40),(7,35))")
# Open the spillway details and use gentler waves with exact extrema.
a.DESIGNS[2]['code']='''
for name,x in [('left',6),('right',34)]:
    poly(name,(x,33),(x+2,6),(x+8,6),(x+8,16),(x+5,33))
line('bridge-top',(14,10),(34,10));line('bridge-bottom',(14,18),(34,18))
for j,x in enumerate((22,30)): line(f'water-{j}',(x,24),(x-1,27))
path('waterline',(6,33),[('C',(15,33),(9,30),(12,36)),('C',(24,33),(18,30),(21,36)),('C',(33,33),(27,30),(30,36)),('C',(42,33),(36,30),(39,36))])
path('river',(6,41),[('C',(15,41),(9,37),(12,45)),('C',(24,41),(18,37),(21,45)),('C',(33,41),(27,37),(30,45)),('C',(42,41),(36,37),(39,45))])
for t in ['left','right']:
    for b in ['bridge-top','bridge-bottom','waterline']:join(t,b)
'''
# Broader, rounder infinity lobes retain natural source proportions.
a.DESIGNS[9]['code']='''
path('infinity',(24,24),[('C',(14,12),(20,18),(19,12)),('C',(4,24),(8,12),(4,17)),('C',(14,36),(4,31),(8,36)),('C',(34,12),(22,36),(26,12)),('C',(44,24),(40,12),(44,17)),('C',(34,36),(44,31),(40,36)),('C',(28,30),(32,36),(30,33))])
'''
replace(10,"(16,21)","(16,22)")
replace(11,"(27,18),(29,13)","(26,20),(28,15)")
for i in (12,13):
    a.DESIGNS[i]['code']=f'''
path('hull',(24,4),[('C',(31,14),(27,8),(30,11)),('C',(34,24),(33,18),(34,21)),('C',(24,44),(34,32),(28,40)),('C',(17,34),(21,40),(18,37)),('C',(14,24),(15,30),(14,27)),('C',(24,4),(14,16),(20,8))],True)
oval('cockpit',24,25,4,{5 if i==12 else 8})
path('blade-upper',(34,12),[('L',(32,10)),('L',(38,4)),('A',(44,10),5,5,True),('L',(38,16)),('L',(34,12))],True)
path('blade-lower',(14,36),[('L',(16,38)),('L',(10,44)),('A',(4,38),5,5,True),('L',(10,32)),('L',(14,36))],True)
line('shaft-upper',(31,14),(34,12));line('shaft-lower',(17,34),(14,36))
for n in ['upper','lower']:
    join('blade-'+n,'shaft-'+n);join('hull','shaft-'+n)
'''
replace(14,"('C',(21,14),(14,8),(21,8))","('C',(21,14),(14,8.6666666667),(21,8.6666666667))")
replace(14,"('C',(28,10),(21,4),(28,4))","('C',(28,10),(21,4.6666666667),(28,4.6666666667))")
replace(14,"('C',(11,20),(3,19),(7,16))","('C',(11,20),(6,17),(8,17))")
# Put horn above the head with an actual open counter, and broaden the foreleg.
replace(15,"('L',(31,10)),('L',(36,10))","('L',(31,14)),('L',(36,14))")
replace(15,"('C',(38,18),(45,18),(41,18))","('C',(38,20),(44,19),(41,20))")
replace(15,"('L',(37,24)),('L',(42,24)),('L',(42,34)),('L',(38,31)),('L',(37,28))","('L',(36,25)),('L',(44,25)),('L',(44,36)),('L',(38,32)),('L',(36,30))")
replace(15,"path('horn',(32,10),[('C',(34,8),(30,8),(31,8)),('L',(42,8))])","path('horn',(31,14),[('C',(34,8),(27,10),(30,8)),('L',(42,8))])")
a.DESIGNS[16]['code']='''
path('dog',(42,42),[('C',(37,29),(38,38),(37,34)),('C',(31,30),(34,32),(33,33)),('C',(33,23),(29,28),(33,26)),('L',(28,23)),('C',(25,20),(26,23),(25,22)),('L',(25,16)),('L',(31,16)),('C',(35,13),(33,16),(33,13)),('L',(37,13)),('L',(40,6)),('C',(42,14),(42,9),(42,11))])
circle('ball',22,34,3)
path('hand',(6,24),[('C',(13,29),(10,25),(12,27)),('L',(15,32)),('C',(11,34),(16,35),(13,36)),('L',(9,33))])
path('palm',(6,37),[('C',(10,40),(7,39),(8,40)),('L',(14,42))])
'''
replace(17,"circle('therapist-head',15,10,4)","circle('therapist-head',12,10,4)")
replace(17,"(15,22)","(12,22)")
replace(17,"(15,31)","(12,31)")
replace(17,"circle('patient-head',42,32,4)","circle('patient-head',40,32,4)")
replace(17,"(30,32)","(28,32)")
replace(17,"(21,18)","(24,17)")
replace(17,"('L',(16,37)),('L',(25,40))","('L',(20,40)),('L',(29,40))")
# Broad stump; omit the tiny elliptical cut seam that pinches shut at native size.
replace(18,"circle('growth-ring',16,28,4)","circle('growth-ring',16,28,3)")
replace(18,"path('stump',(33,8),[('C',(42,8),(35,11),(39,11))])", "")
replace(18,"join('cut-face','body');join('body','stump')", "join('cut-face','body')")
# Lift landing leg clear of ground and set exact vertical head/body alignment.
replace(19,"(17,17)","(17,20)")
replace(19,"(40,36)","(40,31)")
replace(19,"(31,31)","(31,29)")
replace(19,"(18,34),(10,32)","(17,31),(10,28)")
a.DESIGNS[19]['plan']='Outlined circular radius-4 head at (28,8) with actual torso neck at (28,20): exactly 4 ink units. Split airborne legs and detached ground; natural action proportions preserved.'
selected=[1,2,9,10,11,12,13,14,15,16,17,18,19]
for i in selected:a.write(i,'02')
(a.HERE/'items.json').write_text(json.dumps(a.ITEMS,indent=2))
