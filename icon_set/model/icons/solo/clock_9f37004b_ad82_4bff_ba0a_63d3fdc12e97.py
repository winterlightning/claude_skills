'Clock: concentric circular rim and joined hands centered at (24,24). Lucide clock informs clear, restrained hand lengths.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f37004b-ad82-4bff-ba0a-63d3fdc12e97'
SOURCE_PATH = 'pictographic-primitives/office/clock_9f37004b-ad82-4bff-ba0a-63d3fdc12e97.svg'
AUTHOR = 'gpt-6'

class Clock9f37004b(Solo48):
    icon_id = 'clock-9f37004b'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    categories = ('office', 'primitives')
    aliases = ()
    keywords = ('clock', 'office')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_polyline('hands',(24,13),(24,24),(31,24))
