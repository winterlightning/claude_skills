'Skull: mirrored smooth dome and cheek transitions replace the polygonal trace, retaining the open jaw and original facial marks.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7b01deac-dd2c-4265-92f5-d17735f0c07e'
SOURCE_PATH = 'pictographic-primitives/interface-essential/skull_7b01deac-dd2c-4265-92f5-d17735f0c07e.svg'
AUTHOR = 'gpt-6'

class Skull(Solo48):
    icon_id = 'skull'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'interface-essential'
    categories = ('interface-essential', 'other', 'primitives-generate')
    aliases = ()
    keywords = ('skull', 'interface-essential')

    def build(self) -> None:
        # Lucide skull: smooth cranial dome and softened cheek-to-jaw transition.
        # Open lower jaw and small eyes preserve this original variant.
        self.add_bezier('left',(14,44),((14,41),(14,39),(12,35)),((10,31),(8,29),(8,22)),((8,12),(14,4),(24,4)))
        self.add_bezier('right',(24,4),((34,4),(40,12),(40,22)),((40,29),(38,31),(36,35)),((34,39),(34,41),(34,44)))
        self.add_contour('outline','left','right')
        self.add_line('tooth',(24,44),(24,39))
        self.add_dot('eye-left',(17,21))
        self.add_dot('eye-right',(31,21))
