'Location pin above ground: smooth symmetric teardrop and a clear five-unit ink gap.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd10f1e5a-a22b-515b-9731-8a58e4e155be'
SOURCE_PATH = 'pictographic-primitives/interface-essential/pin_d10f1e5a-a22b-515b-9731-8a58e4e155be.svg'
AUTHOR = 'gpt-6'

class PinD10f1e5a(Solo48):
    icon_id = 'pin-d10f1e5a'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'primitives')
    aliases = ()
    keywords = ('pin', 'interface-essential')

    def build(self) -> None:
        # The shortened lower point reserves a real gap above the separate ground line.
        self.add_arc('dome',(8,20),(40,20),radius_x=16)
        self.add_bezier('right',(40,20),((40,27),(30,32),(24,35)))
        self.add_bezier('left',(24,35),((18,32),(8,27),(8,20)))
        self.add_contour('pin','dome','right','left',closed=True)
        self.add_line('ground',(9,44),(39,44))
