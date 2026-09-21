'overlapping-lapel-pea-coat. Plan: Short coat with paired sleeves and asymmetrical overlapping lapel. Keyshape: HRECT_L, exact SOLO48 bounds. Construction: Lucide shirt: simple continuous garment outline. Reduction: Removed secondary lapel notches; retained V lapels and a slightly offset center opening.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f03ab0c6-da99-45a0-a9ca-6050b49aee92'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/peacoat_f03ab0c6-da99-45a0-a9ca-6050b49aee92.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'overlapping-lapel-pea-coat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('coat', 'peacoat', 'lapels', 'clothing', 'winter', 'sleeves')

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
        path('coat',(16,8),[('L',(32,8)),('L',(38,14)),('L',(44,32)),('L',(34,32)),('L',(34,40)),('L',(14,40)),('L',(14,32)),('L',(4,32)),('L',(10,14)),('L',(16,8))],True)
        self.add_polyline('lapel',(16,8),(24,22),(32,8));self.relate('connect','coat','lapel')
        self.add_polyline('opening',(24,22),(22,28),(22,40));self.relate('connect','coat','opening');self.relate('connect','lapel','opening')
