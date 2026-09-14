'Departing plane: smooth semicircular nose and a wider fuselage above a straight runway.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2782429-745d-5835-abe8-ed5499875d12'
SOURCE_PATH = 'icons-json/travel/plane on runway_c2782429-745d-5835-abe8-ed5499875d12.json'
AUTHOR = 'gpt-6'

class PlaneOnRunway(Solo48):
    icon_id = 'plane-on-runway'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'on', 'runway', 'travel')

    def build(self):
        # Departing plane: naturally balanced broad wing, tail and fuselage with a smooth nose above the runway.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('plane',(36,6),(24,12),(18,6),(10,10),(19,20),(10,24),(6,20),(6,34),(14,34),(36,18))
        a('nose',(36,18),(36,6),6,sweep=False)
        link('connect','plane','nose')
        l('runway',(6,42),(42,42))
