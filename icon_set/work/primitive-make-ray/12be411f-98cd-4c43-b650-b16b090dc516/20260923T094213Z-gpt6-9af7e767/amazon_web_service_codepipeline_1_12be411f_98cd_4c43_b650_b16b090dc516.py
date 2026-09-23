"""AWS CodePipeline brackets enclosing a code chevron and slash."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = "12be411f-98cd-4c43-b650-b16b090dc516"
SOURCE_PATH = "icon_set/work/todo-references/amazon web service codepipeline 1_12be411f-98cd-4c43-b650-b16b090dc516.svg"
AUTHOR = "gpt-6"


class AmazonWebServiceCodePipeline(Solo48):
    icon_id = "amazon-web-service-codepipeline-1"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "technology/cloud"
    aliases = ("aws-codepipeline",)
    keywords = ("amazon", "aws", "code", "pipeline", "development")

    def build(self) -> None:
        # Fixed side rails frame a centered code symbol.
        self.add_polyline("left-rail", (10, 6), (6, 6), (6, 42), (10, 42))
        self.add_polyline("right-rail", (38, 6), (42, 6), (42, 42), (38, 42))
        self.add_polyline("left-chevron", (19, 16), (11, 24), (19, 32))
        self.add_polyline("right-chevron", (29, 16), (37, 24), (29, 32))
        self.add_line("slash", (27, 14), (21, 34))
