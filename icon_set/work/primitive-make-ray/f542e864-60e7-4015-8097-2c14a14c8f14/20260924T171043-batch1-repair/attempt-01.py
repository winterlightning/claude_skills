"""Amazon EMR mark: a source hub feeding four square data nodes."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "f542e864-60e7-4015-8097-2c14a14c8f14"
SOURCE_PATH = 'pictographic-primitives/_uncategorized_02/amazon emr_f542e864-60e7-4015-8097-2c14a14c8f14.svg'
AUTHOR = 'gpt-6'


class AmazonEmr(Solo48):
    icon_id = "amazon-emr"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/cloud"
    aliases = ("elastic-mapreduce",)
    keywords = ("amazon", "aws", "emr", "data", "cluster", "nodes")

    def build(self) -> None:
        # A round plus-marked source fans out to four square destinations.
        self.add_arc("hub-upper", (6, 24), (28, 24), radius_x=11)
        self.add_arc("hub-lower", (28, 24), (6, 24), radius_x=11)
        self.add_contour("hub", "hub-upper", "hub-lower", closed=True)
        self.add_line("plus-horizontal", (15, 24), (19, 24))
        self.add_line("plus-vertical", (17, 22), (17, 26))
        self.relate("connect", "plus-horizontal", "plus-vertical")
        for name, box, start, end in (
            ("upper", ((32, 6), (40, 14)), (21, 17), (32, 10)),
            ("right-upper", ((34, 16), (42, 24)), (24, 22), (34, 20)),
            ("right-lower", ((34, 26), (42, 34)), (24, 26), (34, 30)),
            ("lower", ((32, 34), (40, 42)), (21, 31), (32, 38)),
        ):
            (x1, y1), (x2, y2) = box
            self.add_polyline(f"{name}-node", (x1, y1), (x2, y1), (x2, y2), (x1, y2), closed=True)
            self.add_line(f"{name}-link", start, end)
            self.relate("connect", "hub", f"{name}-link")
            self.relate("connect", f"{name}-link", f"{name}-node")
