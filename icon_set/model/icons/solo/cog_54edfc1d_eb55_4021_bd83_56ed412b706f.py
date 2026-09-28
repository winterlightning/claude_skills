"""Seven broad gear teeth on a rotationally balanced polygon; use one authored vertex series instead of uneven mirrored six-tooth zigzags.
Construction: Lucide settings: repeated tooth/valley rhythm.
Omissions: Omit the nearly invisible source center speck; preserve the solid gear silhouette.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '54edfc1d-eb55-4021-bd83-56ed412b706f'
SOURCE_PATH = 'pictographic-primitives/interface-essential/cog_54edfc1d-eb55-4021-bd83-56ed412b706f.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cog-54edfc1d'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    categories = ("interface-essential", "primitives")
    aliases = ()
    keywords = ('cog',)

    def build(self):
        # Symbol plan: Seven broad gear teeth on a rotationally balanced polygon; use one authored vertex series instead of uneven mirrored six-tooth zigzags.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        # Seven teeth: common angular spacing, rounded integer vertices.
        import math
        vertices=[]
        for tooth in range(7):
         for angle_offset,radius in ((-8,19),(8,19),(15,14),(36,14)):
          angle=math.radians(-90+tooth*360/7+angle_offset)
          vertices.append((24+round(18*radius/19*math.cos(angle)),24+round(radius*math.sin(angle))))
        vertices[0]=(vertices[0][0],6);vertices[1]=(vertices[1][0],6)
        poly('gear',*vertices,closed=True)

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
