"""cabin-tent: Mirrored pitched eaves and cabin walls with a centered round arch door."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b98c4a8a-02a1-59a5-9c72-d10b833b416e'
SOURCE_PATH = 'pictographic-primitives/outdoors/camping tent_b98c4a8a-02a1-59a5-9c72-d10b833b416e.svg'
AUTHOR = 'gpt-6'


class CabinTent(Solo48):
    icon_id = 'cabin-tent'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('tent', 'camping', 'cabin-tent', 'shelter', 'campsite', 'outdoors', 'door', 'outdoors-batch-01')

    def build(self):
        # Plan: Mirrored pitched eaves and cabin walls with a centered round arch door.
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
        axis=24
        poly('roof',(4,28),(8,24),(axis,8),(40,24),(44,28))
        poly('walls',(8,24),(8,40),(16,40),(16,32))
        path('door',(16,32),[('A',(32,32),8,8,True),('L',(32,40)),('L',(40,40)),('L',(40,24))])
        join('walls','roof');join('door','roof');join('walls','door')
