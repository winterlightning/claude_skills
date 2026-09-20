"""Gripping Hand Gesture.

Plan: Closed fist with four repeated knuckle lobes and folded thumb contour; bounds (6,6)-(42,42).
Construction: Lucide hand: repeat finger radii and a broad rounded palm; reauthored as a clenched fist.
Reduction: No identifying parts omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5972302f-f4e3-4809-adcf-7d3a8633b8a6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/42-5972302f-f4e3-4809-adcf-7d3a8633b8a6.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'compact-closed-fist'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('compact', 'closed', 'fist')

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
        path('fist',(6,24),[('C',(10,17),(6,20),(7,17)),('L',(10,10)),('A',(18,10),4,4,True),('A',(26,10),4,4,True),('A',(34,10),4,4,True),('A',(42,10),4,4,True),('L',(42,28)),('A',(28,42),14,14,True),('L',(20,42)),('A',(6,28),14,14,True),('L',(6,24))],True)
        path('thumb',(10,17),[('L',(18,17)),('A',(18,27),5,5,True),('L',(15,27))]);join('fist','thumb')
