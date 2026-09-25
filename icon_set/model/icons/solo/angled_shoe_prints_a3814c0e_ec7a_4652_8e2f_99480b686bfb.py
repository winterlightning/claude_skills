"""Pair of Shoe Footprints.

Symbol plan: Staggered sole pair; right print deliberately tilted, left upright. Visible (4,4)-(44,44). No tread detail.
Construction references: Lucide footprints: tapered sole contours; original establishes the stagger and tilt.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a3814c0e-ec7a-4652-8e2f-99480b686bfb'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/police footsteps_a3814c0e-ec7a-4652-8e2f-99480b686bfb.svg'
AUTHOR = 'gpt-6'


class AngledShoePrints(Solo48):
    icon_id = 'angled-shoe-prints'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('angled', 'shoe', 'prints')

    def build(self):
        def path(name, start, steps, closed=False):
            ids = []
            point = start
            for i, step in enumerate(steps):
                member = f"{name}-{i}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                ids.append(member)
            self.add_contour(name, *ids, closed=closed)

        def circle(name, x, y, r):
            path(name, (x,y-r), [((x+r,y),r,r,True), ((x,y+r),r,r,True), ((x-r,y),r,r,True), ((x,y-r),r,r,True)], True)

        path('left-sole',(6,13),[((13,6),7,7,True),((20,13),7,7,True),(18,22),(8,22),(6,13)],True)
        path('left-heel',(9,30),[(17,30),(17,34),((13,38),4,4,True),((9,34),4,4,True),(9,30)],True)
        path('right-sole',(28,17),[((35,10),7,7,True),((42,17),7,7,True),(40,28),(30,26),(28,17)],True)
        self.add_line('heel-top',(29,34),(39,36))
        self.add_bezier('heel-round',(39,36),((39,40),(37,42),(34,42)),((30,42),(27,39),(29,34)))
        self.add_contour('right-heel','heel-top','heel-round',closed=True)
