"""Tracked Bulldozer with Front Blade
Plan: Track capsule, raised cab and front blade
Keyshape HRECT_L: (2, 6, 46, 42).
Construction reference: Lucide construction and truck silhouette.
Reduction: Remove track rollers and tiny cab details."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd0f99117-6bd5-4d22-aa8c-bb2c7264ee3a'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_08/bulldozer_d0f99117-6bd5-4d22-aa8c-bb2c7264ee3a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'tracked-bulldozer-with-front-blade'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('bulldozer', 'construction', 'tracks', 'blade', 'vehicle', 'machine', 'earthmoving')

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
        rect('track',4,30,24,10,5)
        path('cab',(8,30),[('L',(8,8)),('L',(24,8)),('L',(24,20)),('L',(32,20)),('L',(28,30))]);self.relate('connect','cab','track')
        self.add_line('arm',(28,30),(40,30));self.relate('connect','arm','track')
        path('blade',(44,16),[('C',(40,40),(42,22),(40,34)),('L',(44,40))]);self.relate('connect','blade','arm')
