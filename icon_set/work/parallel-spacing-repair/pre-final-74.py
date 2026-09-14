'Departing plane: smooth semicircular nose and a wider fuselage above a straight runway.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'c2782429-745d-5835-abe8-ed5499875d12'
SOURCE_PATH = 'icons-json/travel/plane on runway_c2782429-745d-5835-abe8-ed5499875d12.json'
AUTHOR = 'gpt-6'

class PlaneOnRunway(Solo48):
    icon_id = 'plane-on-runway'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'travel'
    aliases = ()
    keywords = ('plane', 'on', 'runway', 'travel')

    def build(self):
        # Departing plane: smooth semicircular nose and a wider fuselage above a straight runway.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('upper',(38,8),(26,14),(16,8),(10,11),(18,19),(12,23),(6,19),(4,21),(10,30),(16,31),(38,20))
        a('nose',(38,20),(38,8),6,sweep=False)
        link('connect','upper','nose')
        l('runway',(4,40),(44,40))
