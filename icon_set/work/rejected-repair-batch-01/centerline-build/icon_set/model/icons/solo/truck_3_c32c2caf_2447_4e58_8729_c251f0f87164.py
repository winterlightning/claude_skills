"""truck-3-transportation: reconstructed stroke graph on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c32c2caf-2447-4e58-8729-c251f0f87164'
SOURCE_PATH = 'pictographic-primitives/transportation/truck 3_c32c2caf-2447-4e58-8729-c251f0f87164.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Truck3Transportation(Solo48):
    icon_id = 'truck-3-transportation'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('truck', 'transportation')

    def build(self):
        # Plan: HRECT_L; equal round wheels with chassis rails stopping exactly at their extremes; a tangent cab corner and shared cargo seam.
        # Reference: No exact inspected Lucide truck match; matched wheel definition and exact axle-height contacts.
        def path(name,start,commands,closed=False):
            members=[];previous=start
            for i,cmd in enumerate(commands):
                eid=f'{name}-{i}';members.append(eid)
                if cmd[0]=='L':self.add_line(eid,previous,cmd[1])
                elif cmd[0]=='C':self.add_bezier(eid,previous,tuple(cmd[1:]))
                elif cmd[0]=='A':self.add_arc(eid,previous,cmd[1],radius_x=cmd[2],radius_y=cmd[3],sweep=cmd[4])
                previous=cmd[-1] if cmd[0]=='C' else cmd[1]
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry=None):
            ry=rx if ry is None else ry
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)

        for name,cx in [('front',13),('back',35)]:oval(name,cx,35,5)
        path('cab',(8,35),[('L',(7,35)),('A',(4,32),3,3,True),('L',(4,23)),('C',(4,18),(7,14),(12,14)),('L',(20,14))])
        path('cargo',(20,21),[('L',(20,14)),('L',(20,8)),('L',(44,8)),('L',(44,32)),('A',(41,35),3,3,True),('L',(40,35))])
        self.add_polyline('chassis',(18,35),(20,35),(30,35))
        self.relate('connect','cab','cargo');self.relate('connect','cab','front');self.relate('connect','cargo','back')
        self.relate('connect','chassis','front');self.relate('connect','chassis','back')
