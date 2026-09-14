"""An underlined capital P. VRECT_L extremes (8,4)-(40,44). No useful exact Lucide letter match; use a semicircular bowl with tangent horizontal joins. Retain the tall stem and separate underline."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f4ccc80a-2c90-4322-986f-12721c0cba8d'
SOURCE_PATH = 'pictographic-primitives/symbol/p (text u)_f4ccc80a-2c90-4322-986f-12721c0cba8d.svg'
AUTHOR = 'gpt-6'


class PLetterUnderlined(Solo48):
    icon_id = 'p-letter-underlined'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('p', 'letter', 'text', 'underline', 'typography', 'alphabet', 'language')

    def build(self) -> None:
        self.add_polyline('stem',(12,4),(12,22),(12,32))
        self.add_line('bowl-top',(12,4),(30,4))
        self.add_arc('bowl-round',(30,4),(30,22),radius_x=9)
        self.add_line('bowl-bottom',(30,22),(12,22))
        self.add_contour('bowl','bowl-top','bowl-round','bowl-bottom')
        self.relate('connect','stem','bowl')
        self.add_line('underline',(8,44),(40,44))
