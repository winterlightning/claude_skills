'Koala: round head and ear, smooth sitting back and a single clear gripping arm on the branch.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '95f00a8c-536e-5767-97fa-8968fad8e99a'
SOURCE_PATH = 'pictographic-primitives/animals/koala bamboo_95f00a8c-536e-5767-97fa-8968fad8e99a.svg'
AUTHOR = 'gpt-6'


class KoalaWithBranch(Solo48):
    icon_id = 'koala-with-branch'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "nature/animals"
    aliases = ()
    keywords = ('koala', 'branch', 'eucalyptus', 'holding', 'marsupial', 'australia', 'animal', 'sitting')

    def build(self):
        # Koala: round centered nose and head, an open outlined ear, smooth sitting body and a clear gripping arm.
        l = self.add_line
        p = self.add_polyline
        link = self.relate

        def a(name, start, end, rx, ry=None, sweep=True):
            self.add_arc(name, start, end, radius_x=rx,
                         radius_y=rx if ry is None else ry, sweep=sweep)

        def c(name, x, y, radius):
            a(name+'-top', (x-radius,y), (x+radius,y), radius)
            a(name+'-bottom', (x+radius,y), (x-radius,y), radius)
            self.add_contour(name, name+'-top', name+'-bottom', closed=True)

        c('head',20,18,10)
        p('ear-top',(20,8),(16,6),(10,6))
        a('ear-left',(10,6),(6,10),4,sweep=False)
        l('ear-side',(6,10),(6,14))
        a('ear-bottom',(6,14),(10,18),4,sweep=False)
        link('connect','ear-top','ear-left')
        link('connect','ear-left','ear-side')
        link('connect','ear-side','ear-bottom')
        link('connect','ear-top','head')
        link('connect','ear-bottom','head')
        self.add_dot('nose',(20,18))
        a('back',(12,24),(10,36),18,14,sweep=False)
        a('bottom',(10,36),(20,42),10,6,sweep=False)
        l('foot',(20,42),(30,42))
        self.add_contour('body','back','bottom','foot')
        link('connect','body','head')
        l('branch',(30,42),(42,8))
        link('connect','branch','body')
        l('arm',(20,28),(36,25))
        link('connect','arm','branch')
        link('connect','arm','head')
