"""Stepped Cliffs beneath Sun
Plan: Three receding stepped cliff faces under a circular sun.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Tiny sun rays omitted; three receding cliff faces retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c86f69ad-1fb2-4e7d-ac5c-71c6bf72365c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/cliffs of mother_c86f69ad-1fb2-4e7d-ac5c-71c6bf72365c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stepped-cliffs-beneath-sun'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cliffs', 'sun', 'landscape', 'rock', 'ledges', 'geology', 'outdoors')

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
        poly('cliff-a',(6,6),(14,6),(14,23),(19,30),(19,42));poly('cliff-b',(14,19),(24,19),(25,30),(30,34),(30,42));join('cliff-a','cliff-b')
        poly('cliff-c',(25,28),(35,28),(36,32),(42,34),(42,42));join('cliff-b','cliff-c')
        poly('ground',(6,42),(19,42),(30,42),(42,42));join('ground','cliff-a');join('ground','cliff-b');join('ground','cliff-c')
        circle('sun',35,12,4)
