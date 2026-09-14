'Crystal ball on stand.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9acd961d-254b-46da-a4e6-47bf2a234155'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/sphere_9acd961d-254b-46da-a4e6-47bf2a234155.svg'
AUTHOR = 'gpt-6'

class CrystalBallOnStand(Solo48):
    icon_id = 'crystal-ball-on-stand'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/culture'
    aliases = ()
    keywords = ('crystal ball', 'sphere', 'fortune', 'divination', 'psychic', 'mystic', 'orb', 'future')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_10_19 = (10, 19)
        p_38_19 = (38, 19)
        p_8_44 = (8, 44)
        p_11_35 = (11, 35)
        p_37_35 = (37, 35)
        p_40_44 = (40, 44)
        self.add_arc('orb-top', p_10_19, p_38_19, radius_x=14, radius_y=15, sweep=True, large_arc=False)
        self.add_arc('orb-bottom', p_38_19, p_10_19, radius_x=14, radius_y=15, sweep=True, large_arc=False)
        self.add_line('stand-1', p_8_44, p_11_35)
        self.add_line('stand-2', p_11_35, p_37_35)
        self.add_line('stand-3', p_37_35, p_40_44)
        self.add_line('stand-4', p_40_44, p_8_44)
        self.add_contour('orb', 'orb-top', 'orb-bottom', closed=True)
        self.add_contour('stand', 'stand-1', 'stand-2', 'stand-3', 'stand-4', closed=True)
        self.relate('connect', 'orb', 'stand')
