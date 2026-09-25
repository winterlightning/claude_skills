"""Doghouse with Thick Gabled Roof
Plan: Gabled doghouse with an arched doorway.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide house: shared roof/wall junction.
Reduction: Roof thickness simplified to single 4px run."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '58681f4e-f40c-47aa-8ab2-a64e586e388e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/dog house 2_58681f4e-f40c-47aa-8ab2-a64e586e388e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'doghouse-with-thick-gabled-roof'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('doghouse', 'kennel', 'pet', 'roof', 'doorway', 'house', 'shelter')

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
        self.add_polyline('roof',(6,24),(24,6),(42,24))
        path('walls',(10,20),[('L',(10,42)),('L',(18,42)),('L',(18,32)),('A',(30,32),6,6,True),('L',(30,42)),('L',(38,42)),('L',(38,20))]);self.relate('connect','roof','walls')
