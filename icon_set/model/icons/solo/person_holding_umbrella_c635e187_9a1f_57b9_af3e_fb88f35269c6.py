"""person-holding-umbrella: Upper-body person holding an open umbrella. Head radius 3 at (10,17); shoulder y28 gives exact 4-unit ink clearance. Scallops and top tip omitted; canopy and raised forearm retained."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c635e187-9a1f-57b9-af3e-fb88f35269c6'
SOURCE_PATH = 'pictographic-primitives/outdoors/hold umbrella_c635e187-9a1f-57b9-af3e-fb88f35269c6.svg'
AUTHOR = 'gpt-6'


class PersonHoldingUmbrella(Solo48):
    icon_id = 'person-holding-umbrella'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('umbrella', 'person', 'rain', 'weather', 'holding', 'shelter', 'protection', 'outdoors-batch-02')

    def build(self):
        # Plan: Upper-body person holding an open umbrella. Head radius 3 at (10,17); shoulder y28 gives exact 4-unit ink clearance. Scallops and top tip omitted; canopy and raised forearm retained.
        # Lucide umbrella original and atomic-debug inspected for construction.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (4, 8, 44, 40).
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
        circle('head',10,17,3)
        path('body',(4,40),[('L',(4,34)),('A',(10,28),6,6,True),('L',(16,28)),('L',(24,32)),('L',(33,32))])
        line('torso',(16,28),(16,40));join('torso','body')
        path('canopy',(22,16),[('A',(44,16),11,8,True),('L',(33,16)),('L',(22,16))],True)
        line('shaft',(33,16),(33,32));join('shaft','canopy');join('shaft','body')
