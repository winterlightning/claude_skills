"""Linked Square Network
Plan: Six square nodes in two linked rows; rows reduced to fit clear node openings
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide network square nodes.
Reduction: Retain six nodes, reduce chain to readable orthogonal connections."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f228f910-7628-4523-9b12-97555f48ba01'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/block chain_f228f910-7628-4523-9b12-97555f48ba01.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'linked-square-network'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('network', 'blocks', 'nodes', 'connections', 'blockchain', 'squares', 'diagram')

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
        positions=[(4,10),(20,10),(36,10),(4,30),(20,30),(36,30)]
        for i,(x,y) in enumerate(positions):rect(f'node-{i}',x,y,8,8)
        for i,(a,b,start,end) in enumerate(((0,1,(12,14),(20,14)),(1,2,(28,14),(36,14)),(0,3,(8,18),(8,30)),(3,4,(12,34),(20,34)),(4,5,(28,34),(36,34)))):
            self.add_line(f'link-{i}',start,end);self.relate('connect',f'link-{i}',f'node-{a}');self.relate('connect',f'link-{i}',f'node-{b}')

# Final review: Six nodes retained in two rows instead of three staggered levels so all square openings and links remain clear.
