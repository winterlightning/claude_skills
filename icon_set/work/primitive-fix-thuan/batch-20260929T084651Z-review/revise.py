from author import *

updates={
1: '''
 # Plan: three concentric rainbow bands, symmetric heart below.
 for i,r in enumerate((18,12,6)):
     s.add_arc(f'rainbow-{i}',(24-r,22),(24+r,22),radius_x=r,sweep=True)
 path(s,'heart',(24,31),('C',(13,34),(18,25),(10,28)),('C',(24,44),(14,37),(20,41)),('C',(35,34),(28,41),(34,37)),('C',(24,31),(38,28),(30,25)),closed=True)
 ''',
5: '''
 # Plan: leaning mast with broad curved sail, shallow board and separate low wave.
 path(s,'sail',(19,4),('C',(7,27),(9,10),(7,17)),('L',(26,22)),('L',(19,4)),closed=True)
 s.add_line('mast',(26,22),(29,32));s.relate('connect','mast','sail')
 s.add_line('boom',(8,20),(29,14));s.relate('connect','boom','sail')
 path(s,'board',(8,34),('L',(42,28)),('C',(29,36),(41,34),(35,36)))
 path(s,'water',(4,44),('C',(14,42),(8,44),(11,44)),('C',(24,44),(17,44),(20,44)),('C',(34,42),(28,44),(31,44)),('C',(44,44),(37,44),(40,44)))
 ''',
6: '''
 # Plan: single bowed sail, shallow hull, visibly detached wave band.
 path(s,'sail',(17,4),('C',(37,23),(28,5),(36,13)),('L',(22,25)),('L',(17,4)),closed=True)
 path(s,'hull',(4,33),('L',(44,33)),('C',(39,38),(43,35),(41,37)))
 path(s,'hull-left',(4,33),('C',(9,38),(5,35),(7,37)));s.relate('connect','hull','hull-left')
 path(s,'water',(5,44),('C',(15,42),(9,45),(12,44)),('C',(25,44),(18,44),(21,45)),('C',(35,42),(29,45),(32,44)),('C',(43,44),(38,44),(41,45)))
 ''',
7: '''
 # Plan: five differently oriented tapered seed ovals; smaller center owns clearance.
 path(s,'seed-a',(14,6),('C',(7,20),(5,11),(3,18)),('C',(18,16),(14,24),(20,22)),('C',(14,6),(18,12),(15,10)),closed=True)
 path(s,'seed-b',(31,6),('C',(30,20),(28,11),(26,18)),('C',(42,17),(35,26),(44,22)),('C',(31,6),(43,12),(36,10)),closed=True)
 path(s,'seed-c',(24,24),('C',(21,30),(21,24),(19,28)),('C',(27,30),(22,34),(26,34)),('C',(24,24),(29,27),(26,26)),closed=True)
 path(s,'seed-d',(9,32),('C',(6,42),(6,34),(2,39)),('C',(17,39),(12,47),(19,44)),('C',(9,32),(17,35),(12,34)),closed=True)
 path(s,'seed-e',(41,32),('C',(34,39),(36,32),(34,35)),('C',(42,42),(36,45),(42,46)),('C',(41,32),(47,38),(45,33)),closed=True)
 ''',
8: '''
 # Plan: single domed hair mass, center part joined at crown; circular jaw and coat.
 path(s,'hair',(7,27),('C',(8,14),(10,22),(8,19)),('C',(24,4),(8,7),(16,4)),('C',(40,14),(32,4),(40,7)),('C',(41,27),(40,19),(38,22)))
 path(s,'part',(12,14),('C',(24,4),(18,14),(24,11)),('C',(36,14),(24,11),(30,14)))
 s.relate('connect','hair','part')
 s.add_arc('jaw',(36,14),(12,14),radius_x=12,sweep=True);s.relate('connect','part','jaw')
 path(s,'shoulders',(6,44),('L',(6,40)),('C',(24,30),(6,34),(16,30)),('C',(42,40),(32,30),(42,34)),('L',(42,44)))
 s.add_polyline('lapels',(17,32),(24,44),(31,32))
 s.human_construction='bust'
 s.relate('connect','jaw','shoulders')
 ''',
10: '''
 # Plan: one seal silhouette with a foreground flipper interrupting the belly line.
 path(s,'outline',(10,10),('C',(23,14),(16,0),(23,6)),('L',(23,21)),('C',(43,35),(35,20),(43,25)),('C',(38,44),(45,40),(42,44)),('L',(32,44)),('L',(36,37)),('L',(32,32)),('C',(23,35),(29,34),(25,35)),('L',(23,36)),('C',(26,44),(23,40),(24,42)),('C',(15,40),(19,44),(17,43)),('C',(8,18),(10,32),(8,25)),('C',(4,14),(3,18),(2,15)),('C',(10,10),(4,12),(7,12)),closed=True)
 path(s,'front-flipper',(18,30),('C',(23,36),(18,33),(20,36)));s.relate('connect','front-flipper','outline')
 path(s,'far-flipper',(12,34),('C',(5,40),(10,37),(7,39)),('L',(15,40)));s.relate('connect','far-flipper','outline')
 s.add_dot('eye',(14,13))
 ''',
12: '''
 # Plan: dragon snout, eye and zigzag mouth; clean crest without crowded subdivisions.
 path(s,'profile',(16,44),('C',(28,29),(16,36),(21,33)),('C',(28,20),(34,25),(32,20)),('L',(24,20)),('C',(18,26),(24,25),(22,26)),('L',(7,26)),('A',(4,23),3,3,True),('L',(4,16)),('A',(8,12),4,4,True),('L',(14,12)),('C',(25,9),(18,7),(20,9)),('C',(40,22),(34,8),(40,15)),('C',(33,36),(42,29),(37,33)),('C',(27,44),(29,39),(27,41)))
 s.add_polyline('mouth',(4,22),(9,19),(14,22));s.relate('connect','mouth','profile')
 s.add_dot('eye',(19,15))
 path(s,'crest',(25,9),('C',(42,9),(30,0),(37,3)),('L',(44,18)),('L',(40,20)));s.relate('connect','crest','profile')
 ''',
13: '''
 # Plan: adult holds the smaller child on their lap; shared knee/lap node is deliberate.
 circle(s,'adult-head',13,9,5)
 s.add_line('adult-torso',(13,22),(13,32))
 s.add_polyline('adult-leg',(13,32),(28,32),(32,44));s.relate('connect','adult-torso','adult-leg')
 path(s,'chair',(5,24),('L',(5,35)),('A',(11,41),6,6,False),('L',(20,41)))
 circle(s,'child-head',28,16,3)
 s.add_line('child-torso',(28,27),(28,32))
 s.add_polyline('child-leg',(28,32),(37,33),(41,40));s.relate('connect','child-torso','child-leg')
 s.relate('connect','adult-leg','child-torso');s.relate('connect','adult-leg','child-leg')
 s.add_polyline('holding-arm',(13,22),(18,28),(28,27));s.relate('connect','adult-torso','holding-arm');s.relate('connect','child-torso','holding-arm')
 s.mark_human_figure('adult',head='adult-head',torso='adult-torso',torso_junction='start')
 s.mark_human_figure('child',head='child-head',torso='child-torso',torso_junction='start')
 ''',
14: '''
 # Plan: right seated angler on stool, curved rod and small suspended fish.
 circle(s,'head',35,10,5)
 s.add_line('torso',(35,23),(35,33))
 s.add_polyline('leg',(35,33),(25,33),(24,44));s.relate('connect','torso','leg')
 s.add_polyline('arm',(35,23),(29,28),(22,23));s.relate('connect','torso','arm')
 path(s,'rod',(22,23),('C',(7,5),(19,12),(13,5)))
 s.add_line('line',(7,5),(7,24));s.relate('connect','line','rod')
 path(s,'fish',(7,24),('C',(7,36),(0,28),(2,33)),('C',(7,24),(12,32),(13,28)),closed=True);s.relate('connect','line','fish')
 s.add_polyline('tail',(3,41),(7,36),(11,41));s.relate('connect','tail','fish')
 s.add_polyline('stool',(35,33),(43,33),(43,44));s.relate('connect','stool','torso');s.relate('connect','stool','leg')
 s.mark_human_figure('angler',head='head',torso='torso',torso_junction='start')
 ''',
15: '''
 # Plan: exact horizontal head/upper-torso alignment, smooth reach and low seated legs.
 circle(s,'head',10,20,5)
 s.add_bezier('torso',(23,20),((32,20),(44,19),(44,30)))
 path(s,'hip-leg',(44,30),('C',(26,41),(44,39),(37,41)),('L',(4,41)));s.relate('connect','torso','hip-leg')
 path(s,'arm',(23,20),('C',(17,33),(22,28),(21,33)),('L',(4,33)));s.relate('connect','arm','torso')
 s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
 ''',
18: '''
 # Plan: laptop rests on desktop; reaching arm connects keyboard; seat joins body.
 circle(s,'head',35,9,5)
 s.add_line('torso',(35,22),(35,36))
 s.add_polyline('arm',(35,22),(30,28),(24,28));s.relate('connect','torso','arm')
 s.add_polyline('leg',(35,36),(25,36),(22,44));s.relate('connect','torso','leg')
 s.add_polyline('laptop',(7,14),(11,28),(24,28));s.relate('connect','arm','laptop')
 s.add_line('desk',(4,28),(11,28));s.relate('connect','laptop','desk')
 s.add_line('desk-leg',(8,28),(8,44));s.relate('connect','desk','desk-leg')
 s.add_polyline('chair',(35,36),(43,36),(43,44));s.relate('connect','chair','torso');s.relate('connect','chair','leg')
 s.mark_human_figure('worker',head='head',torso='torso',torso_junction='start')
 ''',
20: '''
 # Plan: relaxed upright torso, lowered arms and a wide low folded-leg silhouette.
 circle(s,'head',24,9,5)
 s.add_line('torso',(24,22),(24,33))
 path(s,'shoulders',(12,34),('L',(12,30)),('A',(20,22),8,8,True),('L',(28,22)),('A',(36,30),8,8,True),('L',(36,34)));s.relate('connect','torso','shoulders')
 path(s,'leg-front',(12,34),('L',(8,35)),('C',(7,41),(2,35),(2,39)),('L',(38,44)))
 path(s,'leg-back',(36,34),('L',(40,35)),('C',(41,41),(46,35),(46,39)),('L',(10,44)))
 s.relate('connect','shoulders','leg-front');s.relate('connect','shoulders','leg-back')
 s.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
 ''',
}
updates[9]=updates[8]
updates[11]=updates[10]
for i in (3,4):
    updates[i]=DESIGNS[i-1][4].replace("(24,17),(28,17)","(23,17),(27,17)").replace("(23,19),(28,16)","(22,19),(27,16)").replace("(22,32),('C',(29,30),(24,30),(27,29))","(20,33),('C',(26,31),(22,31),(24,30))")
for i,body in updates.items():
    old=DESIGNS[i-1];DESIGNS[i-1]=(*old[:4],body)
author(sorted(updates))
