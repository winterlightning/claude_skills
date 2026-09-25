"""A key sits inside a message bubble.
Construction reference: key-round.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'eb0b6680-3f5b-40fd-9a39-04012841c110'
SOURCE_PATH = 'icon_set/work/todo-references/message key_eb0b6680-3f5b-40fd-9a39-04012841c110.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'message-key'
    keyshape = Keyshape.SQUARE
    # Visible ink extrema: (4, 4, 44, 44).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('message', 'key')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: speech enclosure with lower-left tail; ring, shaft and tooth inside.
        self.add_polyline('bubble',(6,6),(42,6),(42,34),(24,34),(14,42),(14,34),(6,34),closed=True)
        self.circle('key-ring',19,20,4)
        self.add_polyline('key-shaft',(23,20),(34,20),(34,16))
        self.relate('connect','key-ring','key-shaft')
