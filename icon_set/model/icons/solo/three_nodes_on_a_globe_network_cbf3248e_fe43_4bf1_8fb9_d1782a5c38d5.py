"""Three Nodes on a Globe Network
Plan: Globe boundary with three circular network nodes and curved links
Keyshape CIRCLE: (2, 2, 46, 46).
Construction reference: Lucide network attachment logic.
Reduction: Reduce globe mesh to three major links."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cbf3248e-fe43-4bf1-8fb9-d1782a5c38d5'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon cloud front_cbf3248e-fe43-4bf1-8fb9-d1782a5c38d5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-nodes-on-a-globe-network'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('globe', 'network', 'nodes', 'connections', 'world', 'circle', 'topology')

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
        circle('globe',24,24,20)
        for name,x,y in [('a',16,20),('b',32,20),('c',24,32)]:circle(name,x,y,2)
        path('ab',(18,20),[('C',(30,20),(22,16),(26,16))]);self.relate('connect','ab','a');self.relate('connect','ab','b')
        path('ac',(16,22),[('C',(22,32),(16,28),(18,32))]);self.relate('connect','ac','a');self.relate('connect','ac','c')
        path('edge',(24,34),[('L',(24,44))]);self.relate('connect','edge','c');self.relate('connect','edge','globe')
