"""A compact disc with a concentric spindle hole.

CIRCLE: radial: center (24,24), centerline radius 22.
Lucide disc: concentric arcs / matched tangent corners and shared-axis geometry.
Source duplicates are retained in SOURCE_REFERENCES.
"""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c291f8c9-ddd6-4932-81de-5eec49892319'
SOURCE_PATH = 'pictographic-primitives/computers/batch-03/cd_c291f8c9-ddd6-4932-81de-5eec49892319.svg'
AUTHOR = 'astra-chatgpt'
SOURCE_REFERENCES = (('c291f8c9-ddd6-4932-81de-5eec49892319', 'pictographic-primitives/computers/batch-03/cd_c291f8c9-ddd6-4932-81de-5eec49892319.svg'),)


class CompactDisc(Solo48):
    icon_id = 'compact-disc'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('compact', 'disc')

    def build(self) -> None:
        self.add_arc('disc-upper', (2, 24), (46, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_arc('disc-lower', (46, 24), (2, 24), radius_x=22, radius_y=22, sweep=True)
        self.add_contour('disc', 'disc-upper', 'disc-lower', closed=True)
        self.add_arc('hole-upper', (18, 24), (30, 24), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('hole-lower', (30, 24), (18, 24), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('hole', 'hole-upper', 'hole-lower', closed=True)
