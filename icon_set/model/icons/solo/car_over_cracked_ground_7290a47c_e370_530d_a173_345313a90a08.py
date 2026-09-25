'car-over-cracked-ground: independent smooth-curve repair.\n\nConstruction: A front-facing car above a broad road fracture; paired roof curves and short wheel legs.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/car-front.svg and atomic-debug/car-front.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '7290a47c-e370-530d-a173-345313a90a08'
SOURCE_PATH = 'pictographic-primitives/weather/earthquake car shaking_7290a47c-e370-530d-a173-345313a90a08.svg'
AUTHOR = 'gpt-6'


class CarOverCrackedGround(Solo48):
    icon_id = 'car-over-cracked-ground'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'weather'
    aliases = ()
    keywords = ('car', 'earthquake', 'crack', 'road', 'tremor', 'disaster')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'car',(4,24),('L',(4,16)),('L',(12,16)),('C',(16,16),(17,8),(21,8)),('L',(27,8)),('C',(31,8),(32,16),(36,16)),('L',(44,16)),('L',(44,24)),('L',(36,24)),('L',(12,24)),('L',(4,24)),closed=True)
        line(self,'wheel-left',(12,24),(12,28))
        line(self,'wheel-right',(36,24),(36,28))
        poly(self,'ground',(4,38),(16,38),(24,40),(32,38),(44,38))
        contacts(self)
