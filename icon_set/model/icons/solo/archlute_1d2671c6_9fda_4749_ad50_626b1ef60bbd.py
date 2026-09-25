"""Pear bowl on diagonal with a longer single-line neck and a tuning crossbar. Body and neck share one shoulder point. Omit strings and bridge. Extremes (6,6)-(42,42); Lucide guitar diagonal concept."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1d2671c6-9fda-4749-ad50-626b1ef60bbd'
SOURCE_PATH = 'pictographic-primitives/music/archlute_1d2671c6-9fda-4749-ad50-626b1ef60bbd.svg'
AUTHOR = 'gpt-6'

class Archlute(Solo48):
    icon_id = 'archlute'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "music"
    aliases = ()
    keywords = ('archlute', 'lute', 'string', 'instrument', 'baroque', 'music', 'plucked')

    def build(self):
        self.add_bezier('bowl',(26,22), ((17,18),(6,22),(6,30)), ((6,37),(11,42),(18,42)), ((26,42),(29,31),(26,22)))
        self.add_contour('body','bowl',closed=True)
        self.add_line('neck',(26,22),(42,6))
        self.add_line('pegs',(34,6),(42,14))
        self.relate('connect','neck','body')
        self.relate('occlude','neck','pegs')
