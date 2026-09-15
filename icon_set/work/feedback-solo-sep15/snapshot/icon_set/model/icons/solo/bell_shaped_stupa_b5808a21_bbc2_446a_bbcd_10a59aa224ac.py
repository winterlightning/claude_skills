"""Tapered finial over a rounded bell body and broad plinth. Lucide bell informs the coherent silhouette; thin stepped collars omitted."""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b5808a21-bbc2-446a-bbcd-10a59aa224ac'
SOURCE_PATH = 'pictographic-primitives/landmarks/batch-05/wat phra kaew_b5808a21-bbc2-446a-bbcd-10a59aa224ac.svg'
AUTHOR = 'gpt-6'

class BellShapedStupa(Solo48):
    icon_id = 'bell-shaped-stupa'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/landmarks'
    aliases = ()
    keywords = ('wat phra kaew', 'stupa', 'chedi', 'thailand', 'temple', 'buddhist', 'landmark', 'religion')

    def build(self) -> None:
        # Height repair: exact SOLO48 keyshape extremes; original subject and stroke retained.
        self.add_line('finial-1', (17, 18), (24, 4))
        self.add_line('finial-2', (24, 4), (31, 18))
        self.add_arc('bell-right', (31, 18), (37, 34), radius_x=6, radius_y=16)
        self.add_line('base', (37, 34), (11, 34))
        self.add_arc('bell-left', (11, 34), (17, 18), radius_x=6, radius_y=16)
        self.add_contour('body', 'finial-1', 'finial-2', 'bell-right', 'base', 'bell-left', closed=True)
        self.add_line('plinth', (8, 44), (40, 44))
