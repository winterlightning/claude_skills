"""Feathered war bonnet with hanging side feathers. SQUARE (2,2)-(46,46). Five upright feathers reduced to three; removed veins and band thickness for clearance. Shared axis, mirrored feathers; no useful direct Lucide match."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5ae08697-a439-498f-937f-0695fa985da7'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/indian feather_5ae08697-a439-498f-937f-0695fa985da7.svg'


class FeatheredWarBonnet(Solo48):
    icon_id = 'feathered-war-bonnet'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('headdress', 'war bonnet', 'feather', 'native american', 'tribal', 'ceremonial', 'plains', 'culture')

    def build(self) -> None:
        self.add_arc('band', (8,32), (40,32), radius_x=24, radius_y=12)
        self.add_polyline('center-feather', (19,21), (19,10), (24,2), (29,10), (29,21))
        self.add_polyline('left-feather', (11,24), (4,14), (2,7), (10,11), (12,17))
        self.add_polyline('right-feather', (37,24), (44,14), (46,7), (38,11), (36,17))
        self.add_arc('left-pendant', (8,39), (8,46), radius_x=5, radius_y=7, sweep=False)
        self.add_arc('right-pendant', (40,39), (40,46), radius_x=5, radius_y=7)
