"""Trowel beside Unfinished Brick Wall
Plan: Unfinished brick wall on left and bottom; trowel at upper-right is a physical companion tool.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide brick-wall: minimal courses and attached joints.
Reduction: Reduced wall courses and trowel handle to one stroke; kept triangular blade.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '838089d0-2c44-4425-80d7-6b79b53a0caf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/construction brick_838089d0-2c44-4425-80d7-6b79b53a0caf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'trowel-beside-unfinished-brick-wall'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects/construction'
    aliases = ()
    keywords = ('bricks', 'wall', 'trowel', 'masonry', 'construction', 'tool', 'building')

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
        self.add_polyline('wall',(6,6),(18,6),(18,30),(42,30),(42,42),(6,42),(6,6))
        self.add_line('course',(6,18),(18,18));self.relate('connect','course','wall-2');self.relate('connect','course','wall-6')
        self.add_line('joint',(24,30),(24,42));self.relate('connect','joint','wall-3');self.relate('connect','joint','wall-5')
        self.add_polyline('blade',(27,20),(35,12),(40,22),closed=True)
        self.add_line('handle',(35,12),(42,6));self.relate('connect','handle','blade-1');self.relate('connect','handle','blade-2')
