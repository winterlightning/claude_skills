'Snow scooter: a clear stepped body, balanced track and separated ski without fitted micro-curves.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'a0980517-7981-47f9-b740-8ade748f0d74'
SOURCE_PATH = 'icons-json/sports/skiing snow scooter_a0980517-7981-47f9-b740-8ade748f0d74.json'
AUTHOR = 'gpt-6'

class SkiingSnowScooter(Solo48):
    icon_id = 'skiing-snow-scooter'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'sports'
    aliases = ()
    keywords = ('skiing', 'snow', 'scooter', 'sports')

    def build(self):
        # Snow scooter: a clear stepped body, balanced track and separated ski without fitted micro-curves.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('body',(4,16),(12,16),(18,22),(26,22),(32,14),(38,18),(44,30),(36,32),(20,32),(4,24),(4,16))
        p('handle',(32,14),(28,8),(20,8))
        link('connect','handle','body')
        p('track',(12,28),(6,34),(6,40),(22,40),(28,32))
        link('connect','track','body')
        p('ski',(34,32),(38,40),(44,40))
        link('connect','ski','body')
