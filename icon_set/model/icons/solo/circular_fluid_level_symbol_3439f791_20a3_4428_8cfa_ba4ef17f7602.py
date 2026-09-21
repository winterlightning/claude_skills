"""Circular Fluid Level Symbol
Plan: Circular fluid container with a shallow continuous wave from side to side. This is an intrinsic level mark, not an independent modifier.
Keyshape CIRCLE: (2, 2, 46, 46).
Construction reference: No useful exact Lucide match; symmetric wave and circular envelope.
Reduction: No omissions.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3439f791-20a3-4428-8cfa-ba4ef17f7602'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/brake fluid_3439f791-20a3-4428-8cfa-ba4ef17f7602.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'circular-fluid-level-symbol'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/automotive'
    aliases = ()
    keywords = ('fluid', 'liquid', 'level', 'circle', 'wave', 'indicator', 'symbol')

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
        circle('circle',24,24,20)
        path('level',(4,24),[('C',(24,24),(11,32),(17,16)),('C',(44,24),(31,32),(37,16))])
        for m in ['circle-0','circle-3']:self.relate('connect','level-0',m)
        for m in ['circle-1','circle-2']:self.relate('connect','level-1',m)
