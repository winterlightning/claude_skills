"""Three elongated pointed crystals form an uneven fan with complete lower ends."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ad287d09-ed0b-449e-9e30-f234e0f18b97'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-01/crystals_ad287d09-ed0b-449e-9e30-f234e0f18b97.svg'
AUTHOR = 'gpt-6'


class PointedCrystalCluster(Solo48):
    icon_id = 'pointed-crystal-cluster'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('crystal', 'cluster', 'mineral', 'quartz', 'geology', 'points', 'gem')

    def build(self) -> None:
        self.add_polyline('central',(16,46),(16,12),(24,2),(32,12),(32,46),closed=True)
        self.add_polyline('left',(16,46),(5,22),(9,12),(16,20))
        self.add_polyline('right',(32,20),(39,14),(43,24),(32,46))
        self.relate('connect','left','central')
        self.relate('connect','right','central')
