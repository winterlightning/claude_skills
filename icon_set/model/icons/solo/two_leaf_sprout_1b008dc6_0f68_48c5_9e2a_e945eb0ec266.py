"""Two-Leaf Sprout
Plan: Large right leaf, smaller left leaf, straight stem and ground.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide sprout: asymmetric botanical layout.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1b008dc6-0f68-48c5-9e2a-e945eb0ec266'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stem_1b008dc6-0f68-48c5-9e2a-e945eb0ec266.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-leaf-sprout'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('sprout', 'plant', 'stem', 'leaf', 'growth', 'seedling', 'botanical', 'garden')

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
        path('right-leaf',(25,25),[('C',(42,6),(24,12),(31,6)),('C',(25,25),(42,19),(36,25))],True)
        path('left-leaf',(16,29),[('C',(6,13),(7,29),(6,21)),('C',(16,29),(16,13),(16,21))],True)
        self.add_line('stem',(25,25),(25,42));self.add_line('ground',(14,42),(36,42));self.relate('connect','stem','ground');self.relate('connect','stem','right-leaf')
