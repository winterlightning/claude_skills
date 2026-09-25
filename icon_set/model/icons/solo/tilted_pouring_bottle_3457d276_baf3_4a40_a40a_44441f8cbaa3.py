"""Tilted Bottle with Liquid Drop.

Plan: Centerline6,6,42,42. Diagonal bottle with open lower-left mouth and detached falling drop; interior liquid kept clear.
Construction: Lucide droplet original/debug: pointed rounded drop. Deliberately asymmetric tilted open bottle.
Reduction: Rounded upper bottle corners simplified to short chamfers; liquid and separate drop retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3457d276-baf3-4a40-a40a-44441f8cbaa3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/50-3457d276-baf3-4a40-a40a-44441f8cbaa3.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'tilted-pouring-bottle'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('tilted', 'pouring', 'bottle')

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
        path('bottle',(18,25),[('L',(20,23)),('L',(20,17)),('L',(27,10)),('L',(31,6)),('L',(34,6)),('L',(42,14)),('L',(42,18)),('L',(35,25)),('L',(31,29)),('L',(27,29)),('L',(24,32))])
        path('liquid',(27,10),[('C',(35,25),(31,14),(27,21))]);join('bottle','liquid')
        path('drop',(10,31),[('C',(6,38),(8,34),(6,35)),('A',(14,38),4,4,False),('C',(10,31),(14,35),(12,34))],True)
