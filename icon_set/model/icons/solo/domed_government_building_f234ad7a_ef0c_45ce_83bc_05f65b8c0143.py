'Government hall with dome and three windows. SQUARE centerlines (6,6)-(42,42). Repeated windows share spacing. Lucide landmark informs rhythm; extra cornices and drum window omitted.'
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
    category = "landmarks"
    aliases = ()
    keywords = ('government', 'official', 'building', 'dome', 'civic', 'parliament', 'institution', 'architecture')

    def build(self) -> None:
        axis, left, right, bottom = 24, 6, 42, 42
        self.add_polyline('base',(left,bottom),(left,26),(14,26),(34,26),(right,26),(right,bottom),closed=True)
        self.add_polyline('drum',(14,26),(14,18),(34,18),(34,26))
        self.add_arc('dome-left',(14,18),(axis,8),radius_x=10)
        self.add_arc('dome-right',(axis,8),(34,18),radius_x=10)
        self.add_contour('dome','dome-left','dome-right')
        self.add_line('finial',(axis,6),(axis,8))
        for n in range(3):
            self.add_dot(f'window-{n}',(axis+(n-1)*10,34))
        for a,b in [('base','drum'),('drum','dome'),('dome','finial')]:
            self.relate('connect',a,b)
