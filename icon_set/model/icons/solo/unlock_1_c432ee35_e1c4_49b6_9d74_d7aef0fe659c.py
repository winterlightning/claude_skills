"""Open shackle with a true semicircle and smooth rounded lower lock body; shared node at shackle attachment.
Construction: Lucide lock-open: semicircular open shackle and rounded rectangular body.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'c432ee35-e1c4-49b6-9d74-d7aef0fe659c'
SOURCE_PATH = 'pictographic-primitives/symbol/unlock 1_c432ee35-e1c4-49b6-9d74-d7aef0fe659c.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'unlock-1'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "symbol"
    categories = ("symbol",)
    aliases = ()
    keywords = ('unlock', '1')

    def build(self):
        # Symbol plan: Open shackle with a true semicircle and smooth rounded lower lock body; shared node at shackle attachment.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('body',(8,24),[('L',(14,24)),('L',(40,24)),('L',(40,38)),('A',(34,44),6,6,True),('L',(14,44)),('A',(8,38),6,6,True),('L',(8,24))],True)
        p('shackle',(14,24),[('L',(14,14)),('A',(34,14),10,10,True)])
        join('shackle','body')

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
