'closed-carton-with-front-tape-tab. Plan: Trapezoid carton lid, rectangular front and centered tape. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide package: shared panel seams. Reduction: Use a single tape stroke and plain front.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9fefb84d-51a5-48e9-a1e8-eda6bcef1e28'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/stuff_9fefb84d-51a5-48e9-a1e8-eda6bcef1e28.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-carton-with-front-tape-tab'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('carton', 'box', 'package', 'tape', 'storage', 'container')

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
        path('box',(4,20),[('L',(12,8)),('L',(36,8)),('L',(44,20)),('L',(44,36)),('A',(40,40),4,4,True),('L',(8,40)),('A',(4,36),4,4,True),('L',(4,20))],True)
        self.add_line('lid',(4,20),(44,20));self.relate('connect','box','lid')
        self.add_line('tape',(24,8),(24,28));self.relate('connect','box','tape');self.relate('connect','lid','tape')
