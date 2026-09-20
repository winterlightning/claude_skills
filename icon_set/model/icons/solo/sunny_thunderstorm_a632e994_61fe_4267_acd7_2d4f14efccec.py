"""Sun and Thunderstorm Cloud.

Plan: Sun partly occluded by an open-bottom cloud over a broad lightning stroke; bounds (6,6)-(42,42).
Construction: Lucide cloud-sun: partially occluded sun and a coherent cloud outline; lightning follows source weather scene.
Reduction: Two lightning strokes reduced to one broad bolt; three sun rays reduced to one.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a632e994-61fe-4267-acd7-2d4f14efccec'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/49-a632e994-61fe-4267-acd7-2d4f14efccec.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'sunny-thunderstorm'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('sunny', 'thunderstorm')

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
        self.add_arc('sun',(8,24),(24,8),radius_x=16,radius_y=16,sweep=True)
        path('cloud',(6,24),[('L',(8,24)),('A',(24,8),16,16,False),('C',(34,16),(30,8),(34,11)),('A',(42,24),8,8,True)]);join('sun','cloud')
        poly('lightning',(30,24),(12,33),(30,33),(12,42))
        line('ray',(6,6),(7,7))
