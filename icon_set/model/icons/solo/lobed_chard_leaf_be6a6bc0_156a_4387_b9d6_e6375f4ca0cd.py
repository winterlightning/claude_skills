"""Lobed Chard Leaf
Plan: Symmetric lobed chard leaf with central stem and two side veins.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'be6a6bc0-156a-4387-b9d6-e6375f4ca0cd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/chard_be6a6bc0-156a-4387-b9d6-e6375f4ca0cd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lobed-chard-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('chard', 'leaf', 'vegetable', 'veins', 'plant', 'greens', 'botanical')

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
        path('leaf',(24,4),[('C',(32,14),(32,4),(32,8)),('C',(40,24),(40,15),(40,18)),('C',(34,33),(40,28),(37,30)),('C',(24,40),(37,38),(29,38)),('C',(14,33),(19,38),(11,38)),('C',(8,24),(11,30),(8,28)),('C',(16,14),(8,18),(8,15)),('C',(24,4),(16,8),(16,4))],True)
        poly('vein',(24,12),(24,28),(24,40),(24,44));join('vein','leaf');poly('branches',(16,22),(24,28),(32,22));join('branches','vein')
