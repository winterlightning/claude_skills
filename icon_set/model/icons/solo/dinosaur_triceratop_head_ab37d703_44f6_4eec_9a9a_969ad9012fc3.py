"""Triceratops profile with large rounded frill, two visible horns, hooked beak and a short neck; remove polygonal kinks from the face and frill.
Construction: Lucide bird: coherent curved animal contour; no useful dinosaur match.
Omissions: Omit the added eye absent from the original; keep horn and frill silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ab37d703-44f6-4eec-9a9a-969ad9012fc3'
SOURCE_PATH = 'pictographic-primitives/animals/dinosaur triceratop head_ab37d703-44f6-4eec-9a9a-969ad9012fc3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'triceratops-head-side'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('dinosaur', 'triceratop', 'head')

    def build(self):
        # Symbol plan: Triceratops profile with large rounded frill, two visible horns, hooked beak and a short neck; remove polygonal kinks from the face and frill.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('head',(31,6),[('C',(42,23),(38,10),(42,17)),('C',(28,37),(42,31),(36,37)),('C',(14,35),(22,37),(18,35)),('L',(7,32)),('L',(12,28)),('L',(6,28)),('C',(9,21),(6,25),(7,22)),('C',(7,12),(7,18),(6,15)),('C',(15,21),(9,17),(12,20)),('L',(26,21)),('C',(22,7),(26,15),(25,11)),('C',(32,21),(28,10),(31,15)),('C',(31,6),(36,20),(31,14))],True)
        p('neck',(28,37),[('C',(35,42),(29,39),(32,41))]);join('neck','head')

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
