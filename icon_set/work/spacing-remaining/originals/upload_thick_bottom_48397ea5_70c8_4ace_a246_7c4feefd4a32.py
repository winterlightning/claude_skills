'Upload tray: symmetric arrow with a spacious shaft and 10-unit tray clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48397ea5-70c8-4ace-a246-7c4feefd4a32'
SOURCE_PATH = 'icons-json/arrows/upload thick bottom_48397ea5-70c8-4ace-a246-7c4feefd4a32.json'
AUTHOR = 'gpt-6'

class UploadThickBottom(Solo48):
    icon_id = 'upload-thick-bottom'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('upload', 'thick', 'bottom', 'arrows')

    def build(self):
        # Upload tray: symmetric arrow with a spacious shaft and 10-unit tray clearance.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('arrow',(18,30),(18,20),(10,20),(24,8),(38,20),(30,20),(30,30),(18,30))
        p('tray',(4,32),(4,40),(44,40),(44,32))
