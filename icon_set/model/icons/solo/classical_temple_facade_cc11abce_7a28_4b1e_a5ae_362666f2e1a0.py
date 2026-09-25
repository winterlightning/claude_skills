'Classical temple facade.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc11abce-7a28-4b1e-a5ae-362666f2e1a0'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/greek building_cc11abce-7a28-4b1e-a5ae-362666f2e1a0.svg'
AUTHOR = 'gpt-6'

class ClassicalTempleFacade(Solo48):
    icon_id = 'classical-temple-facade'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('temple', 'greek', 'classical', 'architecture', 'parthenon', 'columns', 'museum', 'antiquity')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_6_17 = (6, 17)
        p_24_6 = (24, 6)
        p_42_17 = (42, 17)
        p_13_25 = (13, 25)
        p_13_34 = (13, 34)
        p_24_25 = (24, 25)
        p_24_34 = (24, 34)
        p_35_25 = (35, 25)
        p_35_34 = (35, 34)
        p_9_34 = (9, 34)
        p_39_34 = (39, 34)
        p_6_42 = (6, 42)
        p_42_42 = (42, 42)
        self.add_line('pediment-1', p_6_17, p_24_6)
        self.add_line('pediment-2', p_24_6, p_42_17)
        self.add_line('pediment-3', p_42_17, p_6_17)
        self.add_line('column-left', p_13_25, p_13_34)
        self.add_line('column-middle', p_24_25, p_24_34)
        self.add_line('column-right', p_35_25, p_35_34)
        self.add_line('upper-step-1', p_9_34, p_13_34)
        self.add_line('upper-step-2', p_13_34, p_24_34)
        self.add_line('upper-step-3', p_24_34, p_35_34)
        self.add_line('upper-step-4', p_35_34, p_39_34)
        self.add_line('lower-step', p_6_42, p_42_42)
        self.add_contour('pediment', 'pediment-1', 'pediment-2', 'pediment-3', closed=True)
        self.add_contour('upper-step', 'upper-step-1', 'upper-step-2', 'upper-step-3', 'upper-step-4', closed=False)
        self.relate('connect', 'column-left', 'upper-step')
        self.relate('connect', 'column-middle', 'upper-step')
        self.relate('connect', 'column-right', 'upper-step')
