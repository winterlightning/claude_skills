"""Upright Sepal with Central Vein
Plan: Upright pointed sepal and centered vein/stem.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide leaf: continuous stem and internal vein.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cafb429b-195a-4ac5-a51d-c27387977241'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_33/sepal_cafb429b-195a-4ac5-a51d-c27387977241.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'upright-sepal-with-central-vein'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('sepal', 'leaf', 'plant', 'vein', 'stem', 'botanical')

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
        path('sepal',(24,4),[('C',(40,27),(29,11),(40,18)),('C',(24,38),(40,35),(33,38)),('C',(8,27),(15,38),(8,35)),('C',(24,4),(8,18),(19,11))],True)
        self.add_line('vein',(24,17),(24,44));self.relate('connect','sepal','vein')
