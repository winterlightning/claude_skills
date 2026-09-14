'Sheltered bench: straight structural edges and evenly spaced table and seat levels.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '1fd48bb2-3ac8-46c0-a63f-a618a4f6efc3'
SOURCE_PATH = 'icons-json/outdoors/outdoors barn bench_1fd48bb2-3ac8-46c0-a63f-a618a4f6efc3.json'
AUTHOR = 'gpt-6'

class OutdoorsBarnBench(Solo48):
    icon_id = 'outdoors-barn-bench'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'outdoors'
    aliases = ()
    keywords = ('outdoors', 'barn', 'bench')

    def build(self):
        # Sheltered bench: straight structural edges and evenly spaced table and seat levels.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        l('roof',(6,18),(42,6))
        p('shelter',(9,17),(9,42),(42,42))
        link('connect','roof','shelter')
        l('table',(20,24),(34,24))
        l('bench',(16,33),(38,33))
        p('legs',(18,42),(24,24),(30,24),(36,42))
        link('connect','legs','table')
        link('connect','legs','bench')
        link('connect','legs','shelter')
