"""warp-fish: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cf262ac0-6a03-43ea-a2f5-d9b248545818'
SOURCE_PATH = 'pictographic-primitives/design/warp fish_cf262ac0-6a03-43ea-a2f5-d9b248545818.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class WarpFish(Solo48):
    icon_id = 'warp-fish'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('warp', 'fish', 'design')

    def build(self):
        # Plan: HRECT_L; mirrored neck and rounded left mass; preserve the fish warp silhouette.
        # Reference: Geometric mirrored cubic construction.
        self.add_bezier('upper-left',(4,24),((4,15),(10,8),(18,8)))
        self.add_bezier('upper-neck',(18,8),((27,8),(28,20),(35,20)),((39,20),(42,16),(44,12)))
        self.add_line('tail',(44,12),(44,36))
        self.add_bezier('lower-neck',(44,36),((42,32),(39,28),(35,28)),((28,28),(27,40),(18,40)))
        self.add_bezier('lower-left',(18,40),((10,40),(4,33),(4,24)))
        self.add_contour('outline','upper-left','upper-neck','tail','lower-neck','lower-left',closed=True)
