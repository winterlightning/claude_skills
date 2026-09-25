"""Fresh, reference-led SOLO48 revisions; writes only this batch's work folders."""
import json
from pathlib import Path

AUTHOR = 'gpt-6'
ROOT = Path(__file__).resolve().parents[3]
BATCH = Path(__file__).resolve().parent
ROWS = json.loads((BATCH / 'config.json').read_text())

HELPERS = '''
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            eid=f'{n}-{i}'; kind,end,*args=c
            if kind=='L' and here==end: continue
            if kind=='L': self.add_line(eid,here,end)
            elif kind=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)
    def phone(self):
        self.box('phone',8,4,40,44,4)
        self.add_line('phone-band',(8,36),(40,36))
    def calendar(self,wide=False):
        l,t,r,b,bind,divider=(6,10,42,42,6,18) if wide else (8,8,40,44,4,16)
        self.box('calendar',l,t,r,b,4)
        self.add_line('divider',(l,divider),(r,divider))
        for x in (16,32): self.add_line(f'binding-{x}',(x,bind),(x,t))
    def dollar(self,x=24,y=24):
        self.path('dollar',(x+4,y-5),[('C',(x,y-6),(x+3,y-6),(x+1,y-6)),('C',(x,y),(x-8,y-6),(x-8,y-1)),('C',(x,y+6),(x+8,y+1),(x+8,y+6)),('C',(x-4,y+5),(x-1,y+6),(x-3,y+6))])
        self.add_line('dollar-top',(x,y-8),(x,y-6))
        self.add_line('dollar-bottom',(x,y+6),(x,y+8))
    def cross(self,n,x,y,r):
        for j,(dx,dy) in enumerate(((-r,0),(r,0),(0,-r),(0,r))):self.add_line(f'{n}-{j}',(x,y),(x+dx,y+dy))
    def handset(self,x=24,y=23):
        self.path('handset',(x-3,y-5),[('L',(x-6,y-6)),('L',(x-7,y-6)),('C',(x+4,y+5),(x-7,y),(x-1,y+5)),('L',(x+7,y+2)),('L',(x+4,y-1))])
    def contacts(self):
        # Split only actual straight attachment nodes; connect exact shared endpoints.
        from icon_set.model.primitives import Line
        from dataclasses import replace
        points={p.start for p in self.primitives}|{p.end for p in self.primitives}
        changes={}; fresh=[]
        for p in self.primitives:
            if isinstance(p,Line) and p.start!=p.end:
                a,b=p.start,p.end;dx,dy=b.x-a.x,b.y-a.y
                cuts=[q for q in points if q not in (a,b) and (q.x-a.x)*dy==(q.y-a.y)*dx and 0<(q.x-a.x)*dx+(q.y-a.y)*dy<dx*dx+dy*dy]
                if cuts:
                    nodes=[a]+sorted(cuts,key=lambda q:(q.x-a.x)*dx+(q.y-a.y)*dy)+[b]; ids=[]
                    for j,(u,v) in enumerate(zip(nodes,nodes[1:])):
                        name=f'{p.element_id}-join-{j}'; fresh.append(Line(name,u,v));ids.append(name)
                    changes[p.element_id]=ids;continue
            fresh.append(p)
        self.primitives[:]=fresh
        self.contours[:]=[replace(c,members=tuple(k for m in c.members for k in changes.get(m,[m]))) for c in self.contours]
        for j,a in enumerate(self.primitives):
            for b in self.primitives[j+1:]:
                if {a.start,a.end}&{b.start,b.end}:self.relate('connect',a.element_id,b.element_id)
'''

DESIGNS = {}
def design(i,key,plan,code,refs,omissions='None.'):
    DESIGNS[i]=(key,plan,code,refs,omissions)

