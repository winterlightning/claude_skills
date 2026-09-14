'Tropical island with palm tree.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The VRECT_L visible envelope is (6, 2, 42, 46).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/tropical_island_with_palm_tree.py'
AUTHOR = 'gpt-6'

class TropicalIslandWithPalmTree(Solo48):
    icon_id = 'tropical-island-with-palm-tree'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/nature'
    aliases = ('tropical-island', 'palm-tree-island', 'island-palm')
    keywords = ('island', 'palm', 'tree', 'beach', 'tropical', 'vacation', 'holiday', 'sea', 'sand', 'water')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_24_15 = (24, 15)
        p_10_10 = (10, 10)
        p_38_10 = (38, 10)
        p_10_20 = (10, 20)
        p_38_20 = (38, 20)
        p_25_4 = (25, 4)
        p_24_29 = (24, 29)
        p_12_39 = (12, 39)
        p_36_39 = (36, 39)
        p_8_41 = (8, 41)
        p_15_41 = (15, 41)
        p_21_41 = (21, 41)
        p_27_41 = (27, 41)
        p_33_41 = (33, 41)
        p_40_41 = (40, 41)
        self.add_arc('frond-upper-left', p_24_15, p_10_10, radius_x=15, radius_y=19, sweep=False, large_arc=False)
        self.add_arc('frond-upper-right', p_24_15, p_38_10, radius_x=15, radius_y=19, sweep=True, large_arc=False)
        self.add_arc('frond-lower-left', p_24_15, p_10_20, radius_x=14, radius_y=17, sweep=True, large_arc=False)
        self.add_arc('frond-lower-right', p_24_15, p_38_20, radius_x=14, radius_y=17, sweep=False, large_arc=False)
        self.add_arc('frond-top', p_24_15, p_25_4, radius_x=9, radius_y=11, sweep=False, large_arc=False)
        self.add_arc('trunk', p_24_15, p_24_29, radius_x=17, radius_y=22, sweep=True, large_arc=False)
        self.add_arc('mound-left', p_12_39, p_24_29, radius_x=12, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('mound-right', p_24_29, p_36_39, radius_x=12, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('water-crest-left-a', p_8_41, p_12_39, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('water-crest-left-b', p_12_39, p_15_41, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('water-trough-left', p_15_41, p_21_41, radius_x=3, radius_y=3, sweep=False, large_arc=False)
        self.add_arc('water-crest-centre', p_21_41, p_27_41, radius_x=3, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('water-trough-right', p_27_41, p_33_41, radius_x=3, radius_y=3, sweep=False, large_arc=False)
        self.add_arc('water-crest-right-a', p_33_41, p_36_39, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_arc('water-crest-right-b', p_36_39, p_40_41, radius_x=4, radius_y=3, sweep=True, large_arc=False)
        self.add_contour('mound', 'mound-left', 'mound-right', closed=False)
        self.add_contour('waterline', 'water-crest-left-a', 'water-crest-left-b', 'water-trough-left', 'water-crest-centre', 'water-trough-right', 'water-crest-right-a', 'water-crest-right-b', closed=False)
        self.relate('connect', 'trunk', 'frond-upper-left')
        self.relate('connect', 'trunk', 'frond-upper-right')
        self.relate('connect', 'trunk', 'frond-lower-left')
        self.relate('connect', 'trunk', 'frond-lower-right')
        self.relate('connect', 'trunk', 'frond-top')
        self.relate('connect', 'trunk', 'mound')
        self.relate('connect', 'mound', 'waterline')
