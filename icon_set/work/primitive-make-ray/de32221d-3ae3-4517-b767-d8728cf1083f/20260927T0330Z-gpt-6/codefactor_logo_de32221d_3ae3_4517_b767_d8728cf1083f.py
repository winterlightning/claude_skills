"""A regular three-ring column and two unequal horizontal bars; collapse capsules to round-capped strokes; extremes (6,6)-(42,42)."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'de32221d-3ae3-4517-b767-d8728cf1083f'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__codefactor-logo/20260927T032242Z-thuan-mac-1/reference/codefactor logo_de32221d-3ae3-4517-b767-d8728cf1083f.svg'
AUTHOR = "gpt-6"

class CodefactorLogo(Solo48):
    icon_id = 'codefactor-logo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'logos'
    categories = ('logos', 'primitives')
    aliases = ()
    keywords = ('codefactor', 'code-review', 'logo', 'brand', 'developer', 'list', 'quality')

    def build(self) -> None:
        # Three equal bullets paired with two unequal brand strokes.
        for i,y in enumerate((9,24,39)):
            self.add_arc(f'bullet-{i}-a',(6,y),(12,y),radius_x=3,radius_y=3,sweep=True)
            self.add_arc(f'bullet-{i}-b',(12,y),(6,y),radius_x=3,radius_y=3,sweep=True)
            self.add_contour(f'bullet-{i}',f'bullet-{i}-a',f'bullet-{i}-b',closed=True)
        self.add_line('top-bar',(23,9),(42,9))
        self.add_line('middle-bar',(23,24),(34,24))
