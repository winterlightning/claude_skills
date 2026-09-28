"""Right-facing broad speaker cone with two separated sound waves. The local Lucide volume-2 original and atomic debug informed the cone and nested curves."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '1ce1c1bb-d2b6-40e7-af58-c1f83f3763c9'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__speaker-sound-waves/20260927T172707Z-thuan-mac-1/reference/volume control full 1_1ce1c1bb-d2b6-40e7-af58-c1f83f3763c9.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'speaker-sound-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('speaker', 'sound', 'audio', 'volume', 'waves', 'loud')

    def build(self):
        # Source's broad loudspeaker cone and two full sound waves.
        self.add_polyline('speaker',(4,18),(10,18),(20,8),(20,40),(10,30),(4,30),closed=True)
        self.add_bezier('wave-near',(28,15),((38,19),(38,29),(28,33)))
        self.add_bezier('wave-far',(38,8),((46,14),(46,34),(38,40)))
