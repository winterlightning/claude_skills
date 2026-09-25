"""Arrow Down Made of Circles.

Plan: Six identical circular outlines; four form the shaft and two flank its lower section. Radius 2 preserves all six circular marks within the existing small-circle rule; at stroke 4 these read as solid round dots. VRECT centerlines (8,4)-(40,44), HRECT (4,8)-(44,40).
Construction references: No useful exact Lucide match; supplied six-circle arrow controls the construction.
Reduction: Increased contrast and regularized circle size; no circles removed.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '43fc21fd-3e9b-576e-b230-2a28bf2432cb'
SOURCE_PATH = 'pictographic-primitives/arrows/arrow thick dot bottom_43fc21fd-3e9b-576e-b230-2a28bf2432cb.svg'
SOURCE_ICON_IDS = ('43fc21fd-3e9b-576e-b230-2a28bf2432cb',)
SOURCE_PATHS = ('pictographic-primitives/arrows/arrow thick dot bottom_43fc21fd-3e9b-576e-b230-2a28bf2432cb.svg',)
AUTHOR = 'gpt-6'


class ArrowDownMadeOfCircles(Solo48):
    icon_id = 'arrow-down-made-of-circles'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'arrows'
    categories = ('arrows', 'primitives')
    aliases = ()
    keywords = ('arrow', 'down', 'made', 'of', 'circles')

    def build(self) -> None:
        radius = 2
        centers = [(24,6),(24,18),(24,30),(24,42),(10,30),(38,30)]

        for i,(x,y) in enumerate(centers):
            k=f"circle-{i}"
            self.add_arc(k+"-top",(x-radius,y),(x+radius,y),radius_x=radius)
            self.add_arc(k+"-bottom",(x+radius,y),(x-radius,y),radius_x=radius)
            self.add_contour(k,k+"-top",k+"-bottom",closed=True)
