"""Crescent Moon beside Five-Point Star
Plan: Crescent and five-point star form celestial emblem
Keyshape SQUARE: (4, 4, 44, 44).
Construction reference: Lucide moon and star.
Reduction: Preserve star outline; narrow crescent simplified to smooth sweep."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b261f656-d077-46a8-afd0-2ebb46927dab'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_36/star and crescent_b261f656-d077-46a8-afd0-2ebb46927dab.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crescent-moon-beside-five-point-star'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('crescent', 'moon', 'star', 'emblem', 'sky', 'symbol')

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
        path('moon',(20,6),[('C',(6,24),(12,6),(6,14)),('C',(20,42),(6,34),(12,42)),('C',(13,24),(14,36),(13,32)),('C',(20,6),(13,16),(14,12))],True)
        self.add_polyline('star',(34,12),(37,20),(42,20),(38,26),(40,34),(33,30),(26,34),(28,26),(24,20),(31,20),closed=True)
