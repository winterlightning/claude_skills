# Variant of curved-monitor; parent file remains unchanged.
'Continuous screen curves. Independent feedback revision; preserve source subject.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '588496c1-7ce3-521d-af0b-e0c4cec28e66'
SOURCE_PATH = 'pictographic-primitives/computers/batch-04/screen curved_588496c1-7ce3-521d-af0b-e0c4cec28e66.svg'
AUTHOR = 'gpt-6'

class CurvedMonitorVariant2(Solo48):
    icon_id = 'curved-monitor-v2'
    variant_of = 'curved-monitor'
    variant_label = 'Continuous screen curves'
    keyshape = Keyshape.HRECT_XL
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/device'
    aliases = ()
    keywords = ('monitor', 'curved', 'screen', 'display', 'widescreen', 'gaming', 'computer', 'ultrawide')

    def build(self) -> None:
        # HRECT_XL centerline extremes (2,5)-(46,43).
        self.add_arc('top', (2,5), (46,5), radius_x=62, sweep=False)
        self.add_line('right', (46,5), (46,31))
        self.add_arc('bottom-right', (46,31), (24,35), radius_x=22, radius_y=4)
        self.add_arc('bottom-left', (24,35), (2,31), radius_x=22, radius_y=4)
        self.add_line('left', (2,31), (2,5))
        self.add_contour('screen','top','right','bottom-right','bottom-left','left',closed=True)
        self.add_line('stem',(24,35),(24,43))
        self.add_polyline('base',(12,43),(24,43),(36,43))
        self.relate('connect','screen','stem')
        self.relate('connect','stem','base')
