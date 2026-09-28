"""Domed Serving Cloche
Plan: Semicircular cover with stem knob above shallow platter
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide cooking-pot dome and knob.
Reduction: Use stem knob and one platter curve."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0da9fd79-5a92-42be-9541-8fcbf7d7bf03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pate_0da9fd79-5a92-42be-9541-8fcbf7d7bf03.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'domed-serving-cloche'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cloche', 'platter', 'serving', 'cover', 'food', 'dome')

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
        path('dome',(6,32),[('A',(42,32),18,18,True)])
        self.add_line('knob',(24,8),(24,14));self.relate('connect','knob','dome')
        path('platter',(4,32),[('L',(10,40)),('L',(38,40)),('L',(44,32)),('L',(4,32))],True);self.relate('connect','dome','platter')
