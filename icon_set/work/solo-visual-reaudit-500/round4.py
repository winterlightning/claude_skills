from humans import *
from dataclasses import replace
for n in [13,89,102,232,425]:
 r=next(r for r in records if r['number']==n);d=create(r['icon_id']).draw();pm={};rp={};heads={};key=None;reason=r['reason']
 if n==13:pm={(16,26):(17,26)}
 if n==89:rp={'person-1':Bezier('person-1',Point(14,24),Point(14,32),(((14,27),(14,30),(14,32)),))}
 if n==102:
  pm={(20,22):(20,20),(6,42):(8,44),(34,40):(32,42),(42,42):(40,44)};heads={'head':(20,8,4)};key='VRECT_L'
  rp={'torso':Bezier('torso',Point(20,20),Point(18,26),(((20,23),(19,25),(18,26)),))}
  reason='Snowboarder on ramp: VRECT_L gives the lifted board a full8-unit separation from the curved ramp. Radius4 head(20,8), shoulder(20,20), exact4 painted gap. Two spread legs preserve the landing stance; the source raised arm remains clear.'
 if n==232:pm={(6,35):(6,36)}
 if n==425:d=replace(d,relationships=tuple(replace(rel,members=tuple('person-arms-1' if m=='person-arms' else m for m in rel.members)) for rel in d.relationships))
 save(n,emit(d,heads,rp,pm),reason,key)
