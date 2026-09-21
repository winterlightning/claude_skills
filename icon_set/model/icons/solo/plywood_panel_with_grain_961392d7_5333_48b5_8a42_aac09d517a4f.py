"""Plywood Panel with Grain
Plan: Square plywood panel with four fixings and flowing grain.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Fine grain series and small knot reduced to one flowing grain stroke; all four fixings retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '961392d7-5333-48b5-8a42-aac09d517a4f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_31/plywood_961392d7-5333-48b5-8a42-aac09d517a4f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plywood-panel-with-grain'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('plywood', 'wood', 'panel', 'grain', 'board', 'material')

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
        rect('panel',6,6,36,36,4)
        for x in (15,33):
         for y in (15,33):self.add_dot(f'fixing-{x}-{y}',(x,y))
        path('grain',(6,24),[('C',(42,24),(14,23),(34,23))]);self.relate('connect','grain','panel')
