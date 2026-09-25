"""Complete source composition; see the accompanying visual and validation evidence."""
from ...keyshapes import Keyshape
from ._base import Sub32

SOURCE_ICON_ID = '96fa9fe4-386f-4d65-8531-a569bd794200'
SOURCE_PATH = 'pictographic-primitives/state/circle fork knife_96fa9fe4-386f-4d65-8531-a569bd794200.svg'
AUTHOR = 'gpt-6'
REFERENCE_PARTS = ('circle frame', 'three-tined fork with bowl and handle', 'curved knife blade and handle')

class Drawing(Sub32):
    icon_id = 'fork-knife-circle-sub32'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'SUB'
    semantic_kind = 'modifier'
    category = 'state'
    keywords = ('fork', 'and', 'knife', 'dining', 'symbol')


    def build(self):
        self.circle('frame',16,16,14)
        self.add_line('fork-left',(7,9),(7,13))
        self.add_arc('fork-bl',(7,13),(12,18),radius_x=5,sweep=False)
        self.add_arc('fork-br',(12,18),(17,13),radius_x=5,sweep=False)
        self.add_line('fork-right',(17,13),(17,9))
        self.add_contour('fork-cup','fork-left','fork-bl','fork-br','fork-right')
        self.add_line('fork-center',(12,9),(12,24))
        self.relate('connect','fork-center','fork-bl','fork-br')
        self.add_line('knife-back',(21,9),(21,24))
        self.add_bezier('blade',(21,9),((26,11),(27,15),(27,18)))
        self.add_line('heel',(27,18),(21,18))
        self.relate('connect','knife-back','blade','heel')
        self.relate('connect','blade','heel')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-top',name+'-bottom',closed=True)

