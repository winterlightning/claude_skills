"""Controls rewind (video), converted from the icons-json construction graph by json_to_solo --mode fit. VRECT_L keyshape; curves fitted to integer lines and arcs."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '2736daad-03fd-5c48-9a0d-f54eed191916'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__controls-rewind/20260927T032242Z-thuan-mac-1/reference/controls rewind_2736daad-03fd-5c48-9a0d-f54eed191916.svg'
AUTHOR = "gpt-6"

class ControlsRewind(Solo48):
    icon_id = 'controls-rewind'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'video'
    categories = ('video', 'primitives')
    aliases = ()
    keywords = ('controls', 'rewind', 'video')

    def build(self):
        self.add_line('e0', (40, 4), (8, 24))
        self.add_line('e1', (8, 24), (40, 44))
        self.add_line('e2', (40, 44), (40, 4))
        self.add_contour('c0', 'e0', 'e1', 'e2', closed=True)
