"""refresh: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '2fd1c079-cf3a-416d-9512-f7ec606bfef0'
SOURCE_PATH = 'pictographic-primitives/interface-essential/refresh_2fd1c079-cf3a-416d-9512-f7ec606bfef0.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class Refresh(Solo48):
    icon_id = 'refresh'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    aliases = ()
    keywords = ('refresh', 'interface-essential')

    def build(self):
        # Plan: SQUARE; continuous circular lower turn and smooth transition into arrowhead.
        # Reference: Lucide undo-2: circle-to-curve tangency.
        self.add_arc('lower',(42,24),(6,24),radius_x=18)
        self.add_arc('upper-left',(6,24),(24,6),radius_x=18)
        self.add_bezier('upper-right',(24,6),((31,6),(35,10),(40,16)))
        self.add_contour('turn','lower','upper-left','upper-right')
        self.add_polyline('head',(40,6),(40,16),(30,16))
        self.relate('connect','head','turn')
