"""Tulip with Three Sharp Petal Tips
Plan: Three pointed petal tips, bowl bloom, central stem and two basal leaves.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fefc148c-419b-4eff-8873-939105252efd'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/mario flower 1_fefc148c-419b-4eff-8873-939105252efd.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tulip-with-three-sharp-petal-tips'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'Uncategorized'
    aliases = ()
    keywords = ('tulip', 'flower', 'petals', 'stem', 'leaves', 'plant', 'bloom')

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
        path('bloom',(8,6),[('L',(16,12)),('L',(24,4)),('L',(32,12)),('L',(40,6)),('L',(40,16)),('A',(24,28),16,12,True),('A',(8,16),16,12,True),('L',(8,6))],True)
        self.add_line('stem',(24,28),(24,44))
        path('leaves',(24,44),[('C',(8,44),(17,32),(8,32)),('L',(40,44)),('C',(24,44),(40,32),(31,32))],True)
        self.relate('connect','bloom','stem');self.relate('connect','leaves','stem')
