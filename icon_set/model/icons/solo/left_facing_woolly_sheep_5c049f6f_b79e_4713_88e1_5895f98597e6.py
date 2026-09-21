"""Left-Facing Woolly Sheep
Plan: Left-facing woolly sheep with scalloped back and two short legs.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Tiny eye and small ear fold omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c049f6f-b79e-4713-88e1-5895f98597e6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_27/mouton_5c049f6f-b79e-4713-88e1-5895f98597e6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'left-facing-woolly-sheep'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sheep', 'wool', 'livestock', 'farm', 'animal', 'mammal')

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
        path('sheep',(4,20),[('C',(14,8),(4,12),(7,8)),('C',(22,14),(17,8),(21,8)),('C',(33,14),(26,9),(32,9)),('C',(44,23),(44,10),(44,17)),('C',(40,31),(44,28),(42,30)),('L',(40,40)),('L',(32,40)),('L',(31,31)),('C',(18,31),(27,34),(22,34)),('L',(17,40)),('L',(9,40)),('L',(9,28)),('C',(4,20),(4,25),(4,24))],True)
