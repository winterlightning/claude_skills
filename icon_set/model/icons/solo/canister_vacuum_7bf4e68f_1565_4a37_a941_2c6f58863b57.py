"""Canister Vacuum Cleaner.

Plan: Canister at lower left under looping hose; floor nozzle at right. x6..42 y6..42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Removed tiny canister wheel and top handle after overlap repairs failed; hose, canister and nozzle preserve vacuum identity.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7bf4e68f-1565-4a37-a941-2c6f58863b57'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/26-7bf4e68f-1565-4a37-a941-2c6f58863b57.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'canister-vacuum'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "electronics"
    categories = ("electronics", "primitive", "primitives")
    aliases = ()
    keywords = ('canister', 'vacuum')

    def build(self):

        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2])
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name, (x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name, a, b): self.add_line(name,a,b)
        def poly(name, *points, closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        path('canister',(14,24),[('L',(22,24)),('L',(22,42)),('L',(12,42)),('A',(6,36),6,6,True),('L',(6,32)),('A',(14,24),8,8,True)],True)
        path('hose',(18,24),[('L',(18,16)),('A',(38,16),10,10,True),('L',(38,34))]);join('hose','canister')
        rect('nozzle',32,34,10,8);join('nozzle','hose')
