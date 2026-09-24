"""Low roadster with two equal wheels, rounded hood and a broader triangular windscreen; wheel rims remain uninterrupted at body joins.
Construction: Lucide car (inspected in prior batch): coherent side body and shared wheel attachment nodes.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '269607c3-5f5c-5934-b3a2-328e079b9643'
SOURCE_PATH = 'pictographic-primitives/transportation/car convertible_269607c3-5f5c-5934-b3a2-328e079b9643.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'roadster-convertible'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/transportation"
    aliases = ()
    keywords = ('car', 'convertible')

    def build(self):
        # Symbol plan: Low roadster with two equal wheels, rounded hood and a broader triangular windscreen; wheel rims remain uninterrupted at body joins.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        for n,x in [('rear',12),('front',36)]:oval(n,x,32,6,6)
        p('body',(6,32),[('L',(4,32)),('L',(4,26)),('A',(9,21),5,5,True),('L',(20,21)),('L',(34,21)),('C',(44,29),(39,21),(44,25)),('L',(44,32)),('L',(42,32))])
        line('chassis',(18,32),(30,32))
        for n in ('rear','front'):join('body',n);join('chassis',n)
        poly('windscreen',(20,21),(16,10),(34,21));join('windscreen','body')

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
