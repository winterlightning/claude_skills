"""Deep rounded fish with fan tail and projecting fin tips; use the Lucide fish principle of a coherent body with sparse detail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '74be0015-3ba7-55f3-9fe4-881684a7dad4'
SOURCE_PATH = 'pictographic-primitives/animals/fish 1_74be0015-3ba7-55f3-9fe4-881684a7dad4.svg'
AUTHOR = 'gpt-6'


class ReefFish(Solo48):
    icon_id = 'reef-fish'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('reef', 'fish')

    def build(self) -> None:
        # Visible keyshape bounds: (0, 0, 48, 48); centerlines inset by 2.
        self.add_bezier('body-upper', (17, 6), *(((27.85802261, 6), (37.44842352, 11.19601141), (40, 19)),))
        self.add_line('snout-upper', (40, 19), (42, 24))
        self.add_line('snout-lower', (42, 24), (40, 29))
        self.add_bezier('body-lower', (40, 29), *(((37.44842352, 36.80398859), (27.85802261, 42), (17, 42)),))
        self.add_bezier('body-back-low',(17,42),((17,36),(16,29),(16,24)))
        self.add_bezier('body-back-high',(16,24),((16,19),(17,12),(17,6)))
        self.add_contour('body', 'body-upper', 'snout-upper', 'snout-lower', 'body-lower', 'body-back-low', 'body-back-high')
        self.add_line('fin-top', (17, 6), (10, 6))
        self.add_line('fin-bottom', (17, 42), (10, 42))
        self.relate("connect", 'body', 'fin-top')
        self.relate("connect", 'body', 'fin-bottom')
        self.add_polyline('tail',(16,24),(6,15),(6,33),(16,24))
        self.relate("connect", 'body', 'tail')
