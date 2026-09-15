'Elephant head friendly.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/elephant_head_friendly.py'
AUTHOR = 'gpt-6'

class ElephantHeadFriendly(Solo48):
    icon_id = 'elephant-head-friendly'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'animals'
    aliases = ('elephant-head',)
    keywords = ('elephant', 'head', 'ears', 'trunk', 'friendly', 'wildlife')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_11_20 = (11, 20)
        p_37_20 = (37, 20)
        p_37_25 = (37, 25)
        p_29_28 = (29, 28)
        p_29_35 = (29, 35)
        p_19_35 = (19, 35)
        p_19_28 = (19, 28)
        p_11_25 = (11, 25)
        p_9_13 = (9, 13)
        p_4_22 = (4, 22)
        p_11_32 = (11, 32)
        p_39_13 = (39, 13)
        p_44_22 = (44, 22)
        p_37_32 = (37, 32)
        p_20_20 = (20, 20)
        p_28_20 = (28, 20)
        self.add_arc('forehead', p_11_20, p_37_20, radius_x=13, radius_y=12, sweep=True, large_arc=False)
        self.add_line('cheek-right', p_37_20, p_37_25)
        self.add_arc('jaw-right', p_37_25, p_29_28, radius_x=8, radius_y=3, sweep=True, large_arc=False)
        self.add_line('trunk-right', p_29_28, p_29_35)
        self.add_arc('trunk-tip', p_29_35, p_19_35, radius_x=5, radius_y=5, sweep=True, large_arc=False)
        self.add_line('trunk-left', p_19_35, p_19_28)
        self.add_arc('jaw-left', p_19_28, p_11_25, radius_x=8, radius_y=3, sweep=True, large_arc=False)
        self.add_line('cheek-left', p_11_25, p_11_20)
        self.add_arc('ear-left-crest', p_11_20, p_9_13, radius_x=2, radius_y=7, sweep=False, large_arc=False)
        self.add_arc('ear-left-upper', p_9_13, p_4_22, radius_x=5, radius_y=9, sweep=False, large_arc=False)
        self.add_arc('ear-left-lower', p_4_22, p_11_32, radius_x=7, radius_y=10, sweep=False, large_arc=False)
        self.add_arc('ear-left-base', p_11_32, p_19_28, radius_x=8, radius_y=4, sweep=False, large_arc=False)
        self.add_arc('ear-right-crest', p_37_20, p_39_13, radius_x=2, radius_y=7, sweep=True, large_arc=False)
        self.add_arc('ear-right-upper', p_39_13, p_44_22, radius_x=5, radius_y=9, sweep=True, large_arc=False)
        self.add_arc('ear-right-lower', p_44_22, p_37_32, radius_x=7, radius_y=10, sweep=True, large_arc=False)
        self.add_arc('ear-right-base', p_37_32, p_29_28, radius_x=8, radius_y=4, sweep=True, large_arc=False)
        self.add_line('eye-left', p_20_20, p_20_20)
        self.add_line('eye-right', p_28_20, p_28_20)
        self.add_contour('face', 'forehead', 'cheek-right', 'jaw-right', 'trunk-right', 'trunk-tip', 'trunk-left', 'jaw-left', 'cheek-left', closed=True)
        self.add_contour('ear-left', 'ear-left-crest', 'ear-left-upper', 'ear-left-lower', 'ear-left-base', closed=False)
        self.add_contour('ear-right', 'ear-right-crest', 'ear-right-upper', 'ear-right-lower', 'ear-right-base', closed=False)
        self.relate('connect', 'face', 'ear-left')
        self.relate('connect', 'face', 'ear-right')
