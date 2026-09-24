"""Mirrored pointed crab claws above a broad curved carapace, with paired raised arms and two pairs of splayed legs.
Construction: No useful Lucide crab match; mirrored coherent contour construction.
Omissions: Reduce three leg pairs to two, preserving large claws and the tapered shell.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '406a4e43-dd7b-4875-91ac-e8710df0dfae'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__crab-with-raised-claws/20260924T083118Z-thuan-mac/reference/crab_406a4e43-dd7b-4875-91ac-e8710df0dfae.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'crab-with-raised-claws-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('crab',)

    def build(self):
        # Symbol plan: Mirrored pointed crab claws above a broad curved carapace, with paired raised arms and two pairs of splayed legs.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('shell',(12,27),[('C',(24,23),(16,23),(20,23)),('C',(36,27),(28,23),(32,23)),('C',(33,35),(36,30),(35,33)),('C',(24,42),(30,39),(27,42)),('C',(15,35),(21,42),(18,39)),('C',(12,27),(13,33),(12,30))],True)
        for side in (-1,1):
         m=lambda x,y:(24+side*x,y)
         p('claw-'+str(side),m(9,6),[('C',m(18,12),m(14,6),m(18,8)),('C',m(13,17),m(18,16),m(16,17)),('C',m(6,12),m(9,17),m(7,14)),('L',m(10,12)),('L',m(6,8)),('C',m(9,6),m(6,7),m(7,6))],True)
         p('arm-'+str(side),m(13,17),[('C',m(12,27),m(13,22),m(13,24))]);join('arm-'+str(side),'claw-'+str(side));join('arm-'+str(side),'shell')
         line('upper-leg-'+str(side),m(12,27),m(18,32));line('lower-leg-'+str(side),m(9,35),m(18,42))
         join('upper-leg-'+str(side),'shell');join('upper-leg-'+str(side),'arm-'+str(side));join('lower-leg-'+str(side),'shell')

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
