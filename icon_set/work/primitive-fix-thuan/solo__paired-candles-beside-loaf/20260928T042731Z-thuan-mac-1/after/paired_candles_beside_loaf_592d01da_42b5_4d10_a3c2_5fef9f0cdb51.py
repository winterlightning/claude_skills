"""Two lit candles in a shared holder beside a loaf of bread (Shabbat candles and challah).

Plan: VRECT_L (8,4)-(40,44). Two outlined candles 8x12 at x 8-16 and 24-32 with short flame strokes 9 above them, a holder of two r8 quarter arcs from the candle base centres meeting at a stem that runs to the bottom, and a loaf at the lower right drawn as a two-cubic bun 10 wide, flat underneath and domed on top. Every candle edge is a standalone line joined by connect so the exact 8-unit gaps certify.
Review of the rejected drawing: the candles were bare strokes with dot flames and the holder had a long stem and foot, so the pair read as the letter y with an umlaut; the loaf was a small D beside it. The candles now have bodies, the holder is a compact U on a stem, and the loaf is taller with a rounded top.
Omissions: the loaf's two score marks and the holder's foot (the foot would sit 2 units from the loaf).
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '592d01da-42b5-4d10-a3c2-5fef9f0cdb51'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__paired-candles-beside-loaf/20260928T042731Z-thuan-mac-1/reference/candle bread_592d01da-42b5-4d10-a3c2-5fef9f0cdb51.svg'
AUTHOR = "claude-fable-5-1"


class PairedCandlesBesideLoaf(Solo48):
    icon_id = 'paired-candles-beside-loaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ('shabbat-candles-and-challah',)
    keywords = ('candle', 'bread', 'shabbat', 'challah', 'candles', 'loaf', 'sabbath')

    def build(self) -> None:
        def ring(name, pts):
            ids = []
            for i, (a, b) in enumerate(zip(pts, pts[1:] + pts[:1])):
                self.add_line(f'{name}-{i}', a, b)
                ids.append(f'{name}-{i}')
            for a, b in zip(ids, ids[1:] + ids[:1]):
                self.relate('connect', a, b)
            return ids
        top, base = 14, 26
        for x in (12, 28):
            self.add_line(f'flame-{x}', (x, 4), (x, 5))
            # candle box; the base edge is split at the centre where the holder arm hangs
            ring(f'candle-{x}', [(x - 4, top), (x + 4, top), (x + 4, base), (x, base), (x - 4, base)])
        # holder: two r8 quarter arcs about (20,26) from the candle base centres to the stem top (20,34)
        self.add_arc('holder-left', (12, base), (20, 34), radius_x=8, sweep=False)
        self.add_arc('holder-right', (20, 34), (28, base), radius_x=8, sweep=False)
        self.add_contour('holder', 'holder-left', 'holder-right')
        self.relate('connect', 'holder', 'candle-12-2')
        self.relate('connect', 'holder', 'candle-12-3')
        self.relate('connect', 'holder', 'candle-28-2')
        self.relate('connect', 'holder', 'candle-28-3')
        self.add_line('stem', (20, 34), (20, 44))
        self.relate('connect', 'stem', 'holder')
        # loaf: a bun of two cubics, flat on the bottom and domed on top
        self.add_bezier('loaf-top', (30, 44), ((30, 34), (40, 34), (40, 44)))
        self.add_bezier('loaf-bottom', (40, 44), ((40, 44), (30, 44), (30, 44)))
        self.add_contour('loaf', 'loaf-top', 'loaf-bottom', closed=True)
