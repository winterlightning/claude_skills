'Meerkat: preserve its alert upright posture while opening the head enough for a clear eye.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b4920684-b8a7-4041-8e84-67476dd1c016'
SOURCE_PATH = 'pictographic-primitives/animals/meerkat_b4920684-b8a7-4041-8e84-67476dd1c016.svg'
AUTHOR = 'gpt-6'


class Meerkat(Solo48):
    icon_id = 'meerkat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('meerkat', 'animal')

    def build(self) -> None:
        self.add_bezier('back',(6,42),((16,40),(19,39),(19,31)))
        self.add_line('neck-back',(19,31),(21,12))
        self.add_bezier('crown',(21,12),((20,7),(23,6),(28,6)))
        self.add_line('face-1',(28,6),(42,6))
        self.add_line('face-2',(42,6),(40,22))
        self.add_line('face-3',(40,22),(32,24))
        self.add_bezier('chest',(32,24),((28,27),(31,30),(33,33)),((35,37),(32,40),(31,42)))
        self.add_line('base',(31,42),(6,42))
        self.add_contour('outline','back','neck-back','crown','face-1','face-2','face-3','chest','base',closed=True)
        self.add_dot('eye',(31,15))
        self.add_line('paw',(32,24),(26,29));self.relate('connect','paw','outline')
