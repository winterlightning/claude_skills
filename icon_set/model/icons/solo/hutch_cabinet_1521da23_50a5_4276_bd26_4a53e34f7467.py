"""Storage Cabinet with Drawers and Door.

Plan: Hutch cabinet with three left compartments, tall right door and two legs; bounds (8,4)-(40,44).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Upper drawer pull omitted; three compartments and right door handle retained.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1521da23-50a5-4276-bd26-4a53e34f7467'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/33-1521da23-50a5-4276-bd26-4a53e34f7467.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'hutch-cabinet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    aliases = ()
    keywords = ('hutch', 'cabinet')

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
        poly('cabinet',(8,4),(24,4),(40,4),(40,36),(32,36),(24,36),(16,36),(8,36),(8,24),(8,14),closed=True)
        poly('partition',(24,4),(24,14),(24,24),(24,36));join('cabinet','partition')
        for j,y in enumerate((14,24)):
         line(f'shelf-{j}',(8,y),(24,y));join('cabinet',f'shelf-{j}');join('partition',f'shelf-{j}')
        line('leg-left',(16,36),(16,44));line('leg-right',(32,36),(32,44));join('cabinet','leg-left');join('cabinet','leg-right')
        line('handle',(32,18),(32,24))