avatar='''
        # Shared human vocabulary: radius8 circular jaw; bottom28, shoulders36 => 4u ink gap.
        self.path('fringe',(16,20),[('C',(24,13),(20,19),(23,16)),('C',(32,20),(25,16),(28,19))])
        self.path('jaw',(32,20),[('A',(24,28),8,8,True),('A',(16,20),8,8,True)])
        self.path('shoulders',(8,44),[('A',(16,36),8,8,True),('L',(32,36)),('A',(40,44),8,8,True)])
'''
for i,label,end in [(1,'long straight',30),(22,'side-parted bob',27),(32,'short bob',26),(36,'long center-parted',30)]:
    fringe=avatar
    if i==22:fringe=fringe.replace("('C',(24,13),(20,19),(23,16)),('C',(32,20),(25,16),(28,19))", "('C',(27,14),(21,19),(25,17)),('C',(32,20),(28,17),(30,19))")
    hair=f"        self.path('hair',(8,{end}),[('L',(8,20)),('A',(24,4),16,16,True),('A',(40,20),16,16,True),('L',(40,{end}))])\n"

    design(i,'VRECT_L',f'Expand the circular face and preserve {label} hair; coherent circular jaw and broad shoulders.',hair+fringe,['human_ref/user.svg'], 'Neck seams and shirt collar omitted to protect the exact detached face-to-body gap; hairstyle retained.')

