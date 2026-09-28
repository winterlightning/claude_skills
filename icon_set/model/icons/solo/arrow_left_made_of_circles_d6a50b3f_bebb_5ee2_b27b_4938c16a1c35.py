"""Arrow Left Made of Circles.

Plan: Six identical circular outlines; four form the shaft and two flank its lower section. Radius 2 preserves all six circular marks within the existing small-circle rule; at stroke 4 these read as solid round dots. VRECT centerlines (8,4)-(40,44), HRECT (4,8)-(44,40).
Construction references: No useful exact Lucide match; supplied six-circle arrow controls the construction.
Reduction: Increased contrast and regularized circle size; no circles removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd6a50b3f-bebb-5ee2-b27b-4938c16a1c35'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick dot left_d6a50b3f-bebb-5ee2-b27b-4938c16a1c35.svg'
SOURCE_ICON_IDS = ('d6a50b3f-bebb-5ee2-b27b-4938c16a1c35',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow thick dot left_d6a50b3f-bebb-5ee2-b27b-4938c16a1c35.svg',)
AUTHOR = 'gpt-6'


class ArrowLeftMadeOfCircles(Solo48):
    icon_id = 'arrow-left-made-of-circles'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'left', 'made', 'of', 'circles')

    def build(self) -> None:
        radius = 2
        centers = [(24,6),(24,18),(24,30),(24,42),(10,30),(38,30)]
        centers = [(y,48-x) for x,y in centers]

        for i,(x,y) in enumerate(centers):
            k=f"circle-{i}"
            self.add_arc(k+"-top",(x-radius,y),(x+radius,y),radius_x=radius)
            self.add_arc(k+"-bottom",(x+radius,y),(x-radius,y),radius_x=radius)
            self.add_contour(k,k+"-top",k+"-bottom",closed=True)
