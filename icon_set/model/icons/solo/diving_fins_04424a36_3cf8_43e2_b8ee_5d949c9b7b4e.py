"""diving-fins: Two tapered fins in opposite directions; same outline and pocket divider derived by half-turn. Long decorative ribs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '04424a36-3cf8-43e2-b8ee-5d949c9b7b4e'
SOURCE_PATH = 'pictographic-primitives/outdoors/diving fins_04424a36-3cf8-43e2-b8ee-5d949c9b7b4e.svg'
AUTHOR = 'gpt-6'


class DivingFins(Solo48):
    icon_id = 'diving-fins'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('fins', 'diving', 'flippers', 'swimming', 'snorkeling', 'scuba', 'water', 'gear', 'outdoors-batch-01')

    def build(self):
        # Plan: Two tapered fins in opposite directions; same outline and pocket divider derived by half-turn. Long decorative ribs omitted.
        # Lucide backpack: original and atomic-debug inspected for contour construction.
        # Keyshape centerline extremes: (6, 6, 42, 42).

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
        for i in range(2):
            def p(x,y): return (x,y) if i==0 else (48-x,48-y)
            poly(f'fin-{i}',p(6,42),p(6,18),p(9,6),p(17,6),p(20,18),p(20,42),closed=True)
            line(f'pocket-{i}',p(6,18),p(20,18));join(f'pocket-{i}',f'fin-{i}')
