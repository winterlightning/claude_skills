"""Ionic capital with paired round volutes, plain shaft and plinth. Extremes (2,2)-(46,46). Lucide landmark vertical rhythm; tight spiral interiors removed."""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'ab30910c-5cac-52c8-af79-c6cb1c622466'
SOURCE_PATH = 'pictographic-primitives/culture/batch-04/empire_ab30910c-5cac-52c8-af79-c6cb1c622466.svg'
AUTHOR = 'astra-chatgpt'

class IonicColumn(Solo48):
    icon_id = 'ionic-column'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/culture"
    aliases = ()
    keywords = ('column', 'ionic', 'classical', 'greek', 'roman', 'architecture', 'pillar', 'antiquity')

    def build(self) -> None:
        self.add_arc('left-scroll-a',(9,2),(9,16),radius_x=7,sweep=False)
        self.add_arc('left-scroll-b',(9,16),(9,2),radius_x=7,sweep=False)
        self.add_contour('left-scroll','left-scroll-a','left-scroll-b',closed=True)
        self.add_arc('right-scroll-a',(39,2),(39,16),radius_x=7)
        self.add_arc('right-scroll-b',(39,16),(39,2),radius_x=7)
        self.add_contour('right-scroll','right-scroll-a','right-scroll-b',closed=True)
        self.add_line('capital-top',(9,2),(39,2))
        self.add_line('capital-bottom',(9,16),(39,16))
        for scroll in ('left-scroll','right-scroll'):
            self.relate('connect',scroll,'capital-top')
            self.relate('connect',scroll,'capital-bottom')
        self.add_line('shaft-left',(9,16),(9,38))
        self.add_line('shaft-right',(39,16),(39,38))
        self.add_polyline('plinth',(6,46),(6,38),(9,38),(39,38),(42,38),(42,46),(6,46))
        self.relate('connect','shaft-left','plinth')
        self.relate('connect','shaft-left','left-scroll')
        self.relate('connect','shaft-left','capital-bottom')
        self.relate('connect','shaft-right','right-scroll')
        self.relate('connect','shaft-right','capital-bottom')
        self.relate('connect','shaft-right','plinth')
