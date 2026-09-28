"""Rail Grid with Three Crossbars
Plan: Two rails and three evenly spaced crossbars.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Removed extraction scratch at middle-left junction."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1ec1f880-2ec0-4be3-9c5c-9c4cad6deda9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_32/rail_1ec1f880-2ec0-4be3-9c5c-9c4cad6deda9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rail-grid-with-three-crossbars'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('rail', 'grid', 'crossbar', 'fence', 'structure', 'framework')

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
        for x in (12,36):self.add_line(f'rail-{x}',(x,6),(x,42))
        for y in (10,24,38):
         self.add_line(f'bar-{y}',(6,y),(42,y))
         for x in (12,36):self.relate('connect',f'rail-{x}',f'bar-{y}')
