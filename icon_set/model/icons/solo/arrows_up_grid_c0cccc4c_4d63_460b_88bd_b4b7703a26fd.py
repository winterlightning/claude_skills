"""Four upward arrows form a two-by-two grid. SQUARE extremes (6,6)-(42,42). Lucide arrow-up informs repeated heads and shafts; all four use identical dimensions and pitch."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c0cccc4c-4d63-460b-88bd-b4b7703a26fd'
SOURCE_PATH = 'pictographic-primitives/symbol/four arrows up_c0cccc4c-4d63-460b-88bd-b4b7703a26fd.svg'
AUTHOR = 'gpt-6'


class ArrowsUpGrid(Solo48):
    icon_id = 'arrows-up-grid'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    aliases = ()
    keywords = ('arrows', 'up', 'upload', 'increase', 'grid', 'upward', 'boost', 'rise')

    def build(self) -> None:
        for row,y in enumerate((6,28)):
            for col,x in enumerate((13,35)):
                name=f'arrow-{row}-{col}'
                self.add_polyline(name+'-head', (x-7,y+7), (x,y), (x+7,y+7))
                self.add_line(name+'-shaft', (x,y), (x,y+14))
                self.relate('connect', name+'-head', name+'-shaft')
