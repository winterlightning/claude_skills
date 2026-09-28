"""Cloudberry with four rounded fruit regions and two spreading pointed leaves around a shared junction; retain center fruit rather than a generic cloud.
Construction: Lucide grape: a small set of legible fruit regions; leaf shape from supplied original.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7431aa93-ec98-4aa4-8564-823e23c54a49'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__cloudberry-with-spreading-leaves/20260924T071425Z-thuan-mac/reference/cloud berry_7431aa93-ec98-4aa4-8564-823e23c54a49.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'cloudberry-with-spreading-leaves-solo'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "food"
    categories = ("primitives", "food")
    aliases = ()
    keywords = ('cloud', 'berry')

    def build(self):
        # Symbol plan: Cloudberry with four rounded fruit regions and two spreading pointed leaves around a shared junction; retain center fruit rather than a generic cloud.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('center-fruit',(24,15),[('C',(31,26),(29,19),(31,22)),('C',(24,33),(31,29),(27,32)),('C',(17,26),(21,32),(17,29)),('C',(24,15),(17,22),(19,19))],True)
        p('outer-fruit',(17,26),[('C',(9,18),(11,25),(9,22)),('C',(17,13),(9,12),(13,10)),('C',(24,6),(17,8),(20,6)),('C',(31,13),(28,6),(31,8)),('C',(39,18),(35,10),(39,12)),('C',(31,26),(39,22),(37,25))])
        join('center-fruit','outer-fruit')
        for side in (-1,1):
         m=lambda x,y:(24+side*x,y)
         p('leaf-'+str(side),m(0,33),[('C',m(18,24),m(8,32),m(15,29)),('C',m(0,33),m(18,42),m(7,43))],True)
         join('leaf-'+str(side),'center-fruit')
        join('leaf--1','leaf-1')
        line('stem',(24,33),(24,42))
        for n in ('center-fruit','leaf--1','leaf-1'):join('stem',n)

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
