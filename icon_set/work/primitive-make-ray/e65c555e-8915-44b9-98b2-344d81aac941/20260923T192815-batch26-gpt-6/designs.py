"""Fresh SOLO48 plans for batch 26; identifiers are retained in every output module."""
SOURCE_ICON_ID='e65c555e-8915-44b9-98b2-344d81aac941'
SOURCE_PATH='icon_set/work/todo-references/mobile phone headphone_e65c555e-8915-44b9-98b2-344d81aac941.svg'
AUTHOR='gpt-6'
PHONE='''
        # Plan: rounded upright phone and lower band; content owns its own geometry.
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')
'''
CONTENTS=[
('headphones','Earcups and headband retained; small corner fillets reduced.', '''
        # Bilateral headband and matched rectangular earcups.
        self.add_arc('headband',(17,20),(31,20),radius_x=7)
        self.add_polyline('ear-left',(17,20),(21,20),(21,28),(17,28),closed=True)
        self.add_polyline('ear-right',(27,20),(31,20),(31,28),(27,28),closed=True)
        self.relate('connect','headband','ear-left')
        self.relate('connect','headband','ear-right')
'''),
('house','None: plain roof-and-wall silhouette retained.', '''
        # Single mirrored house contour, with no door in the reference.
        self.add_polyline('house',(17,28),(17,20),(24,13),(31,20),(31,28),closed=True)
'''),
('lock','None: closed shackle and lock body retained.', '''
        # Rounded body and tangent shackle, with exact shared attachment endpoints.
        self.rect('lock-body',18,20,12,8)
        self.add_line('shackle-left',(20,20),(20,17))
        self.add_arc('shackle-top',(20,17),(28,17),radius_x=4)
        self.add_line('shackle-right',(28,17),(28,20))
        self.add_contour('shackle','shackle-left','shackle-top','shackle-right')
        self.relate('connect','shackle','lock-body')
'''),
('moon','None: left-facing crescent retained.', '''
        # Closed crescent; intentional asymmetry is the moon phase.
        self.add_bezier('crescent',(28,13),((14,12),(14,29),(28,28)),((21,24),(21,17),(28,13)))
        self.add_contour('moon','crescent',closed=True)
'''),
('smartphone','Round note head substitutes for the small tilted oval; stem and flag retained.', '''
        # One note head, upright stem, and a flowing flag.
        self.circle('note-head',20,25,3)
        self.add_line('note-stem',(23,25),(23,13))
        self.add_bezier('flag',(23,13),((24,17),(31,16),(28,23)))
        self.relate('connect','note-head','note-stem')
        self.relate('connect','note-stem','flag')
'''),
('smartphone','Handset corner fillets simplified; both terminal pads retained.', '''
        # Curved handset with deliberately unequal terminal orientations.
        self.add_bezier('handset',(17,14),((11,18),(26,33),(31,27)))
        self.add_polyline('terminal-right',(31,27),(28,23),(24,26))
        self.add_bezier('handset-inner',(24,26),((21,24),(20,23),(19,20)))
        self.add_polyline('terminal-left',(19,20),(22,17),(19,13),(17,14))
        self.add_contour('receiver','handset','terminal-right-1','terminal-right-2','handset-inner','terminal-left-1','terminal-left-2','terminal-left-3',closed=True)
'''),
('map-pin','Microscopic central source point omitted; pin silhouette retained.', '''
        # Rounded pin crown tapers smoothly to the centered point.
        self.add_arc('pin-crown',(17,20),(31,20),radius_x=7)
        self.add_bezier('pin-tip',(31,20),((31,23),(27,27),(24,29)),((21,27),(17,23),(17,20)))
        self.add_contour('pin','pin-crown','pin-tip',closed=True)
'''),
('smartphone','None: source takeoff-plane gesture retained as three coherent strokes.', '''
        # Source is a minimal side-profile aircraft, intentionally diagonal.
        self.add_bezier('fuselage',(16,26),((20,30),(22,28),(25,26)),((28,24),(33,22),(32,18)))
        self.add_line('wing',(18,18),(27,24))
        self.relate('connect','fuselage','wing')
'''),
('smartphone','None: pound stem, curved cap, bar and foot retained.', '''
        # Pound sign: cap flows to a stem and leftward foot, crossed once.
        self.add_bezier('pound',(30,16),((29,10),(21,11),(21,18)),((21,24),(23,27),(18,28)))
        self.add_line('foot',(18,28),(31,28))
        self.add_line('bar',(18,21),(27,21))
        self.relate('connect','pound','foot')
        self.relate('connect','pound','bar')
'''),
('smartphone','Microscopic center mark omitted; circular record symbol retained.', '''
        self.circle('record',24,20,7)
'''),
('smartphone','Eyes enlarged to profile-width dots; skull dome and three lower strokes retained.', '''
        # Bilateral skull dome, cheek transitions and open jaw strokes.
        self.add_arc('skull-top',(17,20),(31,20),radius_x=7)
        self.add_bezier('cheek-right',(31,20),((31,24),(28,24),(28,26)))
        self.add_line('jaw-right',(28,26),(28,29))
        self.add_bezier('cheek-left',(20,26),((20,24),(17,24),(17,20)))
        self.add_line('jaw-left',(20,29),(20,26))
        self.add_line('jaw-center',(24,27),(24,29))
        self.add_contour('skull','jaw-left','cheek-left','skull-top','cheek-right','jaw-right')
        for x in (21,27):self.add_dot('eye-'+str(x),(x,20))
'''),
('lock','None: open shackle and rectangular lock body retained.', '''
        self.rect('lock-body',18,21,12,8)
        self.add_line('shackle-stem',(20,21),(20,17))
        self.add_arc('shackle-cap',(20,17),(28,17),radius_x=4)
        self.add_contour('open-shackle','shackle-stem','shackle-cap')
        self.relate('connect','open-shackle','lock-body')
'''),
('human_ref/user.svg','Small hair strands reduced; head, hair, collar and shoulders retained.', '''
        # Human reference: icon_set/references/human_ref/user.svg.
        # Detached head lower centerline y=23; shoulders begin y=31: exact ink gap 4.
        self.circle('head',24,19,4)
        self.add_bezier('hair',(18,25),((21,21),(15,13),(24,13)),((33,13),(27,21),(30,25)))
        self.add_bezier('shoulders',(16,36),((17,32),(20,31),(21,31)))
        self.add_polyline('collar',(21,31),(24,35),(27,31))
        self.add_bezier('shoulders-right',(27,31),((28,31),(31,32),(32,36)))
        self.relate('connect','shoulders','collar')
        self.relate('connect','shoulders-right','collar')
        self.relate('connect','shoulders','separator')
        self.relate('connect','shoulders-right','separator')
'''),
('smartphone','None: opposing open wrench jaws and diagonal shaft retained.', '''
        # Two open semicircular jaws joined by a diagonal shaft.
        self.add_arc('jaw-bottom',(16,26),(22,30),radius_x=4,large_arc=True)
        self.add_arc('jaw-top',(28,13),(32,19),radius_x=4,large_arc=True,sweep=False)
        self.add_line('shaft',(22,24),(27,19))
'''),
('smartphone','None: Y-shaped yuan sign and single source crossbar retained.', '''
        # Symmetric currency sign built around the shared branch junction.
        self.add_polyline('yuan',(17,13),(24,22),(31,13))
        self.add_line('stem',(24,22),(24,29))
        self.add_line('bar',(19,24),(29,24))
        self.relate('connect','yuan','stem')
        self.relate('connect','stem','bar')
'''),
('smartphone','None: empty phone screen and lower band retained.',''),
]
DESIGNS=[]
for m,(ref,omit,body) in zip(ROWS,CONTENTS):
    DESIGNS.append(('VRECT_L','A '+m['concept'].replace('mobile phone ','mobile phone displaying ')+' icon.',ref,omit,PHONE+body))
