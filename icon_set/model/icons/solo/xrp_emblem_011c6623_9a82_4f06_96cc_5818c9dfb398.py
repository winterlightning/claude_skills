"""Mirrored curved chevrons of the XRP emblem. SQUARE extremes (6,6)-(42,42). Matching central curves and diagonal arms, separated by an open horizontal band. No useful exact Lucide match; preserve all identifying strokes."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='011c6623-9a82-4f06-96cc-5818c9dfb398'
SOURCE_PATH='pictographic-primitives/money/virtual coin crypto xrp_011c6623-9a82-4f06-96cc-5818c9dfb398.svg'
AUTHOR='gpt-6'

class XrpEmblem(Solo48):
    icon_id='xrp-emblem'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "money"
    categories = ("primitives", "money")
    aliases=()
    keywords=('xrp', 'crypto', 'emblem', 'currency', 'chevron', 'symbol')

    def build(self):
        for name,sign in (('upper',1),('lower',-1)):
            def p(x,y):return (x,24+sign*(y-24))
            self.add_line(f'{name}-left',p(6,6),p(18,16))
            self.add_bezier(f'{name}-curve',p(18,16),(p(24,21),p(24,21),p(30,16)))
            self.add_line(f'{name}-right',p(30,16),p(42,6))
            self.add_contour(name,f'{name}-left',f'{name}-curve',f'{name}-right')
