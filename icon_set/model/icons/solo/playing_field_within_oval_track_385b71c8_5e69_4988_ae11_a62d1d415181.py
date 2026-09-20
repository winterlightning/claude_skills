"""Sports Stadium Field.

Plan: Oval running track around rectangular pitch with central halfway line; bounds (4,8)-(44,40).
Construction: No useful direct Lucide match; coherent arcs and shared endpoints.
Reduction: Center circle omitted to retain a clear pitch inside the oval track.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '385b71c8-5e69-4988-ae11-a62d1d415181'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/icon_set/.local/work/solo-saved-briefs-20260920/batch-folders/batch-014/references/11-385b71c8-5e69-4988-ae11-a62d1d415181.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'playing-field-within-oval-track'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('playing', 'field', 'within', 'oval', 'track')

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
        path('track',(20,8),[('L',(28,8)),('A',(44,24),16,16,True),('A',(28,40),16,16,True),('L',(20,40)),('A',(4,24),16,16,True),('A',(20,8),16,16,True)],True)
        poly('pitch',(16,18),(24,18),(32,18),(32,30),(24,30),(16,30),closed=True)
        line('halfway',(24,18),(24,30));join('pitch','halfway')
