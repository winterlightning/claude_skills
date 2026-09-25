"""Turntable with a rounded deck, circular platter and diagonal tonearm crossing the rim, as in the reference. Preserve 9-unit clearance between platter and deck.
Construction: Lucide disc-3: circular platter; Lucide smartphone: consistent rounded housing corners.
Omissions: Spindle reduced to tonearm endpoint; omit tiny lower-right indicator to keep the deck clear.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'e9cd57fe-7fff-4612-94f9-7ee4f0e25305'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__record-turntable/20260924T083118Z-thuan-mac/reference/turntable 1_e9cd57fe-7fff-4612-94f9-7ee4f0e25305.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'record-turntable-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "computers"
    aliases = ()
    keywords = ('turntable', '1')

    def build(self):
        # Symbol plan: Turntable with a rounded deck, circular platter and diagonal tonearm crossing the rim, as in the reference. Preserve 9-unit clearance between platter and deck.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('deck',(10,6),[('L',(38,6)),('A',(42,10),4,4,True),('L',(42,38)),('A',(38,42),4,4,True),('L',(10,42)),('A',(6,38),4,4,True),('L',(6,10)),('A',(10,6),4,4,True)],True)
        oval('platter',24,24,9,9)
        # The source tonearm crosses the platter rim, rather than ending at it.
        # Length sqrt(8^2+9^2)>9 proves a real rim intersection on this ray.
        line('tonearm',(24,24),(16,33));join('tonearm','platter')

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
