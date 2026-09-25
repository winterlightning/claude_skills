"""Slithering Snake Symbol.

Plan: Upright snake with rounded head and broad S-shaped single-stroke body; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Body outline reduced to one broad winding stroke; head retained without tiny eye.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2ec00ca4-5f8a-4ca6-b750-8ed6a3306564'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/12-2ec00ca4-5f8a-4ca6-b750-8ed6a3306564.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'curving-snake'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('curving', 'snake')

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
        path('head',(24,16),[('L',(24,12)),('A',(32,4),8,8,True),('A',(40,12),8,8,True),('A',(32,20),8,8,True),('L',(24,20))])
        path('body',(24,16),[('C',(8,28),(14,16),(8,20)),('C',(24,36),(8,36),(24,28)),('C',(8,44),(24,44),(16,44))]);join('head','body')
