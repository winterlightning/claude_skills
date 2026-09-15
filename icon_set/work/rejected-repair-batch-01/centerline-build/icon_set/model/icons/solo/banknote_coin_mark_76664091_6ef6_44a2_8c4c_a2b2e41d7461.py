"""Banknote. Keeps the large central ring; drops the tiny side ovals to preserve required ink clearance.

HRECT_L visible extremes (2, 6, 46, 42); centerlines (4, 8, 44, 40).
Lucide banknote: rounded rectangular bill and central circular denomination mark.
Repeated features share dimensions; deliberate asymmetry preserves the
letter order, handles and chart heights. Authored directly on SOLO48.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '76664091-6ef6-44a2-8c4c-a2b2e41d7461'
SOURCE_PATH = 'pictographic-primitives/symbol/cash card_76664091-6ef6-44a2-8c4c-a2b2e41d7461.svg'
AUTHOR = 'gpt-6'


class BanknoteCoinMark(Solo48):
    icon_id = 'banknote-coin-mark'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbols/standalone"
    aliases = ()
    keywords = ('banknote', 'cash', 'money', 'bill', 'payment', 'currency', 'finance', 'note')

    def build(self) -> None:
        # Envelope repair: shared boundary nodes and cardinal curve extrema;
        # retain the subject, grid, stroke, and declared physical joins.
        self.add_line('bill-top-1', (8, 8), (40, 8))
        self.add_arc('bill-ne', (40, 8), (44, 12), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bill-right', (44, 12), (44, 36))
        self.add_arc('bill-se', (44, 36), (40, 40), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bill-bottom-1', (40, 40), (8, 40))
        self.add_arc('bill-sw', (8, 40), (4, 36), radius_x=4, radius_y=4, sweep=True)
        self.add_line('bill-left', (4, 36), (4, 12))
        self.add_arc('bill-nw', (4, 12), (8, 8), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('bill', 'bill-top-1', 'bill-ne', 'bill-right', 'bill-se', 'bill-bottom-1', 'bill-sw', 'bill-left', 'bill-nw', closed=True)
        self.add_arc('coin-right', (24, 17), (24, 31), radius_x=7, radius_y=7, sweep=True)
        self.add_arc('coin-left', (24, 31), (24, 17), radius_x=7, radius_y=7, sweep=True)
        self.add_contour('coin', 'coin-right', 'coin-left', closed=True)
