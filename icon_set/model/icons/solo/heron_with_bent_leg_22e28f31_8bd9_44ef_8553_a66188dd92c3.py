"""Standing Heron Bird.

Plan: Heron with curved open neck and head, pointed beak, leaflike body and two long crossing legs; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Neck and beak reduced to one flowing stroke; folded body and bent stilt leg retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '22e28f31-8bd9-44ef-8553-a66188dd92c3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/25-22e28f31-8bd9-44ef-8553-a66188dd92c3.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'heron-with-bent-leg'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('heron', 'with', 'bent', 'leg')

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
        path('body',(8,30),[('C',(22,18),(14,20),(18,18)),('C',(32,24),(28,18),(32,21)),('C',(28,30),(32,27),(30,30)),('L',(18,30)),('L',(8,30))],True)
        path('neck',(22,18),[('C',(24,10),(28,18),(22,13)),('A',(30,4),6,6,True),('L',(40,9))]);join('body','neck')
        poly('straight-leg',(28,30),(28,38),(28,44));poly('bent-leg',(18,30),(14,38),(28,38),(38,38),(38,44));join('body','straight-leg');join('body','bent-leg');join('straight-leg','bent-leg')
