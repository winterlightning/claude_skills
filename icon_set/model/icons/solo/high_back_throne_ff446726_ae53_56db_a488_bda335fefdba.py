"""Royal High Back Throne.

Plan: Throne with tall domed back, broad armrests and seat between two long supports. Extremes8,4,40,44.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Reduce rounded armrest/seat thickness to solid strokes; keep tall arch and long front supports.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff446726-ae53-56db-a488-bda335fefdba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/42-ff446726-ae53-56db-a488-bda335fefdba.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'high-back-throne'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('high', 'back', 'throne')

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
        path('back',(14,26),[('L',(14,14)),('A',(34,14),10,10,True),('L',(34,26))])
        for x in (8,40):
         poly(f'post-{x}',(x,26),(x,35),(x,44))
         line(f'arm-{x}',(x,26),(14 if x==8 else 34,26));join(f'post-{x}',f'arm-{x}');join('back',f'arm-{x}')
        poly('seat',(8,35),(40,35));join('seat','post-8');join('seat','post-40')
