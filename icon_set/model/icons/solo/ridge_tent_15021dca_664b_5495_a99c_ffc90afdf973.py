"""ridge-tent: Perspective tent, shared ridge nodes and an open front doorway. Intentional asymmetric roof panel."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '15021dca-664b-5495-a99c-ffc90afdf973'
SOURCE_PATH = 'pictographic-primitives/outdoors/camping tent_15021dca-664b-5495-a99c-ffc90afdf973.svg'
AUTHOR = 'gpt-6'


class RidgeTent(Solo48):
    icon_id = 'ridge-tent'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('tent', 'camping', 'ridge-tent', 'shelter', 'campsite', 'outdoors', 'canvas', 'outdoors-batch-01')

    def build(self):
        # Plan: Perspective tent, shared ridge nodes and an open front doorway. Intentional asymmetric roof panel.
        # Lucide tent: original and atomic-debug inspected for contour construction.
        # Keyshape centerline extremes: (4, 8, 44, 40).

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
        apex=(18,8)
        poly('roof',(4,40),apex,(32,8),(44,40),(32,40),apex)
        poly('front-left',(4,40),(13,40),(18,32),(23,40),(32,40))
        join('roof','front-left')
