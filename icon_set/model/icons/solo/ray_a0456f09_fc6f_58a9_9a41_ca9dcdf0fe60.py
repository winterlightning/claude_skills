"""Diagonal manta ray with pointed wings and curled whip tail. Extrema (6,6)-(42,42). Reduced cephalic lobe retained; no useful Lucide subject match. Asymmetry expresses swimming."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0456f09-fc6f-58a9-9a41-ca9dcdf0fe60'
SOURCE_PATH = 'pictographic-primitives/animals/ray_a0456f09-fc6f-58a9-9a41-ca9dcdf0fe60.svg'
AUTHOR = 'gpt-6'


class MantaRay(Solo48):
    icon_id = 'manta-ray'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('manta ray', 'stingray', 'sea', 'ocean', 'marine', 'fish', 'wings', 'swim')

    def build(self) -> None:
        # Diagonal manta ray with pointed wings and curled whip tail. Extrema (6,6)-(42,42). Reduced cephalic lobe retained; no useful Lucide subject match. Asymmetry expresses swimming.
        self.add_arc('front-lobe', (10, 6), (12, 12), radius_x=12, radius_y=12, sweep=True)
        self.add_arc('head', (12, 12), (6, 14), radius_x=8, radius_y=8, sweep=True)
        self.add_arc('left-shoulder', (6, 14), (7, 24), radius_x=12, radius_y=12, sweep=True)
        self.add_line('left-wing', (7, 24), (6, 42))
        self.add_arc('trailing-left', (6, 42), (24, 36), radius_x=26, radius_y=26, sweep=True)
        self.add_bezier('trailing-right',(24,36),((31,34),(33,29),(33,22)))
        self.add_arc('right-wing',(33,22),(42,6),radius_x=28)
        self.add_bezier('leading-right', (42, 6), *(((34.93681772, 6), (27.82695379, 6.09836534), (21, 8)),))
        self.add_arc('leading-left', (21, 8), (10, 6), radius_x=14, radius_y=14, sweep=True)
        self.add_contour('disc', 'front-lobe', 'head', 'left-shoulder', 'left-wing', 'trailing-left', 'trailing-right', 'right-wing', 'leading-right', 'leading-left')
        self.add_arc('tail-root', (24, 36), (28, 42), radius_x=6, radius_y=6, sweep=True)
        self.add_bezier('tail-curl', (28, 42), *(((30.47520861, 42), (33.52479139, 42), (36, 42)),))
        self.add_arc('tail-tip', (36, 42), (42, 36), radius_x=10, radius_y=10, sweep=False)
        self.add_contour('tail', 'tail-root', 'tail-curl', 'tail-tip')
        self.relate("connect", 'tail', 'disc')