design(3,'VRECT_L','Separate rounded square dial and trapezoid straps; longer yuan stem and clear fork.', '''
        self.box('dial',8,10,40,38,4)
        self.add_polyline('strap-top',(16,10),(18,4),(30,4),(32,10))
        self.add_polyline('strap-bottom',(16,38),(18,44),(30,44),(32,38))
        self.add_polyline('yuan',(18,18),(24,25),(30,18))
        self.add_line('yuan-stem',(24,25),(24,31))
        self.add_polyline('yuan-bar',(20,27),(24,27),(28,27))
''',['watch'])
design(4,'SQUARE','Rounded calendar with taller rising check; equal top binding strokes.', '''
        self.calendar(wide=True)
        self.add_polyline('check',(16,29),(21,33),(32,26))
''',['calendar-check'])
design(5,'VRECT_L','Tall calendar gives the checkmark a full diagonal ascent rather than a flattened chevron.', '''
        self.calendar()
        self.add_polyline('check',(16,30),(22,35),(31,26))
''',['calendar-check'])
design(6,'VRECT_L','Circular head with gently bowed skullcap seam; detached head gap exactly4 ink units.', '''
        self.circle('head',24,14,10)
        self.path('cap',(14,14),[('C',(34,14),(20,16),(28,16))])
        self.path('shoulders',(8,44),[('A',(20,32),12,12,True),('L',(28,32)),('A',(40,44),12,12,True)])
''',['human_ref/user.svg'])
design(10,'CIRCLE','Circular bitcoin coin with two generous B counters, aligned stem and twin currency bars.', '''
        self.circle('coin',24,24,20)
        self.path('b',(18,15),[('L',(26,15)),('C',(26,24),(33,15),(33,24)),('C',(26,33),(34,24),(34,33)),('L',(18,33)),('L',(18,24)),('L',(18,15))],True)
        self.add_line('b-middle',(18,24),(26,24))
        for x in (18,26):
            self.add_line(f'upper-bar-{x}',(x,14),(x,15))
            self.add_line(f'lower-bar-{x}',(x,33),(x,34))
''',[], 'No omitted defining features; narrow currency bars are reported if they cannot meet spacing.')
design(11,'VRECT_L','Rounded phone, restored bottom band, and recognizable sterling hook and baseline.', '''
        self.phone()
        self.path('pound',(29,17),[('A',(21,17),4,4,False),('L',(21,20)),('L',(21,25)),('C',(18,28),(21,27),(20,28))])
        self.add_polyline('pound-cross',(17,20),(21,20),(28,20))
        self.add_polyline('pound-base',(17,28),(18,28),(31,28))
''',['smartphone'])
design(12,'HRECT_M','Open robotic hand in side profile: coherent palm, bent thumb and extended finger; no crossed wrist.', '''
        self.path('hand',(4,16),[('C',(17,10),(10,16),(12,10)),('C',(29,15),(22,10),(26,12)),('C',(32,23),(32,17),(33,20)),('L',(39,19)),('C',(44,22),(42,16),(44,18)),('C',(41,29),(44,25),(44,26)),('L',(33,36)),('C',(26,38),(31,38),(29,38)),('C',(12,33),(20,38),(18,33)),('L',(4,33))])
        self.path('thumb-fold',(32,23),[('C',(23,21),(29,24),(26,22))])
''',['hand'], 'Mechanical panel seams omitted; the palm, wrist, thumb and extended finger remain.')
design(13,'VRECT_L','Phone security key has an open circular bow, diagonal shaft and one clear tooth; omit the crowded second tooth.', '''
        self.phone()
        self.circle('key-bow',21,24,4)
        self.add_polyline('key-shaft',(21,20),(29,13),(31,15))
        # One clear tooth preserves key identity without a crowded second barb.
''',['smartphone','key-round'])
design(14,'VRECT_L','Book cover and page band with a larger outlined head and coherent upward arms; exact4u detached gap.', '''
        self.box('book',8,4,40,44,4)
        self.add_line('pages',(8,36),(40,36))
        self.circle('head',24,16,4)
        self.path('arms',(16,25),[('C',(22,28),(18,27),(20,28)),('L',(24,28)),('L',(26,28)),('C',(32,25),(28,28),(30,27))])
        self.add_line('torso',(24,28),(24,32))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
''',['book-user','human_ref/user.svg'])
design(15,'VRECT_L','Calendar with a longer slanted seven and spacious lower content area.', '''
        self.calendar()
        self.add_polyline('seven',(18,25),(30,25),(23,35))
''',['calendar-check'], 'Seven follows typeface-v2 flat cap and descending diagonal, snapped to SOLO48 integer grid.')
design(16,'VRECT_L','Calendar with smooth diagonal receiver and rounded frame.', '''
        self.calendar()
        self.handset(24,30)
''',['calendar-check','phone'])
design(17,'HRECT_L','Smooth mirrored car silhouette with round wheel arches and an open double-ended wrench.', '''
        self.path('car',(10,20),[('C',(18,8),(14,12),(15,8)),('L',(30,8)),('C',(38,20),(33,8),(34,12)),('C',(44,26),(42,20),(44,22)),('L',(44,32)),('L',(40,32)),('C',(34,40),(40,37),(38,40)),('C',(28,34),(30,40),(28,37)),('L',(20,34)),('C',(14,40),(20,37),(18,40)),('C',(8,32),(10,40),(8,37)),('L',(4,32)),('L',(4,26)),('C',(10,20),(4,22),(6,20))],True)
        self.path('left-jaw',(16,18),[('A',(20,22),4,4,True),('A',(16,26),4,4,True)])
        self.path('right-jaw',(32,18),[('A',(28,22),4,4,False),('A',(32,26),4,4,False)])
        self.add_line('wrench-shaft',(20,22),(28,22))
''',['car-front'])
design(18,'SQUARE','Hexagonal molecule with equal open circular atoms and exact shared bond endpoints.', '''
        for name,x,y in [('top',22,9),('left-top',9,17),('left-bottom',9,31),('bottom',23,36),('right',29,23),('terminal',39,13)]:self.circle(name,x,y,3)
        self.add_line('upper-left',(12,17),(19,9))
        self.add_line('upper-right',(25,9),(29,20))
        self.add_line('left-edge',(9,20),(9,28))
        self.add_line('lower-left',(12,31),(20,36))
        self.add_polyline('lower-right',(29,26),(29,32),(26,36))
        self.add_line('side-chain',(32,23),(36,13))
        self.add_line('terminal-stem',(39,10),(39,6))
        self.add_line('lower-stem',(23,39),(23,42))
''',['hexagon'], 'Very short outer right twig and lower twig bend omitted; all six atom nodes retained.')
design(19,'VRECT_L','Clipboard with true curved dollar sign and exposed vertical currency stems.', '''
        self.path('board',(16,8),[('L',(12,8)),('A',(8,12),4,4,False),('L',(8,40)),('A',(12,44),4,4,False),('L',(36,44)),('A',(40,40),4,4,False),('L',(40,12)),('A',(36,8),4,4,False),('L',(32,8))])
        self.box('clip',16,4,32,12,4)
        self.dollar(24,28)
''',['clipboard'])
design(20,'SQUARE','Eight smoothly repeated gear teeth surround a taller curved dollar sign.', '''
        quarter=[('C',(30,11),(27,6),(27,10)),('C',(37,11),(33,12),(35,9)),('C',(37,18),(39,13),(36,15)),('C',(42,24),(38,21),(42,21))]
        def rot(p,k):
            x,y=p[0]-24,p[1]-24
            for _ in range(k):x,y=-y,x
            return x+24,y+24
        commands=[('C',rot(c[1],k),rot(c[2],k),rot(c[3],k)) for k in range(4) for c in quarter]
        self.path('gear',(24,6),commands,True)
        self.dollar()
''',['settings'])
design(21,'SQUARE','Pipette with consistent diagonal shaft width, rounded bulb and smooth tapered nozzle.', '''
        self.path('pipette',(6,42),[('C',(10,30),(10,38),(7,34)),('L',(20,20)),('L',(32,8)),('C',(36,6),(33,7),(34,6)),('A',(42,12),6,6,True),('C',(40,18),(42,14),(42,16)),('L',(28,30)),('L',(20,38)),('C',(6,42),(16,42),(11,38))],True)
        self.add_polyline('collar',(16,16),(20,20),(28,28),(34,34))
''',['pipette'])
design(23,'SQUARE','Rounded house with its original circular play medallion restored.', '''
        self.path('house',(6,21),[('L',(24,6)),('L',(42,21)),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,21))],True)
        self.circle('medallion',24,27,8)
        self.add_polyline('play',(22,24),(27,27),(22,30),closed=True)
''',['house'], 'No defining omissions; nested play medallion may require a spacing exception after visual review.')
for i,neck in [(24,"self.path('neckline',(20,40),[('A',(28,40),4,4,False)])"),(35,"self.add_polyline('neckline',(20,40),(24,44),(28,40))")]:
    design(i,'VRECT_L','Enlarge circular head, balance shoulders and retain the shirt neckline; exact4u detached head gap.',f'''
        self.circle('head',24,14,10)
        self.path('body',(8,44),[('A',(20,32),12,12,True),('L',(28,32)),('A',(40,44),12,12,True)])
        {neck}
''',['human_ref/user.svg'])
design(25,'VRECT_M','A single-storey lowercase a with a true round counter and smooth right stem, matching the source.', '''
        self.path('a',(38,24),[('C',(24,4),(38,13),(32,4)),('C',(10,24),(15,4),(10,12)),('C',(24,44),(10,36),(15,44)),('C',(38,31),(32,44),(38,36)),('L',(38,24))],True)
        self.add_line('a-stem',(38,31),(38,44))
''',[], 'Typeface v2 has no lowercase a; preserved the supplied single-storey letter rather than substituting uppercase A.')
design(26,'VRECT_L','Phone with a clean rising airplane-mode motif, restored lower band and readable nose.', '''
        self.phone()
        self.path('plane-body',(16,26),[('C',(21,27),(18,27),(19,28)),('L',(27,24)),('L',(31,21)),('C',(32,17),(32,20),(32,18))])
        self.add_polyline('wing',(18,16),(27,24))
''',['smartphone'], 'The source is a minimalist rising plane stroke; no full airplane silhouette added.')
design(27,'VRECT_L','Phone with a rounded skull, separated eye dots and clear lower jaw; restore bottom phone band.', '''
        self.phone()
        self.path('skull',(19,28),[('L',(19,26)),('C',(16,20),(17,25),(16,23)),('A',(24,12),8,8,True),('A',(32,20),8,8,True),('C',(29,26),(32,23),(31,25)),('L',(29,28))])
        self.add_dot('eye-left',(21,21));self.add_dot('eye-right',(27,21))
        # Omit the tiny central tooth; preserve both outer jaw edges.
''',['smartphone'], 'Tiny central tooth omitted; both jaw edges and reference eye dots retained.')
design(28,'VRECT_L','Air purifier with coherent slender airflow curves, smooth body and upright indicator.', '''
        self.box('body',8,22,40,44,4)
        self.add_line('divider',(8,36),(40,36))
        self.add_line('indicator',(24,29),(24,30))
        for x in (18,30):
            self.path(f'air-{x}',(x,4),[('C',(x,14),(x-4,7),(x+4,11))])
''',['smartphone'])
design(29,'VRECT_L','Smooth speech bubble with a diagonal tail and clear hook-to-dot separation.', '''
        self.path('bubble',(12,4),[('L',(36,4)),('A',(40,8),4,4,True),('L',(40,34)),('A',(36,38),4,4,True),('L',(25,38)),('L',(16,44)),('L',(16,38)),('L',(12,38)),('A',(8,34),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.path('question',(19,17),[('A',(29,17),5,5,True),('C',(24,22),(29,20),(24,20))])
        self.add_dot('question-dot',(24,30))
''',['message-square'])
design(30,'SQUARE','Two circular sync curves with open arrowheads aligned with the motion.', '''
        self.path('upper',(6,24),[('C',(24,6),(6,14),(14,6)),('C',(40,14),(31,6),(36,10))])
        self.add_polyline('upper-arrow',(32,14),(40,14),(40,6))
        self.path('lower',(42,24),[('C',(24,42),(42,34),(34,42)),('C',(8,34),(17,42),(12,38))])
        self.add_polyline('lower-arrow',(16,34),(8,34),(8,42))
''',['refresh-cw'])
design(31,'VRECT_L','Restore a distinct document outline and internal shield with centered medical plus.', '''
        self.path('page',(12,4),[('L',(30,4)),('L',(40,14)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        self.path('shield',(16,18),[('L',(24,15)),('L',(32,18)),('L',(32,25)),('C',(24,36),(32,31),(28,34)),('C',(16,25),(20,34),(16,31)),('L',(16,18))],True)
        self.cross('plus',24,24,3)
''',['shield-plus'], 'No defining omissions. Three nested detail levels cannot all retain a4u ink gap at48; report the exact measurements.')
design(33,'VRECT_L','Phone with curved diagonal receiver and clearly angled earpieces.', '''
        self.phone()
        self.handset(24,22)
''',['phone','smartphone'])
design(34,'HRECT_M','Larger speaker throat, clean diagonal cone and two smooth centered sound waves.', '''
        self.path('speaker',(8,18),[('L',(13,18)),('L',(24,10)),('L',(24,38)),('L',(13,30)),('L',(8,30)),('A',(4,26),4,4,True),('L',(4,22)),('A',(8,18),4,4,True)],True)
        self.path('inner-wave',(33,19),[('C',(33,29),(35,21),(35,27))])
        self.path('outer-wave',(39,12),[('C',(44,24),(43,16),(44,20)),('C',(39,36),(44,28),(43,32))])
''',['volume-2'])

