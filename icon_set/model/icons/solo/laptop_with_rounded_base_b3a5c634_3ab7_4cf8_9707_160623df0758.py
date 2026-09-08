"""An open laptop with a wide, rounded dish base.

HRECT_L: centerline extremes (2,8)-(46,40).
Lucide laptop: concentric arcs / matched tangent corners and shared-axis geometry.
Source duplicates are retained in SOURCE_REFERENCES.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b3a5c634-3ab7-4cf8-9707-160623df0758'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/laptop_b3a5c634-3ab7-4cf8-9707-160623df0758.svg'
SOURCE_REFERENCES = (('b3a5c634-3ab7-4cf8-9707-160623df0758', 'pictographic-primitives/computers/batch-03/laptop_b3a5c634-3ab7-4cf8-9707-160623df0758.svg'), ('f99926f6-12c0-4ba6-aff3-e7bf08c23a81', 'pictographic-primitives/computers/batch-03/laptop_f99926f6-12c0-4ba6-aff3-e7bf08c23a81.svg'))


class LaptopWithRoundedBase(Solo48):
    icon_id = 'laptop-with-rounded-base'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('laptop', 'with', 'rounded', 'base')

    def build(self) -> None:
        self.add_line('screen-left', (6, 31), (6, 13))
        self.add_arc('screen-nw', (6, 13), (11, 8), radius_x=5, radius_y=5, sweep=True)
        self.add_line('screen-top', (11, 8), (37, 8))
        self.add_arc('screen-ne', (37, 8), (42, 13), radius_x=5, radius_y=5, sweep=True)
        self.add_line('screen-right', (42, 13), (42, 31))
        self.add_contour('screen', 'screen-left', 'screen-nw', 'screen-top', 'screen-ne', 'screen-right', closed=False)
        self.add_line('lip-left', (2, 31), (6, 31))
        self.add_line('lip-mid', (6, 31), (42, 31))
        self.add_line('lip-right', (42, 31), (46, 31))
        self.add_line('base-right', (46, 31), (46, 32))
        self.add_line('base-bottom', (38, 40), (10, 40))
        self.add_line('base-left', (2, 32), (2, 31))
        self.add_arc('base-se', (46, 32), (38, 40), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('base-sw', (10, 40), (2, 32), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('base', 'lip-left', 'lip-mid', 'lip-right', 'base-right', 'base-se', 'base-bottom', 'base-sw', 'base-left', closed=True)
        self.relate("connect", 'screen', 'base')
