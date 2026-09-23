from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '86ff6696-4ddd-4dd2-abe4-b1bbb2a48273'
SOURCE_PATH = 'icon_set/work/todo-references/charging battery flash empty_86ff6696-4ddd-4dd2-abe4-b1bbb2a48273.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'charging-battery-flash-empty'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('charging', 'battery', 'flash', 'empty')

    def build(self):
        # Broken battery enclosure around central closed lightning bolt with left charge bar and attached right terminal. x4/44 y8/40.

        def circle(n,x,y,r):
            self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
            self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
            self.add_contour(n,n+'-a',n+'-b',closed=True)
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
        self.add_polyline('battery-left',(16,12),(8,12),(4,16),(4,32),(8,36),(14,36))
        self.add_polyline('battery-right',(30,12),(36,12),(36,20),(36,28),(36,36),(28,36))
        self.add_polyline('terminal',(36,20),(44,20),(44,28),(36,28))
        self.relate('connect','battery-right','terminal')
        self.add_polyline('flash',(26,8),(14,26),(22,26),(20,40),(32,22),(24,22),closed=True)
        self.add_line('charge-bar',(12,21),(12,27))
