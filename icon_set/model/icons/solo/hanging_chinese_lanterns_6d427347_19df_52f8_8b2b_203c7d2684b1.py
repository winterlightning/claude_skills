"""Two suspended paper lanterns at different heights. SQUARE extremes (2,2)-(46,46). Omit bunting and ribs to preserve the paired lantern silhouettes."""

from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '6d427347-19df-52f8-8b2b-203c7d2684b1'
SOURCE_PATH = 'pictographic-primitives/culture/batch-03/chinese lantern_6d427347-19df-52f8-8b2b-203c7d2684b1.svg'
AUTHOR = 'astra-chatgpt'


class HangingChineseLanterns(Solo48):
    icon_id = 'hanging-chinese-lanterns'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "culture/objects"
    aliases = ()
    keywords = ('lantern', 'chinese', 'festival', 'lunar new year', 'hanging', 'bunting', 'celebration', 'asian')

    def build(self) -> None:
        self.add_polyline('cord',(2,2),(10,5),(38,5),(46,2))
        for label,cx,top,bottom in (('left',10,16,38),('right',38,12,32)):
            mid=(top+bottom)//2
            ry=(bottom-top)//2
            self.add_line(label+'-suspension',(cx,5),(cx,top))
            self.add_arc(label+'-ne',(cx,top),(cx+8,mid),radius_x=8,radius_y=ry)
            self.add_arc(label+'-se',(cx+8,mid),(cx,bottom),radius_x=8,radius_y=ry)
            self.add_arc(label+'-sw',(cx,bottom),(cx-8,mid),radius_x=8,radius_y=ry)
            self.add_arc(label+'-nw',(cx-8,mid),(cx,top),radius_x=8,radius_y=ry)
            self.add_contour(label,*[label+s for s in ('-ne','-se','-sw','-nw')],closed=True)
            self.add_line(label+'-cap',(cx-4,top),(cx+4,top))
            self.add_line(label+'-base',(cx-4,bottom),(cx+4,bottom))
            self.add_line(label+'-tassel',(cx,bottom),(cx,bottom+8))
            self.relate('connect',label,label+'-suspension',label+'-cap')
            self.relate('connect',label,label+'-tassel',label+'-base')
            self.relate('connect','cord',label+'-suspension')
