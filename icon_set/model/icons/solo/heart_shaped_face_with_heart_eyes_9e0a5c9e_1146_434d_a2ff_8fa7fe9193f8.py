"""Smiling Heart Face with Heart Eyes.

Plan: Heart-shaped face with two heart eyes and curved smile; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: No identifying parts intentionally omitted; heart eye fit requires release review.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9e0a5c9e-1146-434d-a2ff-8fa7fe9193f8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/43-9e0a5c9e-1146-434d-a2ff-8fa7fe9193f8.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'heart-shaped-face-with-heart-eyes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('heart', 'shaped', 'face', 'with', 'heart', 'eyes')

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
        path('heart',(24,40),[('C',(4,19),(12,32),(4,28)),('A',(14,8),10,11,True),('C',(24,13),(19,8),(21,10)),('C',(34,8),(27,10),(29,8)),('A',(44,19),10,11,True),('C',(24,40),(44,28),(36,32))],True)
        for j,x in enumerate((16,32)):
         path(f'eye-{j}',(x,24),[('C',(x-4,19),(x-3,22),(x-4,21)),('C',(x,18),(x-4,15),(x-1,15)),('C',(x+4,19),(x+1,15),(x+4,15)),('C',(x,24),(x+4,21),(x+3,22))],True)
        path('smile',(21,30),[('C',(27,30),(23,32),(25,32))])
