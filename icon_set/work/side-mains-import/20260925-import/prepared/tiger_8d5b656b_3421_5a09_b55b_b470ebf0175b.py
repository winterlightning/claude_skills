"""Fresh reference repair. Construction reference: Lucide cat (facial feature hierarchy); source bear anatomy.
Keyshape SQUARE; source identity is preserved separately from its icon name.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8d5b656b-3421-5a09-b55b-b470ebf0175b'
SOURCE_PATH = 'pictographic-primitives/animals/tiger_8d5b656b-3421-5a09-b55b-b470ebf0175b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'tiger-face'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('tiger',)

    def path(self,n,start,*steps,closed=False):
        here=start; ids=[]
        for i,step in enumerate(steps):
            kind,end,*v=step; name=f'{n}-{i}';ids.append(name)
            if kind=='L':self.add_line(name,here,end)
            elif kind=='A':self.add_arc(name,here,end,radius_x=v[0],radius_y=v[1],sweep=v[2])
            elif kind=='C':self.add_bezier(name,here,(v[0],v[1],end))
            here=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True),closed=True)

    def build(self):
        # Rounded feline head and ears, small angular nose, and a connected central tiger stripe.
        self.path('head',(6,12),('C',(12,6),(6,8),(8,6)),('C',(18,10),(15,6),(16,8)),('C',(24,8),(20,9),(22,8)),('C',(30,10),(26,8),(28,9)),('C',(36,6),(32,8),(33,6)),('C',(42,12),(40,6),(42,8)),('L',(42,26)),('C',(24,42),(42,36),(34,42)),('C',(6,26),(14,42),(6,36)),('L',(6,12)),closed=True)
        self.add_line('stripe',(24,8),(24,16));self.relate('connect','stripe','head')
        for n,x in [('left',15),('right',33)]:self.add_dot(n+'-eye',(x,22))
        self.add_polyline('nose',(20,29),(24,32),(28,29))
        self.add_line('stripe-left',(6,26),(12,30))
        self.add_line('stripe-right',(42,26),(36,30))
        self.relate('connect','stripe-left','head')
        self.relate('connect','stripe-right','head')

    icon_id = 'bear-muzzle-face'
    category = 'nature/animals'
    aliases = ()
    keywords = ('bear', 'face', 'head', 'muzzle', 'nose', 'animal', 'cute', 'wildlife')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
