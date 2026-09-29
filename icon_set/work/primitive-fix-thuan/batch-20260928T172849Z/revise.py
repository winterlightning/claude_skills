from author_batch import *
DESIGNS[1]=('VRECT_L','A flowing veil with a circular face, touching broad shoulders and a central robe seam.','human_ref/user.svg and Lucide user-round: circle and broad shoulder arcs', '''
path('veil',(8,44),[('L',(8,20)),('A',(40,20),16,16,True),('L',(40,44))])
circle('face',24,20,8)
path('shoulders',(8,44),[('A',(24,32),16,12,True),('A',(40,44),16,12,True)])
line('robe',(24,32),(24,44));join('robe','shoulders');join('veil','shoulders');join('face','shoulders')
''')
s,p,r,b=DESIGNS[10];DESIGNS[10]=(s,p,r,'''
path('body',(4,26),[('C',(14,27),(4,32),(11,32)),('C',(12,20),(14,25),(12,24)),('A',(36,20),12,12,True),('C',(34,27),(36,24),(34,25)),('C',(44,26),(37,32),(44,32))])
path('left-arm',(19,34),[('C',(8,40),(17,38),(14,40))])
path('right-arm',(29,34),[('C',(40,40),(31,38),(34,40))])
''')
s,p,r,b=DESIGNS[13];DESIGNS[13]=(s,p,r,'''
path('circle',(34,20),[('A',(20,6),14,14,False),('A',(6,20),14,14,False),('A',(20,34),14,14,False)])
poly('square',(20,34),(20,20),(34,20),(42,20),(42,42),(20,42),(20,34),closed=True);join('circle','square')
''')
s,p,r,b=DESIGNS[17];DESIGNS[17]=(s,p,r,b.replace('(19,29),(19,32)','(19,30),(19,31)').replace('(29,29),(29,32)','(29,30),(29,31)'))
s,p,r,b=DESIGNS[19];DESIGNS[19]=(s,p,r,'''
poly('outer',(4,40),(14,22),(20,29),(30,8),(44,40),(28,40),closed=True)
line('ridge',(20,29),(28,40));join('outer','ridge')
''')
for n in [1,10,12,13,17,19]:
 run,module=author(n,2)
 if n==12:
  icon=load_icon(module)
  exc={'reason':'User-authorized visual exception: exact diagonal circular cap extends 0.0711 units beyond the square envelope. The smooth symmetric cap and parallel barrel remain crisp at 48px; all strokes are 4 units.','approved_by':'user','approved_on':'2026-09-29','svg_sha256':hashlib.sha256(icon.to_svg().encode()).hexdigest()}
  code=module.read_text().replace("    semantic_role='MAIN'",'    exception='+repr(exc)+"\n    semantic_role='MAIN'")
  module.write_text(code)
 inspect(run,module)
