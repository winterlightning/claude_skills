"""Heaped Rice Bowl
Plan: Rice heap rises above a bowl; three tiny grain strokes establish its contents.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide soup: simple bowl with legible food details.
Reduction: Omitted the narrow foot and double rim.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b7c4dc76-e827-414b-a98e-ca40accd9e03'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_30/pilaf_b7c4dc76-e827-414b-a98e-ca40accd9e03.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'heaped-rice-bowl'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    aliases = ()
    keywords = ('rice', 'bowl', 'food', 'meal', 'grains', 'heap')

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
        path('bowl',(4,29),[('L',(8,29)),('L',(40,29)),('L',(44,29)),('C',(24,40),(43,37),(33,40)),('C',(4,29),(15,40),(5,37))],True)
        path('rice',(8,29),[('C',(16,15),(8,18),(10,15)),('C',(24,8),(17,10),(19,8)),('C',(32,15),(29,8),(31,10)),('C',(40,29),(38,15),(40,18))])
        for m in ['bowl-0','bowl-1']:self.relate('connect','rice-0',m)
        for m in ['bowl-1','bowl-2']:self.relate('connect','rice-3',m)
        self.add_line('grain',(23,19),(25,19))
