"""Ink Bottle with Ribbed Cap and Label
Plan: Squat bottle with ribbed cap and broad label band.
Keyshape: SQUARE; exact inset SOLO48 envelope.
Construction: No useful exact Lucide match; coherent curves and shared geometric parameters.
Reduction: Fine cap ribs reduced to one; central label mark omitted for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1888bc1b-5974-4d14-9f53-439684656693'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_14/design tool ink_1888bc1b-5974-4d14-9f53-439684656693.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'ink-bottle-with-ribbed-cap-and-label'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('ink', 'bottle', 'cap', 'label', 'writing', 'stationery', 'container')

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
        rect('cap',12,6,24,8,2)
        path('bottle',(14,14),[('C',(6,25),(14,20),(6,21)),('L',(6,37)),('A',(11,42),5,5,False),('L',(37,42)),('A',(42,37),5,5,False),('L',(42,25)),('C',(34,14),(42,21),(34,20))]);self.relate('connect','cap','bottle')
        for y in (25,33):self.add_line(f'label-{y}',(6,y),(42,y));self.relate('connect',f'label-{y}','bottle')
        self.add_line('cap-rib',(24,6),(24,14));self.relate('connect','cap-rib','cap')
