"""Corn Cob in Open Husk
Plan: Tall cob with mirrored pointed husk leaves and stem
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: No useful Lucide match; shared mirrored curves.
Reduction: Reduce kernels to two crossbars."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '509d8c81-aff0-4d15-9237-c757ac95069a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/cob_509d8c81-aff0-4d15-9237-c757ac95069a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'corn-cob-in-open-husk'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('corn', 'cob', 'kernels', 'husk', 'maize', 'food', 'vegetable')

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
        path('cob',(16,22),[('L',(16,12)),('A',(32,12),8,8,True),('L',(32,22))])
        path('husk',(24,40),[('C',(8,28),(8,40),(8,34)),('L',(8,18)),('C',(24,40),(20,22),(24,32)),('C',(40,18),(24,32),(28,22)),('L',(40,28)),('C',(24,40),(40,34),(40,40))],True)
        self.add_line('stem',(24,40),(24,44));self.relate('connect','stem','husk');self.relate('connect','cob','husk')
        self.add_line('kernels',(16,16),(32,16));self.relate('connect','kernels','cob')

# Final review: Kernel grid reduced to one broad crossbar; preserve both husk leaves and stem.
