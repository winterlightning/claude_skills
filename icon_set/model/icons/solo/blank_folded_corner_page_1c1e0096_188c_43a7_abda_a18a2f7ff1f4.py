"""Blank Folded-Corner Page
Plan: One upright page with rounded lower corners and a structural fold at upper-right.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide file: shared fold junction.
Reduction: No omitted semantic parts.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1c1e0096-188c-43a7-abda-a18a2f7ff1f4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/nit_1c1e0096-188c-43a7-abda-a18a2f7ff1f4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'blank-folded-corner-page'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('page', 'paper', 'document', 'blank', 'fold', 'sheet')

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
        path('page',(12,4),[('L',(24,4)),('L',(40,20)),('L',(40,40)),('A',(36,44),4,4,True),('L',(12,44)),('A',(8,40),4,4,True),('L',(8,8)),('A',(12,4),4,4,True)],True)
        path('fold',(24,4),[('L',(24,16)),('A',(28,20),4,4,False),('L',(40,20))])
        for m in ['page-0','page-1']:self.relate('connect','fold-0',m)
        for m in ['page-1','page-2']:self.relate('connect','fold-2',m)
