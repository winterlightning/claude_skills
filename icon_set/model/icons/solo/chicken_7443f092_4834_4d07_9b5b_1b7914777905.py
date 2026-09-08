"""Front-facing chicken with symmetric arch, comb and diamond beak. Round head construction informed by Lucide bird; dash eyes reduced to dots."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7443f092-4834-4d07-9b5b-1b7914777905'
SOURCE_PATH = 'pictographic-primitives/animals/chicken_7443f092-4834-4d07-9b5b-1b7914777905.svg'
AUTHOR = 'gpt-6'


class ChickenFace(Solo48):
    icon_id = 'chicken-face'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('chicken', 'hen', 'face', 'head', 'comb', 'beak', 'farm', 'poultry')

    def build(self) -> None:
        # Visible bounds: (6, 0, 42, 48); centerline inset 2.
        self.add_line('left', (8, 46), (8, 27))
        self.add_arc('arch', (8, 27), (40, 27), radius_x=16, radius_y=16, sweep=True)
        self.add_line('right', (40, 27), (40, 46))
        self.add_contour('face', 'left', 'arch', 'right', closed=False)
        self.add_arc('comb-left', (24, 11), (19, 6), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('comb-top', (19, 6), (29, 6), radius_x=5, radius_y=4, sweep=True)
        self.add_arc('comb-right', (29, 6), (24, 11), radius_x=5, radius_y=5, sweep=True)
        self.add_contour('comb', 'comb-left', 'comb-top', 'comb-right', closed=True)
        self.relate("connect", 'comb', 'face')
        self.add_dot('eye-left', (16, 26))
        self.add_dot('eye-right', (32, 26))
        self.add_polyline('beak', (24, 33), (29, 38), (24, 43), (19, 38), (24, 33))
