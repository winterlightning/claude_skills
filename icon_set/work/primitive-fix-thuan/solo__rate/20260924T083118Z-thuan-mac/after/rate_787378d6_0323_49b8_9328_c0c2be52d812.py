"""An exact symmetric diamond divided horizontally at its widest points; remove small off-grid jogs and the uneven top seam.
Construction: No useful exact Lucide rate symbol; use a shared center and equal diamond diagonals.
Omissions: None.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '787378d6-0323-49b8-9328-c0c2be52d812'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__rate/20260924T083118Z-thuan-mac/reference/rate_787378d6-0323-49b8-9328-c0c2be52d812.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'rate'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('rate',)

    def build(self):
        # Symbol plan: An exact symmetric diamond divided horizontally at its widest points; remove small off-grid jogs and the uneven top seam.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        poly('diamond',(6,24),(24,6),(42,24),(24,42),closed=True)
        line('divider',(6,24),(42,24));join('divider','diamond')

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
