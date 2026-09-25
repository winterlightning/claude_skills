'Figure with outstretched limbs.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The SQUARE visible envelope is (4, 4, 44, 44).\nThe parent remains available for comparison.\nHuman construction: icon_set/references/human_ref/full_body_ref.png and\nicon_set/references/human_ref/user.svg. Circular head radius 4,\nwith exactly 8 units of centerline head-to-body separation (4 visible units).'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '385c6908-a197-4341-bf8b-45327ba1ea69'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/warrior_385c6908-a197-4341-bf8b-45327ba1ea69.svg'
AUTHOR = 'gpt-6'

class FigureWithOutstretchedLimbs(Solo48):
    icon_id = 'figure-with-outstretched-limbs'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'culture'
    aliases = ()
    keywords = ('figure', 'warrior', 'human', 'action', 'pose', 'dance', 'movement', 'person')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_20_10 = (20, 10)
        p_28_10 = (28, 10)
        p_21_22 = (21, 22)
        p_19_31 = (19, 31)
        p_6_42 = (6, 42)
        p_32_35 = (32, 35)
        p_35_42 = (35, 42)
        p_6_11 = (6, 11)
        p_14_22 = (14, 22)
        p_42_22 = (42, 22)
        self.add_arc('head-top', p_20_10, p_28_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_arc('head-bottom', p_28_10, p_20_10, radius_x=4, radius_y=4, sweep=True, large_arc=False)
        self.add_line('torso', p_21_22, p_19_31)
        self.add_line('legs-1', p_6_42, p_19_31)
        self.add_line('legs-2', p_19_31, p_32_35)
        self.add_line('legs-3', p_32_35, p_35_42)
        self.add_line('arm-left-0', p_6_11, p_14_22)
        self.add_line('arm-left-1', p_14_22, p_21_22)
        self.add_line('arm-right', p_21_22, p_42_22)
        self.add_contour('head', 'head-top', 'head-bottom', closed=True)
        self.add_contour('legs', 'legs-1', 'legs-2', 'legs-3', closed=False)
        self.add_contour('arm-left', 'arm-left-0', 'arm-left-1', closed=False)
        self.relate('connect', 'legs', 'torso')
        self.relate('connect', 'arm-left', 'arm-right')
        self.relate('connect', 'arm-left', 'torso')
        self.relate('connect', 'arm-right', 'torso')
