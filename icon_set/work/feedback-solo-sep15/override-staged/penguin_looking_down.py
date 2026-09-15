"""Give the penguin a rounder forward belly and a sharper downward-pointing bill, opening up its left profile. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ca363f4-f61f-5da3-a3be-41fa52d1fa3a'
SOURCE_PATH = 'pictographic-primitives/animals/penguin mother_9ca363f4-f61f-5da3-a3be-41fa52d1fa3a.svg'
AUTHOR = 'gpt-6'

class PenguinLookingDown(Solo48):
    icon_id = 'penguin-looking-down'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('penguin', 'bending', 'looking', 'down', 'bird', 'antarctic', 'nurture', 'care')

    def build(self) -> None:
        """Symbol plan: Give the penguin a rounder forward belly and a sharper downward-pointing bill, opening up its left profile. Reference: Lucide bird: a clear bill and one open inner wing curve."""
        self.add_bezier('head', (12, 16), ((14, 9), (19, 4), (24, 4)), ((31, 4), (35, 9), (36, 15)))
        self.add_bezier('back', (36, 15), ((38, 22), (40, 29), (40, 34)), ((40, 40), (34, 44), (28, 44)))
        self.add_line('base', (28, 44), (18, 44))
        self.add_bezier('belly', (18, 44), ((10, 42), (10, 32), (14, 28)))
        self.add_line('beak-low', (14, 28), (8, 26))
        self.add_line('beak-high', (8, 26), (12, 16))
        self.add_contour('outline', 'head', 'back', 'base', 'belly', 'beak-low', 'beak-high', closed=True)
        self.add_dot('eye', (23, 15))
        self.add_bezier('flipper', (28, 25), ((30, 29), (28, 34), (26, 35)))
