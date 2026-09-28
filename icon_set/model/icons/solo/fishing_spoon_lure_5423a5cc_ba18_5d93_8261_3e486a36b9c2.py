"""fishing-spoon-lure: Teardrop spoon and mirrored double hook, shared shank node and hook radius. Tiny top ring replaced by attachment tip."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5423a5cc-ba18-5d93-8261-3e486a36b9c2'
SOURCE_PATH = 'pictographic-primitives/outdoors/fishing lure_5423a5cc-ba18-5d93-8261-3e486a36b9c2.svg'
AUTHOR = 'gpt-6'


class FishingSpoonLure(Solo48):
    icon_id = 'fishing-spoon-lure'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('lure', 'fishing', 'hook', 'bait', 'spoon', 'angling', 'tackle', 'outdoors-batch-01')

    def build(self):
        # Plan: Teardrop spoon and mirrored double hook, shared shank node and hook radius. Tiny top ring replaced by attachment tip.
        # Lucide fishing-hook: original and atomic-debug inspected for contour construction.
        # Keyshape centerline extremes: (8, 4, 40, 44).

        def path(name, start, commands, closed=False):
            members, here = [], start
            for i, (kind, end, *args) in enumerate(commands):
                part = f"{name}-{i}"
                if kind == 'L':
                    self.add_line(part, here, end)
                else:
                    rx, ry, sweep = args
                    self.add_arc(part, here, end, radius_x=rx, radius_y=ry, sweep=sweep)
                members.append(part)
                here = end
            self.add_contour(name, *members, closed=closed)
        def circle(name, cx, cy, r):
            path(name, (cx-r,cy), [('A',(cx+r,cy),r,r,True),('A',(cx-r,cy),r,r,True)], True)
        def rounded(name, x0, y0, x1, y1, r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line, poly = self.add_line, self.add_polyline
        join = lambda a,b: self.relate('connect',a,b)
        path('spoon',(24,4),[('A',(32,20),20,20,True),('A',(24,28),8,8,True),('A',(16,20),8,8,True),('A',(24,4),20,20,True)],True)
        line('shank',(24,28),(24,36));join('shank','spoon')
        path('left-hook',(8,32),[('L',(8,36)),('A',(24,36),8,8,False)])
        path('right-hook',(24,36),[('A',(40,36),8,8,False),('L',(40,32))])
        join('shank','left-hook');join('shank','right-hook');join('left-hook','right-hook')
