"""Seven-Node Branching Network
Plan: Seven equal circular nodes on three levels; shared link endpoints
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide network connection pattern.
Reduction: Use small circular node openings, preserve seven-node branching."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e26a4f4-095f-4d57-81a8-24d0a087aefc'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon web service batch_2e26a4f4-095f-4d57-81a8-24d0a087aefc.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seven-node-branching-network'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('network', 'nodes', 'branch', 'tree', 'connections', 'topology', 'circles')

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
        positions=[(24,9),(9,24),(24,24),(39,24),(9,39),(24,39),(39,39)]
        for i,(x,y) in enumerate(positions):circle(f'node-{i}',x,y,3)
        for i,(a,b) in enumerate(((0,2),(1,2),(2,3),(1,4),(2,5),(3,6))):
            ax,ay=positions[a];bx,by=positions[b]
            if ax==bx: start=(ax,ay+3);end=(bx,by-3)
            else:start=(ax+3,ay);end=(bx-3,by)
            self.add_line(f'link-{i}',start,end);self.relate('connect',f'link-{i}',f'node-{a}');self.relate('connect',f'link-{i}',f'node-{b}')
