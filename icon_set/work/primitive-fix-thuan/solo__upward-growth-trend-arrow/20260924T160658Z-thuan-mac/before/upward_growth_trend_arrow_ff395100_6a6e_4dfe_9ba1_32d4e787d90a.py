'Upward Growth Trend Arrow.\n\nSymbol plan: One increasing zigzag with a joined open arrowhead at (44,8). Natural directional asymmetry; full box (4,8)-(44,40).\nConstruction reference: Lucide plane: preserve direction with coherent diagonal strokes; no useful exact growth reference inspected.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ff395100-6a6e-4dfe-9ba1-32d4e787d90a'
SOURCE_PATH = 'pictographic-primitives/other/arrow trend up_ff395100-6a6e-4dfe-9ba1-32d4e787d90a.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'upward-growth-trend-arrow'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'objects'
    aliases = ()
    keywords = ('upward', 'growth', 'trend', 'arrow')

    def build(self):
        def path(name, start, steps, closed=False):
            members = []
            point = start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)

        def circle(name, x, y, radius):
            path(name, (x-radius,y), [((x+radius,y),radius,radius,True),
                 ((x-radius,y),radius,radius,True)], True)

        def box(name, left, top, right, bottom, radius):
            r = radius
            path(name, (left+r,top), [(right-r,top), ((right,top+r),r,r,True),
                 (right,bottom-r), ((right-r,bottom),r,r,True), (left+r,bottom),
                 ((left,bottom-r),r,r,True), (left,top+r), ((left+r,top),r,r,True)], True)

        self.add_polyline('trend',(4,40),(20,24),(28,32),(44,8))
        self.add_polyline('head',(28,8),(44,8),(44,24))
        self.relate('connect','trend','head')
