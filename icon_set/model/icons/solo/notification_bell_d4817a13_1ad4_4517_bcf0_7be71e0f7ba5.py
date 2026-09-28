"""A domed notification bell with knob and detached clapper. VRECT_L extremes (8,4)-(40,44). Lucide bell informs the round dome and smooth outward flare. Retain knob, flat lip and short clapper; match left and right curves."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd4817a13-1ad4-4517-bcf0-7be71e0f7ba5'
SOURCE_PATH = 'pictographic-primitives/symbol/notification_d4817a13-1ad4-4517-bcf0-7be71e0f7ba5.svg'
AUTHOR = 'gpt-6'


class NotificationBell(Solo48):
    icon_id = 'notification-bell'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('bell', 'notification', 'alert', 'alarm', 'reminder', 'ring', 'sound', 'news')

    def build(self) -> None:
        self.add_arc('dome-left',(12,20),(24,8),radius_x=12)
        self.add_arc('dome-right',(24,8),(36,20),radius_x=12)
        self.add_line('side-right',(36,20),(36,26))
        self.add_arc('flare-right',(36,26),(40,34),radius_x=10,sweep=False)
        self.add_line('lip',(40,34),(8,34))
        self.add_arc('flare-left',(8,34),(12,26),radius_x=10,sweep=False)
        self.add_line('side-left',(12,26),(12,20))
        self.add_contour('bell','dome-left','dome-right','side-right','flare-right','lip','flare-left','side-left',closed=True)
        self.add_line('knob',(24,4),(24,8))
        self.relate('connect','bell','knob')
        self.add_line('clapper',(22,44),(26,44))
