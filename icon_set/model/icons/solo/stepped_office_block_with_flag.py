# Review candidate; original preserved.
"""A stepped embassy office block with a rectangular rooftop flag; window ticks omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3c101274-9d7e-5fd8-9939-907b34ebbabe'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-02/embassy building_3c101274-9d7e-5fd8-9939-907b34ebbabe.svg'
AUTHOR = 'gpt-6'

class SteppedOfficeBlockWithFlag(Solo48):
    icon_id = 'stepped-office-block-with-flag'
    keyshape = Keyshape.VRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('embassy', 'office', 'building', 'government', 'flag', 'civic', 'tower', 'architecture')

    def build(self) -> None:
        """Opening repair: Deepened the rooftop flag from four to eight units, retaining the stepped building."""
        self.add_polyline('building', (6, 42), (6, 30), (15, 30), (15, 20), (35, 20), (35, 42), (6, 42))
        self.add_line('foreground-edge', (15, 30), (23, 30))
        self.add_line('foreground-wall', (23, 30), (23, 42))
        self.relate('connect', 'building', 'foreground-edge')
        self.relate('connect', 'foreground-edge', 'foreground-wall')
        self.relate('connect', 'building', 'foreground-wall')
        self.add_polyline('flag', (23, 20), (23, 14), (23, 6), (37, 6), (37, 14), (23, 14))
        self.relate('connect', 'flag', 'building')
        self.add_line('ground-right', (35, 42), (42, 42))
        self.relate('connect', 'ground-right', 'building')
