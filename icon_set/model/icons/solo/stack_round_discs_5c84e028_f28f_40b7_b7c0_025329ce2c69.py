"""Stack of Round Discs
Plan: Three thick round discs with an oval top.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Small top opening omitted to reserve layer spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5c84e028-f28f-40b7-b7c0-025329ce2c69'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/pancakes_5c84e028-f28f-40b7-b7c0-025329ce2c69.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stack-round-discs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('discs', 'stack', 'round', 'layers', 'hole', 'circular')

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
        path('top',(6,14),[('A',(24,6),18,8,True),('A',(42,14),18,8,True),('A',(24,22),18,8,True),('A',(6,14),18,8,True)],True)
        for y in (24,34):
         path(f'layer-{y}',(6,y-10),[('L',(6,y)),('A',(24,y+8),18,8,False),('A',(42,y),18,8,False),('L',(42,y-10))]);self.relate('connect',f'layer-{y}','top' if y==24 else 'layer-24')
