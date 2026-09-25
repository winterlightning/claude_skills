"""Arched orca with dorsal fin, pectoral fin and notched fluke; preserves source left tail and right snout."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2c27c974-982c-51c2-b118-2da9443f5956'
SOURCE_PATH = 'pictographic-primitives/animals/orca whale_2c27c974-982c-51c2-b118-2da9443f5956.svg'
AUTHOR = 'gpt-6'


class LeapingOrca(Solo48):
    icon_id = 'leaping-orca'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('leaping', 'orca')

    def build(self) -> None:
        # Preserve interior detail sizes; move only the outer edge bands to the exact envelope.
        # Curves reaching an edge use bounded cubic controls, with shared endpoints retained.
        self.add_bezier('back',(9,26),((10,18),(18,15),(25,15)))
        self.add_line('dorsal-rise',(25, 15),(25, 8))
        self.add_bezier('dorsal-fall',(25, 8),*(((29.56722133, 9.25310672), (33.27438444, 12.58955353), (35, 17)),))
        self.add_bezier('head',(35, 17),*(((41.12839831, 21.37337687), (44, 27.58326187), (44, 34)),))
        self.add_bezier('nose',(44, 34),*(((44, 35.08185107), (43.5613883, 36.13451915), (43, 37)),))
        self.add_line('chin',(43, 37),(33, 33))
        self.add_arc('pectoral',(33, 33),(23, 37),radius_x=12,radius_y=12,large_arc=False,sweep=True)
        self.add_line('fin-front',(23, 37),(26, 30))
        self.add_bezier('belly',(26,30),((21,29),(17,32),(13,33)))
        self.add_line('tail-top',(13, 33),(9, 40))
        self.add_line('notch',(9, 40),(5, 32))
        self.add_line('fluke',(5, 32),(4, 30))
        self.add_bezier('tail-back',(4, 30),*(((5.15069965, 28.30947274), (6.88684092, 26.92055972), (9, 26)),))
        self.add_contour('outline',*('back', 'dorsal-rise', 'dorsal-fall', 'head', 'nose', 'chin', 'pectoral', 'fin-front', 'belly', 'tail-top', 'notch', 'fluke', 'tail-back'),closed=True)
