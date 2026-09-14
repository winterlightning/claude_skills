# Variant of ice-cream-cone; parent file remains unchanged.
"""A three-lobed ice-cream scoop sits on a triangular cone with a scalloped join. VRECT_L extremes (8,6)-(40,42). Lucide ice-cream-cone informs the round scoop and simple cone; source scallops retained. Omit no requested feature."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3cb3ca32-1445-4af8-bc72-ddff6a0808bb'
SOURCE_PATH = 'pictographic-primitives/symbol/ice scream_3cb3ca32-1445-4af8-bc72-ddff6a0808bb.svg'
AUTHOR = 'gpt-6'

class IceCreamConeVariant2(Solo48):
    icon_id = 'ice-cream-cone-v2'
    variant_of = 'ice-cream-cone'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('ice-cream', 'cone', 'dessert', 'sweet', 'summer', 'treat', 'gelato', 'food')

    def build(self) -> None:
        self.add_arc('scoop-top', (14, 14), (34, 14), radius_x=10)
        self.add_arc('scoop-right', (34, 14), (34, 28), radius_x=6, radius_y=7)
        self.add_arc('scallop-right', (34, 28), (24, 26), radius_x=8, radius_y=6)
        self.add_arc('scallop-left', (24, 26), (14, 28), radius_x=8, radius_y=6)
        self.add_arc('scoop-left', (14, 28), (14, 14), radius_x=6, radius_y=7)
        self.add_contour('scoop', 'scoop-top', 'scoop-right', 'scallop-right', 'scallop-left', 'scoop-left', closed=True)
        self.add_polyline('cone', (14, 28), (24, 42), (34, 28))
        self.relate('connect', 'scoop', 'cone')
