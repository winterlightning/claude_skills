"""A sailboat with a tall curved sail over an open hull and a smooth wave. SQUARE ink (6,6)-(42,42). Lucide sailboat informed the coherent hull; the parallel deck edge and repeated wave crests are omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'b61a055f-e1d4-4f45-b688-2b287b42a5a9'
SOURCE_PATH = 'pictographic-primitives/transportation/boat_b61a055f-e1d4-4f45-b688-2b287b42a5a9.svg'
SOURCE_REFERENCES = (('b61a055f-e1d4-4f45-b688-2b287b42a5a9', 'pictographic-primitives/transportation/boat_b61a055f-e1d4-4f45-b688-2b287b42a5a9.svg'),)
AUTHOR = 'gpt-6'

class SailboatOnWaves(Solo48):
    icon_id = 'sailboat-on-waves'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/transportation'
    aliases = ()
    keywords = ('sailboat', 'boat', 'sail', 'sailing', 'waves', 'sea', 'nautical', 'yacht')

    def build(self) -> None:
        self.add_line('sail-left',(18,6),(18,22))
        self.add_line('sail-foot',(18,22),(34,22))
        self.add_arc('sail-belly',(34,22),(18,6),radius_x=16,sweep=False)
        self.add_contour('sail','sail-left','sail-foot','sail-belly',closed=True)
        self.add_polyline('hull',(6,28),(12,31),(36,31),(42,28))
        self.add_arc('wave-left',(6,41),(24,41),radius_x=15,radius_y=5)
        self.add_arc('wave-right',(24,41),(42,41),radius_x=15,radius_y=5,sweep=False)
        self.add_contour('wave','wave-left','wave-right')
