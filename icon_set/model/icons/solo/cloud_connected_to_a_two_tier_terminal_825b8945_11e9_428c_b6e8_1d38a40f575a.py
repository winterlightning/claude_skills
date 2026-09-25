'cloud-connected-to-a-two-tier-terminal. Plan: Open cloud above two-tier terminal with two leads and node dots. Keyshape: SQUARE, exact SOLO48 bounds. Construction: Lucide cloud: smooth broad lobes. Reduction: Reduced two terminal tiers to one broad terminal bar and node rings to line ends; unequal lead heights remain.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '825b8945-11e9-428c-b6e8-1d38a40f575a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_02/amazon web service direct connect_825b8945-11e9-428c-b6e8-1d38a40f575a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloud-connected-to-a-two-tier-terminal'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('cloud', 'network', 'terminal', 'connection', 'nodes', 'computing', 'server')

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
        path('cloud',(10,24),[('C',(6,16),(6,22),(6,20)),('C',(18,6),(6,10),(12,6)),('C',(30,12),(24,6),(28,8)),('C',(42,18),(38,8),(42,12)),('C',(38,24),(42,22),(40,24))])
        rect('terminal',10,34,28,8,2)
        for x,y in [(19,18),(29,24)]:
         self.add_line(f'lead-{x}',(x,y),(x,34));self.relate('connect','terminal',f'lead-{x}')
