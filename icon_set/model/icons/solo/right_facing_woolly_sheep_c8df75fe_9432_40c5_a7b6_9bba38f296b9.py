"""Right-Facing Woolly Sheep
Plan: Continuous right-facing sheep, scalloped wool, muzzle and two legs.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: No direct match; shared leg widths and scalloped contour.
Reduction: Tiny eye and ear fold omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c8df75fe-9432-40c5-a7b6-9bba38f296b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/mutton_c8df75fe-9432-40c5-a7b6-9bba38f296b9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'right-facing-woolly-sheep'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('sheep', 'wool', 'livestock', 'animal', 'farm', 'mammal')

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
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('sheep',(4,23),[('C',(10,15),(4,17),(6,15)),('C',(20,14),(12,10),(17,11)),('C',(29,12),(24,10),(26,10)),('C',(34,8),(30,8),(32,8)),('C',(44,20),(40,8),(44,16)),('C',(36,24),(44,25),(40,24)),('L',(35,40)),('L',(27,40)),('L',(27,30)),('C',(14,31),(22,33),(18,33)),('L',(13,40)),('L',(5,40)),('L',(5,29)),('C',(4,23),(4,28),(4,25))],True)
