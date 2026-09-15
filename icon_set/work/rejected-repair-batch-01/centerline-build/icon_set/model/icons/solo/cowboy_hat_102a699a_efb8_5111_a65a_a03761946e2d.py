'cowboy-hat: Narrowed the brim and joined the crown to shared brim points. Keyshape HRECT_L; SOLO48 stroke 4. Reviewed at 48 px in both themes.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '102a699a-efb8-5111-a65a-a03761946e2d'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-04/hat cowboy_102a699a-efb8-5111-a65a-a03761946e2d.svg'
AUTHOR = 'gpt-6'

class CowboyHat(Solo48):
    icon_id = 'cowboy-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('hat', 'cowboy hat', 'western', 'stetson', 'brim', 'ranch', 'headwear', 'country')

    def build(self) -> None:
        self.add_polyline('crown', (11, 28), (16, 8), (24, 12), (32, 8), (37, 28), closed=False)
        self.add_line('brim-left', (4, 24), (11, 28))
        self.add_line('brim-middle', (11, 28), (37, 28))
        self.add_line('brim-right', (37, 28), (44, 24))
        self.add_arc('brim-base', (44, 24), (4, 24), radius_x=20, radius_y=16, sweep=True, large_arc=False)
        self.add_contour('brim', 'brim-left', 'brim-middle', 'brim-right', 'brim-base', closed=True)
        self.relate('connect', 'crown', 'brim')
