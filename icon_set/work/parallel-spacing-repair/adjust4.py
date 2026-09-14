from author import write,ROOT,TARGETS
for i in (35,36):
 write(i,'HRECT_L','''
r('body',4,16,44,30,7)
for x in (12,36):
    l(f'rotor-{x}',(x-8,8),(x+8,8))
    l(f'arm-{x}',(x,8),(x,16))
    link('connect',f'arm-{x}',f'rotor-{x}')
    link('connect',f'arm-{x}','body')
p('landing-left',(14,30),(10,40),(14,40))
p('landing-right',(34,30),(38,40),(34,40))
link('connect','landing-left','body')
link('connect','landing-right','body')
''','Drone: tangent capsule body, equal rotors and clean landing struts joined at exact endpoints.')
write(38,'SQUARE','''
p('cube',(24,14),(34,20),(34,30),(24,36),(14,30),(14,20),(24,14))
p('edges',(14,20),(24,26),(34,20))
l('vertical',(24,26),(24,36))
link('connect','cube','edges')
link('connect','cube','vertical')
link('connect','edges','vertical')
p('outer-left',(12,38),(6,34),(6,14),(18,6))
p('outer-right',(42,14),(42,34),(30,42))
''','MediaConnect: spacious regular cube faces and open outer brackets, avoiding forced compression.')
write(91,'HRECT_L','''
# full_body_ref.png: circular head; bottom 27 to shoulder top 35 gives exactly 4 ink units.
p('house',(4,40),(4,20),(24,8),(44,20),(44,40))
c('head',24,23,4)
a('shoulders',(14,40),(34,40),10,5)
p('laptop',(4,30),(12,30),(14,40))
link('connect','laptop','house')
link('connect','laptop','shoulders')
''','Home-office user: balanced roof, round head, exact 4-unit shoulder gap and a clear open laptop.')
path=ROOT/TARGETS[107]['source_path'];s=path.read_text().replace('(x,28)','(x,24)').replace('(x-4,28)','(x-4,24)').replace('(x+4,28)','(x+4,24)');path.write_text(s)
