"""Round Bomb with Spark
Plan: Round bomb at lower-left with a fuse curving toward a detached spark at upper-right.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide bomb: circular body and angled fuse.
Reduction: Spark reduced to three detached rays; neck integrated into fuse.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '334f5976-14a0-49e2-9421-a907055410d4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bomber_334f5976-14a0-49e2-9421-a907055410d4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'round-bomb-with-spark'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bomb', 'fuse', 'spark', 'explosive', 'round', 'lit', 'ordnance')

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
        circle('bomb',20,28,14)
        path('fuse',(20,14),[('C',(28,10),(20,6),(25,5))])
        self.relate('connect','fuse-0','bomb-0');self.relate('connect','fuse-0','bomb-1')
        self.add_polyline('spark',(38,6),(38,10),(42,10))
        self.add_line('spark-bottom',(38,10),(38,14))
        self.relate('connect','spark-1','spark-bottom');self.relate('connect','spark-2','spark-bottom')
