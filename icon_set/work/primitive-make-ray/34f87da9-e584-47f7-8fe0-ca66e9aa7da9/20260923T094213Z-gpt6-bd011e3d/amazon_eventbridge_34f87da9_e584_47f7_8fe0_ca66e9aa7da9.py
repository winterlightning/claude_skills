"""Amazon EventBridge mark: an outer event network and central hexagon."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "34f87da9-e584-47f7-8fe0-ca66e9aa7da9"
SOURCE_PATH = "icon_set/work/todo-references/amazon eventbridge_34f87da9-e584-47f7-8fe0-ca66e9aa7da9.svg"
AUTHOR = "gpt-6"


class AmazonEventBridge(Solo48):
    icon_id = "amazon-eventbridge"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/cloud"
    aliases = ("event-bus",)
    keywords = ("amazon", "aws", "events", "network", "hexagon", "bridge")

    def build(self) -> None:
        # Six-sided perimeter, four round event nodes, smaller central bus.
        self.add_polyline("perimeter", (14, 6), (34, 6), (42, 24), (34, 42), (14, 42), (6, 24), closed=True)
        self.add_polyline("event-bus", (19, 18), (29, 18), (34, 24), (29, 30), (19, 30), (14, 24), closed=True)
        for name, x, y in (("upper-left", 14, 6), ("upper-right", 38, 16), ("lower-right", 34, 42), ("lower-left", 10, 34)):
            self.add_arc(f"{name}-a", (x-4, y), (x+4, y), radius_x=4)
            self.add_arc(f"{name}-b", (x+4, y), (x-4, y), radius_x=4)
            self.add_contour(name, f"{name}-a", f"{name}-b", closed=True)
            self.relate("connect", "perimeter", name)
