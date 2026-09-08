"""Standing fox with an open tail flowing into the back, a rounded haunch, pointed ear and two visible legs."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2531d4f-210e-48fb-888b-269b7179c1ab'
SOURCE_PATH = 'pictographic-primitives/animals/fox body_a2531d4f-210e-48fb-888b-269b7179c1ab.svg'
AUTHOR = 'gpt-6'


class StandingFox(Solo48):
    icon_id = 'standing-fox'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('standing', 'fox')

    def build(self) -> None:
        # SQUARE visible bounds (0, 0, 48, 48); centerlines (2, 2, 46, 46).
        self.add_arc('tail-outer-top', (2, 17), (14, 2), radius_x=12, radius_y=15, sweep=True)
        self.add_arc('tail-inner', (14, 2), (10, 24), radius_x=27, radius_y=27, sweep=True)
        self.add_arc('tail-root', (10, 24), (12, 26), radius_x=2, radius_y=2, sweep=False)
        self.add_arc('tail-outer-low', (6, 32), (2, 17), radius_x=4, radius_y=15, sweep=True)
        self.add_contour('tail', 'tail-outer-low', 'tail-outer-top', 'tail-inner', 'tail-root')
        self.add_arc('hip-top', (12, 26), (16, 24), radius_x=4, radius_y=2, sweep=True)
        self.add_line('back', (16, 24), (26, 24))
        self.add_line('neck', (26, 24), (26, 16))
        self.add_arc('forehead', (26, 16), (32, 8), radius_x=6, radius_y=8, sweep=True)
        self.add_line('ear', (32, 8), (32, 16))
        self.add_arc('brow', (32, 16), (40, 24), radius_x=8, radius_y=8, sweep=True)
        self.add_line('muzzle', (40, 24), (46, 24))
        self.add_arc('jaw', (46, 24), (36, 34), radius_x=10, radius_y=10, sweep=True)
        self.add_arc('chest', (36, 34), (32, 38), radius_x=4, radius_y=4, sweep=False)
        self.add_line('foreleg', (32, 38), (32, 46))
        self.add_contour('upper', 'hip-top', 'back', 'neck', 'forehead', 'ear', 'brow', 'muzzle', 'jaw', 'chest', 'foreleg')
        self.relate("connect", 'tail', 'upper')
        self.add_line('hind', (6, 32), (6, 40))
        self.add_line('rear-foot', (6, 40), (2, 46))
        self.add_contour('rear', 'hind', 'rear-foot')
        self.relate("connect", 'rear', 'tail')
        self.add_arc('haunch', (18, 30), (10, 38), radius_x=8, radius_y=8, sweep=True)
        self.add_line('hip-low', (10, 38), (6, 40))
        self.add_contour('thigh', 'haunch', 'hip-low')
        self.add_line('belly', (10, 38), (32, 38))
        self.relate("connect", 'thigh', 'belly')
        self.relate("connect", 'rear', 'thigh')
        self.relate("connect", 'belly', 'upper')
