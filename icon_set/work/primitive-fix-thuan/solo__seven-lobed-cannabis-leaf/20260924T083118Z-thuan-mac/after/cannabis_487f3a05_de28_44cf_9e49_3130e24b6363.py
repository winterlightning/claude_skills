"""Seven pointed cannabis lobes around a tall narrow center leaflet. Mirror tapered curves while retaining deliberate sharp valleys and a short stem.
Construction: Lucide cannabis: seven coherent pointed lobes; taller central leaflet preserves the original proportions.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '487f3a05-de28-44cf-9e49-3130e24b6363'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__seven-lobed-cannabis-leaf/20260924T083118Z-thuan-mac/reference/cannabis_487f3a05-de28-44cf-9e49-3130e24b6363.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'seven-lobed-cannabis-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('cannabis',)

    def build(self):
        # Symbol plan: Seven pointed cannabis lobes around a tall narrow center leaflet. Mirror tapered curves while retaining deliberate sharp valleys and a short stem.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        self.mirror('leaf',(24,4),[('C',(27,24),(29,12),(29,18)),('C',(38,14),(31,19),(35,15)),('C',(31,29),(38,21),(34,26)),('C',(40,32),(35,29),(38,30)),('C',(30,35),(37,35),(33,36)),('C',(32,41),(31,37),(32,39)),('C',(24,37),(28,41),(26,39))])
        line('stem',(24,37),(24,44));join('stem','leaf')

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
