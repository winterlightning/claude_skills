"""Bowling Pin beside Ball
Plan: Tall bowling pin at left, round ball at right with one visible finger mark.
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: No useful exact Lucide match; pin has a rounded top and tapered neck.
Reduction: Reduced neck bands to one line and finger holes to one dot.."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff489ec3-8055-4cf9-be9d-85532a1e5a38'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_07/bowling set_ff489ec3-8055-4cf9-be9d-85532a1e5a38.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bowling-pin-beside-ball'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'sports'
    aliases = ()
    keywords = ('bowling', 'pin', 'ball', 'sport', 'game', 'lanes', 'equipment')

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
        path('pin',(8,10),[('A',(16,10),4,4,True),('L',(16,20)),('C',(18,32),(16,25),(18,27)),('C',(14,42),(18,38),(17,42)),('L',(10,42)),('C',(6,32),(7,42),(6,38)),('C',(8,20),(6,27),(8,25)),('L',(8,10))],True)
        circle('ball',35,35,7)
        # Finger holes omitted: a separated ball cannot contain a legal detail at this size.
