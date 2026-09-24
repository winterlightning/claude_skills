"""Six rounded lobes with smooth alternating convex and concave shoulders; mirror both axes using one upper-right definition.
Construction: Lucide settings: tangent alternating convex and concave lobes.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e3d63c1e-a685-484b-8eae-ef88e3411b1e'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/interface-essential/cog_e3d63c1e-a685-484b-8eae-ef88e3411b1e.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'six-lobed-cog-e3d63c1e-a685-484b-8eae-ef88e3411b1e'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "interface-essential"
    aliases = ()
    keywords = ('cog',)

    def build(self):
        # Symbol plan: Six rounded lobes with smooth alternating convex and concave shoulders; mirror both axes using one upper-right definition.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        q=[('C',(32,14),(28,6),(28,14)),('C',(42,16),(36,14),(42,10)),('C',(37,24),(42,20),(37,21)),('C',(42,32),(37,27),(42,28)),('C',(32,34),(42,38),(36,34)),('C',(24,42),(28,34),(28,42))]
        self.mirror('gear',(24,6),q)
        line('center-mark',(24,23),(24,25))

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
