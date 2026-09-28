"""Hanging Rope Noose.

Symbol plan: Centered hanging teardrop rope; one diagonal binding turn replaces three cramped hatches. Visible (8,2)-(40,46).
Construction references: No useful direct Lucide match; coherent geometric contours.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e995c5e1-9866-5328-abea-4a941bd578ac'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/hanging noose_e995c5e1-9866-5328-abea-4a941bd578ac.svg'
AUTHOR = 'gpt-6'


class NooseWithSpiralBinding(Solo48):
    icon_id = 'noose-with-spiral-binding'
    keyshape = Keyshape.VRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('noose', 'with', 'spiral', 'binding')

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

        self.add_bezier('loop-right',(24,24),((24,28),(38,28),(38,34)))
        self.add_arc('loop-bottom',(38,34),(10,34),radius_x=14,radius_y=10)
        self.add_bezier('loop-left',(10,34),((10,28),(24,28),(24,24)))
        self.add_contour('loop','loop-right','loop-bottom','loop-left',closed=True)
        path('rope',(24,4),[(24,12),(24,24)])
        path('binding',(18,16),[(24,12),(30,8)])
        self.relate('connect','rope','binding')
        self.relate('connect','rope','loop')
