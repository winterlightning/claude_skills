from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = "f7fea0fb-aae6-4804-a1bb-402491861c8d"
SOURCE_PATH = "pictographic-primitives/_uncategorized_19/foursquare logo 1_f7fea0fb-aae6-4804-a1bb-402491861c8d.svg"
AUTHOR = "gpt-6"

class SquareSpeechBubble(Solo48):
    icon_id = "square-speech-bubble"
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/message"
    aliases = ("chat bubble", "foursquare bubble")
    keywords = ("speech", "square", "tail")

    def build(self) -> None:
        # Open lower-left tail echoes the source logo's distinctive silhouette.
        self.add_polyline("bubble", (8, 34), (8, 8), (12, 4), (36, 4), (40, 8), (40, 32), (36, 36), (18, 36), (8, 44))
