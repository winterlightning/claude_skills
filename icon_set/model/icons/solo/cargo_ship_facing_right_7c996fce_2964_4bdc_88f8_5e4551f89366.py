"""cargo-ship-facing-right: reconstructed from the supplied transportation reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7c996fce-2964-4bdc-88f8-5e4551f89366'
SOURCE_PATH = 'pictographic-primitives/transportation/ship cargo_7c996fce-2964-4bdc-88f8-5e4551f89366.svg'
AUTHOR = 'gpt-6'


class CargoShipFacingRight(Solo48):
    icon_id = 'cargo-ship-facing-right'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "transportation"
    aliases = ()
    keywords = ('cargo ship', 'container ship', 'freighter', 'ship', 'shipping', 'logistics', 'vessel', 'sea')

    def build(self) -> None:

        # Hull owns a stepped cargo stack; all deck attachments are explicit nodes.
        self.add_polyline('hull',(6,26),(8,26),(22,26),(34,26),(42,26),(36,40),(10,40),(6,26))
        self.add_polyline('cargo',(8,26),(8,8),(22,8),(22,18),(34,18),(34,26))
        self.relate('connect','cargo-1','hull-1')
        self.relate('connect','cargo-1','hull-2')
        self.relate('connect','cargo-5','hull-3')
        self.relate('connect','cargo-5','hull-4')
