"""Bearded Pirate Behind a Laptop
Plan: Pirate hat, rounded face, beard and foreground laptop.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: human_ref/user.svg: circular face; source foreground prop retained.
Reduction: Tiny hat cross omitted for spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'aa4f64c4-a374-44b3-9890-7cd9bfe00eab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/avatar piracy laptop_aa4f64c4-a374-44b3-9890-7cd9bfe00eab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bearded-pirate-behind-a-laptop'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('pirate', 'laptop', 'beard', 'hat', 'computer', 'person', 'software')

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
        path('hat',(10,20),[('C',(16,12),(10,14),(12,13)),('C',(32,12),(20,4),(28,4)),('C',(42,20),(36,12),(42,14)),('L',(10,20))],True)
        path('face',(16,20),[('A',(36,20),10,10,False)])
        self.add_polyline('laptop',(6,29),(24,29),(31,42),(13,42),closed=True)
        path('beard',(26,31),[('C',(35,35),(29,24),(39,29)),('L',(30,42))])
        self.relate('connect','hat','face');self.relate('connect','beard','face');self.relate('connect','beard','laptop')
