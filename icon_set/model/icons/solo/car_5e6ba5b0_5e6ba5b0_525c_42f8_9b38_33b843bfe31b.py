'car-5e6ba5b0: independent smooth-curve repair.\n\nConstruction: Frontal car with a smooth roof, equal wheel circles and body attached at wheel extrema.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nReference inspected: icon_set/references/lucide/original/car-front.svg and atomic-debug/car-front.svg (geometric construction).\nOriginal source and parent geometry preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '5e6ba5b0-525c-42f8-9b38-33b843bfe31b'
SOURCE_PATH = 'pictographic-primitives/transportation/car_5e6ba5b0-525c-42f8-9b38-33b843bfe31b.svg'
AUTHOR = 'gpt-6'


class Car5e6ba5b0(Solo48):
    icon_id = 'car-5e6ba5b0'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('solo-ai-cars-refine', 'solo-ai-next100', 'car-5e6ba5b0')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'roof',(12,19),('L',(17,10)),('C',(18,8),(20,8),(24,8)),('C',(28,8),(30,8),(31,10)),('L',(36,19)))
        path(self,'body',(8,34),('C',(5,34),(4,30),(4,27)),('L',(4,24)),('C',(4,21),(7,19),(12,19)),('L',(36,19)),('C',(41,19),(44,21),(44,24)),('L',(44,27)),('C',(44,30),(43,34),(40,34)))
        ellipse(self,'wheel-left',14,34,6)
        ellipse(self,'wheel-right',34,34,6)
        line(self,'floor',(20,34),(28,34))
        contacts(self)
