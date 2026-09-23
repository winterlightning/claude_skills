from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '9a4c5ce8-1c07-4186-90bf-51f1f80db709'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_11/charging battery empty 1_9a4c5ce8-1c07-4186-90bf-51f1f80db709.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'empty-battery-symbol'
    keyshape = Keyshape.HRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('empty', 'battery', 'symbol')

    def build(self):
        # Empty horizontal battery with integral right terminal. One continuous contour; body corner radius4, terminal radius4, mirror axis y24. HRECT_M ink (2,8)-(46,40).
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
        self.add_line('top',(8,10),(32,10))
        self.add_arc('tr',(32,10),(36,14),radius_x=4)
        self.add_polyline('upper-step',(36,14),(36,20),(40,20))
        self.add_arc('terminal',(40,20),(40,28),radius_x=4)
        self.add_polyline('lower-step',(40,28),(36,28),(36,34))
        self.add_arc('br',(36,34),(32,38),radius_x=4)
        self.add_line('bottom',(32,38),(8,38))
        self.add_arc('bl',(8,38),(4,34),radius_x=4)
        self.add_line('left',(4,34),(4,14))
        self.add_arc('tl',(4,14),(8,10),radius_x=4)
        # Polyline steps remain coherent separate paths joined at their actual endpoints.
        for a,b in [('top','tr'),('tr','upper-step'),('upper-step','terminal'),('terminal','lower-step'),('lower-step','br'),('br','bottom'),('bottom','bl'),('bl','left'),('left','tl'),('tl','top')]:
            self.relate('connect',a,b)
