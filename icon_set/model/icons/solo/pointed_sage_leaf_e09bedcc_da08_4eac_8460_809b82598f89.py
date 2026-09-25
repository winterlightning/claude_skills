"""Pointed Sage Leaf
Plan: Pointed leaning asymmetric sage leaf.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide leaf: broad contour and internal vein.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e09bedcc-da08-4eac-8460-809b82598f89'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/sage_e09bedcc-da08-4eac-8460-809b82598f89.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'pointed-sage-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sage', 'leaf', 'plant', 'vein', 'stem', 'herb')

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
        path('leaf',(10,36),[('C',(18,14),(7,27),(10,19)),('C',(42,6),(26,8),(35,7)),('C',(33,31),(39,18),(40,24)),('C',(10,36),(27,37),(16,36))],True)
        path('vein',(6,42),[('L',(10,36)),('C',(30,17),(17,27),(23,22))])
        self.relate('connect','leaf','vein')
