"""Sun Behind Cloud.

Plan: Partly cloudy scene with exposed sun arc, lobed cloud and one diagonal ray; bounds (6,6)-(42,42).
Construction: Lucide cloud-sun: the visible sun arc ends at actual cloud occlusion nodes.
Reduction: Three rays reduced to one; sun and cloud remain a natural weather scene.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6f54dfef-a732-45c0-83af-be8ae5456b79'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/50-6f54dfef-a732-45c0-83af-be8ae5456b79.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'partly-cloudy'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('partly', 'cloudy')

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
        path('cloud',(8,24),[('A',(24,8),16,16,False),('C',(38,24),(33,8),(38,15)),('A',(42,32),4,8,True),('A',(32,42),10,10,True),('L',(16,42)),('A',(6,32),10,10,True),('C',(8,24),(6,28),(6,26))],True);join('sun','cloud')
        line('ray',(6,6),(7,7))
