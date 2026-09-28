"""Privacy Choice Symbol. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2b732107-c0ac-56a9-a78a-239d30685f97'
SOURCE_PATH = 'pictographic-primitives/websites/ccpa opt out_2b732107-c0ac-56a9-a78a-239d30685f97.svg'
AUTHOR = 'gpt-6'

class PrivacyChoiceSymbol(Solo48):
    icon_id = 'privacy-choice-symbol'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "websites"
    categories = ("websites", "primitives")
    aliases = ()
    keywords = ('privacy', 'choice', 'consent', 'opt-out', 'check', 'cross', 'ccpa')

    def build(self):
        self.add_line('top',(20,8),(28,8))
        self.add_arc('right',(28,8),(28,40),radius_x=16)
        self.add_line('bottom',(28,40),(20,40))
        self.add_arc('left',(20,40),(20,8),radius_x=16)
        self.add_contour('capsule','top','right','bottom','left',closed=True)
        self.add_polyline('check',(13,24),(16,27),(20,21))
        self.add_polyline('cross-a',(29,21),(32,24),(35,27))
        self.add_polyline('cross-b',(35,21),(32,24),(29,27))
        self.relate('connect','cross-a','cross-b')
