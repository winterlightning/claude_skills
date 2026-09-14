'Spartan helmet.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '72959280-0cd4-51d8-9544-b784119c7e1d'
SOURCE_PATH = 'pictographic-primitives/culture/batch-06/spartan helmet_72959280-0cd4-51d8-9544-b784119c7e1d.svg'
AUTHOR = 'gpt-6'

class SpartanHelmet(Solo48):
    icon_id = 'spartan-helmet'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('helmet', 'spartan', 'corinthian', 'greek', 'warrior', 'crest', 'armour', 'soldier')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_25 = (6, 25)
        p_20_13 = (20, 13)
        p_34_25 = (34, 25)
        p_34_31 = (34, 31)
        p_34_35 = (34, 35)
        p_27_33 = (27, 33)
        p_22_39 = (22, 39)
        p_12_42 = (12, 42)
        p_15_28 = (15, 28)
        p_23_25 = (23, 25)
        p_12_25 = (12, 25)
        p_6_31 = (6, 31)
        p_17_6 = (17, 6)
        p_42_27 = (42, 27)
        p_42_34 = (42, 34)
        self.add_arc('dome-left', p_6_25, p_20_13, radius_x=14, radius_y=12, sweep=True, large_arc=False)
        self.add_arc('dome-right', p_20_13, p_34_25, radius_x=14, radius_y=12, sweep=True, large_arc=False)
        self.add_line('guard-1', p_34_25, p_34_31)
        self.add_line('guard-2', p_34_31, p_34_35)
        self.add_line('guard-3', p_34_35, p_27_33)
        self.add_line('guard-4', p_27_33, p_22_39)
        self.add_line('guard-5', p_22_39, p_12_42)
        self.add_line('guard-6', p_12_42, p_15_28)
        self.add_line('guard-7', p_15_28, p_23_25)
        self.add_line('guard-8', p_23_25, p_12_25)
        self.add_line('guard-9', p_12_25, p_6_31)
        self.add_line('guard-10', p_6_31, p_6_25)
        self.add_line('crest-front', p_20_13, p_17_6)
        self.add_arc('crest-top', p_17_6, p_42_27, radius_x=25, radius_y=21, sweep=True, large_arc=False)
        self.add_line('crest-back', p_42_27, p_42_34)
        self.add_line('crest-base', p_42_34, p_34_31)
        self.add_contour('helmet', 'dome-left', 'dome-right', 'guard-1', 'guard-2', 'guard-3', 'guard-4', 'guard-5', 'guard-6', 'guard-7', 'guard-8', 'guard-9', 'guard-10', closed=True)
        self.add_contour('crest', 'crest-front', 'crest-top', 'crest-back', 'crest-base', closed=False)
        self.relate('connect', 'helmet', 'crest')
