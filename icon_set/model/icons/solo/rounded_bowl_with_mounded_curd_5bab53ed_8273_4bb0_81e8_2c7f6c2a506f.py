"""Rounded Bowl with Mounded Curd
Plan: Wide bowl below one rounded three-lobed heap of curd.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide soup: broad bowl silhouette.
Reduction: No interior texture or narrow foot; retained mounded food.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5bab53ed-8273-4bb0-81e8-2c7f6c2a506f'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/curd_5bab53ed-8273-4bb0-81e8-2c7f6c2a506f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rounded-bowl-with-mounded-curd'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bowl', 'curd', 'food', 'dairy', 'mound', 'dish', 'meal')

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
        path('bowl',(4,24),[('L',(10,24)),('L',(38,24)),('L',(44,24)),('C',(24,40),(44,35),(34,40)),('C',(4,24),(14,40),(4,35))],True)
        path('curd',(10,24),[('C',(17,14),(10,16),(11,14)),('C',(31,14),(20,6),(28,6)),('C',(38,24),(37,14),(38,16))])
        for m in ['bowl-0','bowl-1']:self.relate('connect','curd-0',m)
        for m in ['bowl-1','bowl-2']:self.relate('connect','curd-2',m)
