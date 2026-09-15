'Beer mug with foam.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/beer_mug_with_foam.py'
AUTHOR = 'gpt-6'

class BeerMugWithFoam(Solo48):
    icon_id = 'beer-mug-with-foam'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/drink'
    aliases = ('beer-mug', 'beer-stein', 'stein')
    keywords = ('beer', 'mug', 'stein', 'drink', 'pub', 'bar', 'alcohol', 'foam')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_8_16 = (8, 16)
        p_12_10 = (12, 10)
        p_24_10 = (24, 10)
        p_32_16 = (32, 16)
        p_32_24 = (32, 24)
        p_32_39 = (32, 39)
        p_27_44 = (27, 44)
        p_13_44 = (13, 44)
        p_8_39 = (8, 39)
        p_37_24 = (37, 24)
        p_40_28 = (40, 28)
        p_40_35 = (40, 35)
        p_37_39 = (37, 39)
        self.add_arc('foam-left', p_8_16, p_12_10, radius_x=5, radius_y=5, sweep=False, large_arc=False)
        self.add_arc('foam-centre', p_12_10, p_24_10, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('foam-right', p_24_10, p_32_16, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('wall-right-upper', p_32_16, p_32_24)
        self.add_line('wall-right-handle', p_32_24, p_32_39)
        self.add_arc('corner-se', p_32_39, p_27_44, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('base', p_27_44, p_13_44)
        self.add_arc('corner-sw', p_13_44, p_8_39, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('wall-left', p_8_39, p_8_16)
        self.add_line('foam-separator', p_8_16, p_32_16)
        self.add_line('handle-top', p_32_24, p_37_24)
        self.add_arc('handle-corner-ne', p_37_24, p_40_28, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('handle-right', p_40_28, p_40_35)
        self.add_arc('handle-corner-se', p_40_35, p_37_39, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('handle-bottom', p_37_39, p_32_39)
        self.add_contour('mug-outline', 'foam-left', 'foam-centre', 'foam-right', 'wall-right-upper', 'wall-right-handle', 'corner-se', 'base', 'corner-sw', 'wall-left', closed=True)
        self.add_contour('handle', 'handle-top', 'handle-corner-ne', 'handle-right', 'handle-corner-se', 'handle-bottom', closed=False)
        self.relate('connect', 'mug-outline', 'foam-separator')
        self.relate('connect', 'mug-outline', 'handle')
