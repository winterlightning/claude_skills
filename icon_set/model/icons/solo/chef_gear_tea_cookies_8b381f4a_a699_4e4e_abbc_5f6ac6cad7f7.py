from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '8b381f4a-a699-4e4e-abbc-5f6ac6cad7f7'
SOURCE_PATH = 'icon_set/work/todo-references/chef gear tea cookies_8b381f4a-a699-4e4e-abbc-5f6ac6cad7f7.svg'
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

        self.add_polyline('diagonal-wafer',(6,22),(22,6),(28,12),(15,25),closed=True)
        self.add_line('wafer-top',(22,6),(34,6))
        self.add_arc('wafer-upper',(34,6),(38,10),radius_x=4)
        self.add_arc('wafer-lower',(38,10),(34,14),radius_x=4)
        self.add_line('wafer-bottom',(34,14),(26,14))
        self.add_contour('upper-wafer','wafer-top','wafer-upper','wafer-lower','wafer-bottom')
        self.relate('connect','upper-wafer','diagonal-wafer')
        self.add_polyline('lower-wafer',(18,22),(34,22),(34,14))
        self.relate('connect','lower-wafer','upper-wafer','diagonal-wafer')
        self.add_bezier('right-curve',(38,10),((40,10),(42,14),(42,18)),((42,21),(42,23),(42,25)))
        self.relate('connect','right-curve','wafer-upper','wafer-lower')
        self.add_arc('rim-top',(16,35),(40,35),radius_x=12,radius_y=4)
        self.add_arc('rim-bottom',(40,35),(16,35),radius_x=12,radius_y=4)
        self.add_contour('rim','rim-top','rim-bottom',closed=True)
        self.add_arc('bowl',(40,35),(16,35),radius_x=12,radius_y=7)
        self.relate('connect','rim','bowl')
