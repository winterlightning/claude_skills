'Compute stack: regular perspective panels with deliberate 8-unit offsets and straight edges.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'd43e2f1d-9d06-4226-902d-395655ca6921'
SOURCE_PATH = 'icons-json/programing/elastic compute cloud_d43e2f1d-9d06-4226-902d-395655ca6921.json'
AUTHOR = 'gpt-6'

class ElasticComputeCloud(Solo48):
    icon_id = 'elastic-compute-cloud'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('elastic', 'compute', 'cloud', 'programing')

    def build(self):
        # Compute stack: three regular perspective panels with clear diagonal separation.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        p('front',(6,20),(18,26),(18,42),(6,36),(6,20))
        p('middle',(14,12),(28,19),(28,36))
        p('back',(26,6),(42,14),(42,30))
