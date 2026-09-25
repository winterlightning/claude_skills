"""Round the seated fox back and hindquarters, and make the raised tail flow into the base with a continuous tangent. Applied to the original icon identity."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '47ad4fc2-b439-5ef7-adbd-a64d7a859c79'
SOURCE_PATH = 'pictographic-primitives/animals/fox tail_47ad4fc2-b439-5ef7-adbd-a64d7a859c79.svg'
AUTHOR = 'gpt-6'

class SittingFox(Solo48):
    icon_id = 'sitting-fox'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ()
    keywords = ('sitting', 'fox')

    def build(self) -> None:
        """Symbol plan: Round the seated fox back and hindquarters, and make the raised tail flow into the base with a continuous tangent. Reference: Lucide cat: pointed ears above a simple curved body."""
        self.add_line('ear-back', (6, 19), (15, 6))
        self.add_line('ear-front', (15, 6), (15, 12))
        self.add_arc('brow', (15, 12), (24, 21), radius_x=9, radius_y=9, sweep=True)
        self.add_line('snout', (24, 21), (26, 21))
        self.add_bezier('muzzle', (26, 21), ((26, 23), (22, 24), (18, 24)))
        self.add_bezier('chest', (18, 24), ((18, 29), (19, 32), (22, 33)))
        self.add_bezier('tail-inner', (22, 33), ((32, 33), (36, 23), (36, 16)))
        self.add_bezier('tail-outer', (36, 16), ((40, 16), (42, 23), (42, 30)))
        self.add_bezier('base-right', (42, 30), ((42, 38), (35, 42), (27, 42)))
        self.add_line('base', (27, 42), (10, 42))
        self.add_bezier('base-left', (10, 42), *(((8.58489728, 42), (7.12743399, 41.89315455), (6, 41)),))
        self.add_bezier('back', (6, 41), ((6, 34), (8, 26), (6, 19)))
        self.add_contour('silhouette', 'ear-back', 'ear-front', 'brow', 'snout', 'muzzle', 'chest', 'tail-inner', 'tail-outer', 'base-right', 'base', 'base-left', 'back')
