'Top hat with curved brim.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '80871b7a-ea0b-4358-acf0-e5ab77edc416'
SOURCE_PATH = 'pictographic-primitives/accessories/batch-02/hat 1_80871b7a-ea0b-4358-acf0-e5ab77edc416.svg'
AUTHOR = 'gpt-6'

class TopHatWithCurvedBrim(Solo48):
    icon_id = 'top-hat-with-curved-brim'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/accessories'
    aliases = ()
    keywords = ('hat', 'top hat', 'formal', 'brim', 'gentleman', 'magic', 'headwear', 'vintage')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_14_32 = (14, 32)
        p_14_24 = (14, 24)
        p_13_10 = (13, 10)
        p_16_6 = (16, 6)
        p_32_6 = (32, 6)
        p_35_10 = (35, 10)
        p_34_24 = (34, 24)
        p_34_32 = (34, 32)
        p_6_32 = (6, 32)
        p_42_32 = (42, 32)
        p_24_42 = (24, 42)
        self.add_line('crown-left-1', p_14_32, p_14_24)
        self.add_line('crown-left-2', p_14_24, p_13_10)
        self.add_arc('crown-tl', p_13_10, p_16_6, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('crown-top', p_16_6, p_32_6)
        self.add_arc('crown-tr', p_32_6, p_35_10, radius_x=3, radius_y=4, sweep=True, large_arc=False)
        self.add_line('crown-right-1', p_35_10, p_34_24)
        self.add_line('crown-right-2', p_34_24, p_34_32)
        self.add_line('band', p_14_24, p_34_24)
        self.add_line('brim-top-1', p_6_32, p_14_32)
        self.add_line('brim-top-2', p_14_32, p_34_32)
        self.add_line('brim-top-3', p_34_32, p_42_32)
        self.add_arc('brim-right', p_42_32, p_24_42, radius_x=18, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('brim-left', p_24_42, p_6_32, radius_x=18, radius_y=10, sweep=True, large_arc=False)
        self.add_contour('crown', 'crown-left-1', 'crown-left-2', 'crown-tl', 'crown-top', 'crown-tr', 'crown-right-1', 'crown-right-2', closed=False)
        self.add_contour('brim', 'brim-top-1', 'brim-top-2', 'brim-top-3', 'brim-right', 'brim-left', closed=True)
        self.relate('connect', 'crown', 'band')
        self.relate('connect', 'crown', 'brim')
