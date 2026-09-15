"""specialty-heart: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '9d533cf3-02c3-46ff-a9e8-457cd11ab840'
SOURCE_PATH = 'pictographic-primitives/health/specialty heart_9d533cf3-02c3-46ff-a9e8-457cd11ab840.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class SpecialtyHeart(Solo48):
    icon_id = 'specialty-heart'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'health'
    aliases = ()
    keywords = ('specialty', 'heart', 'health')

    def build(self):
        # Plan: SQUARE; preserve tall heart proportions with mirrored smooth lobes.
        # Reference: Lucide heart: shared lobe construction.
        self.add_bezier('left-lobe',(24,12),((20,8),(17,6),(14,6)),((9,6),(6,11),(6,17)))
        self.add_bezier('left-side',(6,17),((6,26),(17,36),(24,42)))
        self.add_bezier('right-side',(24,42),((31,36),(42,26),(42,17)))
        self.add_bezier('right-lobe',(42,17),((42,11),(39,6),(34,6)),((31,6),(28,8),(24,12)))
        self.add_contour('outline','left-lobe','left-side','right-side','right-lobe',closed=True)
