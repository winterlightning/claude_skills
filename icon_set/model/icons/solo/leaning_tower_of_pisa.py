# Review revision; previous candidates preserved.
"""The Leaning Tower of Pisa with sloping floor bands; the doorway and upper mast are omitted for clear spacing."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9a3f8c8c-6f0b-50d0-bd62-91718e949e17'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/pisa tower_9a3f8c8c-6f0b-50d0-bd62-91718e949e17.svg'
AUTHOR = 'gpt-6'

class LeaningTowerOfPisa(Solo48):
    icon_id = 'leaning-tower-of-pisa'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('pisa', 'tower', 'italy', 'leaning', 'landmark', 'campanile', 'travel', 'architecture')

    def build(self) -> None:
        """Opening repair: Raised the lower floor band and respaced the other bands to enlarge the bottom opening."""
        self.add_polyline('shaft', (11, 42), (14, 32), (16, 24), (18, 16), (19, 6), (35, 6), (34, 20), (32, 28), (30, 36), (28, 42), (11, 42), closed=True)
        self.add_line('upper-floor', (18, 16), (34, 20))
        self.add_line('middle-floor', (16, 24), (32, 28))
        self.add_line('lower-floor', (14, 32), (30, 36))
        for part in ('upper-floor', 'middle-floor', 'lower-floor'):
            self.relate('connect', part, 'shaft')
        self.add_polyline('ground', (6, 42), (11, 42), (28, 42), (42, 42))
        self.relate('connect', 'ground', 'shaft')
