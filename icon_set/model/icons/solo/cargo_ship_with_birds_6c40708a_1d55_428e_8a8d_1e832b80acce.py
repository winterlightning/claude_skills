"""cargo-ship-with-birds: reconstructed from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6c40708a-1d55-428e-8a8d-1e832b80acce'
SOURCE_PATH = 'pictographic-primitives/transportation/ship cargo birds_6c40708a-1d55-428e-8a8d-1e832b80acce.svg'
AUTHOR = 'gpt-6'


class CargoShipWithBirds(Solo48):
    icon_id = 'cargo-ship-with-birds'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('cargo ship', 'ship', 'freighter', 'birds', 'sea', 'harbour', 'vessel', 'shipping')

    def build(self) -> None:

        self.add_polyline('hull',(6,30),(10,30),(20,30),(30,30),(40,30),(42,30),(36,42),(12,42),(6,30))
        self.add_polyline('bridge',(10,30),(10,16),(20,16),(20,30))
        self.add_polyline('funnel',(30,30),(30,22),(40,22),(40,30))
        for a,bs in [('bridge-1',['hull-1','hull-2']),('bridge-3',['hull-2','hull-3']),('funnel-1',['hull-3','hull-4']),('funnel-3',['hull-4','hull-5'])]:
            for b in bs: self.relate('connect',a,b)
        self.add_polyline('bird',(24,6),(28,9),(32,6))
        self.add_polyline('bird-far',(38,12),(40,14),(42,12))
