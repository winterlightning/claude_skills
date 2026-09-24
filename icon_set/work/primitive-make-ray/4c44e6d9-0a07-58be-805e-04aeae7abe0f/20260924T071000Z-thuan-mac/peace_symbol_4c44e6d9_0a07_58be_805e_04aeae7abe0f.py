"""Circular peace emblem with a vertical stem and two downward diagonal branches.
Symbol plan: shared parameters and coherent contours.
Construction: No useful exact Lucide match; exact circle and shared junction.
Omissions: None
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='4c44e6d9-0a07-58be-805e-04aeae7abe0f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__peace-symbol/20260924T065933Z-thuan-mac/reference/peace_4c44e6d9-0a07-58be-805e-04aeae7abe0f.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='peace-symbol'
    keyshape=Keyshape.CIRCLE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=('peace', 'symbol')

    def path(self,name,start,commands,closed=False):
        members=[]; here=start
        for i,cmd in enumerate(commands):
            kind,end,*args=cmd; ident=f'{name}-{i}'
            if kind=='L': self.add_line(ident,here,end)
            else: self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            members.append(ident); here=end
        self.add_contour(name,*members,closed=closed)
    def oval(self,name,x,y,rx,ry=None):
        ry=rx if ry is None else ry
        self.path(name,(x-rx,y),[('A',(x+rx,y),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)

    def build(self):
        # All ring nodes lie on radius20 about (24,24), using 12/16/20 triangles.
        nodes=[(24,4),(44,24),(36,40),(24,44),(12,40),(4,24),(24,4)]
        self.path('rim',nodes[0],[('A',p,20,20,True) for p in nodes[1:]],True)
        for n,p in [('top',(24,4)),('bottom',(24,44)),('left',(12,40)),('right',(36,40))]:
            self.add_line(n,(24,24),p);self.relate('connect',n,'rim')
        for i,a in enumerate(['top','bottom','left','right']):
            for b in ['top','bottom','left','right'][i+1:]:self.relate('connect',a,b)
