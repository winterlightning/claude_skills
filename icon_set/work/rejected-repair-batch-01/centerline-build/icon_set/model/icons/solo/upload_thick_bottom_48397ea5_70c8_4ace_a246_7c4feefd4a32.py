'Upload tray: symmetric arrow with a spacious shaft and 10-unit tray clearance.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '48397ea5-70c8-4ace-a246-7c4feefd4a32'
SOURCE_PATH = 'pictographic-primitives/arrows/upload thick bottom_48397ea5-70c8-4ace-a246-7c4feefd4a32.svg'
AUTHOR = 'gpt-6'

class UploadThickBottom(Solo48):
    icon_id = 'upload-thick-bottom'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    aliases = ()
    keywords = ('upload', 'thick', 'bottom', 'arrows')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('arrow-1', (18, 30), (18, 20))
        self.add_line('arrow-2', (18, 20), (10, 20))
        self.add_line('arrow-3', (10, 20), (24, 8))
        self.add_line('arrow-4', (24, 8), (38, 20))
        self.add_line('arrow-5', (38, 20), (30, 20))
        self.add_line('arrow-6', (30, 20), (30, 30))
        self.add_line('arrow-7', (30, 30), (18, 30))
        self.add_line('tray-1', (4, 32), (4, 40))
        self.add_line('tray-2', (4, 40), (44, 40))
        self.add_line('tray-3', (44, 40), (44, 32))
        self.add_contour('arrow', *('arrow-1', 'arrow-2', 'arrow-3', 'arrow-4', 'arrow-5', 'arrow-6', 'arrow-7'), closed=False)
        self.add_contour('tray', *('tray-1', 'tray-2', 'tray-3'), closed=False)
