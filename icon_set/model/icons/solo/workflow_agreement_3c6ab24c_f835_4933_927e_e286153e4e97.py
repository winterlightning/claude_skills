"""workflow agreement: fresh spacing repair.
Plan: Bubble tapers clear of heads. user.svg busts head bottom34 shoulders42 exact gap8.
Keyshape VRECT_L: extrema derived from the profile's standard envelope.
Omissions: Twin bubble tails merged into tapered lower bubble; minimal paired busts.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='3c6ab24c-f835-4933-927e-e286153e4e97'
SOURCE_PATH='pictographic-primitives/_uncategorized_40/workflow agreement_3c6ab24c-f835-4933-927e-e286153e4e97.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='workflow-agreement'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases=()
    keywords=('workflow', 'agreement')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)
    def path(self,n,start,segments,closed=False):
        at=start; members=[]
        for i,s in enumerate(segments):
            eid=f'{n}-{i}'; kind,end,*args=s
            if end==at: continue
            if kind=='L': self.add_line(eid,at,end)
            else: self.add_arc(eid,at,end,radius_x=args[0],sweep=args[1] if len(args)>1 else True)
            at=end; members.append(eid)
        self.add_contour(n,*members,closed=closed)
    def cross(self,n,x,y,r):
        for i,(dx,dy) in enumerate([(-r,0),(r,0),(0,-r),(0,r)]):
            self.add_line(f'{n}-{i}',(x,y),(x+dx,y+dy))
        for i in range(4):
            for j in range(i): self.relate('connect',f'{n}-{i}',f'{n}-{j}')

    def build(self):
        self.add_polyline('bubble',(13,4),(35,4),(35,17),(28,24),(20,24),(13,17),closed=True)
        self.add_polyline('check',(21,13),(23,15),(27,12))
        for i,x in enumerate((11,37)):
            self.circle(f'head-{i}',x,32,2)
            self.add_arc(f'body-{i}',(x-3,44),(x+3,44),radius_x=3,radius_y=2)
