"""Semi Automatic Pistol.

Symbol plan: Directional pistol with long slide, slanted grip and rounded guard; extremes4,8,44,40. Omit small sight and trigger stroke for open guard.
Construction references: No useful direct Lucide match; coherent geometric contours.
Source SVG establishes subject; geometry is authored fresh on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a7ab4586-459b-592f-9e5f-90f4574e3c97'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/crime/gun silent_a7ab4586-459b-592f-9e5f-90f4574e3c97.svg'
AUTHOR = 'gpt-6'


class PistolWithLongSlideAndCurvedGuard(Solo48):
    icon_id = 'pistol-with-long-slide-and-curved-guard'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "crime"
    categories = ("crime", "primitives")
    aliases = ()
    keywords = ('pistol', 'with', 'long', 'slide', 'and', 'curved', 'guard')

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
            path(name, (x-r,y), [((x+r,y),r,r,True), ((x-r,y),r,r,True)], True)

        path('slide',(4,12),[((8,8),4,4,True),(40,8),((44,12),4,4,True),(44,18),(36,18),(28,18),(20,18),(4,18),(4,12)],True)
        path('grip',(4,18),[(10,24),(4,40),(16,40),(20,28),(20,18)])
        path('guard',(20,28),[(28,28),((36,20),8,8,False),(36,18)])
        for a,b in [('slide','grip'),('slide','guard'),('grip','guard')]:self.relate('connect',a,b)
