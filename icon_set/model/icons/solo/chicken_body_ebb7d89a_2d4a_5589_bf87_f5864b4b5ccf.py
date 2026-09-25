"""A right-facing crested chicken with elongated neck, scooped back, rounded belly and visible beak; keep the foot as a distinct extension.
Construction: Lucide bird: circular head, curved belly and deliberate beak attachment.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'ebb7d89a-2d4a-5589-bf87-f5864b4b5ccf'
SOURCE_PATH = 'pictographic-primitives/animals/chicken body_ebb7d89a-2d4a-5589-bf87-f5864b4b5ccf.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crested-bird'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "animals"
    categories = ("animals", "primitives")
    aliases = ()
    keywords = ('chicken', 'body')

    def build(self):
        # Symbol plan: A right-facing crested chicken with elongated neck, scooped back, rounded belly and visible beak; keep the foot as a distinct extension.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('body',(12,25),[('C',(23,23),(20,28),(23,27)),('L',(23,16)),('A',(30,9),7,7,True),('A',(37,16),7,7,True),('C',(42,23),(40,17),(42,20)),('L',(37,23)),('L',(37,26)),('C',(25,36),(37,32),(32,36)),('C',(12,25),(18,36),(12,31))],True)
        p('tail',(6,21),[('L',(9,21)),('C',(12,25),(12,21),(12,23))]);join('tail','body')
        p('crest',(25,6),[('C',(30,9),(28,6),(30,7))]);join('crest','body')
        line('leg',(25,36),(25,42));join('leg','body')

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
