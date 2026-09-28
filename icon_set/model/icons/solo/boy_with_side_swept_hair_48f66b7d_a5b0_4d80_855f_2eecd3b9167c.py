"""Boy with Side Swept Hair
Plan: Boy avatar with circular lower face, side-swept hair, broad shoulders and open bottom. Jaw minimum y28 and shoulder maximum y32 give exactly zero visible ink gap.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Shared human_ref/user.svg: circular head and round open shoulders; icon-avatar touching-ink rule.
Reduction: Omitted ears, neck and collar to preserve the circular face and shoulder construction.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48f66b7d-a5b0-4d80-855f-2eecd3b9167c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/boy_48f66b7d-a5b0-4d80-855f-2eecd3b9167c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'boy-with-side-swept-hair'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('boy', 'person', 'avatar', 'hair', 'portrait', 'child', 'profile')

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
        path('head',(14,18),[('A',(34,18),10,14,True),('A',(14,18),10,10,True)],True)
        path('hair',(14,18),[('C',(30,11),(19,18),(25,17)),('C',(34,18),(30,15),(31,17))])
        self.relate('connect','hair-0','head-0');self.relate('connect','hair-0','head-1')
        self.relate('connect','hair-1','head-0');self.relate('connect','hair-1','head-1')
        path('shoulder-left',(8,44),[('L',(8,42)),('A',(18,32),10,10,True)])
        self.add_line('shoulder-top',(18,32),(30,32))
        path('shoulder-right',(30,32),[('A',(40,42),10,10,True),('L',(40,44))])
        self.relate('connect','head','shoulder-top')
        self.relate('connect','shoulder-left','shoulder-top')
        self.relate('connect','shoulder-right','shoulder-top')
