'Chinese character: preserve balanced sweeping curves, replacing the near-miss crossing with one shared node.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0048393d-1c7b-5fde-b4e1-e018ff09375c'
SOURCE_PATH = 'pictographic-primitives/interface-essential/chinese alphabet_0048393d-1c7b-5fde-b4e1-e018ff09375c.svg'
AUTHOR = 'gpt-6'

class ChineseAlphabet(Solo48):
    icon_id = 'chinese-alphabet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('chinese', 'alphabet', 'interface-essential')

    def build(self) -> None:
        # Preserve the sweeping calligraphic crossing, with a single exact shared intersection.
        self.add_polyline('bar',(6,12),(14,12),(24,12),(34,12),(42,12))
        self.add_line('stem',(24,6),(24,12))
        self.relate('connect','stem','bar')
        self.add_bezier('sweep-right',(14,12),((16,22),(20,27),(24,31)),((29,36),(36,40),(42,42)))
        self.add_bezier('sweep-left',(34,12),((32,22),(28,27),(24,31)),((19,36),(12,40),(6,42)))
        self.relate('connect','sweep-right','bar')
        self.relate('connect','sweep-left','bar')
        self.relate('connect','sweep-right','sweep-left')
