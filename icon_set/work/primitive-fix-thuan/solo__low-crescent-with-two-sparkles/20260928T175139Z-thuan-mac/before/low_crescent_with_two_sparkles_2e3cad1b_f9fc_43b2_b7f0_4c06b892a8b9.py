"""Low Crescent with Two Sparkles
Plan: Low crescent with two small sparkle crosses
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide moon; sparkles reduced to crossed rays.
Reduction: Four-point stars reduced to open cross rays for clearance."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2e3cad1b-f9fc-43b2-b7f0-4c06b892a8b9'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_04/astrology stars_2e3cad1b-f9fc-43b2-b7f0-4c06b892a8b9.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'low-crescent-with-two-sparkles'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('moon', 'crescent', 'sparkles', 'stars', 'night', 'sky', 'celestial')

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
        path('moon',(6,22),[('C',(24,42),(6,34),(14,42)),('C',(42,22),(34,42),(42,34)),('C',(6,22),(34,34),(14,34))],True)
        for name,x,y in [('a',16,10),('b',34,10)]:self.add_line(name+'-v',(x,y-4),(x,y+4));self.add_line(name+'-h',(x-4,y),(x+4,y));self.relate('connect',name+'-v',name+'-h')
