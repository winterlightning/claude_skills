"""Small Sitting Lizard Profile.

Plan: Lizard profile with rounded head and long back, curled tail and two bent legs; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Two bent underside limb cues retained; small scales and eyes omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '101b0aa0-e608-4a90-8f73-ee3d5636dc6e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-013/references/31-101b0aa0-e608-4a90-8f73-ee3d5636dc6e.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'lizard'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('lizard',)

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
        path('lizard',(22,40),[('C',(4,31),(10,40),(4,39)),('C',(24,14),(4,22),(15,15)),('C',(34,8),(28,13),(28,8)),('C',(44,13),(40,8),(44,10)),('C',(34,19),(44,18),(38,19)),('L',(29,29)),('L',(34,30))])
        path('tail',(22,40),[('C',(14,34),(18,39),(14,37)),('C',(21,29),(14,31),(18,29)),('L',(23,29)),('L',(23,32)),('L',(27,32))])
        join('lizard','tail')
