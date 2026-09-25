"""Sputnik satellite with an exact circular body and three long antenna rods attached at integer points on that circle.
Construction: Lucide satellite: coherent body/antenna attachments; source determines spherical Sputnik body and unequal directional rods.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '78fe3b70-a677-407c-a689-55a0827b0ff4'
SOURCE_PATH = 'pictographic-primitives/science/sputnik_78fe3b70-a677-407c-a689-55a0827b0ff4.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'sputnik-satellite'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "science"
    aliases = ()
    keywords = ('sputnik',)

    def build(self):
        # Symbol plan: Sputnik satellite with an exact circular body and three long antenna rods attached at integer points on that circle.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('sphere',(29,6),[('A',(42,19),13,13,True),('A',(41,24),13,13,True),('A',(29,32),13,13,True),('A',(17,24),13,13,True),('A',(16,19),13,13,True),('A',(24,7),13,13,True),('A',(29,6),13,13,True)],True)
        for n,a,b in [('upper',(6,14),(24,7)),('lower-left',(6,42),(17,24)),('lower-right',(36,42),(41,24))]:
         line(n,a,b);join(n,'sphere')

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
