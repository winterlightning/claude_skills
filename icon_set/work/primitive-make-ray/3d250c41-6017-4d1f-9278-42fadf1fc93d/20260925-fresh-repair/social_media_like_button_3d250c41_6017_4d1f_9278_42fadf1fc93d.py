from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='3d250c41-6017-4d1f-9278-42fadf1fc93d'
SOURCE_PATH='pictographic-primitives/other/rectangle like text_3d250c41-6017-4d1f-9278-42fadf1fc93d.svg'
AUTHOR='gpt-6'
PLAN='All four LIKE letters remain in source order inside a rounded horizontal button; taller E strokes cure the old row spacing.'
CONSTRUCTION_REFERENCES='Lucide rectangle-ellipsis original and atomic-debug: rounded horizontal enclosure; supplied reference governs LIKE.'
OMISSIONS=['I serifs omitted.']
class Drawing(Solo48):
    icon_id='social-media-like-button'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('rectangle', 'like', 'text')

    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x,y-r),r,r,True),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,k=4):
        self.path(n,(l+k,t),[('L',(r-k,t)),('A',(r,t+k),k,k,True),('L',(r,b-k)),('A',(r-k,b),k,k,True),('L',(l+k,b)),('A',(l,b-k),k,k,True),('L',(l,t+k)),('A',(l+k,t),k,k,True)],True)

    def build(self):
        # Preserve every letter and its source order; taller strokes cure the old E rows.
        self.box('frame',4,8,44,40,4)
        self.add_polyline('l',(10,16),(10,32),(14,32))
        self.add_line('i',(19,16),(19,32))
        self.add_polyline('k-stem',(24,16),(24,24),(24,32));self.add_polyline('k-arms',(28,16),(24,24),(28,32));self.relate('connect','k-stem','k-arms')
        self.add_polyline('e',(38,16),(33,16),(33,24),(33,32),(38,32));self.add_line('e-middle',(33,24),(38,24));self.relate('connect','e','e-middle')
