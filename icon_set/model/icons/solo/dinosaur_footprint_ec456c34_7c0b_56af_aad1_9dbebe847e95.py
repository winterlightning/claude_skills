"""A three-toed dinosaur track with a broad rounded heel."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ec456c34-7c0b-56af-aad1-9dbebe847e95'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur footprint_ec456c34-7c0b-56af-aad1-9dbebe847e95.svg'
AUTHOR = 'gpt-6'


class DinosaurFootprint(Solo48):
    icon_id = 'dinosaur-footprint'
    keyshape = Keyshape.VRECT_XL
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('dinosaur', 'footprint', 'track', 'claw', 'three-toed', 'prehistoric', 'trace', 'fossil')

    def build(self) -> None:
        # Centerline extremes: (5,2)-(43,46).
        self.add_line("toes-1",(11,32),(5,10))
        self.add_line("toes-2",(5,10),(17,22))
        self.add_line("toes-3",(17,22),(24,2))
        self.add_line("toes-4",(24,2),(31,22))
        self.add_line("toes-5",(31,22),(43,10))
        self.add_line("toes-6",(43,10),(37,32))
        self.add_arc("heel-right",(37,32),(24,46),radius_x=13,radius_y=14)
        self.add_arc("heel-left",(24,46),(11,32),radius_x=13,radius_y=14)
        self.add_contour("track",*["toes-"+str(i) for i in range(1,7)],"heel-right","heel-left",closed=True)
