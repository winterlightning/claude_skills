'A peacock feather with a dot eye. VRECT_L extremes (8,6)-(40,42) retain the tall diagonal vane and quill. The circular eye loop is replaced by one dot. Lucide feather informs the sparse vane and diagonal shaft; the diagonal pose is intentional.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'f40b6248-c81f-53b7-82f1-64f0cd1d0e22'
SOURCE_PATH = 'pictographic-primitives/animals/peacock feather_f40b6248-c81f-53b7-82f1-64f0cd1d0e22.svg'
AUTHOR = 'gpt-6'

class PeacockFeather(Solo48):
    icon_id = 'peacock-feather'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'nature/animals'
    aliases = ()
    keywords = ('peacock', 'feather')

    def build(self) -> None:
        self.add_bezier('left',(40,4),((22,4),(12,19),(12,38)))
        self.add_bezier('right',(12,38),((30,38),(40,23),(40,4)))
        self.add_contour('vane','left','right',closed=True)
        self.add_line('quill',(12,38),(8,44));self.relate('connect','quill','vane')
        self.add_dot('eye',(26,21))
