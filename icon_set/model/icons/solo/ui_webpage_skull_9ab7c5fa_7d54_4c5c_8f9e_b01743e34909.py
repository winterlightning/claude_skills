"""ui webpage skull: fresh SOLO48 repair.
Plan: Geometric skull with beveled cranium and cheeks, paired eyes and a central tooth.
Keyshape: HRECT_L. The wider frame provides room for two eyes, skull outline, and outer frame gaps.
Omissions: Browser header divider and tiny header dashes omitted; cranium is polygonal rather than circular.
Construction reference: No useful additional Lucide match inspected; supplied skull and page reference governs construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ab7c5fa-7d54-4c5c-8f9e-b01743e34909'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__ui-webpage-skull/20260927T140835Z-thuan-mac-1/reference/ui webpage skull_9ab7c5fa-7d54-4c5c-8f9e-b01743e34909.svg'
AUTHOR = "gpt-6"
PARENT_SOURCE = 'icon_set/model/icons/solo/ui_webpage_skull_9ab7c5fa_7d54_4c5c_8f9e_b01743e34909.py'

class Drawing(Solo48):
    icon_id = 'ui-webpage-skull'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('combination', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('ui', 'webpage', 'skull')

    def build(self):
        self.add_polyline('browser', (8, 8), (40, 8), (44, 12), (44, 36), (40, 40), (8, 40), (4, 36), (4, 12), closed=True)
        self.add_line('crown', (16, 16), (32, 16))
        self.add_line('cranium-right', (32, 16), (36, 20))
        self.add_line('temple-right', (36, 20), (36, 28))
        self.add_line('cheek-right', (36, 28), (32, 32))
        self.add_line('cheek-left', (16, 32), (12, 28))
        self.add_line('temple-left', (12, 28), (12, 20))
        self.add_line('cranium-left', (12, 20), (16, 16))
        self.add_contour('skull', 'cheek-left', 'temple-left', 'cranium-left', 'crown', 'cranium-right', 'temple-right', 'cheek-right')
        for x in (20, 28):
            self.add_dot(f'eye-{x}', (x, 24))
        self.add_line('middle-tooth', (24, 31), (24, 32))

