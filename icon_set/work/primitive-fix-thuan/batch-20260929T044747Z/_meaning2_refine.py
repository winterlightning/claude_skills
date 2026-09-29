exec(open('/tmp/meaning2_author.py').read().rsplit("if __name__=='__main__':",1)[0])
specs[1]['body']=specs[1]['body'].replace("(18,33)","(20,33)").replace("(18,32)","(20,32)").replace("(18,30),(21,29)","(20,30),(22,29)").replace("(30,32)","(28,32)").replace("(27,29),(30,30)","(26,29),(28,30)").replace("(30,33)","(28,33)")
# Separate the ribbon from the head while keeping a two-crest wave.
specs[2]['body']=specs[2]['body'].replace("('C',(21,9),(20,7),(19,9))","")
specs[6]['body']='''self.path('head',(10,44),[('L',(10,36)),('C',(6,22),(10,32),(6,30)),('C',(23,4),(6,11),(13,4)),('C',(38,20),(33,4),(38,10)),('L',(42,26)),('L',(36,26)),('L',(36,34)),('A',(32,38),4,4,True),('L',(25,38)),('L',(25,44))])
self.path('brain',(18,25),[('C',(15,18),(11,25),(12,20)),('C',(21,13),(13,12),(17,10)),('C',(29,15),(22,8),(30,10)),('C',(29,23),(35,15),(35,22)),('C',(21,24),(28,29),(23,28)),('C',(18,25),(20,25),(19,26))],True)
self.path('fold',(21,13),[('L',(21,17)),('C',(18,20),(21,20),(20,20))])
self.add_line('brainstem',(29,23),(29,29));self.relate('connect','brain','fold','brainstem')'''
# Clear planet circle and orbital sweep: no ring endpoint protrudes into globe.
specs[7]['body']='''self.circle('planet',21,28,14)
self.path('ring',(7,30),[('C',(4,36),(2,32),(2,35)),('C',(42,24),(17,39),(43,29)),('C',(34,21),(46,19),(39,19))])
self.path('star',(38,5),[('C',(43,10),(38,8),(40,10)),('C',(38,15),(40,10),(38,12)),('C',(33,10),(38,12),(36,10)),('C',(38,5),(36,10),(38,8))],True)
self.relate('connect','planet','ring')'''
specs[11]['body']=specs[11]['body'].replace("self.add_polyline('threat-brow-left',(10,10),(12,11));self.add_polyline('threat-brow-right',(16,10),(14,11))",'')
specs[11]['comparison']='Rejected sticks and trapezoid do not communicate robbery. Restore two distinct people and an unmistakable knife directed toward the victim.'
specs[12]['body']='''self.circle('sample',24,11,6)
self.path('jaw-left',(18,17),[('C',(10,24),(12,18),(10,20)),('C',(18,31),(10,28),(13,31)),('L',(18,25)),('L',(20,23))])
self.path('jaw-right',(30,17),[('C',(38,24),(36,18),(38,20)),('C',(30,31),(38,28),(35,31)),('L',(30,25)),('L',(28,23))])
self.path('wrist',(18,28),[('L',(30,28)),('L',(30,38)),('A',(18,38),6,6,True),('L',(18,28))],True)
self.add_line('feed-top',(8,4),(18,5));self.add_line('feed-bottom',(8,11),(12,12))
self.relate('connect','sample','jaw-left','jaw-right');self.relate('connect','wrist','jaw-left','jaw-right')'''
# Rocket departing: separate rocket, flame and clean round planet/trail.
specs[15]['body']='''self.path('planet',(27,16),[('C',(7,23),(18,10),(8,15)),('C',(20,42),(3,33),(10,42)),('C',(34,27),(30,42),(38,35))])
self.path('rocket',(31,13),[('C',(42,6),(34,8),(38,7)),('C',(37,20),(42,12),(40,17)),('L',(34,23)),('L',(27,16)),('L',(31,13))],True)
self.add_polyline('fin',(31,13),(27,12),(26,15));self.relate('connect','rocket','fin')
self.add_line('exhaust',(29,24),(25,28))
self.path('trail',(19,30),[('C',(6,42),(12,39),(4,46)),('C',(7,32),(2,40),(5,34))])
self.relate('connect','planet','trail')'''
specs[16]['body']='''self.path('rocket',(14,20),[('L',(29,7)),('C',(40,4),(34,5),(38,4)),('C',(36,16),(40,8),(38,13)),('L',(23,28)),('L',(14,20))],True)
self.add_polyline('fin-left',(20,15),(13,15),(8,20),(15,23))
self.add_polyline('fin-right',(29,22),(29,27),(25,31),(23,28))
self.add_line('nose-seam',(30,7),(37,14));self.relate('connect','rocket','fin-left','fin-right','nose-seam')
self.circle('globe',35,37,7)
self.path('continent',(35,30),[('C',(35,37),(29,33),(41,34)),('C',(34,44),(31,40),(36,42))]);self.relate('connect','globe','continent')
self.add_line('exhaust-a',(12,28),(6,34));self.add_line('exhaust-b',(17,33),(12,38))'''
# Shorter upper fins keep two falling rockets separate and their body openings visible.
specs[17]['body']=specs[17]['body'].replace("('left',14,19),('right',34,15)","('left',13,19),('right',35,15)").replace('x-10','x-8').replace('x+10','x+8').replace('x-7','x-6').replace('x+7','x+6')
for i in (18,19):
 specs[i]['body']=specs[i]['body'].replace("self.path('rocker',(6,36),[('C',(42,36),(16,44),(32,44)),('A',(44,42),3,3,True),('C',(4,42),(32,49),(16,49)),('A',(6,36),3,3,True)],True)","self.add_bezier('rocker',(4,36),((14,46),(34,46),(44,36)))")
xs=json.loads((B/'drafts.json').read_text())
for i in (1,2,6,7,11,12,15,16,17,18,19):
 run,module,md=author(i,2);xs[i]=export(run,module,md)
(B/'refined.json').write_text(json.dumps(xs,indent=2))
