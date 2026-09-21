'overlapping-tragedy-and-comedy-masks. Plan: Front tragedy mask and partially occluded rear comedy mask. Keyshape: SQUARE, exact SOLO48 bounds. Construction: Shared human reference: smooth circular face curves; masks retain theatrical shape. Reduction: Omitted eyes, retained opposing mouth curves; tapered front mask exposes more of rear comedy face.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e22cd911-73e7-45a5-9477-67b78f533035'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_26/masks theater_e22cd911-73e7-45a5-9477-67b78f533035.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'overlapping-tragedy-and-comedy-masks'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('masks', 'theater', 'comedy', 'tragedy', 'faces', 'drama', 'performance')

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
        path('front',(6,6),[('L',(30,6)),('L',(30,14)),('C',(18,30),(30,22),(24,28)),('C',(6,14),(12,28),(6,22)),('L',(6,6))],True)
        path('rear',(30,18),[('L',(42,18)),('L',(42,30)),('A',(30,42),12,12,True),('A',(18,30),12,12,True)]);self.relate('connect','front','rear')
        path('frown',(16,18),[('C',(20,18),(17,15),(19,15))])
        path('smile',(30,32),[('C',(33,32),(31,34),(32,34))])
