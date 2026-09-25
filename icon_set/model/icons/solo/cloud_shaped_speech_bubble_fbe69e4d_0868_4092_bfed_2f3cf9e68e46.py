"""Cloud Shaped Speech Bubble. Empty standalone subject, per explicit user correction.
Lucide cloud: one large and one small lobe on a continuous outline. Integral tail belongs to the same contour. Intentional lobe asymmetry preserves the source silhouette.
"""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID = 'fbe69e4d-0868-4092-bfed-2f3cf9e68e46'
SOURCE_PATH = 'pictographic-primitives/container/speech bubble_fbe69e4d-0868-4092-bfed-2f3cf9e68e46.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'cloud-shaped-speech-bubble'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'container'
    categories = ('container',)
    aliases = ()
    keywords = ('cloud', 'shaped', 'speech', 'bubble')
    def build(self):
        self.add_bezier("large-lobe",(18,32),((10,32),(4,28),(4,22)),((4,14),(10,8),(18,8)),((25,8),(30,13),(31,18)))
        self.add_bezier("small-lobe",(31,18),((38,15),(44,19),(44,25)),((44,31),(40,34),(34,34)))
        self.add_line("bottom",(34,34),(28,34))
        self.add_line("tail-slope",(28,34),(18,40))
        self.add_line("tail-upright",(18,40),(18,32))
        self.add_contour("bubble","large-lobe","small-lobe","bottom","tail-slope","tail-upright",closed=True)
