"""Tiered Capitol dome and finial. Centerline extremes (2,2)-(46,46). Lucide landmark: shared axis and sparse facade. Lantern ornament reduced to mast."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b30e317-ba07-5cbb-9aa7-dcd69f1f5fd4'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/capitol hill dc_2b30e317-ba07-5cbb-9aa7-dcd69f1f5fd4.svg'
AUTHOR = 'gpt-6'

class CapitolDomeBuilding(Solo48):
    icon_id = 'capitol-dome-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('capitol', 'washington', 'government', 'dome', 'congress', 'landmark', 'building', 'civic')

    def build(self) -> None:
        self.add_polyline('base', (2, 46), (2, 34), (12, 34), (36, 34), (46, 34), (46, 46), (2, 46), closed=False)
        self.add_polyline('drum', (12, 34), (12, 24), (36, 24), (36, 34), closed=False)
        self.add_arc('dome-left', (12, 24), (24, 10), radius_x=12, radius_y=14, sweep=True)
        self.add_arc('dome-right', (24, 10), (36, 24), radius_x=12, radius_y=14, sweep=True)
        self.add_contour('dome', 'dome-left', 'dome-right', closed=False)
        self.add_line('finial', (24, 2), (24, 10))
        self.add_line('window', (24, 34), (24, 24))
        self.relate("connect", 'base', 'drum')
        self.relate("connect", 'drum', 'dome')
        self.relate("connect", 'dome', 'finial')
