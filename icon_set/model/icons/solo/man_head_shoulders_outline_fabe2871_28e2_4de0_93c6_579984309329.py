"""Man head and shoulders as a single smooth open outline with a continuous neck, circular jaw arcs and rounded shoulder sweeps.
Construction: Human user.svg and full_body_ref.png: smooth head/shoulder construction. The original has a continuous neck, not a detached head.
Omissions: Omit tiny ear bumps; preserve the uninterrupted neck and open shoulder baseline.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'fabe2871-28e2-4de0-93c6-579984309329'
SOURCE_PATH = 'pictographic-primitives/photography/man_fabe2871-28e2-4de0-93c6-579984309329.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'man-head-shoulders-outline'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/photography"
    aliases = ()
    keywords = ('man',)

    def build(self):
        # Symbol plan: Man head and shoulders as a single smooth open outline with a continuous neck, circular jaw arcs and rounded shoulder sweeps.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('portrait',(8,44),[('C',(12,36),(8,40),(9,38)),('L',(20,32)),('L',(20,28)),('A',(14,16),14,14,True),('A',(34,16),10,12,True),('A',(28,28),14,14,True),('L',(28,32)),('L',(36,36)),('C',(40,44),(39,38),(40,40))])

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
