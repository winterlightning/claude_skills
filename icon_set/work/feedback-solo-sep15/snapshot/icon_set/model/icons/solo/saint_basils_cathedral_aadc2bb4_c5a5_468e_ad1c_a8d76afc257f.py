"""VRECT_XL (8,6)-(40,42) centerlines. Preserve three pointed onion domes, taller central tower and broad base. Replace tight upright shoulder notches with open diagonal shoulders. Mirrored radii and coordinates about x=24.
Lucide church and castle inform clear roof/wall structure and simple arch construction.
Re-authored on the active SOLO48 contract from the supplied landmark render.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'aadc2bb4-c5a5-468e-ad1c-a8d76afc257f'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-01/saint basils cathderal_aadc2bb4-c5a5-468e-ad1c-a8d76afc257f.svg'
AUTHOR = 'gpt-6'

class Landmark(Solo48):
    icon_id = 'saint-basils-cathedral'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'places/landmarks'
    aliases = ()
    keywords = ('saint basil', 'moscow', 'russia', 'cathedral', 'onion dome', 'landmark', 'church', 'religion')

    def build(self):
        """Widen the two symmetric dome valleys by lowering their connecting shoulders."""
        self.add_polyline('base', (10, 30), (10, 44), (38, 44), (38, 30))
        for side in (-1, 1):
            p = 'left' if side < 0 else 'right'

            def pt(x, y):
                return (x if side < 0 else 48 - x, y)
            self.add_arc(p + '-lower', pt(10, 30), pt(8, 24), radius_x=2, radius_y=6, sweep=side < 0)
            self.add_arc(p + '-outer', pt(8, 24), pt(12, 16), radius_x=10, radius_y=10, sweep=side < 0)
            self.add_arc(p + '-inner', pt(12, 16), pt(16, 24), radius_x=10, radius_y=10, sweep=side < 0)
            self.add_arc(p + '-inner-lower', pt(16, 24), pt(14, 30), radius_x=2, radius_y=6, sweep=side < 0)
            self.add_polyline(p + '-shoulder', pt(14, 30), pt(19, 28), pt(20, 22))
            self.add_arc(p + '-central-lower', pt(20, 22), pt(18, 16), radius_x=2, radius_y=6, sweep=side < 0)
            self.add_arc(p + '-central-top', pt(18, 16), (24, 4), radius_x=15, sweep=side < 0)
            self.add_contour(p + '-central', p + '-central-lower', p + '-central-top')
            self.add_contour(p + '-silhouette', p + '-lower', p + '-outer', p + '-inner', p + '-inner-lower')
            self.relate('connect', p + '-silhouette', 'base')
            self.relate('connect', p + '-silhouette', p + '-shoulder')
            self.relate('connect', p + '-shoulder', p + '-central')
        self.relate('connect', 'left-central', 'right-central')
