"""Narrow right-facing horn with three nested sound arcs. Local Lucide volume-2 geometry informed smooth sound curves while the source sets the horn shape."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '86cb98f9-4d33-4e0a-b25e-f14ba903609e'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__speaker-horn-with-three-sound-arcs/20260927T172707Z-thuan-mac-1/reference/emitter_86cb98f9-4d33-4e0a-b25e-f14ba903609e.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'speaker-horn-with-three-sound-arcs'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('speaker', 'sound', 'audio', 'horn', 'waves', 'volume', 'emitter')

    def build(self):
        # A narrow horn with three nested outward sound arcs.
        self.add_polyline('horn',(4,20),(8,20),(16,12),(16,36),(8,28),(4,28),closed=True)
        self.add_bezier('wave-near',(24,20),((28.5,22),(28.5,26),(24,28)))
        self.add_bezier('wave-middle',(30,14),((37.3,18),(37.3,30),(30,34)))
        self.add_bezier('wave-far',(38,8),((46,14),(46,34),(38,40)))