# Typeface v2 is a construction source. Reconstruct its proportions on the integer grid,
# preserving stroke4 and using coherent paths rather than tiny exported corner fragments.
text_codes={
2: """
        self.path('s',(19,10),[('L',(11,10)),('C',(8,21),(4,10),(3,17)),('L',(15,27)),('C',(12,38),(22,32),(19,38)),('L',(4,38))])
        self.add_polyline('e',(44,10),(28,10),(28,25),(28,38),(44,38))
        self.add_line('e-arm',(28,25),(38,25))
""",
7: """
        self.path('three',(4,10),[('L',(11,10)),('C',(18,17),(15,10),(18,13)),('C',(11,24),(18,21),(15,24)),('L',(7,24))])
        self.path('three-bottom',(11,24),[('C',(18,31),(15,24),(18,27)),('C',(11,38),(18,35),(15,38)),('L',(4,38))])
""",
8: """
        self.add_line('four-stem',(18,10),(18,38))
        self.add_polyline('four-arm',(4,10),(4,29),(18,29))
""",
9: """
        self.path('five',(18,10),[('L',(4,10)),('L',(4,23)),('L',(11,23)),('C',(18,30),(15,23),(18,26)),('C',(11,38),(18,35),(15,38)),('L',(4,38))])
"""}
gcode="""
        self.path('g',(42,14),[('C',(38,10),(42,11),(40,10)),('L',(35,10)),('C',(28,17),(30,10),(28,12)),('L',(28,31)),('C',(36,38),(28,36),(31,38)),('C',(44,31),(41,38),(44,35)),('L',(44,26)),('L',(38,26))])
"""
for i,code in text_codes.items():
    design(i,'HRECT_M','Typeface v2 letter construction re-authored on integer SOLO48 coordinates with shared cap height and baseline.',code+(gcode if i!=2 else ''),['typeface/glyphs-v2.json'], 'Tiny source corner fragments simplified into coherent joins; retained typeface v2 glyph shape.')

