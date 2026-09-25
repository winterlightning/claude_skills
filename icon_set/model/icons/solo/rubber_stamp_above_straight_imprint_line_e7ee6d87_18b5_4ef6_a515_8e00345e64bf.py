"""Traditional Rubber Stamp Tool.

Symbol plan: Symmetric bulb handle, broad stamp base and detached imprint. Lucide stamp informs separate impression and narrow waist. Shared axis x=24.
Keyshape: VRECT_L; exact visible bounds (6, 2, 42, 46).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'e7ee6d87-18b5-4ef6-a515-8e00345e64bf'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/stamp_e7ee6d87-18b5-4ef6-a515-8e00345e64bf.svg'
AUTHOR = 'gpt-6'


class Drawing(Solo48):
    icon_id = 'rubber-stamp-above-straight-imprint-line'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "state")
    aliases = ()
    keywords = ('traditional', 'rubber', 'stamp', 'tool')

    def build(self):
        self.add_arc('bulb',(16,12),(32,12),radius_x=8)
        self.add_arc('neck-right',(32,12),(28,22),radius_x=15)
        self.add_line('waist-right',(28,22),(28,27))
        self.add_line('shoulder-right',(28,27),(36,27))
        self.add_arc('base-right',(36,27),(40,31),radius_x=4)
        self.add_line('base',(40,31),(40,35))
        self.add_line('bottom',(40,35),(8,35))
        self.add_line('base-left',(8,35),(8,31))
        self.add_arc('round-left',(8,31),(12,27),radius_x=4)
        self.add_line('shoulder-left',(12,27),(20,27))
        self.add_line('waist-left',(20,27),(20,22))
        self.add_arc('neck-left',(20,22),(16,12),radius_x=15)
        self.add_contour('stamp','bulb','neck-right','waist-right','shoulder-right','base-right','base','bottom','base-left','round-left','shoulder-left','waist-left','neck-left',closed=True)
        self.add_line('imprint',(8,44),(40,44))
