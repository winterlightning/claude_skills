from author import write,ROOT,TARGETS
changes={10:[('(34,6),(24,20)','(34,6),(22,22)')],30:[('((22,31,40))','((22,30,40))'),('(22,31,40)','(22,30,40)')],66:[('(10,17),(10,42)','(9,17),(9,42)')],53:[('(26,6),(28,14),(28,24)','(28,6),(30,14),(30,24)')],89:[('(4,20),(4,16)','(4,24),(4,16)')],100:[('(24,14),(24,6),(30,6),(32,12),(28,22)','(22,14),(22,6),(32,6),(34,12),(30,22)')]}
for i,pairs in changes.items():
 path=ROOT/TARGETS[i]['source_path'];s=path.read_text()
 for old,new in pairs:s=s.replace(old,new)
 path.write_text(s)
write(4,'HRECT_L','''
# Shared top endpoints make an intentional connected wordmark, leaving W its natural width.
p('a',(4,40),(4,8),(12,8),(12,40))
l('a-bar',(4,24),(12,24))
link('connect','a','a-bar')
p('w',(12,8),(20,40),(24,20),(28,40),(36,8))
l('d-left',(36,8),(36,40))
a('d-curve',(36,8),(36,40),8,16)
link('connect','a','w')
link('connect','w','d-left')
link('connect','w','d-curve')
link('connect','d-left','d-curve')
''','AWD wordmark: a naturally wide W shares its top endpoints with A and D instead of being squeezed.')
