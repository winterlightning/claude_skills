"""Monitor with download arrow; extremes (2,5)-(46,43). Lucide monitor-down rounded case, central stand and arrow."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7adf19ee-e35e-403f-8547-7156c16131ae'
SOURCE_PATH = 'pictographic-primitives/computers/batch-05/monitor download_7adf19ee-e35e-403f-8547-7156c16131ae.svg'

class MonitorDownloadArrow(Solo48):
    icon_id = 'monitor-download-arrow'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/device"
    aliases = ()
    keywords = ('monitor', 'download', 'arrow', 'screen', 'computer', 'transfer', 'save', 'down')

    def build(self) -> None:
        self.add_line('screen-t', (6, 5), (42, 5))
        self.add_arc('screen-ne', (42, 5), (46, 9), radius_x=4, radius_y=4, sweep=True)
        self.add_line('screen-r', (46, 9), (46, 29))
        self.add_arc('screen-se', (46, 29), (42, 33), radius_x=4, radius_y=4, sweep=True)
        self.add_line('screen-b', (42, 33), (6, 33))
        self.add_arc('screen-sw', (6, 33), (2, 29), radius_x=4, radius_y=4, sweep=True)
        self.add_line('screen-l', (2, 29), (2, 9))
        self.add_arc('screen-nw', (2, 9), (6, 5), radius_x=4, radius_y=4, sweep=True)
        self.add_contour('screen', 'screen-t', 'screen-ne', 'screen-r', 'screen-se', 'screen-b', 'screen-sw', 'screen-l', 'screen-nw', closed=True)
        self.add_line('neck', (24, 33), (24, 43))
        self.add_line('foot', (15, 43), (33, 43))
        self.relate('connect', 'screen', 'neck')
        self.relate('connect', 'neck', 'foot')
        self.add_line('shaft', (24, 13), (24, 24))
        self.add_polyline('arrow', (17, 18), (24, 25), (31, 18), closed=False)
        self.relate('connect', 'shaft', 'arrow')
