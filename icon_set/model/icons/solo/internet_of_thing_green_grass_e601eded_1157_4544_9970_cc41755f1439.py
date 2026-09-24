"""Three open ring nodes with a diagonal inward arrow and a flowing lower U connection. Enlarge nodes and align arrow shaft on a true diagonal.
Construction: Lucide settings circular outline principle; source determines node and arrow arrangement.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e601eded-1157-4544-9970-cc41755f1439'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__merge-arrow-nodes/20260924T071425Z-thuan-mac/reference/internet of thing green grass_e601eded-1157-4544-9970-cc41755f1439.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'merge-arrow-nodes-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('internet', 'of', 'thing', 'green', 'grass')

    def build(self):
        # Symbol plan: Three open ring nodes with a diagonal inward arrow and a flowing lower U connection. Enlarge nodes and align arrow shaft on a true diagonal.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        for n,x,y in [('source',10,10),('upper',36,10),('lower',10,29)]:oval(n,x,y,4,4)
        p('arrow',(14,10),[('L',(28,26))])
        poly('arrow-head',(22,26),(28,26),(28,20));join('arrow','arrow-head');join('arrow','source')
        p('loop',(36,14),[('C',(42,26),(40,17),(42,21)),('C',(27,42),(42,37),(37,42)),('C',(10,33),(19,42),(10,39))]);join('loop','upper');join('loop','lower')

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
