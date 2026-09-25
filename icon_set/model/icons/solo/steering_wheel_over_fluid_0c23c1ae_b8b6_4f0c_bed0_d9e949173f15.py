"""Steering wheel over fluid; independently authored on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0c23c1ae-b8b6-4f0c-bed0-d9e949173f15'
SOURCE_PATH = 'pictographic-primitives/transportation/power steering wheel fluid_0c23c1ae-b8b6-4f0c-bed0-d9e949173f15.svg'
AUTHOR = 'gpt-6'
SOURCE_REFERENCES = [{'SOURCE_ICON_ID': '0c23c1ae-b8b6-4f0c-bed0-d9e949173f15', 'SOURCE_PATH': 'pictographic-primitives/transportation/power steering wheel fluid_0c23c1ae-b8b6-4f0c-bed0-d9e949173f15.svg', 'AUTHOR': 'gpt-6'}]

class SteeringWheelOverFluid(Solo48):
    icon_id = 'steering-wheel-over-fluid'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'transportation'
    aliases = ()
    keywords = ('steering', 'wheel', 'over', 'fluid')

    def build(self) -> None:
        # SQUARE (6,6)-(42,42). Radius-12 steering rim over one coherent wave.
        for name,a,b in [('top-left',(12,18),(24,6)),('top-right',(24,6),(36,18)),('bottom-right',(36,18),(24,30)),('bottom-left',(24,30),(12,18))]:
            self.add_arc('rim-'+name,a,b,radius_x=12)
        self.add_contour('rim','rim-top-left','rim-top-right','rim-bottom-right','rim-bottom-left',closed=True)
        self.add_polyline('horizontal-spokes',(12,18),(24,18),(36,18))
        self.add_line('bottom-spoke',(24,18),(24,30))
        self.relate('connect','rim','horizontal-spokes')
        self.relate('connect','rim','bottom-spoke')
        self.relate('connect','horizontal-spokes','bottom-spoke')
        for j in range(3):
            self.add_arc('water-'+str(j),(6+12*j,40),(18+12*j,40),radius_x=6,radius_y=2,sweep=j!=1)
        self.add_contour('water','water-0','water-1','water-2')
