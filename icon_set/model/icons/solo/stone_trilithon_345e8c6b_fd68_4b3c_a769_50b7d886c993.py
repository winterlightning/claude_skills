"""stone-trilithon: Two tall stones under an overhanging lintel. Shared upright widths and a broad central opening; small surface irregularities omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '345e8c6b-fd68-4b3c-a769-50b7d886c993'
SOURCE_PATH = 'pictographic-primitives/outdoors/landmarks stone_345e8c6b-fd68-4b3c-a769-50b7d886c993.svg'
AUTHOR = 'gpt-6'


class StoneTrilithon(Solo48):
    icon_id = 'stone-trilithon'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    categories = ('outdoors', 'primitives')
    aliases = ()
    keywords = ('stonehenge', 'trilithon', 'stones', 'landmark', 'megalith', 'monument', 'ancient', 'outdoors-batch-02')

    def build(self):
        # Plan: Two tall stones under an overhanging lintel. Shared upright widths and a broad central opening; small surface irregularities omitted.
        # Lucide landmark original and atomic-debug inspected for construction.
        # Human scenes use icon_set/references/human_ref/full_body_ref.png.
        # Centerline envelope: (6, 6, 42, 42).
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
        poly('stones',(6,6),(42,6),(42,16),(39,16),(40,42),(29,42),(29,16),(19,16),(19,42),(8,42),(9,16),(6,16),closed=True)
        line('joint-left',(9,16),(19,16));join('joint-left','stones')
        line('joint-right',(29,16),(39,16));join('joint-right','stones')
