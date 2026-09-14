"""Front rear windows; independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '790ca62d-d763-4431-90d6-607482d5463c'
SOURCE_PATH = 'pictographic-primitives/transportation/power window front rear_790ca62d-d763-4431-90d6-607482d5463c.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '790ca62d-d763-4431-90d6-607482d5463c', 'SOURCE_PATH': 'pictographic-primitives/transportation/power window front rear_790ca62d-d763-4431-90d6-607482d5463c.svg', 'AUTHOR': 'gpt-6'}]

class FrontRearWindows(Solo48):
    icon_id = 'front-rear-windows'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('front', 'rear', 'windows')

    def build(self) -> None:
        # HRECT_L (6,8)-(42,40). Paired glass shapes share dimensions and a ten-unit gap.
        for name,side in [('left',-1),('right',1)]:
            def p(x,y): return (24+side*x,y)
            self.add_polyline(name+'-window',p(6,8),p(10,8),p(20,40),p(6,40),closed=True)
