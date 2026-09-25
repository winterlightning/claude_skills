"""Summation Sign: A large uppercase sigma has long horizontal top and bottom bars joined by two inward-sloping diagonals. The diagonals meet at a central right-facing point, leaving the right side open.

Construction: One open sigma run, with symmetric inward diagonals and matched upper/lower rails.
Keyshape: VRECT_XL; extremes follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '534e35bc-f17a-4308-b045-175383e7b0e9'
SOURCE_PATH = 'pictographic-primitives/state/sum symbol_534e35bc-f17a-4308-b045-175383e7b0e9.svg'
AUTHOR = 'gpt-6'


class SummationSign(Sub32):
    icon_id = 'summation-sign'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "SUB"
    semantic_kind = "modifier"
    category = "state"
    categories = ("state",)
    aliases = ()
    keywords = ('summation', 'sign', 'large', 'uppercase', 'sigma', 'long', 'horizontal', 'top')

    def build(self):
        self.add_polyline("sigma",(28,2),(4,2),(18,16),(4,30),(28,30))
