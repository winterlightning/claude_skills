"""Angular Three-Feather Shuttlecock
Plan: Diagonal shuttlecock with cork and three feather panels.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Three stepped feather tips and cork retained; interior feather rib lines omitted after spacing review.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '333bdaa8-d257-4ba8-bc29-0f4cd1e2c1ae'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/badminton shuttlecock_333bdaa8-d257-4ba8-bc29-0f4cd1e2c1ae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'angular-three-feather-shuttlecock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('shuttlecock', 'badminton', 'feathers', 'cork', 'sport', 'fan', 'angular')

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
        path('cork',(6,34),[('A',(14,42),8,8,False),('A',(22,34),8,8,False),('L',(14,26)),('L',(6,34))],True)
        self.add_polyline('feathers',(14,26),(22,6),(30,8),(32,16),(40,18),(42,28),(22,34));self.relate('connect','feathers','cork')
        # Three stepped feather tips retained; internal ribs omitted for clearance.
