"""Steaming Rounded Mug
Plan: Rounded mug with right handle and two equally sized steam wisps.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide coffee: rounded body, handle attachments and steam.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b95ea80-bb84-4fc5-8be0-88aa2447a110'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mug hot_2b95ea80-bb84-4fc5-8be0-88aa2447a110.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steaming-rounded-mug'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('mug', 'coffee', 'steam', 'hot', 'drink', 'cup')

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
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('mug',(6,22),[('L',(32,22)),('L',(32,30)),('L',(32,34)),('A',(24,42),8,8,True),('L',(14,42)),('A',(6,34),8,8,True),('L',(6,22))],True)
        path('handle',(32,22),[('L',(36,22)),('A',(42,28),6,6,True),('A',(36,34),6,6,True),('L',(32,34))]);join('handle','mug')
        for x in (14,25):path(f'steam-{x}',(x,6),[('C',(x,13),(x+3,8),(x-3,10))])
