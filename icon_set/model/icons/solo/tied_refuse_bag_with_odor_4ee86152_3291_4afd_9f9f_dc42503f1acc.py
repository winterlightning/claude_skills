"""Tied Refuse Bag with Odor
Plan: Tied bulging refuse sack with wavy odor strokes.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Four odor strokes reduced to two broad side wisps."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4ee86152-3291-4afd-9f9f-dc42503f1acc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bin smell_4ee86152-3291-4afd-9f9f-dc42503f1acc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tied-refuse-bag-with-odor'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('garbage', 'bag', 'refuse', 'trash', 'odor', 'waste', 'tied')

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
        path('bag',(18,20),[('L',(16,10)),('L',(32,10)),('L',(30,20)),('C',(39,34),(37,24),(39,29)),('C',(24,42),(39,41),(33,42)),('C',(9,34),(15,42),(9,41)),('C',(18,20),(9,29),(11,24))],True)
        self.add_line('tie',(18,20),(30,20));self.relate('connect','tie','bag')
        for x in (6,42):path(f'odor-{x}',(x,6),[('C',(x,19),(x-2 if x==42 else x+2,10),(x+2 if x==6 else x-2,15))])
