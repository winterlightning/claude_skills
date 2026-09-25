"""Partying Face; independently reconstructed on SOLO48."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dd0fa843-2d46-4121-8643-23b3e856a3bb'
SOURCE_PATH = 'pictographic-primitives/smileys/partying face celebrate_dd0fa843-2d46-4121-8643-23b3e856a3bb.svg'
AUTHOR = 'gpt-6'


class PartyingFace(Solo48):
    icon_id = 'partying-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    aliases = ()
    keywords = ('party', 'celebrate', 'hat', 'blower', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE: leaning hat and rightward curled blower define the costume.
        self.add_polyline("hat",(6,6),(24,12),(9,27),closed=True)
        self.add_arc("head-upper",(24,12),(36,18),radius_x=15)
        self.add_arc("head-lower",(24,42),(9,27),radius_x=15)
        self.relate("connect","head-upper","hat-1")
        self.relate("connect","head-upper","hat-2")
        self.relate("connect","head-lower","hat-2")
        self.relate("connect","head-lower","hat-3")
        self.add_arc("eye",(25,24),(29,24),radius_x=2)
        self.add_line("blower",(24,33),(36,33))
        self.add_arc("blower-curl",(36,33),(42,27),radius_x=6,sweep=False)
        self.add_contour("party-blower","blower","blower-curl")
