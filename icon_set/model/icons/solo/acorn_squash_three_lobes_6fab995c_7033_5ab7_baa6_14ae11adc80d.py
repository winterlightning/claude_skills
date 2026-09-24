"""Three-lobed squash with a full-height central oval rib and smooth paired outer lobes, replacing disconnected short marks.
Construction: Lucide apple: coherent organic silhouette and curved attached stem.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '6fab995c-7033-5ab7-baa6-14ae11adc80d'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/food/acornsquash_6fab995c-7033-5ab7-baa6-14ae11adc80d.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'acorn-squash-three-lobes'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    aliases = ()
    keywords = ('acornsquash',)

    def build(self):
        # Symbol plan: Three-lobed squash with a full-height central oval rib and smooth paired outer lobes, replacing disconnected short marks.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('center',(24,12),[('A',(24,42),9,15,True),('A',(24,12),9,15,True)],True)
        p('outside',(24,12),[('C',(6,25),(12,7),(6,15)),('C',(24,42),(6,38),(15,42)),('C',(42,25),(33,42),(42,38)),('C',(24,12),(42,15),(36,7))],True);join('center','outside')
        p('stem',(24,12),[('C',(28,6),(24,8),(25,6))]);join('stem','center');join('stem','outside')

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
