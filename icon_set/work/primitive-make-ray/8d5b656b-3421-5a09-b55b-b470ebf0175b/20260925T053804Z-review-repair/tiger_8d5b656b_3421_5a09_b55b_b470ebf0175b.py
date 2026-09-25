"""Fresh reference repair. Construction reference: Lucide cat (facial feature hierarchy); source bear anatomy.
Keyshape SQUARE; source identity is preserved separately from its icon name.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8d5b656b-3421-5a09-b55b-b470ebf0175b'
SOURCE_PATH = 'pictographic-primitives/animals/tiger_8d5b656b-3421-5a09-b55b-b470ebf0175b.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'bear-muzzle-face'
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

        # Open round cheeks surround a large muzzle; the ear lobes belong to the outer silhouette.
        self.path('head',(6,34),('C',(10,18),(6,26),(8,22)),('C',(6,12),(8,17),(6,15)),('C',(12,6),(6,8),(8,6)),('C',(18,10),(15,6),(16,8)),('C',(24,8),(20,9),(22,8)),('C',(30,10),(26,8),(28,9)),('C',(36,6),(32,8),(33,6)),('C',(42,12),(40,6),(42,8)),('C',(38,18),(42,15),(40,17)),('C',(42,34),(40,22),(42,26)))
        for n,x in [('left',18),('right',30)]:self.add_dot(n+'-eye',(x,19))
        # The nose blends into two round muzzle cheeks instead of a disconnected mark.
        self.path('muzzle',(20,27),('A',(24,31),4,4,False),('A',(28,27),4,4,False),('C',(32,35),(30,28),(32,32)),('A',(24,42),8,7,True),('A',(16,35),8,7,True),('C',(20,27),(16,32),(18,28)),closed=True)
