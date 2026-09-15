"""A round Chinese cash coin with a square opening. Keep circle and square; omit the redundant inner rim."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0ddd125a-aea1-4b88-80a0-354c17fcbf30'
SOURCE_PATH = 'pictographic-primitives/religion/chinese new year coin_0ddd125a-aea1-4b88-80a0-354c17fcbf30.svg'
AUTHOR = 'gpt-6'


class ChineseCoinWithSquareHole(Solo48):
    icon_id = 'chinese-coin-with-square-hole'
    keyshape = Keyshape.CIRCLE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/religion"
    aliases = ()
    keywords = ('coin', 'chinese', 'cash', 'money', 'square', 'hole', 'currency')

    def oval(self, name, cx, cy, rx, ry=None):
        ry = rx if ry is None else ry
        self.add_arc(name+'-top', (cx-rx,cy), (cx+rx,cy), radius_x=rx, radius_y=ry)
        self.add_arc(name+'-bottom', (cx+rx,cy), (cx-rx,cy), radius_x=rx, radius_y=ry)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

    def build(self) -> None:
        self.oval('coin',24,24,20)
        self.add_polyline('hole',(17,17),(31,17),(31,31),(17,31),closed=True)
