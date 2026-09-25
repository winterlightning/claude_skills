"""An empty writing page with the source's open lower-right edge.

VRECT_L extrema (8,4)-(40,44). One round-cornered outline owns the shape;
the intentional opening preserves the source. Lucide file informs corner flow.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = "b3a0958d-81d7-40c7-b8fc-1bfdf8c22a30"
SOURCE_PATH = "pictographic-primitives/_uncategorized_12/content write_b3a0958d-81d7-40c7-b8fc-1bfdf8c22a30.svg"
AUTHOR = "gpt-6"


class EmptyDocumentWritingPage(Solo48):
    icon_id = "empty-document-writing-page"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ("blank page", "write document")
    keywords = ("empty", "paper", "writing", "open")

    def build(self) -> None:
        self.add_line("bottom",(34,44),(12,44))
        self.add_arc("sw",(12,44),(8,40),radius_x=4,radius_y=4,sweep=True)
        self.add_line("left",(8,40),(8,8))
        self.add_arc("nw",(8,8),(12,4),radius_x=4,radius_y=4,sweep=True)
        self.add_line("top",(12,4),(36,4))
        self.add_arc("ne",(36,4),(40,8),radius_x=4,radius_y=4,sweep=True)
        self.add_line("right",(40,8),(40,18))
        self.add_contour("page","bottom","sw","left","nw","top","ne","right")
