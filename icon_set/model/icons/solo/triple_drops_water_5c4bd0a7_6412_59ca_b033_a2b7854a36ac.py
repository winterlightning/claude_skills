"""Three matched pointed droplets arranged in a triangle; smoothly curved shoulders meet round lower bowls without kinks.
Construction: Lucide droplet (inspected in prior batch): curved sides tangent to the lower circular bowl; one repeated shape owns all drops.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '5c4bd0a7-6412-59ca-b033-a2b7854a36ac'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__three-pointed-water-drops-in-triangular-group/20260924T083118Z-thuan-mac/reference/triple drops water_5c4bd0a7-6412-59ca-b033-a2b7854a36ac.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'three-pointed-water-drops-in-triangular-group-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "ecology"
    categories = ("primitives", "ecology")
    aliases = ()
    keywords = ('triple', 'drops', 'water')

    def build(self):
        # Symbol plan: Three matched pointed droplets arranged in a triangle; smoothly curved shoulders meet round lower bowls without kinks.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        for n,x,t in [('top',24,6),('left',12,26),('right',36,26)]:
         p(n,(x,t),[('C',(x+6,t+10),(x+2,t+3),(x+6,t+7)),('A',(x,t+16),6,6,True),('A',(x-6,t+10),6,6,True),('C',(x,t),(x-6,t+7),(x-2,t+3))],True)

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
