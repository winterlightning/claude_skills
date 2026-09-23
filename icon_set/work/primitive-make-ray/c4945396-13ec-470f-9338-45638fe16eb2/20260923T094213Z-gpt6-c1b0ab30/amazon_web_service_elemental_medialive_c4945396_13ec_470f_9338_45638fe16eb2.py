"""AWS MediaLive play triangle with three media nodes and scan marks."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "c4945396-13ec-470f-9338-45638fe16eb2"
SOURCE_PATH = "icon_set/work/todo-references/amazon web service elemental medialive_c4945396-13ec-470f-9338-45638fe16eb2.svg"
AUTHOR = "gpt-6"


class AmazonElementalMediaLive(Solo48):
    icon_id = "amazon-elemental-medialive"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/media"
    aliases = ("aws-medialive",)
    keywords = ("amazon", "aws", "media", "live", "play", "stream")

    def build(self) -> None:
        # The central play sign is flanked by three repeated hexagonal nodes.
        self.add_polyline("play", (19, 17), (33, 24), (19, 31), closed=True)
        for name, cx, cy in (("top", 24, 9), ("lower-left", 10, 38), ("lower-right", 38, 38)):
            self.add_polyline(name, (cx, cy-4), (cx+4, cy-2), (cx+4, cy+2), (cx, cy+4), (cx-4, cy+2), (cx-4, cy-2), closed=True)
        self.add_polyline("scan-left", (6, 18), (6, 14), (12, 11))
        self.add_polyline("scan-right", (42, 18), (42, 14), (36, 11))
        self.add_polyline("scan-bottom", (19, 40), (24, 44), (29, 40))
