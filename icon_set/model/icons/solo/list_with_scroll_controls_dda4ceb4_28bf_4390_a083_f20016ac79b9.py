"""List with Scroll Controls; re-authored from the supplied visual reference."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'dda4ceb4-28bf-4390-a083-f20016ac79b9'
SOURCE_PATH = 'pictographic-primitives/websites/web form drop down menu form_dda4ceb4-28bf-4390-a083-f20016ac79b9.svg'
SOURCE_REFERENCES = ({'source_icon_id': 'dda4ceb4-28bf-4390-a083-f20016ac79b9', 'source_path': 'pictographic-primitives/websites/web form drop down menu form_dda4ceb4-28bf-4390-a083-f20016ac79b9.svg'},)
AUTHOR = 'gpt-6'

class ListWithScrollControls(Solo48):
    icon_id = 'list-with-scroll-controls'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "websites"
    categories = ("websites", "primitives")
    aliases = ()
    keywords = ('list', 'scroll', 'controls', 'chevrons', 'menu', 'interface', 'form')

    def build(self) -> None:
        # Centerline extremes (6,8)-(42,40). Straight panel sides allow exact grid spacing.
        self.add_polyline('panel',(4,8),(24,8),(44,8),(44,40),(24,40),(4,40),closed=True)
        for n,y in enumerate((20,28)): self.add_line(f'item-{n}',(12,y),(18,y))
        self.add_polyline('up',(28,20),(32,16),(36,20))
        self.add_polyline('down',(28,28),(32,32),(36,28))
