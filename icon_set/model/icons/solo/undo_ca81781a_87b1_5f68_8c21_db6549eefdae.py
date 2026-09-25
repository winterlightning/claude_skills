"""undo: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ca81781a-87b1-5f68-8c21-db6549eefdae'
SOURCE_PATH = 'pictographic-primitives/interface-essential/undo_ca81781a-87b1-5f68-8c21-db6549eefdae.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Undo(Solo48):
    icon_id = 'undo'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('undo', 'interface-essential')

    def build(self):
        # Plan: VRECT_L; a few flowing curves and a clear right-angle arrowhead.
        # Reference: Lucide undo-2: coherent turning stroke.
        self.add_polyline('head',(8,4),(8,16),(18,16))
        self.add_bezier('crest',(8,16),((12,11),(17,8),(23,8)),((33,8),(40,16),(40,27)))
        self.add_bezier('lower',(40,27),((40,34),(36,41),(30,44)))
        self.add_contour('turn','crest','lower')
        self.relate('connect','head','turn')
