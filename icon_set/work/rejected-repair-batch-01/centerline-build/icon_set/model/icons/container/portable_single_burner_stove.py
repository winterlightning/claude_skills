"""A portable cooker with a tapered upper housing, two controls and a broad foot.

Keyshape SQUARE: (0, 0, 64, 64); authored from its exact extremes.
Reference: batch_10 source render. Lucide rectangle-horizontal informs paired corner arcs on the control housing.
Retained both controls and the tapered base; enlarged the control band to preserve clear space.
Hosting measured with compose.py: plus: pass; heart: pass; check: pass.
"""

from ...keyshapes import Keyshape
from ._base import Container64

AUTHOR = 'astra-chatgpt'


class PortableSingleBurnerStove(Container64):
    icon_id = 'portable-single-burner-stove'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "containers"
    aliases = ()
    keywords = ('portable', 'single', 'burner', 'stove')

    def build(self) -> None:
        self.add_line('upper-left', (2, 38), (8, 8))
        self.add_arc('upper-nw', (8, 8), (14, 2), radius_x=6, radius_y=6, sweep=True)
        self.add_line('upper-top', (14, 2), (50, 2))
        self.add_arc('upper-ne', (50, 2), (56, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_line('upper-right', (56, 8), (62, 38))
        self.add_contour('upper', 'upper-left', 'upper-nw', 'upper-top', 'upper-ne', 'upper-right', closed=False)
        self.add_line('band-top', (2, 38), (62, 38))
        self.add_line('band-bottom', (6, 52), (58, 52))
        self.add_line('band-right-side', (62, 38), (62, 48))
        self.add_arc('band-se', (62, 48), (58, 52), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('band-right', 'band-right-side', 'band-se', closed=False)
        self.add_arc('band-sw', (6, 52), (2, 48), radius_x=4, radius_y=4, sweep=True)
        self.add_line('band-left-side', (2, 48), (2, 38))
        self.add_contour('band-left', 'band-sw', 'band-left-side', closed=False)
        self.relate("connect", 'upper', 'band-top')
        self.relate("connect", 'upper', 'band-left')
        self.relate("connect", 'upper', 'band-right')
        self.relate("connect", 'band-top', 'band-left')
        self.relate("connect", 'band-top', 'band-right')
        self.relate("connect", 'band-bottom', 'band-left')
        self.relate("connect", 'band-bottom', 'band-right')
        self.add_line('control-left', (18, 44), (18, 46))
        self.add_line('control-right', (46, 44), (46, 46))
        self.add_polyline('foot', (6, 52), (12, 62), (52, 62), (58, 52), closed=False)
        self.relate("connect", 'foot', 'band-bottom')
        self.relate("connect", 'foot', 'band-left')
        self.relate("connect", 'foot', 'band-right')
