"""Fresh Turmeric Root.

Plan: Organic branching rhizome with a broad vertical central stem and two right lobes; bounds (6,6)-(42,42).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Short skin creases removed; recognizability rests on the curved rhizome and two side lobes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '4e36033e-5958-4af8-aab6-b8c3ef160e17'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-005/references/14-4e36033e-5958-4af8-aab6-b8c3ef160e17.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'turmeric-root'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('turmeric', 'root')

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
        path('root',(14,42),[('C',(6,34),(9,42),(6,39)),('C',(17,18),(6,27),(15,23)),('L',(17,12)),('A',(29,12),6,6,True),('L',(29,19)),('C',(34,17),(31,19),(31,17)),('A',(42,25),8,8,True),('C',(28,30),(41,30),(32,30)),('L',(35,33)),('C',(35,42),(42,35),(40,42)),('C',(24,37),(30,42),(26,39)),('C',(14,42),(22,41),(18,42))],True)
