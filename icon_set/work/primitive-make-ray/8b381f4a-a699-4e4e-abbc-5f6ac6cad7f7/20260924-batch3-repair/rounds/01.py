from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8b381f4a-a699-4e4e-abbc-5f6ac6cad7f7'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/chef gear tea cookies_8b381f4a-a699-4e4e-abbc-5f6ac6cad7f7.svg'
AUTHOR = 'gpt-6'

PLAN = 'Three overlapping wafer-like pieces above a bowl; separate stacked edges and attach the right flourish at a true contour point.'
PARENT_RESULT = 'icon_set/work/primitive-make-ray/8b381f4a-a699-4e4e-abbc-5f6ac6cad7f7/20260922T223100-5b065d/result.json'

class Drawing(Solo48):
    icon_id = 'chef-gear-tea-cookies'
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

        # Main diagonal wafer retains its full silhouette; two stacked exposed ends share exact nodes.
        self.add_polyline('diagonal-wafer',(6,22),(22,6),(28,12),(18,22),(6,22),closed=True)
        self.add_polyline('upper-wafer',(28,12),(36,12),(36,20),(20,20))
        self.relate('connect','upper-wafer','diagonal-wafer')
        self.add_polyline('lower-wafer',(18,22),(18,28),(34,28),(34,20))
        self.relate('connect','lower-wafer','diagonal-wafer')
        self.relate('connect','lower-wafer','upper-wafer')
        self.add_bezier('right-curve',(36,12),((40,12),(42,16),(42,20)),((42,24),(40,26),(40,28)))
        self.relate('connect','right-curve','upper-wafer')
        self.add_line('rim',(12,34),(36,34))
        self.add_arc('bowl',(36,34),(12,34),radius_x=12,radius_y=8)
        self.relate('connect','rim','bowl')
