"""circle skull 1: fresh spacing repair.
Plan: Lucide skull informs dome and narrow jaw. Circle surrounds skull; mirrored socket strokes begin at actual cheek/dome endpoints.
Keyshape CIRCLE: extrema derived from the profile's standard envelope.
Omissions: Slanted eye sockets joined to the outer cheeks.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0275d46c-9a52-48fb-9993-9a0c2a0a4b89'
SOURCE_PATH='pictographic-primitives/other/circle skull 1_0275d46c-9a52-48fb-9993-9a0c2a0a4b89.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='circle-skull-1'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('circle', 'skull', '1')

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
        self.circle('ring',24,24,20)
        self.add_arc('dome',(13,23),(35,23),radius_x=11)
        self.add_bezier('right-cheek',(35,23),((35,28),(32,29),(32,30)))
        self.add_line('right-jaw',(32,30),(32,32))
        self.add_line('left-jaw',(16,32),(16,30))
        self.add_bezier('left-cheek',(16,30),((16,29),(13,28),(13,23)))
        self.add_contour('skull','left-jaw','left-cheek','dome','right-cheek','right-jaw')
        self.add_line('mouth',(24,32),(24,34))
        for side in (-1,1):
            self.add_line('eye-'+str(side),(24+side*11,23),(24+side*4,26))
            self.relate('connect','skull','eye-'+str(side))
