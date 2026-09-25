"""A pitched-roof house on a ground line beside two rising light strokes; deliberate side-weighting. HRECT extremes (4,8)-(44,40).
Reduction: Removed the small door to retain two equal, parallel light strokes alongside the house.
Lucide construction: house
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '284cb87c-559b-4d20-9f49-ec6ac8225270'
SOURCE_PATH = 'pictographic-primitives/nature/light mode home_284cb87c-559b-4d20-9f49-ec6ac8225270.svg'
AUTHOR = 'gpt-6'


class HouseWithLightStrokes(Solo48):
    icon_id = 'house-with-light-strokes'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature"
    categories = ("nature", "primitives")
    aliases = ()
    keywords = ('house', 'home', 'light', 'daylight', 'building', 'ground', 'sun', 'residence')

    def build(self) -> None:
        # Two equal diagonal strokes with a 12-unit horizontal series step.
        self.add_polyline("house",(4,40),(4,20),(14,8),(24,20),(24,40))
        self.add_polyline("ground",(4,40),(24,40),(26,40),(38,40),(44,40))
        self.relate("connect","house-1","ground-1")
        self.relate("connect","house-4","ground-1")
        self.relate("connect","house-4","ground-2")
        for i,x in enumerate((26,38)):
            self.add_line(f"ray-{i}",(x,40),(x+6,34))
            self.relate("connect",f"ray-{i}",f"ground-{i+2}")
            self.relate("connect",f"ray-{i}",f"ground-{i+3}")
