"""Cricket Batter with Raised Bat
Plan: Bent-leg batter holding raised diagonal bat
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: human_ref/full_body_ref.png; exact detached gap.
Reduction: Single-stroke bat; preserve raised arms and bent legs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1f09cd41-0bfa-474e-aa21-4f4bf44d8ab4'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_13/cricketer_1f09cd41-0bfa-474e-aa21-4f4bf44d8ab4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cricket-batter-with-raised-bat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('cricket', 'batter', 'player', 'bat', 'sport', 'person', 'stance')

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
        path('head',(10,12),[('A',(22,12),6,6,True),('A',(10,12),6,6,True)],True)
        self.add_line('torso',(16,26),(16,36))
        path('legs',(6,42),[('L',(10,38)),('L',(16,36)),('L',(24,38)),('L',(28,42))]);self.relate('connect','legs','torso')
        path('arms',(16,26),[('L',(28,26)),('L',(30,20))]);self.relate('connect','arms','torso')
        self.add_line('bat',(30,20),(42,6));self.relate('connect','bat','arms')
        self.mark_human_figure('batter',head='head',torso='torso',torso_junction='start')

# Final review: Head center (16,12), radius6; neck (16,26), exact 8 centerline / 4 ink gap. Keep raised bat and bent legs with clear arm-to-leg spacing.
