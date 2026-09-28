"""Smiling Bald Man Face.

Plan: Bald round head with small ears and a broad open smile, two eye marks. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit tiny nose and brows; keep bald outline, two ears, paired eyes and open smile.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '00de027d-6064-4c84-a342-9fe6d6c6667d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/50-00de027d-6064-4c84-a342-9fe6d6c6667d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'saitama-smiling-head'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    categories = ("primitives", "video-games")
    aliases = ()
    keywords = ('saitama', 'smiling', 'head')

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
        path('face',(24,6),[('A',(40,22),16,16,True),('L',(40,24)),('L',(40,26)),('A',(24,42),16,16,True),('A',(8,26),16,16,True),('L',(8,24)),('L',(8,22)),('A',(24,6),16,16,True)],True)
        for s in (-1,1):
         x=lambda v:24+s*v
         line(f'ear-{s}',(x(16),24),(x(18),24));join('face',f'ear-{s}')
         self.add_dot(f'eye-{s}',(x(6),18))
        path('smile',(18,27),[('A',(30,27),6,6,False),('L',(18,27))],True)
