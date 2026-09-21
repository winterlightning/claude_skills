'closed-paperback-curved-spine. Plan: Blank paperback cover with curved projecting page block. Keyshape: VRECT_L, exact SOLO48 bounds. Construction: Lucide book: spine curve continuous into lower edge. Reduction: Keep page block; reduce corner differences to stable rounded spine.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5fad364e-3e96-45bb-b946-4a64300956cb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_29/paperback_5fad364e-3e96-45bb-b946-4a64300956cb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'closed-paperback-curved-spine'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('paperback', 'book', 'cover', 'spine', 'pages', 'reading')

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
        path('outline',(16,4),[('L',(40,4)),('L',(40,28)),('L',(36,28)),('L',(36,44)),('L',(16,44)),('A',(8,36),8,8,True),('L',(8,12)),('A',(16,4),8,8,True)],True)
        path('pages',(8,36),[('A',(16,28),8,8,True),('L',(40,28))]);self.relate('connect','outline','pages')
