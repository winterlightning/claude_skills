'Death Star Space Station.\nSymbol plan: Circle radius20 with equatorial seam y24. Dish reduced to one round dot at(18,14) to preserve upper-left position and clear spacing; secondary panel seam omitted.\nConstruction reference: Lucide orbit: circle hierarchy; source dish and equatorial seam preserved.\nOriginal reference: SOURCE_PATH below.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '94cb7bfa-11e5-4ca8-bd46-dfa778f2b951'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_18/fiction death star 1_94cb7bfa-11e5-4ca8-bd46-dfa778f2b951.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'death-star-equatorial-station'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ()
    keywords = ('death', 'star', 'equatorial', 'station')

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

        path('sphere',(4,24),[((44,24),20,20,True),((4,24),20,20,True)],True)
        self.add_line('equator',(4,24),(44,24))
        self.relate('connect','sphere','equator')
        self.add_dot('dish',(18,14))
