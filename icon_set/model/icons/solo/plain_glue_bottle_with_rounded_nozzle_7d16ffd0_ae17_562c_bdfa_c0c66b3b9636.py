"""Symmetric tapered glue bottle with a distinct cap collar, smoothly rounded base and a tapered rounded nozzle.
Construction: Lucide milk: a continuous bottle silhouette with deliberately joined cap sections.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '7d16ffd0-ae17-562c-bdfa-c0c66b3b9636'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/design/design tool paper glue_7d16ffd0-ae17-562c-bdfa-c0c66b3b9636.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'plain-glue-bottle-with-rounded-nozzle'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "design"
    categories = ("design", "primitives")
    aliases = ()
    keywords = ('design', 'tool', 'paper', 'glue')

    def build(self):
        # Symbol plan: Symmetric tapered glue bottle with a distinct cap collar, smoothly rounded base and a tapered rounded nozzle.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('body',(14,22),[('L',(34,22)),('C',(37,26),(36,22),(37,24)),('L',(40,38)),('A',(34,44),6,6,True),('L',(14,44)),('A',(8,38),6,6,True),('L',(11,26)),('C',(14,22),(11,24),(12,22))],True)
        p('collar',(14,22),[('L',(14,14)),('L',(18,14)),('L',(30,14)),('L',(34,14)),('L',(34,22))]);join('collar','body')
        p('nozzle',(18,14),[('L',(21,6)),('C',(24,4),(22,4),(23,4)),('C',(27,6),(25,4),(26,4)),('L',(30,14))]);join('nozzle','collar')

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
