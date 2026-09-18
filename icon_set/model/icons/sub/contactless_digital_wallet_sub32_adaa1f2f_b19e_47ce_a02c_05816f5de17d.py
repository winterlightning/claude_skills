"""Contactless Digital Wallet: user-requested grid-fitted 32px version of contactless-digital-wallet-solo.
Plan: retain source primitive/contour topology and fit SQUARE ink (0, 0, 32, 32).
All geometry nodes, controls and radii are whole integers; final stroke stays 4.
Source construction and visual references are retained from the solo model.
"""
from ...keyshapes import Keyshape
from ._base import Sub32
SOURCE_ICON_ID='adaa1f2f-b19e-47ce-a02c-05816f5de17d'
SOURCE_PATH='pictographic-primitives/other/wallet wifi_adaa1f2f-b19e-47ce-a02c-05816f5de17d.svg'
SOLO_SOURCE_ICON_ID='contactless-digital-wallet-solo'
AUTHOR='gpt-6'
class Drawing(Sub32):
    icon_id='contactless-digital-wallet-sub32'
    keyshape=Keyshape.SQUARE
    semantic_role='SUB'
    semantic_kind='modifier'
    category='objects/interface-essential'
    tags=('sub icon',)
    keywords=('sub icon', 'grid fitted', 'contactless digital wallet')
    def build(self):
        self.add_bezier('signal-outer', (2, 7), ((10, 0), (22, 0), (30, 7)))
        self.add_bezier('signal-inner', (9, 12), ((13, 9), (19, 9), (23, 12)))
        self.add_line('wallet-0', (9, 19), (23, 19))
        self.add_arc('wallet-1', (23, 19), (25, 21), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('wallet-2', (25, 21), (25, 28))
        self.add_arc('wallet-3', (25, 28), (23, 30), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('wallet-4', (23, 30), (9, 30))
        self.add_arc('wallet-5', (9, 30), (7, 28), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('wallet-6', (7, 28), (7, 21))
        self.add_arc('wallet-7', (7, 21), (9, 19), radius_x=2, radius_y=2, large_arc=False, sweep=True)
        self.add_line('flap-1', (9, 19), (17, 24))
        self.add_line('flap-2', (17, 24), (17, 30))
        self.add_contour('wallet', 'wallet-0', 'wallet-1', 'wallet-2', 'wallet-3', 'wallet-4', 'wallet-5', 'wallet-6', 'wallet-7', closed=True)
        self.add_contour('flap', 'flap-1', 'flap-2', closed=False)
        self.relate('connect', 'wallet', 'flap')
        self.add_anchor('center',(16, 16))
