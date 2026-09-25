"""Curved Soy Pod with Two Seeds
Plan: Curved vertical pod with two separate seed openings and short stem.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Pod rebalanced diagonally; two seed openings retained and normalized to circles.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6436c37f-dede-41c3-b03d-3c1b6a4b1db6'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_35/soy_6436c37f-dede-41c3-b03d-3c1b6a4b1db6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-soy-pod-with-two-seeds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('soy', 'pod', 'seeds', 'legume', 'plant', 'food')

    def build(self):
        def path(name, start, commands, closed=False):
            here = start
            members = []
            for index, (kind, end, *args) in enumerate(commands):
                member = f"{name}-{index}"
                if kind == 'L': self.add_line(member, here, end)
                elif kind == 'A': self.add_arc(member, here, end, radius_x=args[0], radius_y=args[1], sweep=args[2], large_arc=args[3] if len(args)>3 else False)
                elif kind == 'C': self.add_bezier(member, here, (args[0], args[1], end))
                members.append(member)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, x, y, r):
            path(name, (x-r,y), [('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)], True)
        def rect(name, x, y, w, h, r=0):
            if not r:
                self.add_polyline(name,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True)
            else:
                path(name,(x+r,y), [('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        path('pod',(6,42),[('C',(6,25),(6,35),(6,30)),('C',(14,15),(6,19),(10,15)),('C',(24,9),(17,15),(18,10)),('C',(42,21),(35,9),(42,10)),('C',(28,39),(42,32),(36,37)),('C',(6,42),(20,42),(12,42))],True)
        path('stem',(24,9),[('C',(26,6),(26,9),(26,7))]);self.relate('connect','stem','pod')
        circle('upper-seed',30,22,3);circle('lower-seed',18,30,3)
