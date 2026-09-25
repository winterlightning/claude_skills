"""Ham Leg with Bone.

Plan: Ham with rounded meat, central cut bone and broad lobed upper-right bone; bounds (6,6)-(42,42).
Construction: Lucide drumstick: rounded meat silhouette and protruding bone connected at exact nodes.
Reduction: Cut-face rings reduced to one central bone; protruding bone widened for legal clearances.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fd7ba626-c30a-4140-8bc3-a2f36f3e9b70'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/48-fd7ba626-c30a-4140-8bc3-a2f36f3e9b70.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'ham-leg-with-exposed-bone'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('ham', 'leg', 'with', 'exposed', 'bone')

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
        path('meat',(6,27),[('C',(26,14),(6,17),(16,14)),('L',(34,22)),('C',(27,42),(34,30),(35,42)),('C',(6,27),(15,42),(6,38))],True)
        circle('cut',20,29,4)
        path('bone',(26,14),[('L',(32,10)),('A',(40,10),4,4,True),('C',(42,14),(42,10),(42,12)),('C',(38,18),(42,16),(40,18)),('L',(34,22))]);join('bone','meat')
