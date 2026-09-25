"""Bengal cat face with tall rounded ears, soft cheeks and tapered chin; mirror one side to avoid uneven jaws.
Construction: Lucide cat: coherent mirrored ear/cheek outline.
Omissions: No added eyes; reference has only the small nose/mouth mark.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7702e4e2-e41d-5abb-87f2-54692461fd5d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__bengal-cat-face/20260924T071425Z-thuan-mac/reference/bengal_7702e4e2-e41d-5abb-87f2-54692461fd5d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'bengal-cat-face-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "pets"
    categories = ("pets", "primitives")
    aliases = ()
    keywords = ('bengal',)

    def build(self):
        # Symbol plan: Bengal cat face with tall rounded ears, soft cheeks and tapered chin; mirror one side to avoid uneven jaws.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        self.mirror('head',(24,16),[('C',(31,17),(27,16),(29,16)),('C',(39,6),(35,12),(37,6)),('C',(42,10),(41,6),(42,7)),('C',(39,25),(42,15),(40,21)),('C',(34,35),(42,30),(39,33)),('C',(24,42),(31,39),(29,42))])
        p('mouth',(21,30),[('L',(24,27)),('L',(27,30))])
        line('nose',(24,25),(24,27));join('nose','mouth')

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
