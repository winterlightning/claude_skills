"""ui webpage skull: fresh SOLO48 repair.
Plan: Geometric skull with beveled cranium and cheeks, paired eyes and a central tooth.
Keyshape: HRECT_L. The wider frame provides room for two eyes, skull outline, and outer frame gaps.
Omissions: Browser header divider and tiny header dashes omitted; cranium is polygonal rather than circular.
Construction reference: No useful additional Lucide match inspected; supplied skull and page reference governs construction.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '9ab7c5fa-7d54-4c5c-8f9e-b01743e34909'
SOURCE_PATH = 'pictographic-primitives/other/ui webpage skull_9ab7c5fa-7d54-4c5c-8f9e-b01743e34909.svg'
AUTHOR = 'gpt-6'
PARENT_SOURCE = 'icon_set/model/icons/solo/ui_webpage_skull_9ab7c5fa_7d54_4c5c_8f9e_b01743e34909.py'

class Drawing(Solo48):
    icon_id = 'ui-webpage-skull'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('ui', 'webpage', 'skull')

    def build(self):
        self.add_polyline('browser', (4, 8), (44, 8), (44, 40), (4, 40), closed=True)
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

# Explicit user approval for this exact SVG; changes invalidate the exception.
Drawing.exception = {'reason': 'User explicitly approved the repaired main icons as exceptions, retaining their current artwork and original validation findings.', 'approved_by': 'user', 'approved_on': '2026-09-25', 'svg_sha256': '78799426a8d8cfac522902478733cbffed30160293c71e51ef872b4e59c24927', 'approval_scope': '47 repaired side-main sources identified in this task', 'source_uuid': '9ab7c5fa-7d54-4c5c-8f9e-b01743e34909'}
