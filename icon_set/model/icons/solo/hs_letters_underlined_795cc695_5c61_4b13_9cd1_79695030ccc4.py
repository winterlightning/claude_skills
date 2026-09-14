"""A capital H and smaller lowercase s share an underline. SQUARE extremes (6,6)-(42,42). Lucide case-sensitive informs the mixed-case proportions; coherent semicircles form the s. Preserve the letters, underline and height contrast."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '795cc695-5c61-4b13-9cd1-79695030ccc4'
SOURCE_PATH = 'pictographic-primitives/symbol/hs (text u)_795cc695-5c61-4b13-9cd1-79695030ccc4.svg'
AUTHOR = 'gpt-6'


class HsLettersUnderlined(Solo48):
    icon_id = 'hs-letters-underlined'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/symbols"
    aliases = ()
    keywords = ('hs', 'letters', 'text', 'underline', 'typography', 'abbreviation', 'language')

    def build(self) -> None:
        self.add_polyline('h-left',(6,6),(6,19),(6,32))
        self.add_polyline('h-right',(18,6),(18,19),(18,32))
        self.add_line('h-crossbar',(6,19),(18,19))
        self.relate('connect','h-left','h-crossbar')
        self.relate('connect','h-right','h-crossbar')
        self.add_line('underline',(6,42),(42,42))
        self.add_line('s-top',(40,14),(33,14))
        self.add_arc('s-upper',(33,14),(33,22),radius_x=5,radius_y=4,sweep=False)
        self.add_line('s-middle',(33,22),(37,22))
        self.add_arc('s-lower',(37,22),(37,32),radius_x=5)
        self.add_line('s-bottom',(37,32),(30,32))
        self.add_contour('s','s-top','s-upper','s-middle','s-lower','s-bottom')
