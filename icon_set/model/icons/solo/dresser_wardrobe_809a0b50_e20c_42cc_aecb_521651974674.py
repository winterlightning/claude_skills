'Wardrobe: symmetric doors and handles, with consistent clearance from the centre seam.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '809a0b50-e20c-42cc-aecb-521651974674'
SOURCE_PATH = 'pictographic-primitives/furnitures/dresser wardrobe_809a0b50-e20c-42cc-aecb-521651974674.svg'
AUTHOR = 'gpt-6'

class DresserWardrobe(Solo48):
    icon_id = 'dresser-wardrobe'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'furnitures'
    aliases = ()
    keywords = ('dresser', 'wardrobe', 'furnitures')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('cabinet-1', (6, 38), (6, 6))
        self.add_line('cabinet-2', (6, 6), (42, 6))
        self.add_line('cabinet-3', (42, 6), (42, 38))
        self.add_line('cabinet-4', (42, 38), (6, 38))
        self.add_line('seam', (24, 6), (24, 38))
        self.add_line('handle-15', (15, 20), (15, 24))
        self.add_line('handle-33', (33, 20), (33, 24))
        self.add_line('foot-10', (10, 38), (10, 42))
        self.add_line('foot-38', (38, 38), (38, 42))
        self.add_contour('cabinet', *('cabinet-1', 'cabinet-2', 'cabinet-3', 'cabinet-4'), closed=False)
        self.relate('connect', *('seam', 'cabinet'))
        self.relate('connect', *('foot-10', 'cabinet'))
        self.relate('connect', *('foot-38', 'cabinet'))
