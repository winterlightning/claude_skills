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
        # Rounded web window contains a domed skull with cheek tapers and two
        # separated eye marks, retaining the source page-plus-skull composition.
        self.add_line('frame-top',(8,8),(40,8))
        self.add_arc('frame-tr',(40,8),(44,12),radius_x=4)
        self.add_line('frame-right',(44,12),(44,36))
        self.add_arc('frame-br',(44,36),(40,40),radius_x=4)
        self.add_line('frame-bottom',(40,40),(8,40))
        self.add_arc('frame-bl',(8,40),(4,36),radius_x=4)
        self.add_line('frame-left',(4,36),(4,12))
        self.add_arc('frame-tl',(4,12),(8,8),radius_x=4)
        self.add_contour('browser','frame-top','frame-tr','frame-right','frame-br','frame-bottom','frame-bl','frame-left','frame-tl',closed=True)
        self.add_line('jaw-left',(16,32),(16,30))
        self.add_arc('cheek-left',(16,30),(12,26),radius_x=4)
        self.add_line('temple-left',(12,26),(12,22))
        self.add_arc('crown-left',(12,22),(18,16),radius_x=6)
        self.add_line('crown',(18,16),(30,16))
        self.add_arc('crown-right',(30,16),(36,22),radius_x=6)
        self.add_line('temple-right',(36,22),(36,26))
        self.add_arc('cheek-right',(36,26),(32,30),radius_x=4)
        self.add_line('jaw-right',(32,30),(32,32))
        self.add_contour('skull','jaw-left','cheek-left','temple-left','crown-left','crown','crown-right','temple-right','cheek-right','jaw-right')
        self.add_dot('eye-left',(20,24))
        self.add_dot('eye-right',(28,24))
        self.add_line('nose',(24,31),(24,32))
