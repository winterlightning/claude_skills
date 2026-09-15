"""Right-facing bucket seat with leaning backrest and rounded cushion. Lucide armchair informs coherent upholstery contours; no exact side-view match. No structural features omitted.

SOLO48 SQUARE; live visible envelope (4, 4, 44, 44).
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0d65c65-f181-4b40-b0ec-6cdf61983966'
SOURCE_PATH = 'pictographic-primitives/symbol/seat car_a0d65c65-f181-4b40-b0ec-6cdf61983966.svg'
AUTHOR = 'gpt-6'


class CarSeat(Solo48):
    icon_id = 'car-seat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('seat', 'car-seat', 'chair', 'vehicle', 'interior', 'passenger', 'driver', 'automotive')

    def build(self) -> None:

        self.add_arc('back-top',(6,10),(14,10),radius_x=4)
        self.add_line('back-inner',(14,10),(20,26))
        self.add_arc('seat-transition',(20,26),(32,32),radius_x=12,radius_y=6,sweep=False)
        self.add_line('cushion-top',(32,32),(36,32))
        self.add_arc('cushion-front',(36,32),(36,42),radius_x=6,radius_y=5)
        self.add_line('cushion-bottom',(36,42),(22,42))
        self.add_arc('back-bottom',(22,42),(6,26),radius_x=16)
        self.add_line('back-outer',(6,26),(6,10))
        self.add_contour('seat','back-top','back-inner','seat-transition','cushion-top','cushion-front','cushion-bottom','back-bottom','back-outer',closed=True)
