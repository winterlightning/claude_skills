'Stove with Range Hood.\n\nSymbol plan: Symmetric chimney and sloped extractor hood above a plain range cabinet, with required 8-unit separation. Box extremes (6,6)-(42,42).\nConstruction reference: Lucide lamp-ceiling: sloping shade geometry; preserve unadorned schematic source range.\nOriginal reference: SOURCE_PATH below.\n'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '49d355c0-de69-4354-820f-358930bb7fc2'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_24/kitchen_49d355c0-de69-4354-820f-358930bb7fc2.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'kitchen-range-extractor-hood'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('kitchen', 'range', 'extractor', 'hood')

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

        self.add_polyline('hood',(6,22),(16,14),(16,6),(32,6),(32,14),(42,22),closed=True)
        self.add_polyline('range',(6,30),(42,30),(42,42),(6,42),closed=True)
