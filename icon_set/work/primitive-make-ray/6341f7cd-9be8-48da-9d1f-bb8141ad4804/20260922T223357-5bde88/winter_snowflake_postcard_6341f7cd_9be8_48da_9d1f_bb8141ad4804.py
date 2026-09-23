from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '6341f7cd-9be8-48da-9d1f-bb8141ad4804'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/christmas postcard 2_6341f7cd-9be8-48da-9d1f-bb8141ad4804.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'winter-snowflake-postcard'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('winter', 'snowflake', 'postcard')

    def build(self):
        # Postcard enclosure with branched snowflake at left, vertical divider and stamp circle over address rules at right. Shared snowflake axis(15,24) and branch offsets; HRECT_L visible(2,6)-(46,42).
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
        rounded('card',4,8,44,40,3)
        self.add_line('divider',(26,15),(26,33))
        self.add_polyline('flake-v',(15,16),(15,20),(15,24),(15,28),(15,32))
        self.add_polyline('flake-h',(8,24),(11,24),(15,24),(19,24),(22,24))
        self.relate('connect','flake-v','flake-h')
        for n,pts,parent in [
        ('north',[(12,18),(15,20),(18,18)],'flake-v'),
        ('south',[(12,30),(15,28),(18,30)],'flake-v'),
        ('west',[(9,21),(11,24),(9,27)],'flake-h'),
        ('east',[(21,21),(19,24),(21,27)],'flake-h')]:
            self.add_polyline(n,*pts);self.relate('connect',n,parent)
        circle('stamp',35,18,3)
        for i in range(2):self.add_line(f'address-{i}',(32,28+6*i),(39,28+6*i))
