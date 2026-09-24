"""Sloped upper panel, round control and softened body corners, symmetric about x=24; seam attachment nodes explicitly shared.
Construction: Lucide air-vent: simple slat and coherent rounded housing.
Omissions: Flattened the top vent to a single open slat so its small hole cannot fill in.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e3b1dda5-6739-48a8-9b7e-aa74e8a061ed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__air-purifier-with-sloped-top-vent-and-round-control/20260924T071425Z-thuan-mac/reference/air purifier 3_e3b1dda5-6739-48a8-9b7e-aa74e8a061ed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'air-purifier-with-sloped-top-vent-and-round-control'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('air', 'purifier', '3')

    def build(self):
        # Symbol plan: Sloped upper panel, round control and softened body corners, symmetric about x=24; seam attachment nodes explicitly shared.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('body',(8,21),[('L',(12,7)),('C',(16,4),(13,4),(14,4)),('L',(32,4)),('C',(36,7),(34,4),(35,4)),('L',(40,21)),('L',(40,38)),('A',(34,44),6,6,True),('L',(14,44)),('A',(8,38),6,6,True),('L',(8,21))],True)
        line('seam',(8,21),(40,21));join('seam','body')
        line('vent',(21,13),(27,13))
        oval('control',24,32,3,3)

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
