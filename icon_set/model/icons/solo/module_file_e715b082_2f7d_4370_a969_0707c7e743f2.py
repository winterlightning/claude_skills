"""module file: complete SOLO48 repair.
Retained the clipped document corner and three square modules. Joined the modules along common edges instead of squeezing three separate outlines.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e715b082-2f7d-4370-a969-0707c7e743f2'
SOURCE_PATH = 'pictographic-primitives/other/module file_e715b082-2f7d-4370-a969-0707c7e743f2.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'module-file'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('module', 'file')


    def build(self):
        self.add_polyline('document',(8,4),(30,4),(40,14),(40,44),(8,44),closed=True)
        self.add_polyline('modules',(20,18),(28,18),(28,26),(32,26),(32,34),(24,34),(16,34),(16,26),(20,26),closed=True)
        self.add_line('vertical',(24,26),(24,34))
        self.add_polyline('horizontal',(20,26),(24,26),(28,26))
        self.relate('connect','modules','vertical')
        self.relate('connect','modules','horizontal')
        self.relate('connect','horizontal','vertical')
