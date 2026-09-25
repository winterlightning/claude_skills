"""Three Petal Tulip with Leaf
Plan: Rounded three-petal bloom, straight stem and single rising right leaf.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8cdd054-83a5-4649-96a1-c482018d42fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/blossom_b8cdd054-83a5-4649-96a1-c482018d42fa.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-petal-tulip-with-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('tulip', 'flower', 'petals', 'leaf', 'stem', 'plant', 'bloom')

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

        path('bloom',(8,12),[('C',(18,12),(8,4),(16,4)),('A',(30,12),6,8,True),('C',(40,12),(32,4),(40,4)),('C',(24,26),(40,21),(32,26)),('C',(8,12),(16,26),(8,21))],True)
        self.add_line('stem',(24,26),(24,44));self.relate('connect','stem','bloom')
        path('leaf',(24,44),[('C',(40,32),(32,44),(40,40)),('C',(24,44),(32,32),(24,36))],True)
        self.relate('connect','leaf','stem')
