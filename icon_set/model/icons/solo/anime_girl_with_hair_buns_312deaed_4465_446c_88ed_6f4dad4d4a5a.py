"""Cute Anime Girl with Hair Buns.

Plan: Round girl face with paired round buns and long hair locks. Extremes6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Omit smile and tiny heart to retain round face, round buns and long hair without cramming features.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '312deaed-4465-446c-88ed-6f4dad4d4a5a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/41-312deaed-4465-446c-88ed-6f4dad4d4a5a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'anime-girl-with-hair-buns'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('anime', 'girl', 'with', 'hair', 'buns')

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
        path('hair',(6,42),[('L',(10,26)),('L',(10,18)),('C',(6,12),(6,18),(6,15)),('A',(18,12),6,6,True),('L',(18,14)),('L',(30,14)),('L',(30,12)),('A',(42,12),6,6,True),('C',(38,18),(42,15),(42,18)),('L',(38,26)),('L',(42,42))])
        path('face',(10,26),[('A',(38,26),14,14,False)]);join('hair','face')
        for x in (20,28):self.add_dot(f'eye-{x}',(x,26))
