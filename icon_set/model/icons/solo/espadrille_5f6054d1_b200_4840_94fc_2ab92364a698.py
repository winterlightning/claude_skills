"""Canvas Espadrille Shoe.

Plan: Slip-on shoe with low left heel and right round toe, broad sole8 high and tongue; x4..44 y10..38.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: No texture; sole seam and raised tongue retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f6054d1-b200-4840-94fc-2ab92364a698'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/28-5f6054d1-b200-4840-94fc-2ab92364a698.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'espadrille'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('espadrille',)

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
        path('upper',(4,30),[('L',(4,14)),('C',(20,18),(9,18),(15,18)),('C',(20,10),(16,14),(16,10)),('C',(36,22),(24,10),(28,19)),('A',(44,30),8,8,True),('L',(4,30))],True)
        path('sole',(4,30),[('L',(4,34)),('A',(8,38),4,4,False),('L',(40,38)),('A',(44,34),4,4,False),('L',(44,30))]);join('sole','upper')
