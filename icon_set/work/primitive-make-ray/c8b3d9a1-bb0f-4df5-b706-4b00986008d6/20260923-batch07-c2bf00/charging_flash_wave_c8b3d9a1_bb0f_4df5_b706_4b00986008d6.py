from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c8b3d9a1-bb0f-4df5-b706-4b00986008d6'
SOURCE_PATH = 'icon_set/work/todo-references/charging flash wave_c8b3d9a1-bb0f-4df5-b706-4b00986008d6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'charging-flash-wave'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('charging', 'flash', 'wave')

    def build(self):
        # Central closed bolt flanked by two mirrored wave pairs. Outer semicircles reachx4/44; bolt reachesy8/40. Equal nested wave radii.

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
        self.add_polyline('flash',(26,8),(16,26),(24,26),(22,40),(32,22),(24,22),closed=True)
        for side in [-1,1]:
            for name,x,rx,ry in [('outer',10,6,14),('inner',16,4,7)]:
                x = x if side<0 else 48-x
                self.add_arc(('left' if side<0 else 'right')+'-'+name,(x,24-ry),(x,24+ry),radius_x=rx,radius_y=ry,sweep=side>0)
