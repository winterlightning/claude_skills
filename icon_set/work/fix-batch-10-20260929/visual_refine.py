from author import make
make(13,'VRECT_L','The rejected metal detector reduced the person to a ring over a cup. Restore a complete standing person with shoulders, torso and two legs inside a smooth portal. Omit the small top control and beep rays to give the person enough room.', '''
line('wall-left',(8,44),(8,10));line('wall-right',(40,10),(40,44))
path('arch',(8,10),[('A',(14,4),6,6,True),('L',(34,4)),('A',(40,10),6,6,True)])
join('arch','wall-left');join('arch','wall-right')
circle('head',24,18,4)
line('torso',(24,30),(24,38))
poly('arms',(16,30),(24,30),(32,30));join('torso','arms')
poly('legs',(18,44),(24,38),(30,44));join('torso','legs')
self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''','human_ref/full_body_ref.png: complete stick figure and circular head; head bottom22 to shoulder30 gives exact4 ink gap.')
make(16,'CIRCLE','The rejected infinity had very tall narrow loops. Restore broad horizontal mirrored bowls and a smooth central crossover, using the radial envelope to preserve its natural proportions.', '''
path('infinity',(24,24),[('C',(13,14),(19,19),(18,14)),('C',(4,24),(7,14),(4,18)),('C',(13,34),(4,30),(7,34)),('C',(24,24),(18,34),(19,29)),('C',(35,14),(29,19),(30,14)),('C',(44,24),(41,14),(44,18)),('C',(35,34),(44,30),(41,34)),('C',(24,24),(30,34),(29,29))],True)
''','Original infinity; mirrored horizontal bowls and tangent-continuous crossover. CIRCLE radial envelope preserves horizontal form.')
make(17,'HRECT_M','The rejected gamepad had no controls and vibration bars above and below. Restore a central direction pad, rounded paired grips and vibration marks beside the controller.', '''
path('body',(17,12),[('L',(31,12)),('C',(36,18),(35,12),(36,15)),('L',(36,31)),('A',(30,37),6,6,True),('C',(24,34),(27,37),(28,34)),('C',(18,37),(20,34),(21,37)),('A',(12,31),6,6,True),('L',(12,18)),('C',(17,12),(12,15),(13,12))],True)
poly('pad-h',(21,23),(24,23),(27,23));poly('pad-v',(24,21),(24,23),(24,25));join('pad-h','pad-v')
line('buzz-left',(4,10),(4,38));line('buzz-right',(44,10),(44,38))
''','Lucide gamepad-2 rounded grips and crossed pad; source side vibration marks. One central pad preserves space at native size.')
