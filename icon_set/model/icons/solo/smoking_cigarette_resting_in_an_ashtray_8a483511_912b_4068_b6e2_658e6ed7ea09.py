"""Smoking Cigarette Resting in an Ashtray
Plan: Diagonal cigarette rests in rounded ashtray with curling smoke.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide cigarette: long narrow body and separated smoke stroke.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8a483511-912b-4068-b6e2-658e6ed7ea09'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/ashtray_8a483511-912b-4068-b6e2-658e6ed7ea09.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'smoking-cigarette-resting-in-an-ashtray'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('ashtray', 'cigarette', 'smoke', 'tray', 'smoking', 'ash', 'curl')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        path('tray',(6,30),[('L',(6,37)),('A',(11,42),5,5,False),('L',(37,42)),('A',(42,37),5,5,False),('L',(42,26))])
        self.add_line('rim',(6,30),(17,30));self.relate('connect','rim','tray')
        self.add_polyline('cigarette',(18,34),(16,26),(40,18),(42,26),closed=True);self.relate('connect','cigarette','tray');self.relate('connect','cigarette','rim')
        path('smoke',(37,9),[('C',(23,6),(38,1),(25,13)),('L',(23,6))])
