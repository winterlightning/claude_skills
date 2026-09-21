"""Bird on Straight Perch
Plan: Right-facing bird with a pointed beak, downward tail, one foot and a horizontal perch.
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: Lucide bird: flowing back and long tail.
Reduction: Omitted internal wing and tiny eye; kept head, beak, tail and foot on perch.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95f36efc-1966-49b5-978a-2938622f39c8'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/perch_95f36efc-1966-49b5-978a-2938622f39c8.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bird-straight-perch'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    aliases = ()
    keywords = ('bird', 'perch', 'branch', 'wing', 'tail', 'wildlife')

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
        path('bird',(8,36),[('L',(19,15)),('C',(24,8),(20,12),(20,8)),('A',(36,8),6,4,True),('L',(40,12)),('L',(35,16)),('C',(21,32),(35,27),(29,32)),('L',(15,32)),('L',(8,36))],True)
        self.add_polyline('leg',(21,32),(25,44),(40,44))
        self.add_line('perch-left',(14,44),(25,44))
        self.relate('connect','bird-5','leg-1');self.relate('connect','bird-6','leg-1')
        self.relate('connect','leg-1','perch-left');self.relate('connect','leg-2','perch-left')
