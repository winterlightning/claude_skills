"""Steak Beside a Curled Shrimp
Plan: Natural surf-and-turf group; kidney steak with bone, curled shrimp upper right.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No exact match.
Reduction: Shrimp segmentation omitted; steak bone and separate curled shrimp retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3081d7ba-fd1d-4243-a12c-2d199b56c7ab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_05/barbecue steak shrimp_3081d7ba-fd1d-4243-a12c-2d199b56c7ab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'steak-beside-a-curled-shrimp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('steak', 'shrimp', 'food', 'meal', 'surf and turf', 'bone', 'seafood')

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
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def line(name,a,b): self.add_line(name,a,b)
        def join(a,b): self.relate('connect',a,b)
        path('steak',(6,31),[('C',(17,18),(6,22),(10,18)),('C',(31,30),(28,18),(29,26)),('C',(42,34),(32,30),(42,28)),('C',(32,42),(42,42),(39,42)),('L',(17,42)),('C',(6,31),(10,42),(6,40))],True)
        circle('bone',18,30,3)
        path('shrimp',(30,12),[('A',(36,6),6,6,True),('A',(42,12),6,6,True),('A',(36,18),6,6,True)])
