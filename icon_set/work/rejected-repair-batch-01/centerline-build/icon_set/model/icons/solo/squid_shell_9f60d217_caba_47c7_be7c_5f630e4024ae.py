'Opened the spiral to nine-unit centerline spacing with tangent circular turns.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9f60d217-caba-47c7-be7c-5f630e4024ae'
SOURCE_PATH = 'pictographic-primitives/animals/squid shell_9f60d217-caba-47c7-be7c-5f630e4024ae.svg'
AUTHOR = 'gpt-6'


class NautilusShell(Solo48):
    icon_id = 'nautilus-shell'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    aliases = ()
    keywords = ('nautilus', 'shell', 'spiral', 'sea', 'marine', 'cephalopod', 'coil', 'ocean')

    def build(self) -> None:
        self.add_line('tentacle',(6,42),(6,24))
        self.add_arc('outer-tl',(6,24),(24,6),radius_x=18)
        self.add_arc('outer-tr',(24,6),(42,24),radius_x=18)
        self.add_arc('outer-br',(42,24),(24,42),radius_x=18)
        self.add_arc('coil-entry',(24,42),(15,33),radius_x=9)
        self.add_line('coil-left',(15,33),(15,24))
        self.add_arc('coil-tl',(15,24),(24,15),radius_x=9)
        self.add_arc('coil-tr',(24,15),(33,24),radius_x=9)
        self.add_arc('coil-br',(33,24),(24,33),radius_x=9)
        self.add_contour('spiral','tentacle','outer-tl','outer-tr','outer-br','coil-entry','coil-left','coil-tl','coil-tr','coil-br')
