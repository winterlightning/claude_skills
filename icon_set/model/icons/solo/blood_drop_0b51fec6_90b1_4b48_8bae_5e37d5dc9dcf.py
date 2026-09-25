"""An upright liquid drop with a pointed crown and smoothly joined rounded bowl; VRECT extremes (8,4)-(40,44).
Reduction: None.
Lucide construction: droplet
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '0b51fec6-90b1-4b48-8bae-5e37d5dc9dcf'
SOURCE_PATH = 'pictographic-primitives/nature/blood drop_0b51fec6-90b1-4b48-8bae-5e37d5dc9dcf.svg'
AUTHOR = 'gpt-6'


class BloodDrop(Solo48):
    icon_id = 'blood-drop'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    aliases = ()
    keywords = ('drop', 'blood', 'liquid', 'water', 'donation', 'teardrop', 'fluid', 'nature')

    def build(self) -> None:
        # The lower ellipse and two circular shoulders share vertical tangents.
        tip, left, right = (24,4), (8,32), (40,32)
        self.add_line("upper-left", tip, (12,20))
        self.add_arc("shoulder-left", (12,20), left, radius_x=20, sweep=False)
        self.add_arc("base-left", left, (24,44), radius_x=16, radius_y=12, sweep=False)
        self.add_arc("base-right", (24,44), right, radius_x=16, radius_y=12, sweep=False)
        self.add_arc("shoulder-right", right, (36,20), radius_x=20, sweep=False)
        self.add_line("upper-right", (36,20), tip)
        self.add_contour("drop", "upper-left", "shoulder-left", "base-left", "base-right", "shoulder-right", "upper-right", closed=True)
        self.add_line("highlight", (29,29), (26,33))
