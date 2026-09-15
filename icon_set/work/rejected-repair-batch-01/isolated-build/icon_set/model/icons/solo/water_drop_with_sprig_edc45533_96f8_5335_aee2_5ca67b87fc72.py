"""An upright liquid drop with a pointed crown and smoothly joined rounded bowl; VRECT extremes (8,4)-(40,44). Its own planted sprig is reduced to one pair of shoots.
Reduction: Removed the curved ground line and secondary branches to keep the plant open.
Lucide construction: droplet
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'edc45533-96f8-5335-aee2-5ca67b87fc72'
SOURCE_PATH = 'pictographic-primitives/nature/aquascaping_edc45533-96f8-5335-aee2-5ca67b87fc72.svg'
AUTHOR = 'gpt-6'


class WaterDropWithSprig(Solo48):
    icon_id = 'water-drop-with-sprig'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/batch-01"
    aliases = ()
    keywords = ('aquascaping', 'water', 'drop', 'plant', 'sprig', 'aquarium', 'nature', 'ecology')

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
        self.add_line("stem-upper", (24,21), (24,31))
        self.add_line("stem-lower", (24,31), (24,35))
        for side,x in (("left",19),("right",29)):
            self.add_line(side+"-shoot", (x,25), (24,31))
            self.relate("connect", side+"-shoot", "stem-upper")
            self.relate("connect", side+"-shoot", "stem-lower")
