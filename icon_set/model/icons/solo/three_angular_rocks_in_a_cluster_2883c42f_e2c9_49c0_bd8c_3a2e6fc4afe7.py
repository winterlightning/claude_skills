'three-angular-rocks-in-a-cluster. Plan: Tall rear rock and two smaller polygon stones with shared boundaries. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: No useful Lucide match; coherent polygon contours. Reduction: Remove tiny triangular foreground chip, keep three main rocks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2883c42f-e2c9-49c0-bd8c-3a2e6fc4afe7'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_06/bedrock_2883c42f-e2c9-49c0-bd8c-3a2e6fc4afe7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-angular-rocks-in-a-cluster'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('rocks', 'stones', 'cluster', 'jagged', 'geology', 'bedrock', 'nature')

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
        self.add_polyline('rear',(12,24),(16,12),(24,8),(34,14),(38,24),(30,40),(20,40),(12,24),closed=True)
        self.add_polyline('left',(12,24),(6,28),(4,40),(20,40));self.relate('connect','rear','left')
        self.add_polyline('right',(38,24),(42,28),(44,40),(30,40));self.relate('connect','rear','right')
