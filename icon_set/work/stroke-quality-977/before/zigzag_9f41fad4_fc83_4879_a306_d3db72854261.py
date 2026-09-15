"""zigzag-9f41fad4: reviewed and repaired in place on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f41fad4-fc83-4879-a306-d3db72854261'
SOURCE_PATH = 'pictographic-primitives/interface-essential/zigzag_9f41fad4-fc83-4879-a306-d3db72854261.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-repaired'

class Zigzag9f41fad4(Solo48):
    icon_id = 'zigzag-9f41fad4'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('zigzag', 'interface-essential')

    def build(self):
        # SQUARE (6,6)-(42,42); equal eight-unit semicircular turns.
        # Construction reference: Lucide undo-2: tangent turns
        self.add_line('tail',(6,42),(34,42))
        self.add_arc('lower-turn',(34,42),(34,26),radius_x=8,sweep=False)
        self.add_line('middle',(34,26),(14,26))
        self.add_arc('upper-turn',(14,26),(14,10),radius_x=8)
        self.add_line('shaft',(14,10),(38,10))
        self.add_contour('run','tail','lower-turn','middle','upper-turn','shaft')
        self.add_polyline('head',(34,6),(38,10),(34,14))
        self.relate('connect','run','head')
