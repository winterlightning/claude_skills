"""Side Table with Lower Crossbar
Plan: Rounded tabletop and upright legs with lower crossbar.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Apron absorbed into thick tabletop; double outlined feet reduced to single strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a6383b55-59e6-4ac8-95c0-daacbaf6cdbe'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/end table_a6383b55-59e6-4ac8-95c0-daacbaf6cdbe.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'side-table-with-lower-crossbar'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('table', 'side', 'furniture', 'legs', 'crossbar', 'top', 'interior')

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
        rect('top',6,6,36,8,3)
        for x in (10,38):self.add_line(f'leg-{x}',(x,14),(x,42));self.relate('connect','top',f'leg-{x}')
        self.add_line('crossbar',(10,32),(38,32))
        for x in (10,38):self.relate('connect','crossbar',f'leg-{x}')
