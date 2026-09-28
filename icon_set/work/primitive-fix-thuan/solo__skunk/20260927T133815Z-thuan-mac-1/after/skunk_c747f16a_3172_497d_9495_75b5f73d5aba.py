'Skunk: independent spacing revision.\n\nRebalanced geometry for eight-unit straight spacing and clear curved openings.\nNative solo family, HRECT_XL keyshape. The original model is preserved.\nDirectional and natural asymmetry follows the supplied subject.\nFinal construction review: Original subject render; no exact Lucide match selected.\n'
# Variant of skunk; parent file remains unchanged.
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c747f16a-3172-497d-9495-75b5f73d5aba'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__skunk/20260927T133815Z-thuan-mac-1/reference/skunk_c747f16a-3172-497d-9495-75b5f73d5aba.svg'
AUTHOR = 'gpt-6'

class Skunk(Solo48):
    icon_id = 'skunk'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('skunk', 'tail', 'bushy', 'stripe', 'animal', 'wildlife', 'spray', 'nocturnal')

    def build(self):
        # Directional silhouette: tall curled plume, low body, tapered muzzle,
        # and two separate feet. The curl is intentionally asymmetric.
        start = (4, 26)
        curves = [
            ((4, 14), (8, 8), (16, 8)),
            ((24, 8), (26, 16), (18, 24)),
            ((24, 20), (28, 21), (30, 22)),
            ((31, 18), (34, 18), (36, 20)),
            ((40, 20), (42, 22), (44, 24)),
            ((41, 28), (39, 28), (37, 28)),
            ((37, 31), (38, 35), (38, 40)),
        ]
        self.add_bezier('upper', start, *curves)
        feet = ((38, 40), (29, 40), (29, 32), (19, 32),
                (19, 40), (10, 40), (10, 27))
        for index, (begin, end) in enumerate(zip(feet, feet[1:])):
            self.add_line(f'feet-{index}', begin, end)
        self.add_bezier('tail-return', (10, 27), ((8, 27), (6, 27), start))
        self.add_contour('skunk', 'upper', *(f'feet-{index}' for index in range(6)),
                         'tail-return', closed=True)
