"""Potato Head Toy Character.

Plan: Potato Head toy: rounded head, hat brim, round eyes, projecting nose and moustache. Extremes8,4,40,44.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Reduce hat to a brim, eyes to dots and large nose to a short solid stroke; retain the rounded toy head and lobed moustache.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '09b060de-331e-4760-a299-7d321fd12cd5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/37-09b060de-331e-4760-a299-7d321fd12cd5.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'potato-head-toy'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('potato', 'head', 'toy')

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
        path('face',(8,15),[('L',(8,24)),('L',(8,28)),('A',(24,44),16,16,False),('A',(40,28),16,16,False),('L',(40,24)),('L',(40,15)),('A',(24,4),16,11,False),('A',(8,15),16,11,False)],True)
        line('brim',(8,15),(40,15));join('face','brim')
        for x in (17,31):self.add_dot(f'eye-{x}',(x,24))
        line('nose',(24,29),(24,32))
        path('moustache',(18,32),[('C',(24,32),(20,34),(21,32)),('C',(30,32),(27,32),(28,34))]);join('nose','moustache')
