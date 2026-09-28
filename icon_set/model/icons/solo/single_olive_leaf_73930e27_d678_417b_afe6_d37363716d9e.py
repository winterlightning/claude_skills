"""Single Olive with Leaf
Plan: Round olive with curved stem and pointed upper leaf.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide leaf: two coherent curves for a lanceolate blade.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '73930e27-d678-417b-afe6-d37363716d9e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/olive_73930e27-d678-417b-afe6-d37363716d9e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'single-olive-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('olive', 'fruit', 'leaf', 'stem', 'food', 'plant')

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
        path('olive',(8,31),[('A',(21,18),13,13,True),('A',(34,31),13,13,True),('A',(21,44),13,13,True),('A',(8,31),13,13,True)],True)
        path('stem',(21,18),[('C',(18,4),(23,11),(20,7))]);self.relate('connect','stem','olive')
        path('leaf',(21,18),[('C',(40,4),(25,6),(33,4)),('C',(21,18),(40,13),(32,18))],True)
        self.relate('connect','leaf','stem');self.relate('connect','leaf','olive')
