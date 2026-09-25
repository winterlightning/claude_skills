"""Two identical pin symbols have a diagonal placement and share their tips with a route line. HRECT extrema (4,8)-(44,40). Lucide route informs repeated endpoint symbols; supplied reference owns the teardrops and straight connection.
Reduction: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb88ce95-8030-4a20-adba-022549a07def'
SOURCE_PATH = 'pictographic-primitives/navigation/trip distance_bb88ce95-8030-4a20-adba-022549a07def.svg'
AUTHOR = 'gpt-6'


class RouteBetweenTwoPins(Solo48):
    icon_id = 'route-between-two-pins'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "navigation"
    categories = ("navigation", "primitives")
    aliases = ()
    keywords = ('route', 'pins', 'distance', 'trip', 'location', 'navigation', 'travel')

    def build(self) -> None:
        tips = []
        for i,(cx,cy) in enumerate(((12,26),(36,16))):
            left, right, tip = (cx-8,cy), (cx+8,cy), (cx,cy+14)
            self.add_arc(f"pin-{i}-cap", left, right, radius_x=8)
            # Radius-10 shoulders leave the radius-8 cap vertically, then
            # meet the 6:8 sloping sides at exact 3:4:5 tangencies.
            shoulder_right, shoulder_left = (cx+6,cy+6), (cx-6,cy+6)
            self.add_arc(f"pin-{i}-shoulder-right", right, shoulder_right, radius_x=10)
            self.add_line(f"pin-{i}-right", shoulder_right, tip)
            self.add_line(f"pin-{i}-left", tip, shoulder_left)
            self.add_arc(f"pin-{i}-shoulder-left", shoulder_left, left, radius_x=10)
            self.add_contour(f"pin-{i}", f"pin-{i}-cap", f"pin-{i}-shoulder-right", f"pin-{i}-right", f"pin-{i}-left", f"pin-{i}-shoulder-left", closed=True)
            tips.append(tip)
        self.add_line("route", *tips)
        for i in range(2):
            for side in ("left","right"):
                self.relate("connect", "route", f"pin-{i}-{side}")
