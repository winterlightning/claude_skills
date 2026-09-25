'hanger-with-hanging-garment. Plan: Hanger above rectangular hanging garment; shared bottom rail. Keyshape: SQUARE, exact SOLO48 bounds. Construction: No useful Lucide match; mirrored triangle and hook. Reduction: Omit rounded tiny corners, preserve hanging cloth.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a8d34e2a-aa59-4609-8339-2e44582330ee'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/checkroom_a8d34e2a-aa59-4609-8339-2e44582330ee.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hanger-with-hanging-garment'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('hanger', 'garment', 'clothes', 'hook', 'wardrobe', 'laundry', 'storage')

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
        self.add_polyline('hanger',(6,26),(24,14),(42,26),(6,26),closed=True)
        path('hook',(20,10),[('A',(28,10),4,4,True),('A',(24,14),4,4,True)]);self.relate('connect','hanger','hook')
        path('garment',(14,26),[('L',(14,38)),('A',(18,42),4,4,False),('L',(30,42)),('A',(34,38),4,4,False),('L',(34,26))]);self.relate('connect','hanger','garment')
