"""Four circular proton/network nodes linked by three diagonal bonds; restore circular nodes and explicit shared attachment points.
Construction: Lucide disc-3: circular construction, with source arrangement and bond directions.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'a59dce1d-df8f-4b36-a178-738d4288393a'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__proton-preview/20260924T083118Z-thuan-mac/reference/proton preview_a59dce1d-df8f-4b36-a178-738d4288393a.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'proton-preview'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('proton', 'preview')

    def build(self):
        # Symbol plan: Four circular proton/network nodes linked by three diagonal bonds; restore circular nodes and explicit shared attachment points.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        def ring(n,x,y,r,extras=()):
         import math
         points=[(x,y-r),(x+r,y),(x,y+r),(x-r,y)]+list(extras)
         points.sort(key=lambda q:math.atan2(q[1]-y,q[0]-x))
         p(n,points[0],[('A',q,r,r,True) for q in points[1:]+points[:1]],True)
        ring('center',24,25,5,((21,21),(20,28),(28,22)))
        ring('upper',11,11,5,((14,15),))
        ring('lower',11,37,5,((15,34),))
        ring('right',38,14,4)
        for n,a,b,outer in [('up',(14,15),(21,21),'upper'),('down',(20,28),(15,34),'lower'),('right-bond',(28,22),(34,14),'right')]:
         line(n,a,b);join(n,'center');join(n,outer)

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
