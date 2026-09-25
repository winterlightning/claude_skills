"""A football boot kicking a paneled ball.
Plan: SQUARE fits the upper-left ball and lower-right boot and sock.
Reduction: Ball reduced to one panel divider; boot stripes and studs omitted. Widened the sole band.
Construction: Lucide circular construction and the source boot silhouette.
Layout: Intentional ball/boot asymmetry preserves the kicking scene."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7637106f-a796-4b5a-8382-ddbd48faa5f0'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_34/soccer kick ball_7637106f-a796-4b5a-8382-ddbd48faa5f0.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'football-boot-kicking-panelled-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    aliases = ()
    keywords = ('football', 'boot', 'ball', 'kick', 'soccer', 'sport')

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
        circle('ball',15,15,9)
        self.add_polyline('boot',(42,24),(39,42),(14,42),(15,33),(31,33),(34,22),closed=True)
        self.add_line('cuff',(34,22),(36,6));self.add_line('sock',(36,6),(42,8));self.relate('connect','cuff','boot');self.relate('connect','cuff','sock')
        self.add_line('panel',(15,6),(15,24));self.relate('connect','panel','ball')
