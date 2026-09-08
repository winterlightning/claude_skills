"""Three-column temple facade and two steps. SQUARE (2,2)-(46,46). Lucide landmark: triangular pediment, single-stroke columns, open base rules. Removed entablature thickness."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cc11abce-7a28-4b1e-a5ae-362666f2e1a0'
SOURCE_PATH = 'pictographic-primitives/culture/batch-02/greek building_cc11abce-7a28-4b1e-a5ae-362666f2e1a0.svg'


class ClassicalTempleFacade(Solo48):
    icon_id = 'classical-temple-facade'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('temple', 'greek', 'classical', 'architecture', 'parthenon', 'columns', 'museum', 'antiquity')

    def build(self) -> None:
        self.add_polyline('pediment', (2,16), (24,2), (46,16), closed=True)
        self.add_line('column-left', (10,24), (10,38))
        self.add_line('column-middle', (24,24), (24,38))
        self.add_line('column-right', (38,24), (38,38))
        self.add_polyline('upper-step', (6,38), (10,38), (24,38), (38,38), (42,38))
        self.add_line('lower-step', (2,46), (46,46))
        for name in ('column-left','column-middle','column-right'):
            self.relate('connect', name, 'upper-step')
