"""Two Burning Candles on Table."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8755e726-15e1-5732-b628-665b56717f32'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__two-lit-candles-on-table/20260927T133645Z-thuan-mac-1/reference/table candles_8755e726-15e1-5732-b628-665b56717f32.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'two-lit-candles-on-table'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'fire'
    categories = ('fire', 'primitives')
    aliases = ()
    keywords = ('candle', 'pair', 'table', 'flame', 'light', 'fire', 'room')

    def build(self):
        # Plan: Two candles share width and a table baseline; flame heights differ. Table apron reduced to one sturdy line. Lucide clean joined geometry. Bounds (6,6)-(42,42).
        # Each candle owns its flame, actual wick junction and U-shaped body.
        for i,(x,top,body_top) in enumerate([(15,6,22),(33,8,24)]):
            base=top+10
            self.add_bezier(f'fire-{i}',(x,top),((x+3,top+4),(x+4,top+5),(x+4,top+6)),((x+4,top+9),(x+3,base),(x,base)),((x-3,base),(x-4,top+9),(x-4,top+6)),((x-4,top+5),(x-3,top+4),(x,top)))
            self.add_contour(f'flame-{i}',f'fire-{i}',closed=True)
            self.add_polyline(f'candle-{i}',(x-4,34),(x-4,body_top),(x+4,body_top),(x+4,34))
            self.add_line(f'wick-{i}',(x,base),(x,body_top))
            self.relate('connect',f'wick-{i}',f'flame-{i}')
            self.relate('connect',f'wick-{i}',f'candle-{i}')
        self.add_polyline('table',(6,34),(42,34))
        for i,x in enumerate((11,37)):
            self.add_line(f'leg-{i}',(x,34),(x,42))
            self.relate('connect',f'leg-{i}','table')
            self.relate('connect',f'candle-{i}','table')
