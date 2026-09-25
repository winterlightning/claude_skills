"""An open droplet at upper left and three elliptical blood cells. Keep oval cell silhouettes instead of the rejected circular substitutions.
Construction: Lucide droplet: continuous curved sides; open source boundary preserved.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e0f429e8-98d9-41b6-ba6b-bd9d729862db'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/health/red blood cells_e0f429e8-98d9-41b6-ba6b-bd9d729862db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'blood-drop-with-cells'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "health"
    categories = ("health", "primitives")
    aliases = ()
    keywords = ('red', 'blood', 'cells')

    def build(self):
        # Symbol plan: An open droplet at upper left and three elliptical blood cells. Keep oval cell silhouettes instead of the rejected circular substitutions.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('drop',(10,26),[('C',(6,20),(7,25),(6,23)),('C',(14,6),(6,15),(10,10)),('C',(21,15),(17,9),(20,12))])
        oval('upper-cell',36,15,6,4)
        oval('middle-cell',15,38,5,4)
        oval('lower-cell',36,38,6,4)

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