# User review corrections, 2026-09-25. Keep approved geometry unchanged.
AVATARS={6,22,24,32,35,36}
DESIGNS[5]=DESIGNS[4]
for i in (6,24,35):
    key,plan,code,refs,omissions=DESIGNS[i]
    code=code.replace("self.path('shoulders',(8,44),[('A',(20,32),12,12,True),('L',(28,32)),('A',(40,44),12,12,True)])", "self.path('shoulders',(8,44),[('L',(8,40)),('A',(20,28),12,12,True),('L',(28,28)),('A',(40,40),12,12,True),('L',(40,44))])")
    code=code.replace("self.path('body',(8,44),[('A',(20,32),12,12,True),('L',(28,32)),('A',(40,44),12,12,True)])", "self.path('body',(8,44),[('L',(8,40)),('A',(20,28),12,12,True),('L',(28,28)),('A',(40,40),12,12,True),('L',(40,44))])")
    code+="\n        self.relate('connect','head',"+repr('shoulders' if i==6 else 'body')+")\n"
    DESIGNS[i]=(key,'Avatar construction: circular face centered at24; body top28 = head bottom24 + HEAD_BODY_CENTERLINE_GAP. Zero visible head/body gap.',code,refs,'No new costume details; retain skullcap or original neckline.')
