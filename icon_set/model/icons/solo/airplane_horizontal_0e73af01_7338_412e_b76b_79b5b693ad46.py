"""Right-facing airliner with swept wings and tail fins. Lucide plane informs a single silhouette; no windows or engines added.

SOLO48 HRECT_XL; geometry authored from its exact centerline extremes.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0e73af01-7338-412e-b76b-79b5b693ad46'
SOURCE_PATH = 'pictographic-primitives/symbol/plane horizontal_0e73af01-7338-412e-b76b-79b5b693ad46.svg'
AUTHOR = 'gpt-6'

class AirplaneHorizontal(Solo48):
    icon_id = 'airplane-horizontal'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('airplane', 'plane', 'flight', 'travel', 'aircraft', 'airport', 'trip', 'aviation')

    def build(self) -> None:
        upper = [(4, 16), (10, 18), (18, 18), (14, 8), (19, 8), (32, 18), (38, 18)]
        lower = [(38, 30), (32, 30), (19, 40), (14, 40), (18, 30), (10, 30), (4, 32), (7, 24), (4, 16)]
        for label, points in [('upper', upper), ('lower', lower)]:
            for i, (a, b) in enumerate(zip(points, points[1:]), 1):
                self.add_line(label + '-' + str(i), a, b)
        self.add_arc('nose', (38, 18), (38, 30), radius_x=6)
        self.add_contour('airframe', *['upper-' + str(i) for i in range(1, 7)], 'nose', *['lower-' + str(i) for i in range(1, 9)], closed=True)