DESIGNS += [
('VRECT_L','A document contains three square modules below a clipped corner.','none','None: document and all three modules retained.', '''
        # Plan: document envelope; three equal square modules on a 12-unit grid.
        self.add_polyline('document',(8,4),(30,4),(40,14),(40,44),(8,44),closed=True)
        size=8
        for i,(x,y) in enumerate([(20,14),(14,28),(28,28)]):
            self.add_polyline('module-'+str(i),(x,y),(x+size,y),(x+size,y+size),(x,y+size),closed=True)
'''),
('HRECT_L','A perspective toy brick has four top studs and two visible side faces.','toy-brick','Stud sidewall details reduced; four oval tops and perspective faces retained.', '''
        # Plan: diamond top and two faces, with four repeated oval studs.
        self.add_polyline('body',(4,22),(24,12),(44,22),(44,32),(24,40),(4,32),closed=True)
        self.add_polyline('front-edge',(4,22),(24,30),(44,22))
        self.add_line('corner',(24,30),(24,40))
        self.relate('connect','body','front-edge')
        self.relate('connect','front-edge','corner')
        self.relate('connect','body','corner')
        for i,(x,y) in enumerate([(24,11),(13,18),(35,18),(24,24)]):
            self.add_arc(f'stud-{i}-a',(x-4,y),(x+4,y),radius_x=4,radius_y=3)
            self.add_arc(f'stud-{i}-b',(x+4,y),(x-4,y),radius_x=4,radius_y=3)
            self.add_contour('stud-'+str(i),f'stud-{i}-a',f'stud-{i}-b',closed=True)
''')]
