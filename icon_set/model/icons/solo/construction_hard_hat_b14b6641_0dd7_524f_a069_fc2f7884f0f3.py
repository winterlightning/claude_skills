"""Hard hat with crown badge and broad brim. HRECT_L extremes (2,8)-(46,40). Lucide hard-hat informs mirrored shell arcs, central crest and rounded brim."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b14b6641-0dd7-524f-a069-fc2f7884f0f3'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/hat architect_b14b6641-0dd7-524f-a069-fc2f7884f0f3.svg'
AUTHOR = 'astra-chatgpt'


class ConstructionHardHat(Solo48):
    icon_id = 'construction-hard-hat'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('hard hat', 'helmet', 'construction', 'safety', 'builder', 'architect', 'worker', 'headwear')

    def build(self) -> None:
        self.add_line('brim-0', (6, 30), (42, 30))
        self.add_arc('brim-1', (42, 30), (46, 34), radius_x=4, radius_y=4, sweep=True)
        self.add_line('brim-2', (46, 34), (46, 36))
        self.add_arc('brim-3', (46, 36), (42, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('brim-4', (42, 40), (6, 40))
        self.add_arc('brim-5', (6, 40), (2, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('brim-6', (2, 36), (2, 34))
        self.add_arc('brim-7', (2, 34), (6, 30), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('brim', 'brim-0', 'brim-1', 'brim-2', 'brim-3', 'brim-4', 'brim-5', 'brim-6', 'brim-7', closed=True)
        self.add_arc('shell-left', (6, 30), (18, 12), radius_x=12, radius_y=18, sweep=True)
        self.add_arc('shell-right', (30, 12), (42, 30), radius_x=12, radius_y=18, sweep=True)
        self.add_line('badge-0', (21, 8), (27, 8))
        self.add_arc('badge-1', (27, 8), (30, 11), radius_x=3, radius_y=3, sweep=True)
        self.add_line('badge-2-attach-0', (30, 11), (30, 12))
        self.add_line('badge-2-attach-1', (30, 12), (30, 18))
        self.add_arc('badge-3', (30, 18), (27, 21), radius_x=3, radius_y=3, sweep=True)
        self.add_line('badge-4', (27, 21), (21, 21))
        self.add_arc('badge-5', (21, 21), (18, 18), radius_x=3, radius_y=3, sweep=True)
        self.add_line('badge-6-attach-0', (18, 18), (18, 12))
        self.add_line('badge-6-attach-1', (18, 12), (18, 11))
        self.add_arc('badge-7', (18, 11), (21, 8), radius_x=3, radius_y=3, sweep=True)
        self.add_contour('badge', 'badge-0', 'badge-1', 'badge-2-attach-0', 'badge-2-attach-1', 'badge-3', 'badge-4', 'badge-5', 'badge-6-attach-0', 'badge-6-attach-1', 'badge-7', closed=True)
        self.relate("connect", 'shell-left', 'brim')
        self.relate("connect", 'shell-right', 'brim')
        self.relate("connect", 'shell-left', 'badge')
        self.relate("connect", 'shell-right', 'badge')
