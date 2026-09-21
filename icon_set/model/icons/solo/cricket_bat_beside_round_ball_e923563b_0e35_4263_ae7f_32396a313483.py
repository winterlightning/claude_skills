"""Cricket Bat Beside Round Ball
Plan: Broad diagonal bat with narrow handle beside ball
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: No useful Lucide cricket match; source diagonal.
Reduction: Handle becomes single stroke; keep ball separate."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e923563b-0e35-4263-ae7f-32396a313483'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cricket_e923563b-0e35-4263-ae7f-32396a313483.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cricket-bat-beside-round-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('cricket', 'bat', 'ball', 'sport', 'equipment', 'blade', 'game')

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
        path('bat',(6,34),[('L',(26,14)),('L',(34,22)),('L',(14,42)),('C',(6,34),(6,42),(6,40))],True)
        self.add_line('handle',(30,18),(42,6));self.relate('connect','handle','bat')
        circle('ball',38,38,4)
