import ast

def revise(i,replacements,plan=None,reason=None,omissions=None):
 r=records[i];run=Path(r['run']);meta=json.loads((run/'candidate.json').read_text());source=Path(r['module']).read_text();tree=ast.parse(source)
 cls=next(n for n in tree.body if isinstance(n,ast.ClassDef));method=next(n for n in cls.body if isinstance(n,ast.FunctionDef) and n.name=='build')
 body='\n'.join(line[8:] for line in source.splitlines()[method.body[0].lineno-1:method.end_lineno])
 for a,b in replacements:
  assert a in body,(i,a);body=body.replace(a,b)
 return author(i,body,next(n.value.attr for n in cls.body if isinstance(n,ast.Assign) and n.targets[0].id=='keyshape'),meta['comparison'],plan or meta['plan'],meta['construction_references'],omissions or meta['omissions'],reason or meta['gate'].get('exception',{}).get('reason'))

author(7,'''
# Circular halo: endpoints are antipodal on r17 about (26,20), keeping every stroke inside the48px canvas.
self.add_arc('halo',(11,12),(41,28),radius_x=17,radius_y=17,sweep=True)
self.circle('head',27,17,5)
self.path('robe-and-arm',(19,44),('L',(22,34)),('L',(13,34)),('A',(9,30),4,4,True),('L',(9,22)),('A',(15,22),3,3,True),('L',(15,30)),('L',(33,30)),('L',(40,44)))
self.add_line('robe-fold',(20,41),(33,30));self.relate('connect','robe-and-arm','robe-fold')
# Head bottom22 to nearest horizontal shoulder at30:8 centerline /4 painted gap.
''','SQUARE','The rejected holy figure became a raised arm over a triangular pedestal and lost the diagonal robe drape. The source shows a detached round head, open halo and flowing robe.',
 'Circular open halo fitted inside the canvas, detached head with exact4px ink gap above shoulders, bent raised arm and long robe with diagonal drape.',
 'human_ref/user.svg and full_body_ref.png: circular head and coherent human construction; supplied source defines halo and drape.',
 'Robe base remains open as in the reference.',
 exception_reason='Halo, arm and robe preserve compact natural spacing and an asymmetric envelope. User authorized visual exception; exact4px detached head gap and48px canvas are maintained.')
revise(8,[("self.path('front-leg',(20,31),('L',(23,37)),('L',(19,44)),('L',(8,44)),('A',(12,40),4,4,True),('L',(16,40)),('L',(18,34)))","self.path('front-leg',(23,34),('L',(18,43)),('L',(9,43)))"),("self.path('rear-leg',(32,31),('L',(36,38)),('L',(32,44)),('L',(25,44)),('A',(29,40),4,4,True),('L',(30,40)),('L',(31,34)))","self.path('rear-leg',(31,34),('L',(35,39)),('L',(31,44)),('L',(25,44)))")],plan='Rounded muzzle and head casing, capsule torso, two clear bent support legs with horizontal feet and an upturned tail; remove crowded duplicate leg outlines.',omissions='Leg outlines reduced to coherent single strokes so both feet remain clear at48px; small body seams omitted.')
revise(11,[("('C',(42,39),(26,31),(26,45))","('C',(43,35),(26,31),(29,39))"),("('support-low',(29,37),(29,44)),",''),("('support-right',(42,39),(42,44))","('support-right',(43,35),(43,44))"),("(27,36),(33,22),(39,36)","(28,32),(33,22),(38,32)")],plan='Two rides remain distinct: rolling coaster track on four open supports and an eight-spoke Ferris wheel with a short tapered stand. Enlarge the gap above the ground to avoid a dark lower-right knot.',omissions='One low track support removed to preserve negative space; tiny wheel cabins omitted as in the original.')
# Separate poison droplet from the head silhouette by shifting it up.
revise(10,[("'poison-drop',(40,14),('C',(35,24),(39,18),(35,20)),('A',(45,24),5,5,False),('C',(40,14),(45,20),(41,18))","'poison-drop',(40,8),('C',(36,17),(39,12),(36,14)),('A',(44,17),4,4,False),('C',(40,8),(44,14),(41,12))")],plan='Curved diagonal dagger, distinct guard and hilt, a fully separate poison droplet at upper right and open-bottom round head at lower right.')
# Circular portrait heads replace the compressed upper ellipse while preserving fan headdresses.
for i in [4,5]:
 revise(i,[("self.path('head',(15,24),('A',(24,18),9,6,True),('A',(33,24),9,6,True),('L',(33,28)),('A',(15,28),9,9,True),('L',(15,24)),closed=True)","self.circle('head',24,27,9)")],plan='Broad scalloped fan headdress with headband above a circular head, paired ears and a V collar; shared x24 axis preserves the reference portrait.')
# Remove the bomb neck's redundant interior overlap by authoring one continuous closed silhouette.
revise(16,[("self.path('bomb',(24,18),('A',(32,27),14,14,True),('A',(18,44),15,15,True),('A',(4,29),14,15,True),('A',(18,15),14,14,True),('L',(21,11)),('L',(29,16)),('L',(26,20)))","self.path('bomb',(26,21),('A',(32,29),14,14,True),('A',(18,44),14,15,True),('A',(4,29),14,15,True),('A',(18,15),14,14,True),('L',(21,11)),('L',(29,16)),('L',(26,21)),closed=True)")])
