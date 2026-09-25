"""Bathtub with Shower.

Plan: Wide rounded bath and tall curved shower pipe at right. Bounds (6,6)-(42,42).
Construction: Lucide bath rounded tub, rim and feet; supplied domed shower head.
Reduction: Curved pipe bend represents the shower outlet; tiny water stroke omitted. Wide bath, rim and feet remain.
"""
from ...keyshapes import Keyshape
from ._base import Solo48, HEAD_BODY_CENTERLINE_GAP

SOURCE_ICON_ID = '94ac4b5f-8583-5824-87a1-c47c0409aead'
SOURCE_PATH = '/Applications/Workspaces/pictographic/icon_simplification/pictographic-primitives/hotels/bathroom shower_94ac4b5f-8583-5824-87a1-c47c0409aead.svg'
AUTHOR = 'gpt-6'


class IconBathtubWithShower(Solo48):
    icon_id = 'bathtub-with-shower'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'hotels'
    categories = ('hotels', 'primitives')
    aliases = ()
    keywords = ('bathtub', 'with', 'shower')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start
            members=[]
            for i, (kind,end,*args) in enumerate(commands):
                k=f"{name}-{i}"
                if kind == "L": self.add_line(k,here,end)
                elif kind == "A": self.add_arc(k,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind == "C": self.add_bezier(k,here,(args[0],args[1],end))
                members.append(k)
                here=end
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[("A",(x+r,y),r,r,True),("A",(x-r,y),r,r,True)],True)
        path('rim',(6,28),[('L',(10,28)),('L',(38,28)),('L',(42,28))])
        path('tub',(10,28),[('L',(10,34)),('A',(16,40),6,6,False),('L',(32,40)),('A',(38,34),6,6,False),('L',(38,28))]);self.relate('connect','rim','tub')
        path('shower',(38,28),[('L',(38,14)),('A',(22,14),8,8,False)]);self.relate('connect','shower','rim')
        # Water mark removed to keep clear space below shower outlet.
        self.add_line('foot-left',(16,40),(14,42));self.add_line('foot-right',(32,40),(34,42));self.relate('connect','foot-left','tub');self.relate('connect','foot-right','tub')
