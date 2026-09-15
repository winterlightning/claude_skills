'Great sphinx.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c701c596-0404-4be0-8228-3ddc825a28fa'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/sphinx_c701c596-0404-4be0-8228-3ddc825a28fa.svg'
AUTHOR = 'gpt-6'

class GreatSphinx(Solo48):
    icon_id = 'great-sphinx'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture/objects'
    aliases = ()
    keywords = ('sphinx', 'egyptian', 'giza', 'pharaoh', 'lion', 'monument', 'ancient', 'mythology')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_14_34 = (14, 34)
        p_6_29 = (6, 29)
        p_8_18 = (8, 18)
        p_34_18 = (34, 18)
        p_35_29 = (35, 29)
        p_27_34 = (27, 34)
        p_14_15 = (14, 15)
        p_27_15 = (27, 15)
        p_27_21 = (27, 21)
        p_14_21 = (14, 21)
        p_42_36 = (42, 36)
        p_42_42 = (42, 42)
        p_6_42 = (6, 42)
        p_13_34 = (13, 34)
        self.add_line('flap-outer-left', p_14_34, p_6_29)
        self.add_line('headdress-left', p_6_29, p_8_18)
        self.add_arc('headdress-top', p_8_18, p_34_18, radius_x=13, radius_y=12, sweep=True, large_arc=False)
        self.add_line('headdress-right', p_34_18, p_35_29)
        self.add_line('flap-outer-right', p_35_29, p_27_34)
        self.add_line('face-top', p_14_15, p_27_15)
        self.add_line('face-right', p_27_15, p_27_21)
        self.add_arc('chin', p_27_21, p_14_21, radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_line('face-left', p_14_21, p_14_15)
        self.add_line('flap-left', p_14_21, p_14_34)
        self.add_line('flap-right', p_27_21, p_27_34)
        self.add_arc('haunch', p_35_29, p_42_36, radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_line('body-right', p_42_36, p_42_42)
        self.add_line('base', p_42_42, p_6_42)
        self.add_arc('paw', p_6_42, p_13_34, radius_x=7, radius_y=8, sweep=True, large_arc=False)
        self.add_line('paw-top', p_13_34, p_14_34)
        self.add_contour('headdress', 'flap-outer-left', 'headdress-left', 'headdress-top', 'headdress-right', 'flap-outer-right', closed=False)
        self.add_contour('face', 'face-top', 'face-right', 'chin', 'face-left', closed=True)
        self.add_contour('body', 'haunch', 'body-right', 'base', 'paw', 'paw-top', closed=False)
        self.relate('connect', 'face', 'flap-left')
        self.relate('connect', 'headdress', 'flap-left')
        self.relate('connect', 'face', 'flap-right')
        self.relate('connect', 'headdress', 'flap-right')
        self.relate('connect', 'body', 'headdress')
        self.relate('connect', 'body', 'flap-left')
