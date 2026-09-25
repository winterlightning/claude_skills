"""At Sign: A circular inner bowl joins a returning curve on the right, surrounded by a broad outer loop. The outer loop remains open near the lower-right edge.

Construction: An inner circular bowl joins an angled return and broad outer circular loop; retain the open lower-right ending.
Keyshape: SQUARE; authored to the SUB32 envelope.
"""
from ...keyshapes import Keyshape
from ._base import Symbol32 as Sub32
SOURCE_ICON_ID = 'adcef252-cf2f-4382-847d-fa142d13d1f0'
SOURCE_PATH = 'pictographic-primitives/state/@ (text)_adcef252-cf2f-4382-847d-fa142d13d1f0.svg'
AUTHOR = 'gpt-6'

class AtSignContainerSymbol(Sub32):
    icon_id = 'at-sign-symbol'
    related_origin_icon_id = 'at-sign'
    variant_label = 'Independent container symbol'
    usage_category = 'symbol'
    related_group = 'sub-origin/at-sign'
    counterpart_icon_id = 'at-sign'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    categories = ('state',)
    aliases = ()
    keywords = ('sign', 'circular', 'inner', 'bowl', 'joins', 'returning', 'curve', 'right')

    def build(self):

        def circle(name, cx, cy, radius):
            self.add_arc(name + '-top', (cx - radius, cy), (cx + radius, cy), radius_x=radius)
            self.add_arc(name + '-bottom', (cx + radius, cy), (cx - radius, cy), radius_x=radius)
            self.add_contour(name, name + '-top', name + '-bottom', closed=True)
        circle('bowl', 16, 16, 6)
        self.add_line('join', (22, 16), (26, 20))
        self.add_arc('return', (26, 20), (30, 16), radius_x=4, sweep=False)
        self.add_arc('outer-upper', (30, 16), (2, 16), radius_x=14, sweep=False)
        self.add_arc('outer-lower', (2, 16), (16, 30), radius_x=14, sweep=False)
        self.add_contour('outer', 'join', 'return', 'outer-upper', 'outer-lower')
        self.relate('connect', 'bowl', 'outer')
