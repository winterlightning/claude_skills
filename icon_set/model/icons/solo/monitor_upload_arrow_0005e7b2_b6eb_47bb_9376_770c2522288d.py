"""A desktop monitor contains an upward upload arrow.

Keyshape HRECT_XL: visible extremes (0, 3, 48, 45).
Lucide monitor: equal corner radii and centered post; source supplies the arrow. Wide keyshape gives the arrow breathing room. No semantic parts dropped."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0005e7b2-b6eb-47bb-9376-770c2522288d'
SOURCE_PATH = 'pictographic-primitives/computers/batch-06/monitor upload_0005e7b2-b6eb-47bb-9376-770c2522288d.svg'
AUTHOR = 'astra-chatgpt'


class MonitorUploadArrow(Solo48):
    icon_id = 'monitor-upload-arrow'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('monitor', 'upload', 'arrow', 'screen', 'computer', 'transfer', 'send', 'up')

    def build(self) -> None:
        self.add_line('screen-top0', (6, 5), (42, 5))
        self.add_arc('screen-ne', (42, 5), (46, 9), radius_x=4, sweep=True)
        self.add_line('screen-right', (46, 9), (46, 29))
        self.add_arc('screen-se', (46, 29), (42, 33), radius_x=4, sweep=True)
        self.add_line('screen-bottom0', (42, 33), (24, 33))
        self.add_line('screen-bottom1', (24, 33), (6, 33))
        self.add_arc('screen-sw', (6, 33), (2, 29), radius_x=4, sweep=True)
        self.add_line('screen-left', (2, 29), (2, 9))
        self.add_arc('screen-nw', (2, 9), (6, 5), radius_x=4, sweep=True)
        self.add_contour('screen', 'screen-top0', 'screen-ne', 'screen-right', 'screen-se', 'screen-bottom0', 'screen-bottom1', 'screen-sw', 'screen-left', 'screen-nw', closed=True)
        self.add_line('stand', (24, 33), (24, 43))
        self.add_polyline('foot', (15, 43), (24, 43), (33, 43), closed=False)
        self.relate("connect", 'screen', 'stand')
        self.relate("connect", 'stand', 'foot')
        self.add_polyline('arrowhead', (17, 20), (24, 13), (31, 20), closed=False)
        self.add_line('shaft', (24, 13), (24, 26))
        self.relate("connect", 'arrowhead', 'shaft')
