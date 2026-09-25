"""Hard Hat Worker with Round Collar
Plan: Centered circular jaw beneath hard hat; curved shoulders and open bottom
Keyshape VRECT_L: (6, 2, 42, 46).
Construction reference: human_ref/user.svg, Lucide hard-hat.
Reduction: Keep hat brim and collar; remove narrow hat ridges."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3e7caf13-9071-4393-a911-7e857d63fad2'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_12/contractor_3e7caf13-9071-4393-a911-7e857d63fad2.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'hard-hat-worker-with-round-collar'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    human_construction = 'bust'
    aliases = ()
    keywords = ('worker', 'hardhat', 'construction', 'helmet', 'person', 'bust', 'safety')

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
        self.add_arc('face',(14,16),(34,16),radius_x=10,radius_y=10,sweep=False)
        path('hat',(14,16),[('L',(14,14)),('A',(34,14),10,10,True),('L',(34,16))]);self.add_line('brim',(10,16),(38,16))
        self.relate('connect','face','brim');self.relate('connect','face','hat');self.relate('connect','hat','brim')
        self.add_arc('body-left',(8,44),(16,30),radius_x=8,radius_y=14,sweep=True)
        self.add_line('body-top',(16,30),(32,30))
        self.add_arc('body-right',(32,30),(40,44),radius_x=8,radius_y=14,sweep=True)
        self.relate('connect','body-left','body-top');self.relate('connect','body-right','body-top');self.relate('connect','face','body-top')
