'hanger-with-inner-trouser-bar. Plan: Rounded triangular hanger and hooked neck; inner bar. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: No useful Lucide match; paired shoulders and broad arc hook. Reduction: Shortened the separate trouser bar to retain certified clearance inside the hanger.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c523587-9090-4f12-8e9f-a33582451d43'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_11/clothes_2c523587-9090-4f12-8e9f-a33582451d43.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hanger-with-inner-trouser-bar'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('hanger', 'clothes', 'hook', 'bar', 'wardrobe', 'garment', 'storage')

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
        path('hanger',(24,20),[('L',(6,32)),('C',(4,36),(4,33),(4,34)),('A',(8,40),4,4,False),('L',(40,40)),('A',(44,36),4,4,False),('C',(42,32),(44,34),(44,33)),('L',(24,20))],True)
        path('hook',(18,14),[('A',(30,14),6,6,True),('A',(24,20),6,6,True)]);self.relate('connect','hanger','hook')
        self.add_line('bar',(22,31),(26,31))
