'car-9e5f3201: distinct review variant.\n\nConstruction: Front-view car with a broad windshield and simple upright tires, distinct from the round wheel version.\nKeyshape: HRECT_L; exact SOLO48 envelope.\nConstruction reference: car-front from the previously inspected Lucide original and atomic-debug library.\nPrevious canonical model is preserved.'
from ...keyshapes import Keyshape
from ._base import Solo48
from ._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '9e5f3201-71ac-4e37-97ac-b3416198d4da'
SOURCE_PATH = 'pictographic-primitives/transportation/car_9e5f3201-71ac-4e37-97ac-b3416198d4da.svg'
AUTHOR = 'gpt-6'


class Car9e5f3201Variant2(Solo48):
    icon_id = 'car-9e5f3201-v2'
    variant_of = 'car-9e5f3201'
    variant_label = 'Distinct subject and smooth curves'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('solo-ai-cars-refine', 'solo-ai-next100', 'car-9e5f3201')
    keyshape = Keyshape.HRECT_L

    def build(self):
        box(self,'body',4,18,44,32,4,xs=(12,36))
        path(self,'roof',(8,18),('L',(13,10)),('C',(14,8),(17,8),(20,8)),('L',(28,8)),('C',(31,8),(34,8),(35,10)),('L',(40,18)))
        line(self,'left-tire',(12,32),(12,40))
        line(self,'right-tire',(36,32),(36,40))
        contacts(self)
