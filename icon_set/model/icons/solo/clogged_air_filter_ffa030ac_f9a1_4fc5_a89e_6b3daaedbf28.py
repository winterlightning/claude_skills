"""Clogged Air Filter, rebuilt from the supplied reference on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ffa030ac-f9a1-4fc5-a89e-6b3daaedbf28'
SOURCE_PATH = 'pictographic-primitives/transportation/clogged air filter_ffa030ac-f9a1-4fc5-a89e-6b3daaedbf28.svg'
AUTHOR = 'gpt-6'

class CloggedAirFilter(Solo48):
    icon_id = 'clogged-air-filter'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    categories = ("transportation", "primitives")
    aliases = ()
    keywords = ('air filter', 'clogged', 'filter', 'engine', 'warning', 'dashboard', 'car', 'maintenance')

    def build(self) -> None:
        # SQUARE: current contract centerline extremes (6, 6)-(42, 42).
        # Four identical shallow flow waves, with an intrinsic blockage across the inner pair.
        for i,x in enumerate((8,18,30,40)):
            self.add_arc(f'flow-{i}-a1',(x,6),(x-2,11),radius_x=2,radius_y=5)
            self.add_arc(f'flow-{i}-a2',(x-2,11),(x,16),radius_x=2,radius_y=5,sweep=False)
            self.add_line(f'flow-{i}-b',(x,16),(x,20))
            self.add_line(f'flow-{i}-c',(x,20),(x,28))
            self.add_line(f'flow-{i}-d',(x,28),(x,32))
            self.add_arc(f'flow-{i}-e1',(x,32),(x+2,37),radius_x=2,radius_y=5,sweep=False)
            self.add_arc(f'flow-{i}-e2',(x+2,37),(x,42),radius_x=2,radius_y=5)
            self.add_contour(f'flow-{i}',*[f'flow-{i}-{s}' for s in ('a1','a2','b','c','d','e1','e2')])
        for y in (20,28):
            self.add_line(f'blockage-{y}',(18,y),(30,y))
            for i in (1,2): self.relate('connect',f'blockage-{y}',f'flow-{i}')
