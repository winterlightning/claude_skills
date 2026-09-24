"""monitor graduation hat: complete SOLO48 repair.
Kept the monitor, stand and mortarboard silhouette. Simplified the shallow crown into a mortarboard with a short tassel.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '25a4cb19-9e79-49d4-b5af-74c85495cf76'
SOURCE_PATH = 'pictographic-primitives/other/monitor graduation hat_25a4cb19-9e79-49d4-b5af-74c85495cf76.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'monitor-graduation-hat'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('monitor graduation hat',)



    def monitor(self):
        # Symmetric rounded screen, split bottom edge at actual stand attachment.
        self.add_line('top',(10,6),(38,6))
        self.add_arc('tr',(38,6),(42,10),radius_x=4)
        self.add_line('right',(42,10),(42,30))
        self.add_arc('br',(42,30),(38,34),radius_x=4)
        self.add_line('bottom-right',(38,34),(24,34))
        self.add_line('bottom-left',(24,34),(10,34))
        self.add_arc('bl',(10,34),(6,30),radius_x=4)
        self.add_line('left',(6,30),(6,10))
        self.add_arc('tl',(6,10),(10,6),radius_x=4)
        self.add_contour('screen','top','tr','right','br','bottom-right','bottom-left','bl','left','tl',closed=True)
        self.add_line('stand',(24,34),(24,42))
        self.add_polyline('foot',(16,42),(24,42),(32,42))
        self.relate('connect','screen','stand')
        self.relate('connect','stand','foot')


    def build(self):
        # Diamond mortarboard over a shallow crown, as in the supplied reference.
        self.monitor()
        self.add_polyline('mortarboard',(15,20),(24,15),(33,20),(24,25),closed=True)
        self.add_line('tassel',(33,20),(33,25))
        self.relate('connect','mortarboard','tassel')
