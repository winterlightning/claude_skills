"""Small Bird with Short Angular Legs
Plan: Small bird with folded wing and two short bent legs.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: Lucide bird: rounded body and folded wing.
Reduction: Tiny eye omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '19d5cc07-c7f1-475e-a0d6-14960a6a634c'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_16/eaglet_19d5cc07-c7f1-475e-a0d6-14960a6a634c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'small-bird-with-short-angular-legs'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('bird', 'chick', 'wing', 'beak', 'legs', 'animal', 'baby')

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
        path('bird',(6,15),[('L',(12,11)),('C',(21,6),(13,8),(17,6)),('C',(30,15),(27,6),(30,9)),('C',(42,27),(36,19),(42,20)),('C',(24,32),(42,33),(31,32)),('C',(10,23),(15,32),(10,30)),('L',(10,18)),('L',(6,15))],True)
        path('wing',(20,20),[('C',(27,23),(20,24),(24,24))])
        for x in (18,32):self.add_polyline(f'leg-{x}',(x,32),(x,42),(x-4,42));self.relate('connect',f'leg-{x}','bird')
