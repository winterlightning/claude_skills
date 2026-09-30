"""A portable cooker with a tapered upper housing, two controls and a broad foot.

Keyshape SQUARE: (0, 0, 64, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide rectangle-horizontal informs paired corner arcs on the control housing.
Retained both controls and the tapered base; enlarged the control band to preserve clear space.
Hosting measured with compose.py: plus: pass; heart: pass; check: pass.

v2 (2026-09-30): resized onto the v2 CONTAINER64 keyshapes by container_v2_fit (portable-single-burner-stove SQUARE -> SQUARE). Lattice snap: shared columns and rows move together, gaps of 8 or less keep their size, stroke stays 4.
"""

from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.container._base import Container64

AUTHOR = 'claude-opus-5-5'


class PortableSingleBurnerStove(Container64):
    icon_id = 'portable-single-burner-stove'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('portable', 'single', 'burner', 'stove')

    def build(self) -> None:
        self.add_line('upper-left', (6, 35), (12, 11))
        self.add_arc('upper-nw', (12, 11), (18, 6), radius_x=6, radius_y=5)
        self.add_line('upper-top', (18, 6), (46, 6))
        self.add_arc('upper-ne', (46, 6), (52, 11), radius_x=6, radius_y=5)
        self.add_line('upper-right', (52, 11), (58, 35))
        self.add_line('band-top', (6, 35), (58, 35))
        self.add_line('band-bottom', (10, 49), (54, 49))
        self.add_line('band-right-side', (58, 35), (58, 45))
        self.add_arc('band-se', (58, 45), (54, 49), radius_x=4)
        self.add_arc('band-sw', (10, 49), (6, 45), radius_x=4)
        self.add_line('band-left-side', (6, 45), (6, 35))
        self.add_line('control-left', (22, 41), (22, 43))
        self.add_line('control-right', (42, 41), (42, 43))
        self.add_line('foot-1', (10, 49), (16, 58))
        self.add_line('foot-2', (16, 58), (48, 58))
        self.add_line('foot-3', (48, 58), (54, 49))
        self.add_contour('upper', 'upper-left', 'upper-nw', 'upper-top', 'upper-ne', 'upper-right')
        self.add_contour('band-right', 'band-right-side', 'band-se')
        self.add_contour('band-left', 'band-sw', 'band-left-side')
        self.add_contour('foot', 'foot-1', 'foot-2', 'foot-3')
        self.relate('connect', 'upper', 'band-top')
        self.relate('connect', 'upper', 'band-left')
        self.relate('connect', 'upper', 'band-right')
        self.relate('connect', 'band-top', 'band-left')
        self.relate('connect', 'band-top', 'band-right')
        self.relate('connect', 'band-bottom', 'band-left')
        self.relate('connect', 'band-bottom', 'band-right')
        self.relate('connect', 'foot', 'band-bottom')
        self.relate('connect', 'foot', 'band-left')
        self.relate('connect', 'foot', 'band-right')
