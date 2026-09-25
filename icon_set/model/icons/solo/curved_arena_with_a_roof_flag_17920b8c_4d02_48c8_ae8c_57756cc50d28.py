"""Curved Arena with a Roof Flag
Plan: Curved stadium wall, roof flag and small arched entrance.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Interior wall bands omitted to retain the curved arena, flag and arched entry with clear spacing.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '17920b8c-4d02-48c8-ae8c-57756cc50d28'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/arena_17920b8c-4d02-48c8-ae8c-57756cc50d28.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-arena-with-a-roof-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('arena', 'stadium', 'flag', 'entrance', 'tiers', 'building', 'sport')

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
        path('arena',(6,28),[('C',(24,22),(6,24),(14,22)),('C',(42,28),(34,22),(42,24)),('L',(38,42)),('L',(10,42)),('L',(6,28))],True)
        self.add_line('pole',(24,22),(24,6));rect('flag',24,6,12,8);self.relate('connect','flag','pole');self.relate('connect','pole','arena')
        path('door',(20,42),[('L',(20,36)),('A',(28,36),4,4,True),('L',(28,42))]);self.relate('connect','door','arena')
