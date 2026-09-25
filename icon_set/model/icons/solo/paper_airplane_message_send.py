'Paper airplane message send.\n\nSymbol plan: shared integer nodes preserve contour order, repeated stations and real\nattachments. The HRECT_L visible envelope is (2, 6, 46, 42).\nThe parent remains available for comparison.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = None
SOURCE_PATH = 'icon_set/model/icons/solo/paper_airplane_message_send.py'
AUTHOR = 'gpt-6'

class PaperAirplaneMessageSend(Solo48):
    icon_id = 'paper-airplane-message-send'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'messages'
    aliases = ('paper-plane', 'message-send', 'send')
    keywords = ('send', 'paper', 'airplane', 'plane', 'message', 'share', 'submit', 'mail', 'dart')

    def build(self) -> None:
        # Shared nodes are reused by every touching member.
        p_44_8 = (44, 8)
        p_33_40 = (33, 40)
        p_24_34 = (24, 34)
        p_19_40 = (19, 40)
        p_18_30 = (18, 30)
        p_4_25 = (4, 25)
        self.add_line('airplane-outline-1', p_44_8, p_33_40)
        self.add_line('airplane-outline-2', p_33_40, p_24_34)
        self.add_line('airplane-outline-3', p_24_34, p_19_40)
        self.add_line('airplane-outline-4', p_19_40, p_18_30)
        self.add_line('airplane-outline-5', p_18_30, p_4_25)
        self.add_line('airplane-outline-6', p_4_25, p_44_8)
        self.add_line('centre-fold', p_18_30, p_44_8)
        self.add_contour('airplane-outline', 'airplane-outline-1', 'airplane-outline-2', 'airplane-outline-3', 'airplane-outline-4', 'airplane-outline-5', 'airplane-outline-6', closed=True)
        self.relate('connect', 'airplane-outline', 'centre-fold')
