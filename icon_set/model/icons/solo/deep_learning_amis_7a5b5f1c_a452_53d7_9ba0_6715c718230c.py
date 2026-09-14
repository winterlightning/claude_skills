'Processing nodes: three equal circular nodes in a square enclosure, with explicit short connecting stems.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '7a5b5f1c-a452-53d7-9ba0-6715c718230c'
SOURCE_PATH = 'icons-json/programing/deep learning amis_7a5b5f1c-a452-53d7-9ba0-6715c718230c.json'
AUTHOR = 'gpt-6'

class DeepLearningAmis(Solo48):
    icon_id = 'deep-learning-amis'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'programing'
    aliases = ()
    keywords = ('deep', 'learning', 'amis', 'programing')

    def build(self) -> None:
        # A shared corner radius keeps all four turns tangent to their walls.
        left, top, right, bottom, radius = 6, 6, 42, 42, 4
        self.add_line('outline-top', (left+radius,top), (right-radius,top))
        self.add_arc('outline-tr', (right-radius,top), (right,top+radius), radius_x=radius)
        self.add_line('outline-right', (right,top+radius), (right,bottom-radius))
        self.add_arc('outline-br', (right,bottom-radius), (right-radius,bottom), radius_x=radius)
        self.add_line('outline-bottom', (right-radius,bottom), (left+radius,bottom))
        self.add_arc('outline-bl', (left+radius,bottom), (left,bottom-radius), radius_x=radius)
        self.add_line('outline-left', (left,bottom-radius), (left,top+radius))
        self.add_arc('outline-tl', (left,top+radius), (left+radius,top), radius_x=radius)
        self.add_contour('outline', *('outline-'+part for part in ('top','tr','right','br','bottom','bl','left','tl')), closed=True)

        # Three linked circular cells share exact tangent nodes; preserve the connected chain topology.
        for name,y in (('top',18),('middle',24),('bottom',30)):
            points=((24,y-3),(27,y),(24,y+3),(21,y),(24,y-3))
            for k,(a,b) in enumerate(zip(points,points[1:])):self.add_arc(name+'-'+str(k),a,b,radius_x=3)
            self.add_contour(name,*(name+'-'+str(k) for k in range(4)),closed=True)
        self.relate('connect','top','middle');self.relate('connect','middle','bottom')
