from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'f45d9583-295d-48ad-a334-df8ed9d7581c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/building user_f45d9583-295d-48ad-a334-df8ed9d7581c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'person-and-office-building'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('person', 'and', 'office', 'building')

    def build(self):
        # Building outline interrupted by a foreground bust; a 2x2 repeated window series. Square visible extremes (4,4)-(44,44). Bust radius 4, shoulders at y=38, exact head/body centerline gap 8.
        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
        def rect(n,l,t,r,b):
            self.add_polyline(n,(l,t),(r,t),(r,b),(l,b),closed=True)
        def rounded(n,l,t,r,b,k):
            self.add_line(n+'-t',(l+k,t),(r-k,t))
            self.add_arc(n+'-tr',(r-k,t),(r,t+k),radius_x=k)
            self.add_line(n+'-r',(r,t+k),(r,b-k))
            self.add_arc(n+'-br',(r,b-k),(r-k,b),radius_x=k)
            self.add_line(n+'-b',(r-k,b),(l+k,b))
            self.add_arc(n+'-bl',(l+k,b),(l,b-k),radius_x=k)
            self.add_line(n+'-l',(l,b-k),(l,t+k))
            self.add_arc(n+'-tl',(l,t+k),(l+k,t),radius_x=k)
            self.add_contour(n,*[n+'-'+s for s in ['t','tr','r','br','b','bl','l','tl']],closed=True)
        self.add_polyline('building',(17,42),(6,42),(6,6),(30,6),(30,14))
        for row in range(2):
            for col in range(2):
                self.add_dot(f'window-{row}-{col}',(14+8*col,14+10*row))
        circle('head',34,26,4)
        self.add_line('shoulder-top',(30,38),(38,38))
        self.add_arc('shoulder-left',(26,42),(30,38),radius_x=4)
        self.add_arc('shoulder-right',(38,38),(42,42),radius_x=4)
        self.add_contour('shoulders','shoulder-left','shoulder-top','shoulder-right')
