"""Redo arrow made from two tangent quarter-circle arcs and one smooth shoulder, with a right-angle arrowhead.
Construction: Lucide redo: coherent curved shaft with an explicit arrowhead junction.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'bdd5c523-073c-40e4-bb23-2bca55ba830d'
SOURCE_PATH = 'pictographic-primitives/interface-essential/redo_bdd5c523-073c-40e4-bb23-2bca55ba830d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'redo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('redo',)

    def build(self):
        # Symbol plan: Redo arrow made from two tangent quarter-circle arcs and one smooth shoulder, with a right-angle arrowhead.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('sweep',(26,44),[('A',(8,26),18,18,True),('A',(26,8),18,18,True),('C',(40,14),(32,8),(36,10))])
        poly('arrowhead',(40,4),(40,14),(30,14));join('arrowhead','sweep')

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
