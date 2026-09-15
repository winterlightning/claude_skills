'car-e1ae9ac1: distinct review variant.\n\nConstruction: Compact car with an arched roof and a central windshield pillar; retain the circular wheels.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: car-front from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = 'e1ae9ac1-dad6-526e-975f-e2ee61a2940d'
SOURCE_PATH = 'pictographic-primitives/transportation/car_e1ae9ac1-dad6-526e-975f-e2ee61a2940d.svg'
AUTHOR = 'gpt-6'


class CarE1ae9ac1Variant2(Solo48):
    icon_id = 'car-e1ae9ac1-v2'
    variant_of = 'car-e1ae9ac1'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('solo-ai-cars-refine', 'solo-ai-next100', 'car-e1ae9ac1')
    keyshape = Keyshape.HRECT_L

    def build(self):
        path(self,'roof',(12,19),('A',12,11,True,(24,8)),('A',12,11,True,(36,19)))
        line(self,'windshield-pillar',(24,8),(24,19))
        path(self,'body',(8,34),('C',(5,34),(4,30),(4,27)),('L',(4,24)),('C',(4,21),(7,19),(12,19)),('L',(36,19)),('C',(41,19),(44,21),(44,24)),('L',(44,27)),('C',(44,30),(43,34),(40,34)))
        ellipse(self,'wheel-left',14,34,6)
        ellipse(self,'wheel-right',34,34,6)
        line(self,'floor',(20,34),(28,34))
        contacts(self)
