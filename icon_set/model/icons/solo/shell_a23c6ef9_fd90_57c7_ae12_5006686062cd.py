from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a23c6ef9-fd90-57c7-ae12-5006686062cd'
SOURCE_PATH = 'pictographic-primitives/animals/shell_a23c6ef9-fd90-57c7-ae12-5006686062cd.svg'
AUTHOR = 'gpt-6'


class ClamShell(Solo48):
    icon_id = 'clam-shell'
    keyshape = Keyshape.HRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals/marine"
    aliases = ()
    keywords = ('shell', 'clam', 'mussel', 'oyster', 'sea', 'beach', 'bivalve', 'marine')

    def build(self) -> None:
        self.add_arc('top-left', (2, 24), (14, 5), radius_x=12, radius_y=19, sweep=True, large_arc=False)
        self.add_arc('top-right', (14, 5), (46, 24), radius_x=32, radius_y=19, sweep=True, large_arc=False)
        self.add_arc('bottom-right', (46, 24), (14, 43), radius_x=32, radius_y=19, sweep=True, large_arc=False)
        self.add_arc('bottom-left', (14, 43), (2, 24), radius_x=12, radius_y=19, sweep=True, large_arc=False)
        self.add_contour('shell', 'top-left', 'top-right', 'bottom-right', 'bottom-left', closed=True)
        self.add_line('valve-1', (10, 10), (36, 24))
        self.add_line('valve-2', (36, 24), (10, 38))
        self.add_contour('valve', 'valve-1', 'valve-2', closed=False)
        self.relate("connect", 'valve', 'shell')
        self.add_line('hinge', (2, 24), (26, 24))
        self.relate("connect", 'hinge', 'shell')
