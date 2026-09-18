"""Ambulance Stretcher Gurney Bed.

Plan: Raised back medical gurney with crossed folding legs and paired small wheels.
Reduction / construction: No exact Lucide match; use an open padded-bed gesture and omit lower crossbar.
Envelope: SQUARE, exact SOLO48 contract extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '427fe096-15cb-4068-b2aa-b0087624ab32'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_23/instrument ambulance bed 1_427fe096-15cb-4068-b2aa-b0087624ab32.svg'
AUTHOR = 'gpt-6'


class Batch064Icon10(Solo48):
    icon_id = 'raised-back-medical-gurney-batch-064'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('raised', 'back', 'medical', 'gurney')

    def build(self):

        def path(name, start, commands, closed=False):
            members=[]
            point=start
            for i,command in enumerate(commands):
                kind,end,*args=command
                member=f"{name}-{i}"
                if kind=='L':
                    self.add_line(member,point,end)
                else:
                    rx,ry,sweep=args
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep)
                members.append(member)
                point=end
            self.add_contour(name,*members,closed=closed)
        def oval(name,cx,cy,rx,ry):
            path(name,(cx-rx,cy),[('A',(cx,cy-ry),rx,ry,True),('A',(cx+rx,cy),rx,ry,True),('A',(cx,cy+ry),rx,ry,True),('A',(cx-rx,cy),rx,ry,True)],True)

        self.add_polyline('bed',(6,6),(12,22),(14,22),(36,22),(42,22))
        self.add_polyline('leg-left',(14,22),(25,29),(36,36))
        self.add_polyline('leg-right',(36,22),(25,29),(14,36))
        self.relate('connect','bed','leg-left')
        self.relate('connect','bed','leg-right')
        self.relate('connect','leg-left','leg-right')
        for x in (14,36):
            oval(f'wheel-{x}',x,39,3,3)
        self.relate('connect','leg-left','wheel-36')
        self.relate('connect','leg-right','wheel-14')