for i in (22,32,36):
    key,plan,code,refs,omissions=DESIGNS[i]
    code=code.replace("self.path('shoulders',(8,44),[('A',(16,36),8,8,True),('L',(32,36)),('A',(40,44),8,8,True)])", "self.path('shoulders',(8,44),[('L',(8,40)),('A',(16,32),8,8,True),('L',(32,32)),('A',(40,40),8,8,True),('L',(40,44))])")
    code=code.replace('# Shared human vocabulary: radius8 circular jaw; bottom28, shoulders36 => 4u ink gap.','# Circular jaw bottom28; shoulder top32 yields zero ink gap at stroke4.')
    if i==22: code=code.replace('(8,27)','(8,26)').replace('(40,27)','(40,26)')
    if i==36:
        code=code.replace('(8,30)','(8,40)').replace('(40,30)','(40,40)')
        code+="\n        self.relate('connect','hair','shoulders')\n"
    code+="\n        self.relate('connect','jaw','shoulders')\n"
    DESIGNS[i]=(key,'Avatar with circular jaw and smooth shoulder arcs. Body top32 = jaw bottom28 + HEAD_BODY_CENTERLINE_GAP; zero visible head/body gap.',code,refs,'Tiny neck seams omitted; original hairstyle and open bust retained.')
