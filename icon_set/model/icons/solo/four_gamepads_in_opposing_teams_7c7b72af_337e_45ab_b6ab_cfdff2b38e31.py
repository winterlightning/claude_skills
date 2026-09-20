"""Multiplayer Team Versus Mode.

Plan: Four compact outlined gamepads in opposing rows with a central separator. Bounds6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit internal controls; keep all four outlined controllers, opposing grip directions and divider.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c7b72af-337e-45ab-b6ab-cfdff2b38e31'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/25-7c7b72af-337e-45ab-b6ab-cfdff2b38e31.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'four-gamepads-in-opposing-teams'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('four', 'gamepads', 'in', 'opposing', 'teams')

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
        for top in (True,False):
         y=lambda v:v if top else 48-v
         for x in (6,28):
          path(f'pad-{top}-{x}',(x,y(6)),[('L',(x,y(12))),('A',(x+4,y(16)),4,4,not top),('L',(x+10,y(16))),('A',(x+14,y(12)),4,4,not top),('L',(x+14,y(6))),('L',(x+10,y(8))),('L',(x+4,y(8))),('L',(x,y(6)))],True)
        line('divider',(6,24),(42,24))
