'Pattern: nine identical rounded cells on a regular grid, replacing warped unequal loops.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'de94b058-ab01-5561-bec1-475160705e72'
SOURCE_PATH = 'icons-json/design/pattern_de94b058-ab01-5561-bec1-475160705e72.json'
AUTHOR = 'gpt-6'

class Pattern(Solo48):
    icon_id = 'pattern'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    aliases = ()
    keywords = ('pattern', 'design')

    def build(self):
        # Pattern: four equal rounded cells with generous uniform gaps, replacing nine undersized loops.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def r(name, x0, y0, x1, y1, radius=4):
            # Equal corner radii and shared tangent endpoints own the rounded box.
            points = [(x0+radius,y0),(x1-radius,y0),(x1,y0+radius),
                      (x1,y1-radius),(x1-radius,y1),(x0+radius,y1),
                      (x0,y1-radius),(x0,y0+radius)]
            ids=[]
            for index,start in enumerate(points):
                end=points[(index+1)%8]
                if start==end:
                    continue
                part=f'{name}-{index}'
                if index%2:
                    a(part,start,end,radius)
                else:
                    l(part,start,end)
                ids.append(part)
            self.add_contour(name,*ids,closed=True)

        # Four equal cells keep the pattern legible without nine cramped counters.
        for row in range(2):
            for col in range(2):
                x,y=6+24*col,6+24*row
                r(f'cell-{row}-{col}',x,y,x+12,y+12,3)
