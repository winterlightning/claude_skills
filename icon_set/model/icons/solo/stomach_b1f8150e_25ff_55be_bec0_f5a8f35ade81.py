"""Stomach outline with a broad smooth gastric sac, a narrowed upper tube and an open lower outlet; replace abrupt elbow-like contours.
Construction: No useful Lucide stomach match; source supplies anatomy, with long coherent tangent curves.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b1f8150e-25ff-55be-bec0-f5a8f35ade81'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/specialty stomach_b1f8150e-25ff-55be-bec0-f5a8f35ade81.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'stomach'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/health"
    aliases = ()
    keywords = ('specialty', 'stomach')

    def build(self):
        # Symbol plan: Stomach outline with a broad smooth gastric sac, a narrowed upper tube and an open lower outlet; replace abrupt elbow-like contours.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('inner',(16,4),[('L',(16,12)),('C',(20,22),(16,17),(18,19)),('C',(12,30),(20,28),(16,29)),('C',(8,38),(8,31),(8,35)),('L',(8,44))])
        p('outer',(26,4),[('L',(26,10)),('C',(30,14),(26,14),(28,15)),('C',(40,24),(36,12),(40,18)),('C',(26,40),(40,34),(34,40)),('C',(21,38),(23,40),(23,39)),('C',(17,40),(18,36),(17,37)),('L',(17,44))])

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
