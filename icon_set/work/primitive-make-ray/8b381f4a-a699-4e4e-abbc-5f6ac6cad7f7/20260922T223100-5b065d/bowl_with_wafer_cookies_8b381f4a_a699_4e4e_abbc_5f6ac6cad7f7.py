from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8b381f4a-a699-4e4e-abbc-5f6ac6cad7f7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/chef gear tea cookies_8b381f4a-a699-4e4e-abbc-5f6ac6cad7f7.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bowl-with-wafer-cookies'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('bowl', 'with', 'wafer', 'cookies')

    def build(self):
        # Shallow oval bowl beneath three elongated overlapping wafers and a rightward curved stroke. Preserve ambiguous source composition without relabeling its components. Square ink(4,4)-(44,44).
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
        self.add_polyline('diagonal-wafer',(6,20),(20,6),(26,12),(12,26),closed=True)
        self.add_line('wafer-top',(26,12),(34,12))
        self.add_arc('wafer-end',(34,12),(34,20),radius_x=4)
        self.add_line('wafer-bottom',(34,20),(18,20))
        self.add_contour('upper-wafer','wafer-top','wafer-end','wafer-bottom')
        self.relate('connect','upper-wafer','diagonal-wafer')
        self.add_polyline('lower-wafer',(14,24),(34,24),(34,20))
        self.relate('connect','lower-wafer','upper-wafer')
        self.relate('connect','lower-wafer','diagonal-wafer')
        self.add_arc('right-curve',(36,14),(36,26),radius_x=6)
        self.add_arc('rim-top',(16,34),(40,34),radius_x=12,radius_y=4)
        self.add_arc('rim-bottom',(40,34),(16,34),radius_x=12,radius_y=4)
        self.add_contour('rim','rim-top','rim-bottom',closed=True)
        self.add_arc('bowl',(40,34),(16,34),radius_x=12,radius_y=8)
        self.relate('connect','rim','bowl')
