# Independent container symbol; edit separately from linked side sub-icon.
"""Ring Target: Two concentric circular outlines share one centre, with a broad empty band between them. The smaller ring encloses an empty centre, and no crosshairs or arrows are visible.

Construction: Two concentric circular outlines share a centre and leave a broad empty band.
Keyshape: CIRCLE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID = 'f12c5f2b-a5cb-4039-97cd-f97f62429f51'
SOURCE_PATH = 'pictographic-primitives/state/circle target_f12c5f2b-a5cb-4039-97cd-f97f62429f51.svg'
AUTHOR = 'gpt-6'

class RingTargetContainerSymbol(Sub32):
    icon_id = 'ring-target-symbol'
    variant_of = 'ring-target'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/ring-target'
    counterpart_icon_id = 'ring-target'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('ring', 'target', 'concentric', 'circular', 'outlines', 'share', 'centre', 'broad')

    def build(self):

        def circle(name, cx, cy, radius):
            self.add_arc(name + '-top', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
            self.add_arc(name + '-bottom', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
            self.add_contour(name, name + '-top', name + '-bottom', closed=True)
        circle('outer', 16, 16, 14)
        circle('inner', 16, 16, 6)
