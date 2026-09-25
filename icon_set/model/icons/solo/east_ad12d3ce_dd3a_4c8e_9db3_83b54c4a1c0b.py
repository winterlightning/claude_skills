from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b'
SOURCE_PATH='pictographic-primitives/weather/east_ad12d3ce-dd3a-4c8e-9db3-83b54c4a1c0b.svg'
AUTHOR='gpt-6'
PLAN='East compass with northeast needle and E below-left, offset to open spacing. VRECT_M10,4–38,44. E bars8 apart; needle meets rim at exact6-8-10 node. Lucide compass circular housing and directional needle; minor cardinal ticks omitted.'
class Drawing(Solo48):
    icon_id='east'
    keyshape=Keyshape.VRECT_M
    semantic_role="MAIN"
    semantic_kind="noun"
    category = "weather"
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def box(self,n,l,t,r,b,q=3):
        pts=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q)]
        ids=[]
        for k in range(8):
            ident=f'{n}-{k}';ids.append(ident)
            if k%2:self.add_arc(ident,pts[k],pts[(k+1)%8],radius_x=q)
            else:self.add_line(ident,pts[k],pts[(k+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):
        pts=[(28,4),(34,6),(38,14),(28,24),(18,14),(28,4)]
        for i,(a,b) in enumerate(zip(pts,pts[1:])):self.add_arc(f'rim-{i}',a,b,radius_x=10)
        self.add_contour('rim',*(f'rim-{i}' for i in range(5)),closed=True)
        self.add_line('needle',(24,20),(34,6));self.relate('connect','needle','rim')
        self.add_polyline('arrowhead',(28,8),(34,6),(34,12));self.relate('connect','arrowhead','needle');self.relate('connect','arrowhead','rim')
        self.add_polyline('letter-e',(16,28),(10,28),(10,36),(10,44),(16,44))
        self.add_line('e-middle',(10,36),(16,36));self.relate('connect','letter-e','e-middle')
