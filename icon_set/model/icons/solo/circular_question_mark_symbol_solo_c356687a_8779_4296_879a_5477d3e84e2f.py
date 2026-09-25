"""Circular help symbol with a smooth question hook, short descending stem and separate dot. Radius20 outer circle; centered question.
Construction reference: Lucide circle-question-mark: smooth hook and clear dot.
Omissions: None.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='c356687a-8779-4296-879a-5477d3e84e2f'
SOURCE_PATH='pictographic-primitives/other/circle question_c356687a-8779-4296-879a-5477d3e84e2f.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'circular-question-mark-symbol-solo'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('circle', 'question')
    def build(self):
        self.circle('outline',24,24,20)
        self.path('question',(18,19),[('A',(30,19),6,6,True),('C',(24,26),(30,23),(24,22))])
        self.add_dot('dot',(24,34))

    def path(self, name, start, commands, closed=False):
        members=[]
        for i,c in enumerate(commands):
            ident=f'{name}-{i}'
            if c[0]=='L': end=c[1];self.add_line(ident,start,end)
            elif c[0]=='A':
                _,end,rx,ry,sweep=c
                self.add_arc(ident,start,end,radius_x=rx,radius_y=ry,sweep=sweep)
            elif c[0]=='C':
                _,end,c1,c2=c
                self.add_bezier(ident,start,(c1,c2,end))
            members.append(ident);start=end
        self.add_contour(name,*members,closed=closed)
    def circle(self,name,x,y,r):
        self.path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
