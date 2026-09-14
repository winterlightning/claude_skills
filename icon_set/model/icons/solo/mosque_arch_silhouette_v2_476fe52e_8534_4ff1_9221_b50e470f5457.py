"""Mosque ogee silhouette, blank as in source. VRECT_XL centerlines (8,6)-(40,42) preserves upright proportions. Shared-axis mirrored shoulders. No useful Lucide ogee match; no added detail."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '476fe52e-8534-4ff1-9221-b50e470f5457'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-04/mosque_476fe52e-8534-4ff1-9221-b50e470f5457.svg'
AUTHOR = 'gpt-6'

class MosqueArchSilhouetteVariant2(Solo48):
    icon_id = 'mosque-arch-silhouette-v2'
    variant_of = 'mosque-arch-silhouette'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('mosque', 'arch', 'ogee', 'islamic', 'mihrab', 'silhouette', 'religion', 'architecture')

    def build(self) -> None:
        self.add_arc('tip-left', (24, 4), (16, 12), radius_x=8, sweep=True)
        self.add_arc('bulb-left', (16, 12), (8, 20), radius_x=8, sweep=False)
        self.add_arc('shoulder-left', (8, 20), (12, 28), radius_x=4, radius_y=8, sweep=False)
        points = [(12, 28), (8, 32), (8, 44), (40, 44), (40, 32), (36, 28)]
        for n, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f'walls-{n}', a, b)
        self.add_arc('shoulder-right', (36, 28), (40, 20), radius_x=4, radius_y=8, sweep=False)
        self.add_arc('bulb-right', (40, 20), (32, 12), radius_x=8, sweep=False)
        self.add_arc('tip-right', (32, 12), (24, 4), radius_x=8, sweep=True)
        self.add_contour('outline', 'tip-left', 'bulb-left', 'shoulder-left', 'walls-1', 'walls-2', 'walls-3', 'walls-4', 'walls-5', 'shoulder-right', 'bulb-right', 'tip-right', closed=True)
