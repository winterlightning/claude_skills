"""Three Rounded Network Nodes
Plan: Three equal rounded square nodes joined by T
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide network.
Reduction: Drop decorative interior; preserve hierarchy."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7fc82a76-4203-44f5-8197-fbc82ad8dca3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_15/distributor_7fc82a76-4203-44f5-8197-fbc82ad8dca3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-rounded-network-nodes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('network', 'nodes', 'connection', 'diagram', 'branch', 'link', 'structure')

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
        rect('top',18,6,12,10,2);rect('left',6,32,12,10,2);rect('right',30,32,12,10,2)
        self.add_line('stem',(24,16),(24,24));path('branch',(12,32),[('L',(12,24)),('L',(36,24)),('L',(36,32))])
        self.relate('connect','stem','top');self.relate('connect','stem','branch');self.relate('connect','branch','left');self.relate('connect','branch','right')
