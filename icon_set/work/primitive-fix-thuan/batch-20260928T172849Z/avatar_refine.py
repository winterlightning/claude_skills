from author_batch import *
DESIGNS[1]=('VRECT_L','Flowing headcloth joins broad shoulders at shared points; circular face touches the shoulder top with zero ink gap.','human_ref/user.svg and Lucide user-round: face and shoulder proportions', '''
path('veil',(12,35),[('C',(8,20),(12,30),(8,26)),('A',(40,20),16,16,True),('C',(36,35),(40,26),(36,30))])
circle('face',24,20,8)
path('shoulders',(8,44),[('C',(12,35),(8,40),(8,37)),('C',(24,32),(16,32),(18,32)),('C',(36,35),(30,32),(32,32)),('C',(40,44),(40,37),(40,40))])
line('robe',(24,32),(24,44));join('robe','shoulders');join('veil','shoulders');join('face','shoulders')
''')
run,module=author(1,3);inspect(run,module)
