'Underlined U: a true semicircular bowl with 8 units above the underline.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b8a7ef4b-af1c-59bd-bb25-170aedf30b04'
SOURCE_PATH = 'pictographic-primitives/interface-essential/text underline_b8a7ef4b-af1c-59bd-bb25-170aedf30b04.svg'
AUTHOR = 'gpt-6'

class TextUnderline(Solo48):
    icon_id = 'text-underline'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('text', 'underline', 'interface-essential')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('left', (12, 6), (12, 22))
        self.add_arc('bowl', (12, 22), (36, 22), radius_x=12, radius_y=12, large_arc=False, sweep=False)
        self.add_line('right', (36, 22), (36, 6))
        self.add_line('underline', (6, 42), (42, 42))
        self.add_contour('letter', *('left', 'bowl', 'right'), closed=False)
