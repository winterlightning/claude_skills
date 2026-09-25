'Virgo specialist zodiac symbol with two arches, three stems and a branching curled tail. Not alphabet text. HRECT_L fits arch radius8 and tail tip at44. Reference supplies glyph topology; Lucide omega contributes coherent curved specialist-symbol construction. Shared arch radius, stem level32, junction(36,32); omit tiny entry serif for clarity.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '4ea58a40-e768-41fb-b322-fda6d281ceb7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/astrology virgo_4ea58a40-e768-41fb-b322-fda6d281ceb7.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'virgo-glyph-with-a-curled-tail'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Virgo Zodiac Sign']
    keywords = ['virgo', 'zodiac', 'astrology', 'glyph', 'arches', 'tail', 'symbol']
    def build(self):
        self.add_arc('arch-left',(4,16),(20,16),radius_x=8)
        self.add_arc('arch-right',(20,16),(36,16),radius_x=8)
        self.add_line('stem-left',(4,16),(4,32))
        self.add_line('stem-middle',(20,16),(20,32))
        self.add_line('stem-right',(36,16),(36,32))
        self.relate('connect','arch-left','stem-left')
        self.relate('connect','arch-left','arch-right','stem-middle')
        self.relate('connect','arch-right','stem-right')
        self.add_bezier('tail-left',(36,32),((34,36),(32,40),(28,40)))
        self.add_bezier('tail-right-a',(36,32),((36,36),(36,40),(40,40)))
        self.add_arc('tail-right-b',(40,40),(44,36),radius_x=4,sweep=False)
        self.add_contour('tail-right','tail-right-a','tail-right-b')
        self.relate('connect','stem-right','tail-left','tail-right')
