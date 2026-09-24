"""Circular synchronization arrows with a diagonal magnifying handle; use a circular lower-right arc and an exact handle attachment point.
Construction: Lucide refresh-cw and search: smooth circular arrows and a handle with a true shared node.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'df40480b-5166-4148-8ffb-4e38ec361c58'
SOURCE_PATH = 'pictographic-primitives/interface-essential/synchronize arrows search_df40480b-5166-4148-8ffb-4e38ec361c58.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'synchronize-arrows-search'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('synchronize', 'arrows', 'search')

    def build(self):
        # Symbol plan: Circular synchronization arrows with a diagonal magnifying handle; use a circular lower-right arc and an exact handle attachment point.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('left-arc',(22,6),[('A',(7,21),15,15,False),('A',(10,30),15,15,False)])
        poly('left-head',(10,22),(10,30),(6,30));join('left-head','left-arc')
        p('right-arc',(34,12),[('A',(37,21),15,15,True),('A',(31,33),15,15,True),('A',(22,36),15,15,True)])
        poly('right-head',(34,20),(34,12),(42,12));join('right-head','right-arc')
        line('handle',(31,33),(42,42));join('handle','right-arc')

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
