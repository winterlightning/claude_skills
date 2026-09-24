"""A rising chart with two smooth dips; use a few coherent cubic curves instead of compressed short arc fragments.
Construction: Lucide chart-line: sparse readable axes; the source requires a smooth data curve.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '82b336ab-b6e2-5e37-a1d9-2432b628d6d6'
SOURCE_PATH = 'pictographic-primitives/business/graph lines_82b336ab-b6e2-5e37-a1d9-2432b628d6d6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rising-line-chart-with-two-dips'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "business"
    aliases = ()
    keywords = ('graph', 'lines')

    def build(self):
        # Symbol plan: A rising chart with two smooth dips; use a few coherent cubic curves instead of compressed short arc fragments.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('axes',(6,6),[('L',(6,38)),('A',(10,42),4,4,False),('L',(42,42))])
        p('data',(15,33),[('C',(22,23),(18,28),(19,19)),('C',(27,28),(24,24),(25,28)),('C',(35,14),(30,28),(30,14)),('C',(40,21),(37,14),(38,21)),('C',(42,18),(41,21),(42,20))])

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
