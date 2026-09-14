# Variant of chicken-face; parent file remains unchanged.
"""Chicken face with circular comb and a larger diamond beak. VRECT_L visible bounds (6,2)-(42,46). Lucide bird informed the simple round head."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7443f092-4834-4d07-9b5b-1b7914777905'
SOURCE_PATH = 'pictographic-primitives/animals/chicken_7443f092-4834-4d07-9b5b-1b7914777905.svg'
AUTHOR = 'gpt-6'

class ChickenFaceVariant2(Solo48):
    icon_id = 'chicken-face-v2'
    variant_of = 'chicken-face'
    variant_label = 'Roomier spacing — review 02'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('chicken', 'hen', 'face', 'head', 'comb', 'beak', 'farm', 'poultry')

    def build(self) -> None:
        self.add_line('left', (8,44), (8,28))
        self.add_arc('arch', (8,28), (40,28), radius_x=16, sweep=True)
        self.add_line('right', (40,28), (40,44))
        self.add_contour('face','left','arch','right')
        self.add_arc('comb-left',(24,12),(20,8),radius_x=4)
        self.add_arc('comb-top',(20,8),(28,8),radius_x=4)
        self.add_arc('comb-right',(28,8),(24,12),radius_x=4)
        self.add_contour('comb','comb-left','comb-top','comb-right',closed=True)
        self.relate('connect','comb','face')
        self.add_dot('eye-left',(17,25))
        self.add_dot('eye-right',(31,25))
        self.add_polyline('beak',(24,32),(30,38),(24,44),(18,38),closed=True)
