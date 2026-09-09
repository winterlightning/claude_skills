# Variant of olive-laurel-wreath; parent file remains unchanged.
"""Mirrored open laurel wreath with two outer leaf strokes per side. Removed interior leaf clutter; the SQUARE footprint preserves the broad award silhouette. No useful exact Lucide match was found."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eb8a9192-a034-4f5e-9ce7-1f936af4994a'
SOURCE_PATH = 'pictographic-primitives/culture/batch-05/olive wreath_eb8a9192-a034-4f5e-9ce7-1f936af4994a.svg'
AUTHOR = 'gpt-6'

class OliveLaurelWreathVariant2(Solo48):
    icon_id = 'olive-laurel-wreath-v2'
    variant_of = 'olive-laurel-wreath'
    variant_label = 'Simpler laurel branches'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('wreath', 'laurel', 'olive', 'victory', 'greek', 'award', 'olympic', 'honour')

    def build(self) -> None:
        for side, flip in (('left', False), ('right', True)):

            def p(x, y):
                return (48 - x if flip else x, y)
            self.add_line(side + '-tip', p(18, 2), p(14, 10))
            self.add_arc(side + '-upper', p(14, 10), p(8, 28), radius_x=6, radius_y=18, sweep=flip)
            self.add_arc(side + '-lower', p(8, 28), p(12, 38), radius_x=16, radius_y=18, sweep=flip)
            self.add_arc(side + '-foot', p(12, 38), p(24, 46), radius_x=16, radius_y=18, sweep=flip)
            self.add_contour(side, side + '-tip', side + '-upper', side + '-lower', side + '-foot')
            for name, a, b in (('outer-high', (8, 28), (2, 18)), ('outer-low', (12, 38), (2, 34))):
                self.add_line(side + '-' + name, p(*a), p(*b))
                self.relate('connect', side, side + '-' + name)
        self.relate('connect', 'left', 'right')
