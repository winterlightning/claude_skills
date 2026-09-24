"""Smartphone Double Tap Gesture.

Plan: Phone with physical tapping hand and one quarter-round contact arc; bounds (6,6)-(42,42).
Construction: Lucide hand: coherent finger/palm outline; phone contact is a physical scene.
Reduction: Two concentric tap arcs reduced to one; index finger, palm and phone silhouette retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f5462084-18e8-4a32-940d-898d288894e7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/34-f5462084-18e8-4a32-940d-898d288894e7.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'finger-touching-smartphone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('finger', 'touching', 'smartphone')

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
        path('phone',(38,14),[('L',(38,10)),('A',(34,6),4,4,False),('L',(10,6)),('A',(6,10),4,4,False),('L',(6,38)),('A',(10,42),4,4,False),('L',(17,42))])
        poly('hand',(42,42),(42,34),(34,26),(26,26),(26,34),(34,42))
        path('tap',(16,26),[('A',(26,16),10,10,True)])
