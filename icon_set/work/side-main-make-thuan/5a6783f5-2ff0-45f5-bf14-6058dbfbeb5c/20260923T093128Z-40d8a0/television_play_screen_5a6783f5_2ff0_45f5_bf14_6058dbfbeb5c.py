from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '5a6783f5-2ff0-45f5-bf14-6058dbfbeb5c'
SOURCE_PATH = 'pictographic-primitives/other/tv control play_5a6783f5-2ff0-45f5-bf14-6058dbfbeb5c.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    """A play triangle on a television with a central pedestal."""
    icon_id = 'television-play-screen'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('television', 'play', 'screen')

    def build(self):
        # Plan: rounded screen owns play glyph, central stem and symmetric split foot.
        # Ink bounds (4,4)-(44,44); centerline extremes (6,6)-(42,42).
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,28))
        self.add_arc('br',(42,28),(38,32),radius_x=4)
        self.add_line('bottom-right',(38,32),(24,32))
        self.add_line('bottom-left',(24,32),(10,32))
        self.add_arc('bl',(10,32),(6,28),radius_x=4)
        self.add_line('left',(6,28),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('screen','top','tr','right','br','bottom-right','bottom-left','bl','left','tl',closed=True)
        self.add_polyline('play',(19,15),(29,19),(19,23),closed=True)
        self.add_line('stem',(24,32),(24,42))
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','screen','stem')
        self.relate('connect','stem','foot')
