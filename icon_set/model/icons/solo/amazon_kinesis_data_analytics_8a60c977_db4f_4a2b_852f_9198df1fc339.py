"""Three fanning data streams converging on an analytics rail."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "8a60c977-db4f-4a2b-852f-9198df1fc339"
SOURCE_PATH = "icon_set/work/todo-references/amazon kinesis data analytics_8a60c977-db4f-4a2b-852f-9198df1fc339.svg"
AUTHOR = "gpt-6"


class AmazonKinesisDataAnalytics(Solo48):
    icon_id = "amazon-kinesis-data-analytics"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("kinesis-analytics",)
    keywords = ("amazon", "aws", "kinesis", "analytics", "stream", "flow")

    def build(self) -> None:
        # Three broad channels share a vertical analytics endpoint.
        self.add_bezier("upper-stream", (6, 6), ((10, 12), (22, 16), (42, 16)))
        self.add_line("middle-stream", (6, 24), (42, 24))
        self.add_bezier("lower-stream", (6, 42), ((10, 36), (22, 32), (42, 32)))
        self.add_line("analytics-rail", (42, 6), (42, 42))
        for name in ("upper-stream", "middle-stream", "lower-stream"):
            self.relate("connect", name, "analytics-rail")
