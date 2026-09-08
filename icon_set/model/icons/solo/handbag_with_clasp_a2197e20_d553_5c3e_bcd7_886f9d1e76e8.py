"""Rounded handbag with an arched handle, curved flap and broad clasp. SQUARE extremes (2,2)-(46,46). Lucide handbag informs handle and rounded shell; clasp enlarged for an open, readable interior."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a2197e20-d553-5c3e-bcd7-886f9d1e76e8'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-03/bag purse_a2197e20-d553-5c3e-bcd7-886f9d1e76e8.svg'
AUTHOR = 'astra-chatgpt'


class HandbagWithClasp(Solo48):
    icon_id = 'handbag-with-clasp'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/accessories"
    aliases = ()
    keywords = ('bag', 'handbag', 'purse', 'clasp', 'fashion', 'accessory', 'satchel', 'flap')

    def build(self) -> None:
        self.add_line('body-0-attach-0', (10, 16), (13, 16))
        self.add_line('body-0-attach-1', (13, 16), (35, 16))
        self.add_line('body-0-attach-2', (35, 16), (38, 16))
        self.add_arc('body-1', (38, 16), (46, 24), radius_x=8, radius_y=8, sweep=True)
        self.add_line('body-2', (46, 24), (46, 38))
        self.add_arc('body-3', (46, 38), (38, 46), radius_x=8, radius_y=8, sweep=True)
        self.add_line('body-4', (38, 46), (10, 46))
        self.add_arc('body-5', (10, 46), (2, 38), radius_x=8, radius_y=8, sweep=True)
        self.add_line('body-6', (2, 38), (2, 24))
        self.add_arc('body-7', (2, 24), (10, 16), radius_x=8, radius_y=8, sweep=True)
        self.add_contour('body', 'body-0-attach-0', 'body-0-attach-1', 'body-0-attach-2', 'body-1', 'body-2', 'body-3', 'body-4', 'body-5', 'body-6', 'body-7', closed=True)
        self.add_arc('handle', (13, 16), (35, 16), radius_x=11, radius_y=14, sweep=True)
        self.relate("connect", 'body', 'handle')
        self.add_arc('flap-left', (2, 24), (18, 32), radius_x=16, radius_y=8, sweep=False)
        self.add_arc('flap-right', (30, 32), (46, 24), radius_x=16, radius_y=8, sweep=False)
        self.add_line('clasp-0', (22, 28), (26, 28))
        self.add_arc('clasp-1', (26, 28), (30, 32), radius_x=4, radius_y=4, sweep=True)
        self.add_line('clasp-2', (30, 32), (30, 34))
        self.add_arc('clasp-3', (30, 34), (26, 38), radius_x=4, radius_y=4, sweep=True)
        self.add_line('clasp-4', (26, 38), (22, 38))
        self.add_arc('clasp-5', (22, 38), (18, 34), radius_x=4, radius_y=4, sweep=True)
        self.add_line('clasp-6', (18, 34), (18, 32))
        self.add_arc('clasp-7', (18, 32), (22, 28), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('clasp', 'clasp-0', 'clasp-1', 'clasp-2', 'clasp-3', 'clasp-4', 'clasp-5', 'clasp-6', 'clasp-7', closed=True)
        self.relate("connect", 'body', 'flap-left')
        self.relate("connect", 'body', 'flap-right')
        self.relate("connect", 'clasp', 'flap-left')
        self.relate("connect", 'clasp', 'flap-right')
