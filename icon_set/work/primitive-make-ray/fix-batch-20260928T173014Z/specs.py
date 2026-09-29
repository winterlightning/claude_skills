drawings={
1:('HRECT_M','video','Rejected body has kinked corners and is too tall. Restore a smooth rounded camera body and proportional right lens wedge.',"""
        path('camera',(8,10),[('L',(28,10)),('A',(32,14),4,True),('L',(32,22)),('L',(44,16)),('L',(44,32)),('L',(32,26)),('L',(32,34)),('A',(28,38),4,True),('L',(8,38)),('A',(4,34),4,True),('L',(4,14)),('A',(8,10),4,True)],True)
        line('lens-root',(32,22),(32,26));join('lens-root','camera')
"""),
2:('HRECT_M','No exact local Lucide match; arc construction','Rejected lower edge is kinked. Restore a symmetric sector with broad convex top and shallow concave bottom.',"""
        path('sector',(4,16),[('C',(24,10),(10,12),(17,10)),('C',(44,16),(31,10),(38,12)),('L',(34,38)),('C',(14,38),(28,34),(20,34)),('L',(4,16))],True)
"""),
3:('SQUARE','box','Rejected cube is flattened into a layered hexagon. Restore three tall equal isometric faces with clean central Y junction.',"""
        poly('outline',(24,4),(42,14),(42,34),(24,44),(6,34),(6,14),closed=True)
        poly('faces',(6,14),(24,24),(42,14));line('vertical',(24,24),(24,44))
        join('faces','outline');join('vertical','outline');join('vertical','faces')
"""),
4:('SQUARE','hand; file-text','Rejected hand is angular and paper loses its upper edge and text. Restore a curved thumb gripping an outlined document with two legible text strokes.',"""
        path('paper',(16,18),[('L',(8,18)),('A',(4,22),4,False),('L',(4,40)),('A',(8,44),4,False),('L',(28,44)),('L',(28,24))])
        path('hand-top',(44,4),[('L',(36,10)),('L',(26,10)),('C',(16,18),(21,10),(19,14))]);join('hand-top','paper')
        path('thumb',(26,16),[('L',(20,22)),('C',(24,28),(16,26),(20,31)),('L',(28,24)),('L',(32,20)),('L',(38,20)),('L',(44,15))]);join('thumb','paper')
        line('text-one',(10,32),(20,32));line('text-two',(10,38),(20,38))
"""),
5:('HRECT_M','mountain','Rejected hill is too steep. Restore a shallow rising slope and clean rounded triangle corners.',"""
        poly('slope',(4,36),(44,12),(44,36),closed=True)
"""),
6:('SQUARE','human_ref/full_body_ref.png; person-standing','Rejected people collapse into a tangled angular shape. Restore two distinct full-body figures, a visible carried box and a separate pointing arm.',"""
        circle('carrier-head',18,8,3);circle('director-head',36,6,3)
        line('carrier-upper',(18,19),(18,21));line('carrier-lower',(18,21),(18,30));join('carrier-upper','carrier-lower')
        poly('carrier-arm',(18,21),(12,24));join('carrier-arm','carrier-upper');join('carrier-arm','carrier-lower')
        poly('box',(4,24),(12,24),(12,32),(4,32),closed=True);join('box','carrier-arm')
        poly('carrier-legs',(13,44),(18,30),(23,44));join('carrier-legs','carrier-lower')
        line('director-upper',(36,17),(36,19));line('director-middle',(36,19),(36,21));line('director-lower',(36,21),(36,30));join('director-upper','director-middle');join('director-middle','director-lower')
        line('point',(36,19),(25,19));join('point','director-upper');join('point','director-middle')
        line('director-arm',(36,21),(44,28));join('director-arm','director-middle');join('director-arm','director-lower')
        poly('director-legs',(31,44),(36,30),(43,44));join('director-legs','director-lower')
        self.mark_human_figure('carrier',head='carrier-head',torso='carrier-upper',torso_junction='start')
        self.mark_human_figure('director',head='director-head',torso='director-upper',torso_junction='start')
        # 19-(8+3)-4=4 and 17-(6+3)-4=4 visible head/body gaps.
"""),
9:('SQUARE','armchair','Rejected chair lacks a crossbar and its shell has a sharp elbow. Restore a smooth continuous shell with splayed legs and crossbar.',"""
        path('shell',(12,4),[('L',(14,4)),('C',(20,18),(18,4),(18,8)),('C',(30,26),(22,25),(24,26)),('L',(40,26)),('C',(40,32),(44,26),(44,32)),('L',(34,32)),('L',(20,32)),('L',(18,32)),('C',(9,22),(12,32),(10,29)),('L',(7,8)),('C',(12,4),(6,4),(8,4))],True)
        poly('left-leg',(18,32),(14,40),(12,44));poly('right-leg',(34,32),(38,40),(40,44))
        line('crossbar',(14,40),(38,40))
        for n in ('left-leg','right-leg'):join(n,'shell');join(n,'crossbar')
"""),
13:('SQUARE','network; bean','Rejected molecule has a flattened angular upper lobe. Restore three rounded lobes and clean internal Y-shaped boundaries.',"""
        path('lobes',(12,22),[('A',(24,4),13,True),('A',(36,22),13,True),('C',(44,34),(42,24),(44,28)),('C',(24,40),(44,46),(32,46)),('C',(4,34),(16,46),(4,46)),('C',(12,22),(4,28),(6,24))],True)
        poly('y',(12,22),(24,30),(36,22));line('center',(24,30),(24,40));join('y','lobes');join('center','lobes');join('center','y')
"""),
14:('SQUARE','No exact local Lucide match; pen-line curved construction','Rejected razor loses the outlined curved handle. Restore the broad blade, diagonal shank and hollow curved handle.',"""
        poly('blade',(4,10),(7,4),(27,15),(23,22),closed=True)
        line('shank',(27,15),(38,22));join('blade','shank')
        path('handle',(40,18),[('C',(42,22),(42,18),(43,19)),('C',(8,44),(37,34),(23,44)),('C',(8,36),(2,44),(2,36)),('C',(38,22),(22,36),(32,30)),('C',(40,18),(39,20),(39,19))],True);join('shank','handle')
"""),
15:('VRECT_L','file','Rejected page has irregular corners and cramped panel. Restore uniform rounded page corners and a taller two-cell panel; preserve source without adding literal letters.',"""
        path('page',(12,4),[('L',(28,4)),('L',(40,16)),('L',(40,40)),('A',(36,44),4,True),('L',(12,44)),('A',(8,40),4,True),('L',(8,8)),('A',(12,4),4,True)],True)
        path('panel',(19,15),[('L',(27,15)),('A',(30,18),3,True),('L',(30,25)),('L',(30,32)),('A',(27,35),3,True),('L',(19,35)),('A',(16,32),3,True),('L',(16,25)),('L',(16,18)),('A',(19,15),3,True)],True)
        line('divider',(16,25),(30,25));join('divider','panel')
"""),
16:('HRECT_L','signature','Rejected signature crowns are flat and kinked. Restore a tall smooth first arch and smaller second arch, with continuous flowing stroke.',"""
        path('signature',(4,40),[('L',(14,16)),('C',(23,8),(17,10),(20,8)),('C',(27,14),(28,8),(29,9)),('L',(20,32)),('C',(22,38),(18,37),(18,40)),('C',(33,24),(26,36),(29,28)),('C',(40,19),(37,20),(40,16)),('C',(38,31),(40,23),(38,28)),('C',(42,37),(38,35),(38,40)),('C',(44,34),(43,36),(44,35))])
"""),
17:('SQUARE','No exact local Lucide match; bean smooth contours','Rejected stem is short and kinked. Restore a broad domed cap and longer gently curved open stem.',"""
        path('cap',(4,24),[('E',(24,8),20,16,True),('E',(44,24),20,16,True),('L',(28,24)),('L',(20,24)),('L',(4,24))],True)
        path('stem',(20,24),[('C',(17,39),(20,30),(19,35)),('C',(22,44),(16,42),(18,44)),('C',(29,38),(29,44),(29,43)),('L',(28,24))]);join('cap','stem')
"""),
18:('SQUARE','No exact local Lucide match; mountain rounded silhouette','Rejected cap has a flattened top and angular shoulders. Restore a gently rounded triangular cap and a flared stem.',"""
        path('cap',(4,28),[('L',(18,8)),('C',(24,4),(20,5),(22,4)),('C',(30,8),(26,4),(28,5)),('L',(44,28)),('C',(40,32),(44,31),(43,32)),('L',(28,32)),('L',(20,32)),('L',(8,32)),('C',(4,28),(5,32),(4,31))],True)
        path('stem',(20,32),[('L',(19,41)),('C',(29,41),(18,45),(30,45)),('L',(28,32))]);join('stem','cap')
"""),
19:('HRECT_M','mountain','Rejected hill is too steep. Restore the source shallow falling slope with clean rounded triangle corners.',"""
        poly('slope',(4,12),(44,36),(4,36),closed=True)
"""),
20:('VRECT_L','brain; human profile reference','Rejected skull is kinked and mouth reads as a blob. Restore a circular cranium, open neck, slanted angry brow and attached curved mouth.',"""
        path('profile',(14,44),[('L',(14,34)),('C',(6,20),(8,30),(6,25)),('A',(22,4),16,True),('A',(38,20),16,True),('L',(42,28)),('L',(36,28)),('L',(36,33)),('A',(28,41),8,True),('L',(28,44))])
        path('mouth',(36,33),[('C',(25,35),(30,32),(27,33))]);join('mouth','profile')
        line('brow',(25,16),(31,19))
"""),
}
for i,seated,kind in [(7,False,'desktop'),(8,False,'writing'),(10,True,'desktop'),(11,True,'laptop'),(12,True,'writing')]:
    x=34 if seated else 36;edge=18 if seated else 24
    body=f"""
        circle('head',{x},8,4)
        line('torso-upper',({x},20),({x},23));line('torso-lower',({x},23),({x},32));join('torso-upper','torso-lower')
        self.mark_human_figure('worker',head='head',torso='torso-upper',torso_junction='start')
        # 20-(8+4)-4=4px visible head-to-body gap, head and upper torso aligned.
"""
    if seated:
        body+="""
        poly('leg',(34,32),(28,32),(24,44));join('leg','torso-lower')
        path('chair',(34,32),[('L',(36,32)),('L',(38,32)),('C',(44,25),(42,32),(44,29)),('L',(44,20))]);join('chair','leg');join('chair','torso-lower')
        line('chair-stem',(36,32),(36,44));join('chair-stem','chair')
        poly('chair-base',(30,44),(36,44),(42,44));join('chair-base','chair-stem')
"""
    else:
        body+="""
        poly('legs',(32,44),(36,32),(42,44));join('legs','torso-lower')
"""
    body+=f"""
        poly('desk',(4,30),(6,30),(18,30),({edge},30),({edge},44),(4,44),closed=True)
""" if edge!=18 else """
        poly('desk',(4,30),(6,30),(18,30),(18,44),(4,44),closed=True)
"""
    if kind=='desktop':
        body+=f"""
        poly('arm',({x},23),(28,27),(22,27),({edge},30));join('arm','torso-upper');join('arm','torso-lower');join('arm','desk')
        poly('monitor',(8,4),(12,16),(14,22))
        path('monitor-stand',(12,16),[('C',(6,30),(7,16),(6,20))]);join('monitor-stand','monitor');join('monitor-stand','desk')
"""
    elif kind=='writing':
        body+=f"""
        poly('arm',({x},23),(28,26),(20,24));join('arm','torso-upper');join('arm','torso-lower')
        poly('pen',(22,18),(20,24),(18,30));join('pen','arm');join('pen','desk')
        line('text-one',(4,8),(12,8));line('text-two',(4,16),(12,16))
"""
    else:
        body+="""
        poly('laptop',(4,12),(8,24),(20,24))
        poly('arm',(34,23),(28,24),(20,24));join('arm','laptop');join('arm','torso-upper');join('arm','torso-lower')
"""
    note='Rejected worker loses furniture outlines and has an oversized ring head. Restore '+('seated pose with chair back, pedestal and ' if seated else 'standing pose and ')+('side-view desktop monitor' if kind=='desktop' else 'laptop' if kind=='laptop' else 'pen and two document marks')+' over a complete desk. Keep aligned circular head and exactly 4px detached head/body gap.'
    drawings[i]=('SQUARE','human_ref/full_body_ref.png; '+('monitor' if kind=='desktop' else 'laptop' if kind=='laptop' else 'pen-line'),note,body)
