'amazon-managed-blockchain revision: two shorter, wider rounded blocks (16 x 28, r4 corners) joined at mid-height by an 8-long link; HRECT_M.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.icons.solo._symmetry_curves import path, ellipse, box, line, poly, contacts

SOURCE_ICON_ID = '881f4502-fae5-4c7e-99a9-18cf1f644952'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__amazon-managed-blockchain/20260926T064521Z-thuan-mac/reference/amazon managed blockchain_881f4502-fae5-4c7e-99a9-18cf1f644952.svg'
AUTHOR = "claude-opus-5-5"


class AmazonManagedBlockchain(Solo48):
    icon_id = 'amazon-managed-blockchain'
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    categories = ('programing', 'primitives')
    aliases = ()
    keywords = ('amazon', 'managed', 'blockchain', 'programing')
    keyshape = Keyshape.HRECT_M

    def build(self):
        # Revision per review: both blocks are shorter and wider rounded squares, 16 wide and
        # 16 tall with r4 corners (were 14 x 36), linked at mid-height by a straight bar 8 long.
        # A CIRCLE-free wide keyshape (HRECT_M) needs 28 of height, so each block is a 16 x 28
        # rounded rectangle, the widest-and-shortest proportion the profile allows.
        t, b, r = 10, 38, 4
        for name, l, rgt in (("left", 4, 20), ("right", 28, 44)):
            join_x = rgt if name == "left" else l
            self.add_line(f"{name}-top", (l + r, t), (rgt - r, t))
            self.add_arc(f"{name}-ne", (rgt - r, t), (rgt, t + r), radius_x=r)
            self.add_line(f"{name}-right-upper", (rgt, t + r), (rgt, 24))
            self.add_line(f"{name}-right-lower", (rgt, 24), (rgt, b - r))
            self.add_arc(f"{name}-se", (rgt, b - r), (rgt - r, b), radius_x=r)
            self.add_line(f"{name}-bottom", (rgt - r, b), (l + r, b))
            self.add_arc(f"{name}-sw", (l + r, b), (l, b - r), radius_x=r)
            self.add_line(f"{name}-left-lower", (l, b - r), (l, 24))
            self.add_line(f"{name}-left-upper", (l, 24), (l, t + r))
            self.add_arc(f"{name}-nw", (l, t + r), (l + r, t), radius_x=r)
            self.add_contour(name, f"{name}-top", f"{name}-ne", f"{name}-right-upper", f"{name}-right-lower",
                             f"{name}-se", f"{name}-bottom", f"{name}-sw", f"{name}-left-lower",
                             f"{name}-left-upper", f"{name}-nw", closed=True)
        self.add_line("link", (20, 24), (28, 24))
        self.relate("connect", "left", "link")
        self.relate("connect", "right", "link")
