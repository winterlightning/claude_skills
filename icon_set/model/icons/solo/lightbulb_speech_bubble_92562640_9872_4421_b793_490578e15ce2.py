from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = "92562640-9872-4421-b793-490578e15ce2"
SOURCE_PATH = "pictographic-primitives/_uncategorized_23/idea message_92562640-9872-4421-b793-490578e15ce2.svg"
AUTHOR = "gpt-6"

class LightbulbSpeechBubble(Solo48):
    icon_id = "lightbulb-speech-bubble"
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "communication/idea"
    aliases = ("idea message",)
    keywords = ("speech bubble", "bulb", "thought")

    def build(self) -> None:
        # Rounded message enclosure has a lower-left tail and one centered bulb.
        self.add_polyline("bubble", (12, 6), (36, 6), (42, 12), (42, 28), (36, 34), (22, 34), (14, 42), (14, 34), (12, 34), (6, 28), (6, 12), (12, 6), closed=True)
        self.add_arc("bulb-dome", (19, 20), (29, 20), radius_x=5, sweep=True)
        points = ((29, 20), (28, 23), (28, 25), (20, 25), (20, 23), (19, 20))
        for i, (a, b) in enumerate(zip(points, points[1:]), 1):
            self.add_line(f"bulb-lower-{i}", a, b)
        self.add_contour("bulb", "bulb-dome", *(f"bulb-lower-{i}" for i in range(1, 6)), closed=True)
