# Independent revision; parent models preserved.
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '3a1ca23c-24a3-4e8f-977d-ba235ab2cd79'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-06/tie_3a1ca23c-24a3-4e8f-977d-ba235ab2cd79.svg'
AUTHOR = 'gpt-6'

class NecktieVariant2(Solo48):
    icon_id = 'necktie-v2'
    variant_of = 'necktie'
    variant_label = 'Exact keyshape envelope and clear spacing'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('necktie',)

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). Diagonal tie; paired edges reflect about
        # x+y=48. Shared neck corners join the trapezoid knot to the blade.
        a,b=(24,14),(34,24)
        self.add_polyline('knot',(30,6),(42,18),b,a,closed=True)
        self.add_polyline('blade',a,(8,28),(6,42),(20,40),b)
        self.relate('connect','knot','blade')
