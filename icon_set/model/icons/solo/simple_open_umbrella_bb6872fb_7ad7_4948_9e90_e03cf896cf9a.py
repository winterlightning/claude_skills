"""An open umbrella with a plain dome, finial and J-shaped handle; omit ribs.

Lucide construction: umbrella: two canopy arcs, flat edge and hooked shaft.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'bb6872fb-7ad7-4948-9e90-e03cf896cf9a'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/umbrella_bb6872fb-7ad7-4948-9e90-e03cf896cf9a.svg'
AUTHOR = 'astra-chatgpt'


class SimpleOpenUmbrella(Solo48):
    icon_id = 'simple-open-umbrella'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('umbrella', 'rain', 'parasol', 'weather', 'canopy', 'handle', 'shelter', 'accessory')

    def build(self) -> None:
        # Exact keyshape envelope: (3, 0, 45, 48).
        self.add_arc('canopy-l', (5, 26), (24, 7), radius_x=19, radius_y=19, sweep=True)
        self.add_arc('canopy-r', (24, 7), (43, 26), radius_x=19, radius_y=19, sweep=True)
        self.add_line('edge-1', (43, 26), (24, 26))
        self.add_line('edge-2', (24, 26), (5, 26))
        self.add_contour('canopy', 'canopy-l', 'canopy-r', 'edge-1', 'edge-2', closed=True)
        self.add_line('finial', (24, 2), (24, 7))
        self.add_line('shaft', (24, 26), (24, 40))
        self.add_arc('hook', (24, 40), (12, 40), radius_x=6, radius_y=6, sweep=True)
        self.add_contour('handle', 'shaft', 'hook', closed=False)
        self.relate("connect", 'finial', 'canopy')
        self.relate("connect", 'handle', 'canopy')
