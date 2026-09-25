"""Two hose curves merge into a nozzle with three spray strokes. Single band replaces nested bands; mirrored quarter ellipses create smooth entry. No useful Lucide nozzle match.
Fresh SOLO48 geometry. Keyshape HRECT_L; bounds are resolved from the live contract.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '853c9087-c4f5-5df0-bff5-1ac1f2b02b6b'
SOURCE_PATH = 'pictographic-primitives/programing/amazon kinesis data firehose_853c9087-c4f5-5df0-bff5-1ac1f2b02b6b.svg'
AUTHOR = 'gpt-6'

class FirehoseNozzle(Solo48):
    icon_id = 'firehose-nozzle'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "programing"
    categories = ("programing", "primitives")
    aliases = ()
    keywords = ('firehose', 'hose', 'nozzle', 'stream', 'data', 'spray', 'pipeline', 'ingest')

    def build(self) -> None:
        def circle(name, x, y, r):
            self.add_arc(name+'-top', (x-r,y), (x+r,y), radius_x=r)
            self.add_arc(name+'-bottom', (x+r,y), (x-r,y), radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def oval(name, x, y, rx, ry):
            self.add_arc(name+'-top', (x-rx,y), (x+rx,y), radius_x=rx,radius_y=ry)
            self.add_arc(name+'-bottom', (x+rx,y), (x-rx,y), radius_x=rx,radius_y=ry)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)
        self.add_arc('upper-hose',(4,8),(24,16),radius_x=20,radius_y=8,sweep=False)
        self.add_arc('lower-hose',(24,32),(4,40),radius_x=20,radius_y=8,sweep=False)
        self.add_polyline('nozzle',(24,16),(32,16),(32,32),(24,32),closed=True)
        self.relate('connect','upper-hose','nozzle')
        self.relate('connect','lower-hose','nozzle')
        for name, a, b in (('upper',(42,15),(44,13)),('middle',(42,24),(44,24)),('lower',(42,33),(44,35))):
            self.add_line('spray-'+name,a,b)
