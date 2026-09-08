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
    category = "objects/animals"
    aliases = ()
    keywords = ('reef', 'fish')

    def build(self) -> None:
        # Visible keyshape bounds: (0, 0, 48, 48); centerlines inset by 2.
        self.add_arc('body-upper', (17, 2), (40, 19), radius_x=23, radius_y=17, sweep=True)
        self.add_line('snout-upper', (40, 19), (46, 24))
        self.add_line('snout-lower', (46, 24), (40, 29))
        self.add_arc('body-lower', (40, 29), (17, 46), radius_x=23, radius_y=17, sweep=True)
        self.add_arc('body-back-low', (17, 46), (12, 24), radius_x=5, radius_y=22, sweep=True)
        self.add_arc('body-back-high', (12, 24), (17, 2), radius_x=5, radius_y=22, sweep=True)
        self.add_contour('body', 'body-upper', 'snout-upper', 'snout-lower', 'body-lower', 'body-back-low', 'body-back-high')
        self.add_line('fin-top', (17, 2), (10, 2))
        self.add_line('fin-bottom', (17, 46), (10, 46))
        self.relate("connect", 'body', 'fin-top')
        self.relate("connect", 'body', 'fin-bottom')
        self.add_polyline('tail', (12, 19), (2, 15), (2, 33), (12, 29))
        self.relate("connect", 'body', 'tail')
