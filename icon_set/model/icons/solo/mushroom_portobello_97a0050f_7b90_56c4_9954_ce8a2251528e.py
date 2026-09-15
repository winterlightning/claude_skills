"""mushroom-portobello: geometric reconstruction on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '97a0050f-7b90-56c4-9954-ce8a2251528e'
SOURCE_PATH = 'pictographic-primitives/food/mushroom portobello_97a0050f-7b90-56c4-9954-ce8a2251528e.svg'
AUTHOR = 'gpt-6'
ORIGINAL_AUTHOR = 'json_to_solo'
REVIEWED_BY = 'gpt-6'
REVIEW_ACTION = 'geometry-reconstructed'

class MushroomPortobello(Solo48):
    icon_id = 'mushroom-portobello'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'food'
    aliases = ()
    keywords = ('mushroom', 'portobello', 'food')

    def build(self):
        # Plan: HRECT_L; symmetric elliptical cap and smoothly mirrored stem.
        # Reference: Geometric dome; retain the source mushroom silhouette.
        self.add_arc('cap',(4,26),(44,26),radius_x=20,radius_y=18)
        self.add_bezier('underside-right',(44,26),((39,26),(35,24),(30,24)))
        self.add_line('underside-middle',(30,24),(18,24))
        self.add_bezier('underside-left',(18,24),((13,24),(9,26),(4,26)))
        self.add_contour('cap-outline','cap','underside-right','underside-middle','underside-left',closed=True)
        self.add_bezier('stem',(18,24),((17,32),(18,40),(24,40)),((30,40),(31,32),(30,24)))
        self.relate('connect','stem','cap-outline')
