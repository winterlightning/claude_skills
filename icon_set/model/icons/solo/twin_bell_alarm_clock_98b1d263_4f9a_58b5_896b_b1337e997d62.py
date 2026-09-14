'Alarm clock: round dial with compact hands, two equal bell curves and attached feet; keep the bells clearly separated.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '98b1d263-4f9a-58b5-896b-b1337e997d62'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/decoration clock retro_98b1d263-4f9a-58b5-896b-b1337e997d62.svg'
AUTHOR = 'gpt-6'

class TwinBellAlarmClock(Solo48):
    icon_id = 'twin-bell-alarm-clock'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('clock', 'alarm', 'bells', 'time', 'retro', 'round', 'feet')

    def build(self) -> None:
        self.add_arc('clock-top', (11,29), (37,29), radius_x=13, radius_y=13)
        self.add_arc('clock-bottom', (37,29), (11,29), radius_x=13, radius_y=13)
        self.add_contour('clock', 'clock-top', 'clock-bottom', closed=True)

        self.add_polyline('hands',(24,25),(24,29),(21,31))
        self.add_arc('bell-left',(8,8),(18,8),radius_x=5,radius_y=4)
        self.add_arc('bell-right',(30,8),(40,8),radius_x=5,radius_y=4)
        self.add_line('foot-left',(19,41),(16,44));self.add_line('foot-right',(29,41),(32,44))
        self.relate('connect','foot-left','clock');self.relate('connect','foot-right','clock')
