"""Finger Tapping Destination Spot.

Plan: Pointing hand with separate destination X and a route curve. Extremes 6,6,42,42.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Finger and destination remain the interaction subject; short route avoids tiny source detail.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e54a956-814a-4581-8d3c-be1a087ebdba'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/23-4e54a956-814a-4581-8d3c-be1a087ebdba.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'finger-selecting-map-destination'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('finger', 'selecting', 'map', 'destination')

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
        path('hand',(19,42),[('L',(12,32)),('C',(18,27),(9,27),(14,23)),('L',(22,31)),('L',(22,26)),('A',(30,26),4,4,True),('L',(30,32)),('L',(34,32)),('A',(42,40),8,8,True),('L',(42,42))])
        poly('destination-a',(24,6),(32,12));poly('destination-b',(32,6),(24,12));join('destination-a','destination-b')
        path('route',(6,18),[('C',(16,9),(6,14),(10,11))])
