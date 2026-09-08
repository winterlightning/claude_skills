"""Round twin-bell alarm clock with two hands and splayed feet; bell supports and hub omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '98b1d263-4f9a-58b5-896b-b1337e997d62'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/decoration clock retro_98b1d263-4f9a-58b5-896b-b1337e997d62.svg'
AUTHOR = 'gpt-6'

class TwinBellAlarmClock(Solo48):
    icon_id = 'twin-bell-alarm-clock'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/decoration"
    aliases = ()
    keywords = ('clock', 'alarm', 'bells', 'time', 'retro', 'round', 'feet')

    def build(self) -> None:
        # SQUARE: exact SOLO48 extremes; geometry authored on the integer grid.
        self.add_arc('face-0', (24, 13), (39, 28), radius_x=15, radius_y=15, sweep=True)
        self.add_arc('face-1', (39, 28), (33, 40), radius_x=15, radius_y=15, sweep=True)
        self.add_arc('face-2', (33, 40), (24, 43), radius_x=15, radius_y=15, sweep=True)
        self.add_arc('face-3', (24, 43), (15, 40), radius_x=15, radius_y=15, sweep=True)
        self.add_arc('face-4', (15, 40), (9, 28), radius_x=15, radius_y=15, sweep=True)
        self.add_arc('face-5', (9, 28), (24, 13), radius_x=15, radius_y=15, sweep=True)
        self.add_contour('face', 'face-0', 'face-1', 'face-2', 'face-3', 'face-4', 'face-5', closed=True)
        self.add_polyline('hands', (24, 21), (24, 28), (18, 32), closed=False)
        self.add_line('left-foot', (15, 40), (12, 46))
        self.add_line('right-foot', (33, 40), (36, 46))
        self.relate('connect', 'left-foot', 'face')
        self.relate('connect', 'right-foot', 'face')
        self.add_arc('bell-left', (2, 8), (14, 8), radius_x=6, radius_y=6, sweep=True)
        self.add_arc('bell-right', (34, 8), (46, 8), radius_x=6, radius_y=6, sweep=True)
