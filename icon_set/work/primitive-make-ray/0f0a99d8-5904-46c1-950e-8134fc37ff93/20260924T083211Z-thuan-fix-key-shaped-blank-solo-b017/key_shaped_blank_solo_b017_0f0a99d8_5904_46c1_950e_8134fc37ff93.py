"""Blank diagonal key with circular bow and broad square-ended shaft. Keep the bow empty as in the source; omit the rejected central dot."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0f0a99d8-5904-46c1-950e-8134fc37ff93'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__key-shaped-blank-solo-b017/20260924T083211Z-thuan-mac/reference/key 2_0f0a99d8-5904-46c1-950e-8134fc37ff93.svg'
AUTHOR='gpt-6'

class Drawing(Solo48):
    icon_id='key-shaped-blank-solo-b017'
    keyshape=Keyshape.SQUARE
    semantic_role="MAIN"
    semantic_kind="noun"
    category="objects/general"
    aliases=()
    keywords=()

    def build(self):
        # Symbol plan: Blank diagonal key with circular bow and broad square-ended shaft. Keep the bow empty as in the source; omit the rejected central dot.

        def path(n,start,commands,closed=False):
            members=[]
            for i,(kind,end,*args) in enumerate(commands):
                m=f'{n}-{i}'
                if kind=='L': self.add_line(m,start,end)
                elif kind=='A': self.add_arc(m,start,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(m,start,(args[0],args[1],end))
                members.append(m);start=end
            self.add_contour(n,*members,closed=closed)
        def oval(n,x,y,rx,ry=None):
            ry=rx if ry is None else ry
            path(n,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def box(n,l,t,r,b,rad=4):
            path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
        line=self.add_line
        join=lambda a,b:self.relate('connect',a,b)

        path('key',(18,18),[('L',(30,6)),('L',(42,6)),('L',(42,12)),('L',(28,26)),('C',(30,32),(29,28),(30,30)),('A',(18,42),12,10,True),('A',(6,30),12,12,True),('A',(18,18),12,12,True)],True)
