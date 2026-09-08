"""Standing wild boar: heavy torso, pricked ear and blunt snout. Two near legs retain the stance; tiny tusk and far legs omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a98da8f2-0b65-4ef8-957c-18e1f4b59c72'
SOURCE_PATH = 'pictographic-primitives/animals/wild pig body_a98da8f2-0b65-4ef8-957c-18e1f4b59c72.svg'
AUTHOR = 'gpt-6'


class WildBoar(Solo48):
    icon_id = 'wild-boar'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/animals"
    aliases = ()
    keywords = ('boar', 'pig', 'hog', 'standing', 'snout', 'tusk', 'farm', 'wildlife')

    def build(self) -> None:
        self.add_arc('back-round', (6, 25), (19, 12), radius_x=13, radius_y=13, sweep=True)
        self.add_line('back', (19, 12), (32, 12))
        self.add_line('ear-1', (32, 12), (37, 8))
        self.add_line('ear-2', (37, 8), (36, 17))
        self.add_arc('face', (36, 17), (46, 24), radius_x=12, radius_y=12, sweep=False)
        self.add_arc('snout', (46, 24), (40, 31), radius_x=6, radius_y=7, sweep=True)
        self.add_line('chin', (40, 31), (35, 29))
        self.add_arc('chest', (35, 29), (30, 34), radius_x=5, radius_y=5, sweep=False)
        self.add_line('foreleg-1', (30, 34), (32, 40))
        self.add_line('foreleg-2', (32, 40), (25, 40))
        self.add_line('foreleg-3', (25, 40), (22, 32))
        self.add_line('foreleg-4', (22, 32), (16, 32))
        self.add_line('foreleg-5', (16, 32), (14, 40))
        self.add_line('foreleg-6', (14, 40), (8, 40))
        self.add_line('foreleg-7', (8, 40), (8, 31))
        self.add_arc('rump', (8, 31), (6, 25), radius_x=10, radius_y=10, sweep=True)
        self.add_contour('outline', 'back-round', 'back', 'ear-1', 'ear-2', 'face', 'snout', 'chin', 'chest', 'foreleg-1', 'foreleg-2', 'foreleg-3', 'foreleg-4', 'foreleg-5', 'foreleg-6', 'foreleg-7', 'rump', closed=True)
        self.add_arc('tail-round', (6, 25), (2, 21), radius_x=4, radius_y=4, sweep=True)
        self.add_line('tail-end', (2, 21), (2, 14))
        self.add_contour('tail', 'tail-round', 'tail-end', closed=False)
        self.relate("connect", 'outline', 'tail')
