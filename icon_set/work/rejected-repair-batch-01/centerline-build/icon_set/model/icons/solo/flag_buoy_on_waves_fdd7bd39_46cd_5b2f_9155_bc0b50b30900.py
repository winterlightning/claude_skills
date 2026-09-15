"""flag-buoy-on-waves: Dome buoy and attached pennant with one wave row. Flag has deliberate directional asymmetry; band and second wave omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'fdd7bd39-46cd-5b2f-9155-bc0b50b30900'
SOURCE_PATH = 'pictographic-primitives/outdoors/diving flag buoys_fdd7bd39-46cd-5b2f-9155-bc0b50b30900.svg'
AUTHOR = 'gpt-6'


class FlagBuoyOnWaves(Solo48):
    icon_id = 'flag-buoy-on-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('buoy', 'flag', 'diving', 'marker', 'sea', 'water', 'float', 'safety', 'outdoors-batch-01')

    def build(self):
        # Plan: Dome buoy and attached pennant with one wave row. Flag has deliberate directional asymmetry; band and second wave omitted.
        # Lucide flag: original and atomic-debug inspected for contour construction.
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
        poly('flag',(24,24),(24,16),(24,8),(40,8),(34,16),(24,16))
        path('float',(12,36),[('A',(24,24),12,12,True),('A',(36,36),12,12,True)])
        join('flag','float')
        path('water',(4,36),[('A',(12,36),4,4,False),('A',(24,36),6,4,True),('A',(36,36),6,4,False),('A',(44,36),4,4,True)])
        join('float','water')
