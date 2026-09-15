"""Lit Pillar Candle reconstructed from the supplied reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '5f3444ae-892d-4884-834e-0ac133b299e6'
SOURCE_PATH = 'pictographic-primitives/lights/candle_5f3444ae-892d-4884-834e-0ac133b299e6.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'lit-pillar-candle-5f3444ae-892d-4884-834e-0ac133b299e6'
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/lighting"
    aliases = ()
    keywords = ('candle', 'flame', 'wick', 'wax', 'light', 'pillar')
    keyshape = Keyshape.VRECT_L

    def build(self):
        # Plan: centered flame and wick above a rounded pillar. VRECT_L extremes
        # (8,4)..(40,44). No useful local Lucide candle match; circular flame base.
        axis, left, right, top, bottom, corner = 24, 8, 40, 28, 44, 4
        self.add_line("flame-right",(axis,4),(axis+4,11))
        self.add_arc("flame-bottom-right",(axis+4,11),(axis,19),radius_x=5)
        self.add_arc("flame-bottom-left",(axis,19),(axis-4,11),radius_x=5)
        self.add_line("flame-left",(axis-4,11),(axis,4))
        self.add_contour("flame","flame-right","flame-bottom-right","flame-bottom-left","flame-left",closed=True)
        self.add_line("wick",(axis,19),(axis,top))
        self.add_line("candle-top-1",(left+corner,top),(axis,top))
        self.add_line("candle-top-2",(axis,top),(right-corner,top))
        self.add_arc("top-right",(right-corner,top),(right,top+corner),radius_x=corner)
        self.add_line("right",(right,top+corner),(right,bottom))
        self.add_line("base",(right,bottom),(left,bottom))
        self.add_line("left",(left,bottom),(left,top+corner))
        self.add_arc("top-left",(left,top+corner),(left+corner,top),radius_x=corner)
        self.add_contour("pillar","candle-top-1","candle-top-2","top-right","right","base","left","top-left",closed=True)
        self.relate("connect","wick","flame")
        self.relate("connect","wick","pillar")
