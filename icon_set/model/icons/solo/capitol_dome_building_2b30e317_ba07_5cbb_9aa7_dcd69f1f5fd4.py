'Capitol dome above a broad base. SQUARE centerlines (6,6)-(42,42). Shared axis, paired dome quarters; Lucide landmark informs sparse facade. Cupola ornament reduced to finial.'
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
    category = "landmarks"
    aliases = ()
    keywords = ('capitol', 'washington', 'government', 'dome', 'congress', 'landmark', 'building', 'civic')

    def build(self) -> None:
        axis, left, right, bottom = 24, 6, 42, 42
        self.add_polyline('base', (left,bottom),(left,32),(14,32),(axis,32),(34,32),(right,32),(right,bottom),closed=True)
        self.add_polyline('drum',(14,32),(14,22),(axis,22),(34,22),(34,32))
        self.add_arc('dome-left',(14,22),(axis,12),radius_x=10)
        self.add_arc('dome-right',(axis,12),(34,22),radius_x=10)
        self.add_contour('dome','dome-left','dome-right')
        self.add_line('finial',(axis,6),(axis,12))
        self.add_line('drum-divider',(axis,22),(axis,32))
        for a,b in [('base','drum'),('drum','dome'),('dome','finial'),('drum','drum-divider'),('base','drum-divider')]:
            self.relate('connect',a,b)
