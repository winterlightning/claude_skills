"""Two rotationally matched synchronization arrows, each a smooth broad arc ending in an open right-angle head.
Construction: Lucide refresh-cw: rotationally matched smooth arcs and clear open arrowheads.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '180d4acb-d66a-4301-9e3b-037ca7e80db1'
SOURCE_PATH = 'pictographic-primitives/interface-essential/synchronize arrows_180d4acb-d66a-4301-9e3b-037ca7e80db1.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'synchronize-arrows'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('synchronize', 'arrows')

    def build(self):
        # Symbol plan: Two rotationally matched synchronization arrows, each a smooth broad arc ending in an open right-angle head.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        for j,flip in enumerate((False,True)):
         m=lambda q:(48-q[0],48-q[1]) if flip else q
         p('arc-'+str(j),m((6,26)),[('A',m((24,6)),18,20,True),('C',m((40,14)),m((31,6)),m((36,9)))])
         poly('head-'+str(j),m((38,6)),m((40,14)),m((32,14)));join('head-'+str(j),'arc-'+str(j))

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
