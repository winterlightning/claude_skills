"""Front-facing panels share a y axis; two broad bellows folds replace the fine pleats. Three keyboard bars share a repeat definition. Extremes (4,8)-(44,40)."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7083ce91-7e5d-5623-a68c-d237791381a4'
SOURCE_PATH = 'pictographic-primitives/music/accordian_7083ce91-7e5d-5623-a68c-d237791381a4.svg'
AUTHOR = 'gpt-6'

class Accordion(Solo48):
    icon_id = 'accordion'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    categories = ("primitives", "music")
    aliases = ()
    keywords = ('accordion', 'instrument', 'bellows', 'keyboard', 'folk', 'music', 'squeezebox')

    def build(self):
        self.add_polyline('left-panel', (12,8), (4,8), (4,16), (4,24), (4,32), (4,40), (12,40), (12,32), (12,24), (12,16), closed=True)
        self.add_polyline('right-panel', (36,8), (44,8), (44,40), (36,40), (36,32), (36,16), closed=True)
        self.add_polyline('bellows-top', (12,16), (24,8), (36,16))
        self.add_polyline('bellows-bottom', (12,32), (24,40), (36,32))
        self.add_line('fold', (24,8), (24,40))
        for part in ('bellows-top','bellows-bottom'):
            self.relate('connect', part, 'left-panel')
            self.relate('connect', part, 'right-panel')
            self.relate('connect', part, 'fold')
        for i,y in enumerate((16,24,32)):
            self.add_line(f'key-{i}', (4,y), (12,y))
            self.relate('connect', f'key-{i}', 'left-panel')
