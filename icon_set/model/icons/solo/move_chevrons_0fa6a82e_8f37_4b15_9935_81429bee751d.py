"""Four outward chevrons around an open center. SQUARE extremes (6,6)-(42,42). Lucide move informs orthogonal directions and matched chevrons; retain the source empty center and omit shafts absent from it."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0fa6a82e-8f37-4b15-9935-81429bee751d'
SOURCE_PATH = 'pictographic-primitives/symbol/move arrows_0fa6a82e-8f37-4b15-9935-81429bee751d.svg'
AUTHOR = 'gpt-6'


class MoveChevrons(Solo48):
    icon_id = 'move-chevrons'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('move', 'drag', 'pan', 'chevrons', 'directions', 'arrows', 'position', 'navigate')

    def build(self) -> None:
        self.add_polyline('up',(18,12),(24,6),(30,12))
        self.add_polyline('right',(36,18),(42,24),(36,30))
        self.add_polyline('down',(30,36),(24,42),(18,36))
        self.add_polyline('left',(12,30),(6,24),(12,18))
