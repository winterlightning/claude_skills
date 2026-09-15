"""Square envelope; opened the plinth band to eight units, moving all attached walls with it.

SQUARE: visible ink (4, 4, 44, 44). Square envelope preserves the subject’s near-equal overall width and height.
No useful exact local Lucide match; retained the inspected parent silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '0448e60a-2fc8-4f3a-970a-2da944490478'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-07/titanic quarter_0448e60a-2fc8-4f3a-970a-2da944490478.svg'
AUTHOR = 'gpt-6'

class TitanicBelfastMuseum(Solo48):
    icon_id = 'titanic-belfast-museum'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('titanic quarter', 'belfast', 'museum', 'building', 'angular', 'landmark', 'architecture', 'modern')

    def build(self) -> None:
        self.add_polyline('center', (16, 34), (16, 7), (24, 6), (32, 7), (32, 34))
        self.add_line('seam', (24, 6), (24, 34))
        self.add_polyline('left-wing', (16, 15), (6, 11), (6, 34))
        self.add_polyline('right-wing', (32, 15), (42, 11), (42, 34))
        self.add_polyline('plinth', (6, 34), (42, 34), (42, 42), (6, 42), closed=True)
        self.relate('connect', 'seam', 'center')
        self.relate('connect', 'left-wing', 'center')
        self.relate('connect', 'right-wing', 'center')
        for part in ('center', 'seam', 'left-wing', 'right-wing'):
            self.relate('connect', part, 'plinth')
