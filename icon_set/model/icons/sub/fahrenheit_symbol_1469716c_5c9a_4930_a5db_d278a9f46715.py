"""Fahrenheit Symbol: A tall uppercase F has a long top bar and a shorter middle bar. A tiny detached degree mark appears above and to its left in the reference.

Construction: Upper-left degree ring and a separated F whose bars meet its vertical stem.
Keyshape: SQUARE; the four extrema follow the SUB32 contract.
"""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '1469716c-5c9a-4930-a5db-d278a9f46715'
SOURCE_PATH = 'pictographic-primitives/state/fahrenheit_1469716c-5c9a-4930-a5db-d278a9f46715.svg'
AUTHOR = 'gpt-6'


class FahrenheitSymbol(Sub32):
    icon_id = 'fahrenheit-symbol'
    keyshape = Keyshape.SQUARE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'primitives/mark'
    aliases = ()
    keywords = ('fahrenheit', 'symbol', 'tall', 'uppercase', 'f', 'long', 'top', 'bar')

    def build(self):
        def circle(name,cx,cy,radius):
            self.add_arc(name+"-top",(cx-radius,cy),(cx+radius,cy),radius_x=radius)
            self.add_arc(name+"-bottom",(cx+radius,cy),(cx-radius,cy),radius_x=radius)
            self.add_contour(name,name+"-top",name+"-bottom",closed=True)
        circle("degree",6,6,4)
        self.add_polyline("f",(18,30),(18,2),(30,2))
        self.add_line("middle",(18,14),(28,14))
        self.relate("connect","f","middle")
