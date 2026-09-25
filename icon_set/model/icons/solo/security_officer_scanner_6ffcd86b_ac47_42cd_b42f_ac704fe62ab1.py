'Security scanner: straight, symmetric portal with an 8-unit header.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6ffcd86b-ac47-42cd-b42f-ac704fe62ab1'
SOURCE_PATH = 'pictographic-primitives/travel/security officer scanner_6ffcd86b-ac47-42cd-b42f-ac704fe62ab1.svg'
AUTHOR = 'gpt-6'

class SecurityOfficerScanner(Solo48):
    icon_id = 'security-officer-scanner'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    categories = ('travel', 'primitives')
    aliases = ()
    keywords = ('security', 'officer', 'scanner', 'travel')

    def build(self):
        # Security scanner: straight, symmetric portal with an 8-unit header.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('scanner',(8,44),(8,4),(40,4),(40,44))
        l('header',(8,12),(40,12))
        link('connect','header','scanner')
