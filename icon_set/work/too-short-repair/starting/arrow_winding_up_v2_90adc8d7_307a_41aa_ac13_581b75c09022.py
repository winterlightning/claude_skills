# Variant of arrow-winding-up; parent file remains unchanged.
"""Winding upward route arrow. Lucide route: tangent quarter-circle turns; source direction preserved.

SOLO48 VRECT_L, live visible envelope (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '90adc8d7-307a-41aa-ac13-581b75c09022'
SOURCE_PATH = 'pictographic-primitives/symbol/right curve 1_90adc8d7-307a-41aa-ac13-581b75c09022.svg'
AUTHOR = 'gpt-6'

class ArrowWindingUpVariant2(Solo48):
    icon_id = 'arrow-winding-up-v2'
    variant_of = 'arrow-winding-up'
    variant_label = 'Height envelope and full spacing repair'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('arrow', 'winding', 'curve', 'route', 'up', 'path', 'detour', 'direction')

    def build(self) -> None:
        self.add_line('rise-left', (8, 42), (8, 34))
        self.add_arc('turn-left', (8, 34), (18, 24), radius_x=10)
        self.add_line('middle', (18, 24), (20, 24))
        self.add_arc('turn-right', (20, 24), (30, 14), radius_x=10, sweep=False)
        self.add_line('rise-right', (30, 14), (30, 6))
        self.add_contour('route', 'rise-left', 'turn-left', 'middle', 'turn-right', 'rise-right')
        self.add_polyline('head', (20, 14), (30, 6), (40, 14))
        self.relate('connect', 'route', 'head')
