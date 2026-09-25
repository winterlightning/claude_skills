"""Classic Y-Shaped Slingshot.

Plan: Symmetric broad Y slingshot with curved band, shared prong nodes. Extremes 10,4,38,44.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Unify capped prongs with band junctions; retain fork and slack band.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '51b2a504-e04e-5984-a428-60dc7adda2b1'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-021/references/39-51b2a504-e04e-5984-a428-60dc7adda2b1.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'y-shaped-slingshot'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "video-games"
    aliases = ()
    keywords = ('y', 'shaped', 'slingshot')

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
        path('body',(10,4),[('L',(10,15)),('C',(19,29),(10,22),(14,25)),('L',(19,44)),('L',(29,44)),('L',(29,29)),('C',(38,15),(34,25),(38,22)),('L',(38,4))])
        path('band',(10,4),[('C',(38,4),(10,15),(38,15))]);join('body','band')
