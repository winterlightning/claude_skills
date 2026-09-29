exec(open('/tmp/meaning_batch_author.py').read().split("if __name__=='__main__':")[0])
# Second attempts preserve all first-draft evidence.
specs[0]['body']='''self.circle('head',38,37,4)
self.add_bezier('torso',(26,37),((22,37),(28,32),(26,28)),((23,23),(6,22),(6,31)))
self.path('bent-leg',(6,31),[('L',(6,37)),('A',(14,37),4,4,False),('L',(18,25))])
self.path('sling',(18,25),[('L',(22,6)),('L',(28,27)),('C',(16,32),(29,33),(21,32))])
self.relate('connect','torso','bent-leg');self.relate('connect','torso','sling');self.relate('connect','bent-leg','sling')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')'''
specs[1]['body']=specs[1]['body'].replace('(34,22)','(34,26)')
specs[2]['body']=specs[2]['body'].replace("(12,24),(20,20),(44,20)","(12,24),(22,24),(26,18),(44,18)").replace('(40,20)','(40,18)').replace('(40,16)','(40,14)')
# Eyepiece separated from stage, smoother compact support.
specs[4]['body']=specs[4]['body'].replace('(44,21),(43,32)','(40,21),(40,32)').replace("(19,27),(16,32)","(19,27),(18,29)")
# Sun rays get deliberate visible separation, body maintains exact 4 px head gap.
specs[5]['body']='''self.add_arc('sun',(6,16),(20,16),radius_x=7,sweep=True)
self.add_line('ray-top',(13,2),(13,3))
self.add_line('ray-left',(3,5),(4,6))
self.add_line('ray-right',(22,5),(23,4))
self.add_line('horizon',(4,22),(20,22))
self.circle('head',35,15,5)
self.path('back',(35,28),[('C',(44,40),(41,28),(44,34)),('L',(37,40))])
self.add_polyline('laptop',(4,29),(24,29),(29,44),(9,44),closed=True)
self.add_dot('logo',(16,36))'''
specs[5]['keyshape']='SQUARE'
for i in (6,16):
 s=specs[i]['body'].replace("11,35,7","11,34,6").replace("38,37,5","39,35,5").replace("(18,37),(33,37)","(17,36),(34,36)")
 s=s.replace("('C',(43,32),(41,29),(43,29))","('C',(44,31),(42,29),(44,29))")
 specs[i]['body']=s
specs[7]['body']=specs[7]['body'].replace("(10,22)","(8,22)").replace("(10,13)","(8,13)")
# Four clean finger levels; remove duplicate overlapping curled-finger line.
specs[8]['body']='''self.path('outline',(23,18),[('C',(24,8),(17,13),(19,8)),('C',(31,12),(27,8),(29,10)),('L',(39,20)),('C',(44,28),(43,24),(44,25)),('L',(44,31)),('A',(35,40),9,9,True),('L',(21,40)),('A',(21,33),4,4,True),('L',(27,33))])
self.path('index',(23,18),[('L',(8,18)),('A',(8,26),4,4,False),('L',(25,26))])
self.path('middle',(18,26),[('A',(18,33),4,4,False),('L',(23,33))])
self.relate('connect','outline','index');self.relate('connect','index','middle');self.relate('connect','middle','outline')'''
# Spots stay in open flank, never on the face/outline.
specs[9]['body']=specs[9]['body'].replace('((16,22),(24,23),(32,19))','((16,23),(24,23))').replace('(3,25),(4,20)','(4,25),(4,20)')
# Move handles onto rim to avoid doubled lines, give steam room.
specs[10]['body']=specs[10]['body'].replace("self.add_line('handle-left',(6,30),(10,30));self.add_line('handle-right',(38,30),(42,30))","").replace(",'handle-left','handle-right'",'').replace('(19,29)','(17,31)').replace('(x,12)','(x,11)')
# True limousine proportion: longer shallow cabin and smaller wheels, preserve full width.
specs[13]['body']='''self.circle('wheel-left',11,34,4);self.circle('wheel-right',37,34,4)
self.path('body',(7,34),[('L',(4,34)),('L',(4,27)),('A',(8,23),4,4,True),('L',(10,23)),('L',(17,15)),('L',(33,15)),('L',(40,23)),('A',(44,27),4,4,True),('L',(44,34)),('L',(41,34))])
self.add_line('sill',(15,34),(33,34));self.add_line('windows',(10,23),(40,23));self.add_line('divider',(25,15),(25,23))
self.relate('connect','body','wheel-left','wheel-right','windows','divider');self.relate('connect','windows','divider');self.relate('connect','sill','wheel-left','wheel-right')'''
# Cuffs use adequate separation between their doubled boundaries; widen true silhouette, documented fit exception.
specs[14]['body']=specs[14]['body'].replace('x,32,5','x,32,4')
# Remove doubled slot to retain a clean dispenser baseline.
specs[15]['body']=specs[15]['body'].replace("self.add_line('slot',(14,21),(34,21))",'').replace("14,21","14,23").replace('34,21','34,23').replace(",'slot'",'')
specs[17]['body']=specs[17]['body'].replace('10,36,6','10,34,6').replace('34,36,6','34,34,6').replace('(16,38),(28,38)','(16,35),(28,35)')
# Slightly airier packing keeps six distinct openings.
specs[18]['body']=specs[18]['body'].replace('r=6','r=5').replace('(24,14),(16,25),(32,25),(10,36),(24,36),(38,36)','(24,13),(16,25),(32,25),(8,37),(24,37),(40,37)')
results=[]
for i in range(20):
 if i in (3,11,12,19):
  results.append(json.loads((B/'drafts.json').read_text())[i]);continue
 run,module,md=author(i,2);results.append(export(run,module,md))
(B/'refined.json').write_text(json.dumps(results,indent=2))
