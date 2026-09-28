'Upload arrow: centered arrowhead and shaft; detached dashes retain 8-unit spacing.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1642e1b5-838a-47dc-b8bc-bf1bcffb0f3f'
SOURCE_PATH = 'pictographic-primitives/arrows/upload dash arrow_1642e1b5-838a-47dc-b8bc-bf1bcffb0f3f.svg'
AUTHOR = 'gpt-6'

class UploadDashArrow(Solo48):
    icon_id = 'upload-dash-arrow'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('upload', 'dash', 'arrow', 'arrows')

    def build(self) -> None:
        # Symbol plan: preserve the subject, contour topology and curve types.
        # Rebalance whole parts on the SOLO48 integer grid; keep real shared contacts.
        self.add_line('arrow-1', (16, 34), (16, 18))
        self.add_line('arrow-2', (16, 18), (8, 18))
        self.add_line('arrow-3', (8, 18), (24, 4))
        self.add_line('arrow-4', (24, 4), (40, 18))
        self.add_line('arrow-5', (40, 18), (32, 18))
        self.add_line('arrow-6', (32, 18), (32, 34))
        self.add_line('dash-16', (16, 42), (16, 44))
        self.add_line('dash-32', (32, 42), (32, 44))
        self.add_contour('arrow', *('arrow-1', 'arrow-2', 'arrow-3', 'arrow-4', 'arrow-5', 'arrow-6'), closed=False)
