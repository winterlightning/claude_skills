"""Car Wheel with Spokes.

Plan: Wheel tire r20 around rimr11; cross-shaped four-spoke hub forms one actual central junction.
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Reduced eight spokes to four and represented hub as central cross junction; separate circular hub omitted.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f3ad62b8-1f6b-4bc2-9a4a-787d847ac0fa'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-002/references/29-f3ad62b8-1f6b-4bc2-9a4a-787d847ac0fa.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'spoked-wheel'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ()
    keywords = ('spoked', 'wheel')

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
        circle('tire',24,24,20)
        circle('rim',24,24,11)
        line('horizontal-spokes',(13,24),(35,24));join('horizontal-spokes','rim')
        line('vertical-spokes',(24,13),(24,35));join('vertical-spokes','rim');join('horizontal-spokes','vertical-spokes')
