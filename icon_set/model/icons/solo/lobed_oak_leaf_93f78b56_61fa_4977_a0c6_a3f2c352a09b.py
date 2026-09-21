"""Lobed Oak Leaf
Plan: Upright lobed oak leaf with central stem.
Keyshape: VRECT_L; exact inset SOLO48 envelope.
Construction: Lucide leaf: continuous stem through broad silhouette.
Reduction: None."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '93f78b56-61fa-4977-a0c6-a3f2c352a09b'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_28/oak_93f78b56-61fa-4977-a0c6-a3f2c352a09b.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'lobed-oak-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('oak', 'leaf', 'lobes', 'tree', 'plant', 'botanical')

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
        # Shared x12 axis owns both sides of the pin, neck width and bulbous base.
        path('leaf',(24,39),[('C',(8,27),(16,36),(8,33)),('C',(13,20),(8,23),(8,19)),('C',(16,12),(8,11),(11,8)),('A',(24,4),8,8,True),('A',(32,12),8,8,True),('C',(35,20),(37,8),(40,11)),('C',(40,27),(40,19),(40,23)),('C',(24,39),(40,33),(32,36))],True)
        self.add_line('vein',(24,17),(24,44));self.relate('connect','leaf','vein')
