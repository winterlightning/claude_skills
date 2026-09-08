"""Central angular prism between flaring ship-prow wings on a plinth."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0448e60a-2fc8-4f3a-970a-2da944490478'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/titanic quarter_0448e60a-2fc8-4f3a-970a-2da944490478.svg'
AUTHOR = 'gpt-6'

class TitanicBelfastMuseum(Solo48):
    icon_id = 'titanic-belfast-museum'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('titanic quarter', 'belfast', 'museum', 'building', 'angular', 'landmark', 'architecture', 'modern')

    def build(self) -> None:
        # HRECT_XL centerline extremes (2,5)-(46,43).
        self.add_polyline('center', (16, 35), (16, 7), (24, 5), (32, 7), (32, 35))
        self.add_line('seam', (24, 5), (24, 35))
        self.add_polyline('left-wing', (16, 15), (2, 11), (5, 35))
        self.add_polyline('right-wing', (32, 15), (46, 11), (43, 35))
        self.add_polyline('plinth', (2, 35), (46, 35), (46, 43), (2, 43), closed=True)
        self.relate('connect', 'seam', 'center')
        self.relate('connect', 'left-wing', 'center')
        self.relate('connect', 'right-wing', 'center')
        for part in ('center', 'seam', 'left-wing', 'right-wing'):
            self.relate('connect', part, 'plinth')
