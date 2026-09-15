from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '05e30020-6fa9-5a1b-bf6d-2af10d819bed'
SOURCE_PATH = 'pictographic-primitives/animals/shell_05e30020-6fa9-5a1b-bf6d-2af10d819bed.svg'
AUTHOR = 'gpt-6'


class ScallopShell(Solo48):
    icon_id = 'scallop-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('shell', 'scallop', 'seashell', 'beach', 'ocean', 'ribs', 'marine', 'fan')

    def build(self) -> None:
        self.add_arc('crown',(16,15),(32,15),radius_x=8,radius_y=9)
        self.add_bezier('right',(32,15),((38,15),(42,19),(42,24)),((42,29),(31,35),(28,39)))
        self.add_bezier('hinge',(28,39),((25,43),(23,43),(20,39)))
        self.add_bezier('left',(20,39),((17,35),(6,29),(6,24)),((6,19),(10,15),(16,15)))
        self.add_contour('shell','crown','right','hinge','left',closed=True)
        self.add_line('rib-left',(16,15),(19,30))
        self.add_line('rib-right',(32,15),(29,30))
        self.relate('connect','rib-left','shell')
        self.relate('connect','rib-right','shell')
