'Monkey head.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9a46ab9a-ddfa-4f55-af29-5b8c5fbf44f9'
SOURCE_PATH = 'pictographic-primitives/animals/monkey 1_9a46ab9a-ddfa-4f55-af29-5b8c5fbf44f9.svg'
AUTHOR = 'gpt-6'

class MonkeyHead(Solo48):
    icon_id = 'monkey-head'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    categories = ('animals', 'primitives')
    aliases = ()
    keywords = ('monkey', 'head', 'animal')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_10_20 = (10, 20)
        p_24_8 = (24, 8)
        p_38_20 = (38, 20)
        p_38_32 = (38, 32)
        p_10_32 = (10, 32)
        p_24_40 = (24, 40)
        p_19_19 = (19, 19)
        p_29_19 = (29, 19)
        self.add_arc('skull-left', p_10_20, p_24_8, radius_x=14, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('skull-right', p_24_8, p_38_20, radius_x=14, radius_y=12, sweep=True, large_arc=False)
        self.add_line('wall-right', p_38_20, p_38_32)
        self.add_line('wall-left', p_10_32, p_10_20)
        self.add_arc('chin-right', p_38_32, p_24_40, radius_x=14, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('chin-left', p_24_40, p_10_32, radius_x=14, radius_y=8, sweep=True, large_arc=False)
        self.add_arc('ear-left', p_10_20, p_10_32, radius_x=6, radius_y=6, sweep=False, large_arc=False)
        self.add_arc('ear-right', p_38_20, p_38_32, radius_x=6, radius_y=6, sweep=True, large_arc=False)
        self.add_arc('muzzle', p_10_32, p_38_32, radius_x=14, radius_y=4, sweep=True, large_arc=False)
        self.add_line('eye-left', p_19_19, p_19_19)
        self.add_line('eye-right', p_29_19, p_29_19)
        self.add_contour('head', 'skull-left', 'skull-right', 'wall-right', 'chin-right', 'chin-left', 'wall-left', closed=True)
        self.relate('connect', 'ear-left', 'head')
        self.relate('connect', 'ear-right', 'head')
        self.relate('connect', 'muzzle', 'head')