design(14,'VRECT_L','Hardbound book with a square front cover, curved spine and recessed page edge. Portrait torso joins the cover edge.', """
        self.path('cover',(8,40),[('L',(8,8)),('A',(12,4),4,4,True),('L',(40,4)),('L',(40,36)),('L',(12,36)),('A',(8,40),4,4,False)])
        self.path('pages',(8,40),[('A',(12,44),4,4,False),('L',(40,44)),('C',(40,36),(38,42),(38,38))])
        self.circle('head',24,16,4)
        self.path('arms',(16,25),[('C',(22,28),(18,27),(20,28)),('L',(24,28)),('L',(26,28)),('C',(32,25),(28,28),(30,27))])
        self.add_line('torso',(24,28),(24,36))
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')
""",['book-user','human_ref/user.svg'])
# Shared telephone receiver: diagonal earpieces and one coherent closed curved silhouette.
def receiver(y):
    return f"""
        def pt(x,v):return (x+1,v+{y})
        self.path('receiver',pt(17,12),[('L',pt(20,12)),('A',pt(22,14),2,2,True),('L',pt(22,16)),('L',pt(21,18)),('C',pt(25,22),pt(22,20),pt(23,21)),('L',pt(27,21)),('L',pt(29,21)),('A',pt(31,23),2,2,True),('L',pt(31,26)),('A',pt(29,28),2,2,True),('C',pt(15,14),pt(21,28),pt(15,22)),('A',pt(17,12),2,2,True)],True)
"""
design(16,'VRECT_L','Calendar with a recognizable curved telephone receiver and angled earpieces.',"        self.calendar()\n"+receiver(9),['calendar-check','phone'],'Tiny earpiece panel seams omitted; retain full receiver silhouette.')
design(33,'VRECT_L','Phone with a recognizable curved telephone receiver and angled earpieces.',"        self.phone()\n"+receiver(0),['smartphone','phone'],'Tiny earpiece panel seams omitted; retain full receiver silhouette.')
k,p,c,r,o=DESIGNS[17]
c=c.replace("(16,18),[('A',(20,22),4,4,True),('A',(16,26),4,4,True)]", "(17,19),[('A',(20,22),3,3,True),('A',(17,25),3,3,True)]").replace("(32,18),[('A',(28,22),4,4,False),('A',(32,26),4,4,False)]", "(31,19),[('A',(28,22),3,3,False),('A',(31,25),3,3,False)]")
DESIGNS[17]=(k,'Smaller wrench inside the same car; stroke remains4, as requested even if compact jaws fail.',c,r,o)
design(18,'SQUARE','Simplified molecular structure: four open atoms and three clear connecting bonds.',"""
        self.circle('center',24,24,4)
        self.circle('left',10,10,4)
        self.circle('right',38,10,4)
        self.circle('bottom',24,38,4)
        self.add_line('left-bond',(14,10),(20,24))
        self.add_line('right-bond',(34,10),(28,24))
        self.add_line('bottom-bond',(24,28),(24,34))
""",['hexagon'],'Removed ring skeleton, secondary atom nodes and short terminal twigs at the user’s request.')
design(26,'VRECT_L','Airplane mode shown by a clear rising fuselage, wide swept wings and tailplane inside the phone.',"""
        self.phone()
        self.add_polyline('fuselage',(19,25),(25,19),(31,13))
        self.add_polyline('wings',(16,15),(25,19),(29,28))
        self.add_polyline('tail',(16,22),(19,25),(22,28))
""",['smartphone'],'Replaced ambiguous source-like stroke with recognizable airplane silhouette at user request.')

def main():
    for i,row in enumerate(ROWS,1):
        SOURCE_ICON_ID=row['id'];SOURCE_PATH=row['source_path']
        key,plan,code,refs,omissions=DESIGNS[i]
        header=f'''"""{row['concept']}. {plan}
Keyshape {key}: extremes authored from its SOLO48 centerline box.
Omissions: {omissions}
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
SOURCE_ICON_ID = {SOURCE_ICON_ID!r}
SOURCE_PATH = {SOURCE_PATH!r}
AUTHOR = {AUTHOR!r}
PLAN = {plan!r}
OMISSIONS = {omissions!r}
CONSTRUCTION_REFERENCES = {refs!r}
PARENT_MODULE = {row['parent']!r}

class Drawing(Solo48):
    icon_id = {row['icon_id']!r}
    keyshape = Keyshape.{key}
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = {('avatars' if i in AVATARS else 'objects/general')!r}
    aliases = ()
    keywords = {tuple(row['concept_input'].split())!r}
'''
        text=header+HELPERS+'\n    def build(self):\n'+code+'\n        self.contacts()\n'
        Path(row['module']).write_text(text)
    print('Authored',len(ROWS),'fresh modules.')

if __name__=='__main__':main()
