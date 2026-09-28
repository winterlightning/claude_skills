"""Bowl of Curled Coleslaw
Plan: Straight-rim bowl with three loose cabbage curls above it.
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide soup: bowl silhouette and separate food strokes.
Reduction: Reduced many strips to three broad curls.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d6010e3-0f0e-4eff-be58-e66150706645'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/coleslaw_9d6010e3-0f0e-4eff-be58-e66150706645.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bowl-of-curled-coleslaw'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'food'
    aliases = ()
    keywords = ('coleslaw', 'bowl', 'salad', 'cabbage', 'food', 'strips', 'meal')

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
        path('bowl',(4,27),[('L',(44,27)),('C',(32,40),(43,35),(37,39)),('L',(16,40)),('C',(4,27),(11,39),(5,35))],True)
        # Loose cabbage curls vary in orientation; upright repeated waves read as steam.
        path('cabbage-left',(8,17),[('C',(16,17),(8,11),(16,11))])
        path('cabbage-center',(24,8),[('C',(28,8),(24,12),(28,12))])
        path('cabbage-right',(35,17),[('C',(40,17),(35,11),(40,11))])
