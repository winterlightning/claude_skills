"""Left-facing hedgehog with pointed muzzle and jagged spine silhouette; two visible feet replace four crowded strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '089d2df6-f974-42a3-9741-489bc35e9055'
SOURCE_PATH = 'pictographic-primitives/animals/hedgehog_089d2df6-f974-42a3-9741-489bc35e9055.svg'
AUTHOR = 'gpt-6'


class Hedgehog(Solo48):
    icon_id = 'hedgehog'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('hedgehog', 'spikes', 'quills', 'animal', 'prickly', 'wildlife', 'porcupine', 'small')

    def build(self) -> None:
        # Keyshape ink extremes: (0, 6, 48, 42); centerlines inset by stroke radius 2.
        self.add_line('body-1', (2, 30), (12, 22))
        self.add_line('body-2', (12, 22), (12, 14))
        self.add_line('body-3', (12, 14), (21, 18))
        self.add_line('body-4', (21, 18), (23, 8))
        self.add_line('body-5', (23, 8), (30, 17))
        self.add_line('body-6', (30, 17), (38, 12))
        self.add_line('body-7', (38, 12), (38, 22))
        self.add_line('body-8', (38, 22), (46, 27))
        self.add_line('body-9', (46, 27), (46, 30))
        self.add_arc('body-10', (46, 30), (34, 35), radius_x=17, radius_y=8, sweep=True)
        self.add_line('body-11', (34, 35), (12, 35))
        self.add_line('body-12', (12, 35), (2, 30))
        self.add_contour('body', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', 'body-8', 'body-9', 'body-10', 'body-11', 'body-12', closed=True)
        self.add_line('front-foot', (12, 35), (12, 40))
        self.relate("connect", 'front-foot', 'body')
        self.add_line('rear-foot', (34, 35), (34, 40))
        self.relate("connect", 'rear-foot', 'body')
