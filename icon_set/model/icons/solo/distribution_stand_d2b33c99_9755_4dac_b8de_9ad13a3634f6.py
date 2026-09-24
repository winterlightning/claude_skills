"""Two bent electrical terminals with real cross arms over a rounded open-bottom housing; panel divided into two roomy cells.
Construction: Lucide smartphone: coherent rounded housing; no exact terminal match.
Omissions: Inset panel reduced from three sections to two to maintain 8-unit centerline bands.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'd2b33c99-9755-4dac-b8de-9ad13a3634f6'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__arched-distribution-stand-with-crossed-terminals/20260924T071425Z-thuan-mac/reference/distribution stand_d2b33c99-9755-4dac-b8de-9ad13a3634f6.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'arched-distribution-stand-with-crossed-terminals-solo'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('distribution', 'stand')

    def build(self):
        # Symbol plan: Two bent electrical terminals with real cross arms over a rounded open-bottom housing; panel divided into two roomy cells.
        p=self.path; oval=self.oval; line=self.add_line; poly=self.add_polyline; dot=self.add_dot
        join=lambda a,b:self.relate("connect",a,b)
        p('housing',(8,44),[('L',(8,22)),('A',(12,18),4,4,True),('L',(14,18)),('L',(30,18)),('L',(36,18)),('A',(40,22),4,4,True),('L',(40,44))])
        for j,x in enumerate((20,36)):
         p(f'terminal-{j}',(x-6,18),[('L',(x-6,10)),('A',(x-2,6),4,4,True),('L',(x,6)),('L',(x+4,6))])
         p(f'cross-{j}',(x,4),[('L',(x,6)),('L',(x,10))])
         join(f'terminal-{j}',f'cross-{j}');join(f'terminal-{j}','housing')
        p('panel',(17,35),[('L',(17,27)),('L',(31,27)),('L',(31,35)),('L',(31,44)),('L',(17,44)),('L',(17,35))],True)
        line('division',(17,35),(31,35));join('division','panel')

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
