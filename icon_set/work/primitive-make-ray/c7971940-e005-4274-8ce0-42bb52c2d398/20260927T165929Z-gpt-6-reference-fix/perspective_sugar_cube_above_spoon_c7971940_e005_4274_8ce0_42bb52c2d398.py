"""Perspective Sugar Cube Above Spoon
Plan: One perspective sugar cube above a deep right-handled spoon.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Spoon flattened to fit the cube and clearances; visual review rejects the loss of a recognizable deep bowl."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c7971940-e005-4274-8ce0-42bb52c2d398'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__perspective-sugar-cube-above-spoon/20260927T165437Z-thuan-mac-1/reference/drinks extra add sugar 1_c7971940-e005-4274-8ce0-42bb52c2d398.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'perspective-sugar-cube-above-spoon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('sugar', 'cube', 'spoon', 'sweetener', 'food', 'utensil', 'drink')

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
        poly('cube',(6,14),(16,6),(30,6),(30,18),(20,24),(6,24),(6,14),(20,14),(30,6));line('cube-edge',(20,14),(20,24));join('cube-edge','cube')
        # A curved bowl and rounded handle replace the rejected rectangular trough.
        path('spoon',(6,34),[('C',(22,34),(8,32),(20,32)),('L',(38,34)),('A',(42,38),4,4,True),('A',(38,42),4,4,True),('L',(22,42)),('C',(6,34),(13,42),(6,42))],True)
