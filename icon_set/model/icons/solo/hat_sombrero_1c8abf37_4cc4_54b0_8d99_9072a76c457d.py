"""Mirror the tapered crown about x=24, using tangent cubic shoulders; a broad curved brim reaches (4,38)-(44,38).
Construction: Lucide soup: tangent rounded lower enclosure, adapted to a wide brim.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '1c8abf37-4cc4-54b0-8d99-9072a76c457d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__sombrero/20260924T071425Z-thuan-mac/reference/hat sombrero_1c8abf37-4cc4-54b0-8d99-9072a76c457d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sombrero-solo'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "accessories"
    categories = ("primitives", "accessories")
    aliases = ()
    keywords = ('hat', 'sombrero')

    def build(self):
        # Symbol plan: Mirror the tapered crown about x=24, using tangent cubic shoulders; a broad curved brim reaches (4,38)-(44,38).
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('crown',(14,28),[('C',(24,10),(18,15),(18,10)),('C',(34,28),(30,10),(30,15))])
        p('brim',(4,28),[('L',(14,28)),('L',(34,28)),('L',(44,28)),('A',(34,38),10,10,True),('L',(14,38)),('A',(4,28),10,10,True)],True)
        join('crown','brim')

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
