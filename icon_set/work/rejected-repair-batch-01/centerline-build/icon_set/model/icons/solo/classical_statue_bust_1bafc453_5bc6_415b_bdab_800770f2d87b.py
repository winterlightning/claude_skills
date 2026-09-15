'Classical statue bust.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1bafc453-5bc6-415b-bdab-800770f2d87b'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/greek statue_1bafc453-5bc6-415b-bdab-800770f2d87b.svg'
AUTHOR = 'gpt-6'

class ClassicalStatueBust(Solo48):
    icon_id = 'classical-statue-bust'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('statue', 'bust', 'greek', 'classical', 'sculpture', 'marble', 'museum', 'antiquity')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_13_13 = (13, 13)
        p_33_13 = (33, 13)
        p_30_24 = (30, 24)
        p_35_26 = (35, 26)
        p_40_35 = (40, 35)
        p_8_35 = (8, 35)
        p_13_26 = (13, 26)
        p_20_23 = (20, 23)
        p_8_19 = (8, 19)
        p_13_44 = (13, 44)
        p_35_44 = (35, 44)
        self.add_arc('crown', p_13_13, p_33_13, radius_x=10, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('back', p_33_13, p_30_24, radius_x=12, radius_y=12, sweep=True, large_arc=False)
        self.add_line('back-neck', p_30_24, p_35_26)
        self.add_arc('shoulder-right', p_35_26, p_40_35, radius_x=5, radius_y=9, sweep=True, large_arc=False)
        self.add_line('base', p_40_35, p_8_35)
        self.add_arc('shoulder-left', p_8_35, p_13_26, radius_x=5, radius_y=9, sweep=True, large_arc=False)
        self.add_line('profile-0', p_13_26, p_20_23)
        self.add_line('profile-1', p_20_23, p_8_19)
        self.add_line('profile-2', p_8_19, p_13_13)
        self.add_line('plinth', p_13_44, p_35_44)
        self.add_contour('bust', 'crown', 'back', 'back-neck', 'shoulder-right', 'base', 'shoulder-left', 'profile-0', 'profile-1', 'profile-2', closed=True)
