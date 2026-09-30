"""Clove Bud with Pointed Sepals
Plan: Diagonal stem, pointed sepals and round bud.
Keyshape: VRECT_M; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Rebalanced upright; tiny individual sepals reduced to a flared calyx beneath round bud.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2fe3535b-ed46-49bc-ad15-b91d93556dfe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cloves_2fe3535b-ed46-49bc-ad15-b91d93556dfe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'clove-bud-with-pointed-sepals'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('clove', 'spice', 'bud', 'stem', 'sepals', 'food', 'botanical')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('clove',(20,44),[('L',(20,30)),('L',(10,20)),('L',(12,20)),('C',(24,4),(9,12),(15,4)),('C',(36,20),(33,4),(39,12)),('L',(38,20)),('L',(28,30)),('L',(28,44)),('L',(20,44))],True)
        self.add_line('calyx',(10,20),(38,20));self.relate('connect','calyx','clove')
