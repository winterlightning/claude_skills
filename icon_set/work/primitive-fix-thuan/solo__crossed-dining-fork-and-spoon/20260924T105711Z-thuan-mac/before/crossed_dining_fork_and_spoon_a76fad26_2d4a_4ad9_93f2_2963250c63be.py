"""Crossed Dining Fork and Spoon
Plan: Crossed spoon and three-tined fork
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide utensils-crossed.
Reduction: Keep fork tines as open strokes, one spoon bowl."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a76fad26-2d4a-4ad9-93f2-2963250c63be'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/cuisine_a76fad26-2d4a-4ad9-93f2-2963250c63be.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crossed-dining-fork-and-spoon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('fork', 'spoon', 'cutlery', 'dining', 'utensils', 'crossed', 'meal')

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
        path('fork',(6,6),[('L',(6,20)),('L',(22,20)),('L',(22,6))])
        self.add_line('middle',(14,6),(14,20));self.relate('connect','middle','fork')
        self.add_line('fork-handle',(14,20),(42,42));self.relate('connect','fork-handle','fork');self.relate('connect','fork-handle','middle')
        circle('spoon',36,14,6)
        self.add_line('spoon-handle',(36,20),(6,42));self.relate('connect','spoon-handle','spoon');self.relate('connect','spoon-handle','fork-handle')

# Final review: Three open tines on a wide U base, round spoon bowl and crossing handles; simplify original diagonal bowls to retain all tines without cramped openings.
