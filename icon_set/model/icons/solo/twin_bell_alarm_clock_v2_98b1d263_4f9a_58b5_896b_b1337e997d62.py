# Variant of twin-bell-alarm-clock; parent file remains unchanged.
"""Twin-bell alarm clock with bells moved inward and slightly reduced for clearance. VRECT_L matches the narrower silhouette; Lucide alarm-clock informs mirrored placement."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '98b1d263-4f9a-58b5-896b-b1337e997d62'
SOURCE_PATH = 'pictographic-primitives/decoration/batch-02/decoration clock retro_98b1d263-4f9a-58b5-896b-b1337e997d62.svg'
AUTHOR = 'gpt-6'

class TwinBellAlarmClockVariant2(Solo48):
    icon_id = 'twin-bell-alarm-clock-v2'
    variant_of = 'twin-bell-alarm-clock'
    variant_label = 'Bells closer together'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/decoration'
    aliases = ()
    keywords = ('clock', 'alarm', 'bells', 'time', 'retro', 'round', 'feet')

    def build(self) -> None:
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
        self.add_arc('bell-left', (8, 7), (18, 7), radius_x=5, radius_y=5, sweep=True)
        self.add_arc('bell-right', (30, 7), (40, 7), radius_x=5, radius_y=5, sweep=True)
