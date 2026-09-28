"""Copper IUD with mirrored curled arms, a banded stem, and a visible terminal ring on a short thread.
Construction: No exact Lucide IUD match; paired smooth curls and round terminal from the supplied reference.
Omissions: Reduce two stem bands to one for clean 8-unit spacing.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '8a3b31c3-a30d-46a8-90d3-db6b6580d6ed'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__copper-iud-rounded-arms/20260924T083118Z-thuan-mac/reference/copper iud_8a3b31c3-a30d-46a8-90d3-db6b6580d6ed.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'copper-iud-rounded-arms'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('copper', 'iud')

    def build(self):
        # Symbol plan: Copper IUD with mirrored curled arms, a banded stem, and a visible terminal ring on a short thread.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        for side in (-1,1):
         m=lambda x,y:(24+side*x,y)
         p('arm-'+str(side),m(12,17),[('C',m(18,12),m(17,17),m(18,15)),('C',m(12,6),m(18,8),m(16,6)),('C',(24,14),m(6,6),m(3,8))])
        p('stem',(20,16),[('A',(22,14),2,2,True),('L',(24,14)),('L',(26,14)),('A',(28,16),2,2,True),('L',(28,22)),('L',(28,28)),('A',(26,30),2,2,True),('L',(24,30)),('L',(22,30)),('A',(20,28),2,2,True),('L',(20,22)),('L',(20,16))],True)
        line('band',(20,22),(28,22));join('band','stem');join('arm--1','stem');join('arm-1','stem');join('arm--1','arm-1')
        p('terminal',(24,36),[('A',(24,42),3,3,True),('A',(24,36),3,3,True)],True)
        line('thread',(24,30),(24,36));join('thread','stem');join('thread','terminal')

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
