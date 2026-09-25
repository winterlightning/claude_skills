"""diver-underwater: Diver descending diagonally with an extended fin. Shared full_body_ref.png construction: head center (36,23), radius 3; arm y34 gives exactly 4 units of ink clearance. Water surface and boundary omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '264f7d10-379d-49b6-ba54-49c000d773b9'
SOURCE_PATH = 'pictographic-primitives/outdoors/diving scuba free diving_264f7d10-379d-49b6-ba54-49c000d773b9.svg'
AUTHOR = 'gpt-6'


class DiverUnderwater(Solo48):
    icon_id = 'diver-underwater'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('diving', 'scuba', 'diver', 'underwater', 'freediving', 'swimming', 'sea', 'fin', 'outdoors-batch-01')

    def build(self):
        # Plan: Diver descending diagonally with an extended fin. Shared full_body_ref.png construction: head center (36,23), radius 3; arm y34 gives exactly 4 units of ink clearance. Water surface and boundary omitted.
        # Lucide sailboat: original and atomic-debug inspected for contour construction.
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
        # Fin-to-foot and shoulder-to-arm are real shared nodes; separated head uses a cardinal circle arc.
        circle('head',36,23,3)
        poly('body',(4,8),(14,18),(24,34))
        poly('arm',(24,34),(36,34),(44,40));join('body','arm')
        poly('fin',(4,8),(4,20),(14,18));join('fin','body')
