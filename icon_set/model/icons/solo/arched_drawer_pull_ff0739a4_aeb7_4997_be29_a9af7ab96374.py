"""Cabinet Drawer Pull Handle.

Plan: Broad squared arch handle with mounting feet, x4..44 y10..38; 8-unit material band.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Mounting feet widened to retain a legible opening.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff0739a4-aeb7-4997-be29-a9af7ab96374'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/23-ff0739a4-aeb7-4997-be29-a9af7ab96374.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'arched-drawer-pull'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('arched', 'drawer', 'pull')

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
        path('pull',(4,38),[('L',(4,30)),('L',(8,30)),('L',(8,16)),('A',(14,10),6,6,True),('L',(34,10)),('A',(40,16),6,6,True),('L',(40,30)),('L',(44,30)),('L',(44,38)),('L',(32,38)),('L',(32,18)),('L',(16,18)),('L',(16,38)),('L',(4,38))],True)
