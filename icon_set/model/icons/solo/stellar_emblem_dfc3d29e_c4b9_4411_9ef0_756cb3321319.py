"""Stellar broken circular orbit and rising diagonal band. Radius20 centered24; opposing arcs share a diagonal endpoint. Lucide circle-slash informs the orbit and line relationship; retain the reference band and open gaps."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='dfc3d29e-c4b9-4411-9ef0-756cb3321319'
SOURCE_PATH='pictographic-primitives/money/virtual coin crypto stellar_dfc3d29e-c4b9-4411-9ef0-756cb3321319.svg'
AUTHOR='gpt-6'

class StellarEmblem(Solo48):
    icon_id='stellar-emblem'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="symbols/finance"
    aliases=()
    keywords=('stellar', 'crypto', 'emblem', 'ring', 'diagonal', 'currency')

    def build(self):
        self.add_arc('upper-a',(4,24),(8,36),radius_x=20,sweep=False)
        self.add_arc('upper-b',(24,4),(4,24),radius_x=20,sweep=False)
        self.add_arc('upper-c',(36,8),(24,4),radius_x=20,sweep=False)
        self.add_line('band-lower',(8,36),(40,12))
        self.add_arc('lower-a',(40,12),(44,24),radius_x=20)
        self.add_arc('lower-b',(44,24),(24,44),radius_x=20)
        self.add_arc('lower-c',(24,44),(12,40),radius_x=20)
        self.add_contour('orbit','upper-c','upper-b','upper-a','band-lower','lower-a','lower-b','lower-c')
        self.add_line('band-upper',(14,21),(24,13))
