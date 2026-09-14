'Clock: concentric circular rim and joined hands centered at (24,24). Lucide clock informs clear, restrained hand lengths.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '64e20f3b-99e4-4b3c-9e26-3b813a564c12'
SOURCE_PATH = 'icons-json/office/clock_64e20f3b-99e4-4b3c-9e26-3b813a564c12.json'
AUTHOR = 'gpt-6'

class Clock64e20f3b(Solo48):
    icon_id = 'clock-64e20f3b'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'office'
    aliases = ()
    keywords = ('clock', 'office')

    def build(self) -> None:
        self.add_arc('rim-top', (4,24), (44,24), radius_x=20, radius_y=20)
        self.add_arc('rim-bottom', (44,24), (4,24), radius_x=20, radius_y=20)
        self.add_contour('rim', 'rim-top', 'rim-bottom', closed=True)
        self.add_polyline('hands',(24,13),(24,24),(31,24))
