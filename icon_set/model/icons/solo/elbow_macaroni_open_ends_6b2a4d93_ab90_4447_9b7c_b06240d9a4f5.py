"""An elbow macaroni tube with two hollow tips and a broad U bend. HRECT_L holds the broad curved silhouette. One outer loop owns the bend and upper rims; lower rim seams meet the same endpoint nodes. Source supplies uneven ends and open rims; Lucide magnet informs the inner and outer U contours. No decorative detail added."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = '6b2a4d93-ab90-4447-9b7c-b06240d9a4f5'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_26/macaroni_6b2a4d93-ab90-4447-9b7c-b06240d9a4f5.svg'
AUTHOR = "gpt-6-astra"

class Drawing(Solo48):
    icon_id = 'elbow-macaroni-open-ends'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Curved Macaroni Tube with Open Ends',)
    keywords = ('elbow', 'macaroni', 'open', 'ends')
    def build(self):
        self.add_arc('left-rim-top',(4,12),(16,12),radius_x=6,radius_y=4,sweep=True)
        self.add_bezier('inner',(16,12),((16,30),(32,30),(32,16)))
        self.add_arc('right-rim-top',(32,16),(44,16),radius_x=6,radius_y=4,sweep=True)
        self.add_bezier('outer',(44,16),((44,29),(35,40),(24,40)),((13,40),(4,29),(4,12)))
        self.add_contour('tube','left-rim-top','inner','right-rim-top','outer',closed=True)
        self.add_arc('left-rim-bottom',(16,12),(4,12),radius_x=6,radius_y=4,sweep=True)
        self.add_arc('right-rim-bottom',(44,16),(32,16),radius_x=6,radius_y=4,sweep=True)
        self.relate('connect','left-rim-bottom','tube')
        self.relate('connect','right-rim-bottom','tube')
