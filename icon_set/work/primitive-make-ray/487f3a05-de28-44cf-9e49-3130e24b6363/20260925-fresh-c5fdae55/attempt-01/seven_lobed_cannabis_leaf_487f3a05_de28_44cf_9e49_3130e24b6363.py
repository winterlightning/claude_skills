"""Seven pointed cannabis lobes around a tall narrow center leaflet. Mirror tapered curves while retaining deliberate sharp valleys and a short stem.
Construction: Lucide cannabis: seven coherent pointed lobes; taller central leaflet preserves the original proportions.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '487f3a05-de28-44cf-9e49-3130e24b6363'
SOURCE_PATH = 'pictographic-primitives/cannabis/cannabis_487f3a05-de28-44cf-9e49-3130e24b6363.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'seven-lobed-cannabis-leaf'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "cannabis"
    aliases = ()
    keywords = ('cannabis',)

    def build(self):
        # Seven lobes mirror about the centre axis; shorter lobes open the narrow valleys.
        self.mirror('leaf',(24,6),[('C',(29,20),(29,12),(30,16)),('C',(40,13),(33,16),(37,13)),('C',(34,27),(40,19),(37,24)),('C',(42,30),(38,27),(40,28)),('C',(32,34),(39,34),(35,34)),('C',(34,40),(33,36),(34,38)),('C',(24,36),(30,40),(26,38))])
        self.add_line('stem',(24,36),(24,42));self.relate('connect','stem','leaf')


    def path(self, name, start, commands, closed=False):
        members=[]
        for i,(kind,end,*args) in enumerate(commands):
            n=f'{name}-{i}'
            if kind=='L': self.add_line(n,start,end)
            elif kind=='A': self.add_arc(n,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(n,start,(args[0],args[1],end))
            members.append(n);start=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,n,x,y,rx,ry):
        self.path(n,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
    def mirror(self,n,start,commands,closed=True):
        axis=24
        m=lambda p:(2*axis-p[0],p[1])
        nodes=[start]+[c[1] for c in commands]
        rev=[]
        for i,c in reversed(list(enumerate(commands))):
            k,end,*args=c
            if k=='C':rev.append((k,m(nodes[i]),m(args[1]),m(args[0])))
            elif k=='A':rev.append((k,m(nodes[i]),*args))
            else:rev.append((k,m(nodes[i])))
        self.path(n,start,commands+rev,closed)
