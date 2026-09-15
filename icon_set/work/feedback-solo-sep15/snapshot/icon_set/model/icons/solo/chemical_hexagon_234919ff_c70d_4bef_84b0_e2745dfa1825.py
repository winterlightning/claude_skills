'Chemical structure: balanced six-sided rings, clear bond lengths and exact branch junctions, preserving the molecular topology.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '234919ff-c70d-4bef-84b0-e2745dfa1825'
SOURCE_PATH = 'pictographic-primitives/health/chemical hexagon_234919ff-c70d-4bef-84b0-e2745dfa1825.svg'
AUTHOR = 'gpt-6'

class ChemicalHexagon(Solo48):
    icon_id = 'chemical-hexagon'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('chemical', 'hexagon', 'health')

    def build(self) -> None:
        # Two matching six-sided rings with separate bonds and explicit real attachment points.
        self.add_polyline('ring-left',(11,24),(18,28),(18,36),(11,40),(4,36),(4,28),closed=True)
        self.add_polyline('ring-right',(33,12),(40,16),(40,24),(33,28),(26,24),(26,16),closed=True)
        self.add_line('bond',(18,28),(26,24))
        self.relate('connect','bond','ring-left')
        self.relate('connect','bond','ring-right')
        self.add_polyline('branch',(4,8),(4,12),(11,16),(18,12),(18,8))
        self.add_line('stem',(11,16),(11,24))
        self.relate('connect','stem','branch')
        self.relate('connect','stem','ring-left')
        self.add_line('terminal',(40,16),(44,12))
        self.relate('connect','terminal','ring-right')
