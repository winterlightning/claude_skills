'Rocking horse toy.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/rocking_horse_toy.py'
AUTHOR = 'gpt-6'

class RockingHorseToy(Solo48):
    icon_id = 'rocking-horse-toy'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/baby'
    aliases = ('rocking-horse',)
    keywords = ('horse', 'rocker', 'toy', 'nursery', 'play')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_19_20 = (19, 20)
        p_26_20 = (26, 20)
        p_29_8 = (29, 8)
        p_35_13 = (35, 13)
        p_39_13 = (39, 13)
        p_39_23 = (39, 23)
        p_35_23 = (35, 23)
        p_35_25 = (35, 25)
        p_29_30 = (29, 30)
        p_15_30 = (15, 30)
        p_9_25 = (9, 25)
        p_13_40 = (13, 40)
        p_35_40 = (35, 40)
        p_4_33 = (4, 33)
        p_44_33 = (44, 33)
        self.add_line('back', p_19_20, p_26_20)
        self.add_line('neck', p_26_20, p_29_8)
        self.add_line('ear', p_29_8, p_35_13)
        self.add_line('forehead', p_35_13, p_39_13)
        self.add_arc('muzzle', p_39_13, p_39_23, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('jaw', p_39_23, p_35_23)
        self.add_line('chest', p_35_23, p_35_25)
        self.add_arc('breast', p_35_25, p_29_30, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('belly', p_29_30, p_15_30)
        self.add_arc('haunch', p_15_30, p_9_25, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_arc('rump', p_9_25, p_19_20, radius_x=9, radius_y=5, sweep=True, large_arc=False)
        self.add_line('hind-support', p_15_30, p_13_40)
        self.add_line('front-support', p_29_30, p_35_40)
        self.add_arc('rocker-left', p_4_33, p_13_40, radius_x=9, radius_y=7, sweep=False, large_arc=False)
        self.add_line('rocker-base', p_13_40, p_35_40)
        self.add_arc('rocker-right', p_35_40, p_44_33, radius_x=9, radius_y=7, sweep=False, large_arc=False)
        self.add_contour('horse', 'back', 'neck', 'ear', 'forehead', 'muzzle', 'jaw', 'chest', 'breast', 'belly', 'haunch', 'rump', closed=True)
        self.add_contour('rocker', 'rocker-left', 'rocker-base', 'rocker-right', closed=False)
        self.relate('connect', 'horse', 'hind-support')
        self.relate('connect', 'horse', 'front-support')
        self.relate('connect', 'rocker', 'hind-support')
        self.relate('connect', 'rocker', 'front-support')
