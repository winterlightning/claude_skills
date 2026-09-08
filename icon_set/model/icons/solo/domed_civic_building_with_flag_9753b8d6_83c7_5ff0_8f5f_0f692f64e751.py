"""Flagged embassy with dome, doorway and low wings. Centerline extremes (2,2)-(46,46). Flag deliberately extends right; fine cornices omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9753b8d6-83c7-5ff0-8f5f-0f692f64e751'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/embassy building_9753b8d6-83c7-5ff0-8f5f-0f692f64e751.svg'
AUTHOR = 'gpt-6'

class DomedCivicBuildingWithFlag(Solo48):
    icon_id = 'domed-civic-building-with-flag'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/landmarks"
    aliases = ()
    keywords = ('embassy', 'government', 'dome', 'civic', 'flag', 'building', 'official', 'architecture')

    def build(self) -> None:
        self.add_polyline('flag', (24, 10), (34, 10), (34, 2), (24, 2), (24, 10), (24, 17), closed=False)
        self.add_arc('dome-left', (12, 29), (24, 17), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('dome-right', (24, 17), (36, 29), radius_x=12, radius_y=12, sweep=True)
        self.add_contour('dome', 'dome-left', 'dome-right', closed=False)
        self.add_polyline('body', (12, 29), (12, 46), (20, 46), (28, 46), (36, 46), (36, 29), (12, 29), closed=False)
        self.add_polyline('wing-left', (12, 34), (2, 34), (2, 46), (12, 46), closed=False)
        self.add_polyline('wing-right', (36, 34), (46, 34), (46, 46), (36, 46), closed=False)
        self.add_line('door-left', (20, 46), (20, 40))
        self.add_arc('door-arch', (20, 40), (28, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('door-right', (28, 40), (28, 46))
        self.add_contour('door', 'door-left', 'door-arch', 'door-right', closed=False)
        self.relate("connect", 'flag', 'dome')
        self.relate("connect", 'dome', 'body')
        self.relate("connect", 'body', 'wing-left')
        self.relate("connect", 'body', 'wing-right')
        self.relate("connect", 'body', 'door')
