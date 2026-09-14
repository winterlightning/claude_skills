"""Winged Server. Authored from the supplied visual brief."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '39f46840-75df-5cb1-a454-c79203494771'
SOURCE_PATH = 'pictographic-primitives/websites/server migration wings_39f46840-75df-5cb1-a454-c79203494771.svg'
AUTHOR = 'gpt-6'

class WingedServer(Solo48):
    icon_id = 'winged-server'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/technology"
    aliases = ()
    keywords = ('server', 'wings', 'migration', 'flying', 'hardware', 'device', 'transfer')

    def build(self):
        self.add_polyline('server',(6,30),(18,18),(30,30),(18,42),closed=True)
        self.add_dot('indicator',(18,30))
        self.add_line('wing-left-root',(18,18),(18,12))
        self.add_arc('wing-left-top',(18,12),(30,6),radius_x=15)
        self.add_arc('wing-left-tip',(30,6),(25,14),radius_x=9)
        self.add_contour('wing-left','wing-left-root','wing-left-top','wing-left-tip')
        self.relate('connect','wing-left','server')
        self.add_arc('wing-right-top',(24,24),(36,12),radius_x=20)
        self.add_arc('wing-right-round',(36,12),(42,18),radius_x=6)
        self.add_arc('wing-right-tip',(42,18),(36,24),radius_x=6)
        self.add_line('wing-right-bottom-1',(36,24),(33,24))
        self.add_line('wing-right-bottom-2',(33,24),(30,30))
        self.add_contour('wing-right','wing-right-top','wing-right-round','wing-right-tip','wing-right-bottom-1','wing-right-bottom-2')
        self.relate('connect','wing-right','server')
