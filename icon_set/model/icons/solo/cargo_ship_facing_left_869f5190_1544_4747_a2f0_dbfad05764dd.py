"""cargo-ship-facing-left: reconstructed from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '869f5190-1544-4747-a2f0-dbfad05764dd'
SOURCE_PATH = 'pictographic-primitives/transportation/ship cargo_869f5190-1544-4747-a2f0-dbfad05764dd.svg'
AUTHOR = 'gpt-6'


class CargoShipFacingLeft(Solo48):
    icon_id = 'cargo-ship-facing-left'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('cargo ship', 'container ship', 'freighter', 'ship', 'shipping', 'logistics', 'vessel', 'sea')

    def build(self) -> None:

        # Mirror the side-view vessel around x=24, including the bow and cargo heights.
        def p(x,y): return (48-x,y)
        self.add_polyline('hull',*[p(x,y) for x,y in [(4,26),(8,26),(22,26),(34,26),(44,26),(36,40),(10,40),(4,26)]])
        self.add_polyline('cargo',*[p(x,y) for x,y in [(8,26),(8,8),(22,8),(22,18),(34,18),(34,26)]])
        self.relate('connect','cargo-1','hull-1')
        self.relate('connect','cargo-1','hull-2')
        self.relate('connect','cargo-5','hull-3')
        self.relate('connect','cargo-5','hull-4')
