"""Low whale with smooth back, rising tail, two flukes and a pectoral fin; water spout grows from the back. Preserve horizontal animal proportions.
Construction: Lucide bird: coherent animal silhouette; source supplies whale tail and spout.
Omissions: Omit the fine internal lower belly line to preserve open space.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '769eae2e-e0b1-5885-a663-304ba6167b21'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__spouting-whale/20260924T071425Z-thuan-mac/reference/whale body_769eae2e-e0b1-5885-a663-304ba6167b21.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'spouting-whale'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('whale', 'body')

    def build(self):
        # Symbol plan: Low whale with smooth back, rising tail, two flukes and a pectoral fin; water spout grows from the back. Preserve horizontal animal proportions.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('body',(4,29),[('C',(15,25),(5,26),(10,25)),('L',(20,25)),('L',(32,25)),('C',(36,21),(35,25),(36,24)),('C',(30,19),(36,19),(33,18)),('C',(38,15),(31,12),(35,13)),('C',(44,8),(38,10),(40,8)),('L',(44,25)),('C',(35,36),(44,30),(40,34)),('L',(37,40)),('C',(28,38),(33,40),(30,39)),('C',(4,29),(18,41),(7,35))],True)
        p('fin',(25,31),[('L',(28,38))]);join('fin','body')
        p('spout-left',(10,10),[('C',(20,17),(12,6),(18,8))])
        p('spout-right',(20,17),[('C',(30,10),(22,8),(28,6))]);join('spout-left','spout-right')
        line('spout-stem',(20,17),(20,25));join('spout-stem','spout-left');join('spout-stem','spout-right');join('spout-stem','body')

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
