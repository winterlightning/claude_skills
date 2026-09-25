"""axe-with-wood-chips: Diagonal axe with broad curved blade and long handle. Two detached chip strokes replace three detailed fragments."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6cafadfb-83a3-4195-881b-b8727a773f98'
SOURCE_PATH = 'pictographic-primitives/outdoors/outdoors woodchopping 1_6cafadfb-83a3-4195-881b-b8727a773f98.svg'
AUTHOR = 'gpt-6'

class AxeWithWoodChips(Solo48):
    icon_id = 'axe-with-wood-chips'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('axe', 'woodchopping', 'chips', 'firewood', 'hatchet', 'camping', 'lumber', 'outdoors-batch-03')

    def build(self):
        # Plan: Diagonal axe with broad curved blade and long handle. Two detached chip strokes replace three detailed fragments.
        # Lucide construction reference: axe; original and atomic-debug inspected where named.
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
        path('axe',(20,8),[('L',(32,16)),('L',(40,16)),('A',(24,32),16,16,True),('L',(20,24)),('L',(4,40)),('L',(4,28)),('L',(16,16)),('L',(20,8))],True)
        line('chip-low',(28,40),(32,40))
        line('chip-right',(44,32),(44,36))
