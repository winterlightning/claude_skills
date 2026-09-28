"""Simple Walking Turtle Icon.

Plan: Turtle with domed shell, upright neck and two opposite feet. Extremes4,8,44,40.
Construction: Lucide turtle original/atomic-debug: dome and prominent head.
Reduction: Open belly and solid opposing feet; preserve tall neck and domed shell, omit tiny eye.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9c7c74da-c103-4fea-9bf5-13a249aa772b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-022/references/48-9c7c74da-c103-4fea-9bf5-13a249aa772b.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'walking-turtle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('walking', 'turtle')

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
        path('body',(4,32),[('A',(18,18),14,14,True),('A',(32,32),14,14,True),('L',(32,14)),('A',(38,8),6,6,True),('A',(44,14),6,6,True),('L',(44,22)),('L',(40,22)),('L',(40,32)),('A',(32,40),8,8,True)])
        poly('belly',(4,32),(12,32),(32,32));join('body','belly')
        line('foot-left',(12,32),(4,40));join('belly','foot-left')
