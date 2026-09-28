"""Right-Facing Loudspeaker with Two Sound Waves
Plan: Right-facing speaker with 2 sound arcs; arc count is retained.
Keyshape: HRECT_L; exact inset SOLO48 envelope.
Construction: Lucide volume-2: flared speaker and separate sound emanations.
Reduction: None."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '57fe8f91-559f-4932-b706-8c9dc391b19c'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__right-facing-loudspeaker-with-two-sound-waves/20260927T171300Z-thuan-mac-1/reference/speakerphone_57fe8f91-559f-4932-b706-8c9dc391b19c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'right-facing-loudspeaker-with-two-sound-waves'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('speaker', 'loudspeaker', 'sound', 'waves', 'audio', 'volume')

    def build(self):
        # Broad right-facing cone, compact grip, and two spaced sound waves.
        self.add_polyline('speaker',(4,20),(10,20),(22,8),(22,40),(10,28),(4,28),closed=True)
        self.add_bezier('wave-inner',(32,18),((35,20),(35,28),(32,30)))
        self.add_bezier('wave-outer',(42,12),((44,18),(44,22),(44,24)),((44,26),(44,30),(42,36)))
