"""A circular fuel gauge labelled E with a diagonal needle. CIRCLE visible radius 22, centerline radius 20. Lucide gauge informed the face and needle; narrow monoline E retains the empty reading."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '293432b3-59da-44f7-9810-43c9f99bcef0'
SOURCE_PATH = 'pictographic-primitives/transportation/car dashboard e_293432b3-59da-44f7-9810-43c9f99bcef0.svg'
SOURCE_REFERENCES = (('293432b3-59da-44f7-9810-43c9f99bcef0', 'pictographic-primitives/transportation/car dashboard e_293432b3-59da-44f7-9810-43c9f99bcef0.svg'),)
AUTHOR = 'gpt-6'

class FuelGaugeEmpty(Solo48):
    icon_id = 'fuel-gauge-empty'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('fuel gauge', 'empty', 'fuel', 'gauge', 'dashboard', 'car', 'petrol', 'low fuel')

    def build(self) -> None:
        self.add_arc('face-top',(6,24),(42,24),radius_x=20)
        self.add_arc('face-bottom',(42,24),(6,24),radius_x=20)
        self.add_contour('face','face-top','face-bottom',closed=True)
        self.add_polyline('e-outline',(22,16),(16,16),(16,24),(16,32),(22,32))
        self.add_line('e-middle',(16,24),(22,24))
        self.relate('connect','e-middle','e-outline')
        self.add_line('needle',(30,32),(34,24))
