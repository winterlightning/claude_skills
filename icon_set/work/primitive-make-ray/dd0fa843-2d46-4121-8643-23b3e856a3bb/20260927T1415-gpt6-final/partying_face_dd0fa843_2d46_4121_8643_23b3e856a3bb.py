"""Partying Face; independently reconstructed on SOLO48."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'dd0fa843-2d46-4121-8643-23b3e856a3bb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__partying-face/20260927T133654Z-thuan-mac-1/reference/partying face celebrate_dd0fa843-2d46-4121-8643-23b3e856a3bb.svg'
AUTHOR = 'gpt-6'


class PartyingFace(Solo48):
    icon_id = 'partying-face'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "smileys"
    categories = ("smileys", "primitives")
    aliases = ()
    keywords = ('party', 'celebrate', 'hat', 'blower', 'face', 'emoji')

    def build(self) -> None:

        # SQUARE: leaning hat and rightward curled blower define the costume.
        self.add_polyline("hat",(6,6),(20,10),(10,20),closed=True)
        self.add_arc("head-upper",(20,10),(36,18),radius_x=16)
        self.add_bezier("head-right-upper",(36,18),((40,22),(40,28),(38,32)))
        self.add_bezier("head-right-lower",(38,32),((36,39),(31,42),(24,42)))
        self.add_arc("head-lower",(24,42),(10,20),radius_x=16)
        self.relate("connect","head-upper","hat")
        self.relate("connect","head-lower","hat")
        self.add_dot("eye-left",(20,23))
        self.add_dot("eye-right",(29,23))
        self.add_line("blower",(28,32),(38,32))
        self.add_arc("blower-curl",(38,32),(42,27),radius_x=6,sweep=False)
        self.add_contour("party-blower","blower","blower-curl")
        self.relate("connect","party-blower","head-right-upper")
        self.relate("connect","party-blower","head-right-lower")
