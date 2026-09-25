"""Spiral Notebook with Cover Lines
Plan: Upright notebook with four binding strokes and three cover marks.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide notebook: binding strokes cross the cover edge.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'acbf3d78-5d54-4049-90fd-c37a4cbc04b8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/notebook_acbf3d78-5d54-4049-90fd-c37a4cbc04b8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spiral-notebook-cover-lines'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('notebook', 'spiral', 'binding', 'cover', 'stationery', 'paper')

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
        rect('cover',12,4,28,40,4)
        for y in (12,20,28,36):self.add_line(f'binding-{y}',(8,y),(16,y));self.relate('connect',f'binding-{y}','cover')
        for y in (15,24,33):self.add_line(f'text-{y}',(25,y),(31,y))
