"""Three Acupuncture Needles.

Plan: Centerline4,8,44,40. Three equal hollow pin heads with a staggered center pin; upper/lower shafts fan from the left.
Construction: No useful direct Lucide match; repeated equal circular heads with true left cardinal attachment points.
Reduction: Middle pin shortened and outer shafts opened symmetrically to preserve three hollow heads with4u ink clearance.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2a9825e4-53aa-42cd-9b85-3cf1cc9cdb2d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-019/references/45-2a9825e4-53aa-42cd-9b85-3cf1cc9cdb2d.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'three-round-head-pins'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('three', 'round', 'head', 'pins')

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
        for name,x,y in [('upper',40,12),('middle',23,24),('lower',40,36)]:
         circle(name,x,y,4)
        line('shaft-upper',(4,8),(36,12));line('shaft-middle',(4,24),(19,24));line('shaft-lower',(4,40),(36,36))
        for n in ('upper','middle','lower'):join(n,f'shaft-{n}')
