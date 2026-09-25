"""Two Burning Candles on Table."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8755e726-15e1-5732-b628-665b56717f32'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/fire/table candles_8755e726-15e1-5732-b628-665b56717f32.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'two-lit-candles-on-table'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    aliases = ()
    keywords = ('candle', 'pair', 'table', 'flame', 'light', 'fire', 'room')

    def build(self):
        # Plan: Two candles share width and a table baseline; flame heights differ. Table apron reduced to one sturdy line. Lucide clean joined geometry. Bounds (6,6)-(42,42).
        # Each candle owns its flame, actual wick junction and U-shaped body.
        for i,(x,top,body_top) in enumerate([(15,6,24),(33,8,26)]):
            base=top+10
            self.add_bezier(f'fire-{i}',(x,top),((x+3,top+4),(x+4,top+5),(x+4,top+6)),((x+4,top+9),(x+3,base),(x,base)),((x-3,base),(x-4,top+9),(x-4,top+6)),((x-4,top+5),(x-3,top+4),(x,top)))
            self.add_contour(f'flame-{i}',f'fire-{i}',closed=True)
            self.add_polyline(f'candle-{i}',(x-4,34),(x-4,body_top),(x,body_top),(x+4,body_top),(x+4,34))
            self.add_line(f'wick-{i}',(x,base),(x,body_top))
            self.relate('connect',f'wick-{i}',f'flame-{i}')
            self.relate('connect',f'wick-{i}',f'candle-{i}')
        self.add_polyline('table',(6,34),(11,34),(19,34),(29,34),(37,34),(42,34))
        for i,x in enumerate((11,37)):
            self.add_line(f'leg-{i}',(x,34),(x,42))
            self.relate('connect',f'leg-{i}','table')
            self.relate('connect',f'candle-{i}','table')
