"""messages bubble square information.
Plan: Restored a serif lowercase i, with a separate dot, upper flag and baseline, inside a square message bubble with an angular tail.
Construction: message-square: rounded box and intentional angular tail.
Keyshape: SQUARE; preserve the original's recognizable proportions.
"""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'e7d4da24-f043-4585-a63c-70bfb89da8a0'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__information-message-bubble-solo/20260929T033633Z-thuan-mac/reference/messages bubble square information_e7d4da24-f043-4585-a63c-70bfb89da8a0.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'information-message-bubble-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('messages', 'bubble', 'square', 'information')

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def rect(self,n,x,y,w,h,r=3):
        self.add_line(n+'t',(x+r,y),(x+w-r,y))
        self.add_arc(n+'tr',(x+w-r,y),(x+w,y+r),radius_x=r)
        self.add_line(n+'r',(x+w,y+r),(x+w,y+h-r))
        self.add_arc(n+'br',(x+w,y+h-r),(x+w-r,y+h),radius_x=r)
        self.add_line(n+'b',(x+w-r,y+h),(x+r,y+h))
        self.add_arc(n+'bl',(x+r,y+h),(x,y+h-r),radius_x=r)
        self.add_line(n+'l',(x,y+h-r),(x,y+r))
        self.add_arc(n+'tl',(x,y+r),(x+r,y),radius_x=r)
        self.add_contour(n,*[n+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)

    def build(self):

        self.add_polyline('bottom-tail',(42,30),(42,34),(23,34),(14,43),(14,34),(9,34))
        self.add_arc('bl',(9,34),(5,30),radius_x=4)
        self.add_line('left',(5,30),(5,9));self.add_arc('tl',(5,9),(9,5),radius_x=4)
        self.add_line('top',(9,5),(38,5));self.add_arc('tr',(38,5),(42,9),radius_x=4)
        self.add_line('right',(42,9),(42,30));self.add_contour('bubble','bottom-tail','bl','left','tl','top','tr','right',closed=True)
        self.add_dot('dot',(24,13))
        self.add_polyline('info',(20,21),(24,21),(24,29));self.add_line('serif',(19,29),(29,29));self.relate('connect','info','serif')
