"""An open folding fan with a broad curved edge and three radiating ribs. HRECT_XL extremes (2,5)-(46,43). Remove the tiny squared pivot tab."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e42cbce0-9cff-57ad-9095-13c8d5b279a0'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/fan_e42cbce0-9cff-57ad-9095-13c8d5b279a0.svg'


class FoldingHandFan(Solo48):
    icon_id = 'folding-hand-fan'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/objects"
    aliases = ()
    keywords = ('fan', 'folding fan', 'hand fan', 'japanese', 'asian', 'accessory', 'cooling', 'traditional')

    def build(self) -> None:
        self.add_arc('edge-left-outer',(2,18),(12,8),radius_x=29)
        self.add_arc('edge-left-inner',(12,8),(24,5),radius_x=29)
        self.add_arc('edge-right-inner',(24,5),(36,8),radius_x=29)
        self.add_arc('edge-right-outer',(36,8),(46,18),radius_x=29)
        self.add_line('right-rib',(46,18),(24,43))
        self.add_line('left-rib',(24,43),(2,18))
        self.add_contour('fan','edge-left-outer','edge-left-inner','edge-right-inner','edge-right-outer','right-rib','left-rib',closed=True)
        self.add_line('centre-rib',(24,5),(24,43))
        self.relate('connect','fan','centre-rib')
        self.add_line('rib-left',(12,8),(24,43))
        self.add_line('rib-right',(36,8),(24,43))
        self.relate('connect','fan','rib-left')
        self.relate('connect','fan','rib-right')
        self.relate('connect','centre-rib','rib-left','rib-right')
