# Variant of hammerhead-shark; parent file remains unchanged.
'Hammerhead shark with an enlarged angular tail and straight fork edges. SQUARE (2,2)-(46,46) preserves hammer width and tail extent. Curved tail edge replaced; swept body remains deliberately asymmetric.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bdd1577c-6f14-5bee-a41f-fac2b80017a7'
SOURCE_PATH = 'pictographic-primitives/animals/shark hammer_bdd1577c-6f14-5bee-a41f-fac2b80017a7.svg'
AUTHOR = 'gpt-6'

class HammerheadSharkVariant2(Solo48):
    icon_id = 'hammerhead-shark-v2'
    variant_of = 'hammerhead-shark'
    variant_label = 'Larger geometric tail'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals/marine'
    aliases = ()
    keywords = ('hammerhead', 'shark', 'head', 'fins', 'sea', 'ocean', 'fish', 'predator')

    def build(self) -> None:
        self.add_line('body-1', (2, 2), (35, 2))
        self.add_line('body-2', (35, 2), (35, 10))
        self.add_line('body-3', (35, 10), (27, 10))
        self.add_line('body-4', (27, 10), (27, 20))
        self.add_line('body-5', (27, 20), (35, 26))
        self.add_line('body-6', (35, 26), (27, 26))
        self.add_line('body-7', (27, 26), (27, 29))
        self.add_arc('body-8', (27, 29), (36, 38), radius_x=9, radius_y=9, sweep=False)
        self.add_line('body-9', (36, 38), (36, 34))
        self.add_line('body-10', (36, 34), (46, 26))
        self.add_line('tail-notch-top', (46,26), (42,36))
        self.add_line('body-11', (42,36), (46,46))
        self.add_line('body-12', (46, 46), (34, 43))
        self.add_line('body-13', (34, 43), (29, 43))
        self.add_arc('body-14', (29, 43), (13, 27), radius_x=16, radius_y=16, sweep=True)
        self.add_line('body-15', (13, 27), (5, 27))
        self.add_line('body-16', (5, 27), (13, 19))
        self.add_line('body-17', (13, 19), (13, 10))
        self.add_line('body-18', (13, 10), (2, 10))
        self.add_line('body-19', (2, 10), (2, 2))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'tail-notch-top', 'body-11', 'body-12', 'body-13', 'body-14', 'body-15', 'body-16', 'body-17', 'body-18', 'body-19', closed=True)
        self.add_line('gill-1', (20, 18), (20, 23))
        self.add_contour('gill', 'gill-1', closed=False)
