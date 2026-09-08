"""Domed government hall. Centerline extremes (2,2)-(46,46); symmetric sparse window ticks follow Lucide landmark. Extra cornice bands omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f234ad7a-ef0c-45ce-83bc-05f65b8c0143'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/official building 2_f234ad7a-ef0c-45ce-83bc-05f65b8c0143.svg'
AUTHOR = 'gpt-6'

class DomedGovernmentBuilding(Solo48):
    icon_id = 'domed-government-building'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('government', 'official', 'building', 'dome', 'civic', 'parliament', 'institution', 'architecture')

    def build(self) -> None:
        self.add_polyline('base', (2, 46), (2, 30), (12, 30), (36, 30), (46, 30), (46, 46), closed=True)
        self.add_polyline('drum', (12, 30), (12, 20), (36, 20), (36, 30), closed=False)
        self.add_arc('dome-left', (12, 20), (24, 8), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('dome-right', (24, 8), (36, 20), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('dome', 'dome-left', 'dome-right', closed=False)
        self.add_line('mast', (24, 2), (24, 8))
        self.add_line('window12', (12, 37), (12, 39))
        self.add_line('window24', (24, 37), (24, 39))
        self.add_line('window36', (36, 37), (36, 39))
        self.relate("connect", 'base', 'drum')
        self.relate("connect", 'drum', 'dome')
        self.relate("connect", 'dome', 'mast')
