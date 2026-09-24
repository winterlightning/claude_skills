"""Oatmeal Bowl and Spoon
Plan: Deep bowl with a simple oatmeal mound and a spoon angling up-right.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide soup: spoon above the bowl.
Reduction: Omitted narrow foot and grain marks; kept food mound and spoon.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '683a2acb-7114-4e54-a1d8-6e9238c88f36'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/oatmeal_683a2acb-7114-4e54-a1d8-6e9238c88f36.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'oatmeal-bowl-spoon'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    aliases = ()
    keywords = ('oatmeal', 'bowl', 'spoon', 'breakfast', 'porridge', 'food')

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
        path('bowl',(6,26),[('L',(10,26)),('L',(35,26)),('L',(36,26)),('L',(42,26)),('C',(24,42),(41,38),(34,42)),('C',(6,26),(14,42),(7,38))],True)
        path('oatmeal',(10,26),[('C',(22,15),(10,18),(16,15)),('C',(35,26),(29,15),(34,20))])
        for m in ['bowl-0','bowl-1']:self.relate('connect','oatmeal-0',m)
        for m in ['bowl-1','bowl-2']:self.relate('connect','oatmeal-1',m)
        self.relate('connect','spoon','bowl-2');self.relate('connect','spoon','bowl-3')
        self.add_line('spoon',(36,26),(42,6))
