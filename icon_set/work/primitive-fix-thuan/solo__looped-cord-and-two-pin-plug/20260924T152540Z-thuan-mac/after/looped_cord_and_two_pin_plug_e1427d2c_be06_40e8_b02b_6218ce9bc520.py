"""Looped cord with a rounded two-pin plug; one continuous cable curls into the center of its rear wall. Equal pins share length and spacing.
Keyshape HRECT_L: exact SOLO48 contract envelope.
Construction references: Lucide plug and cable: smooth cable turns, rounded housing and equal pins.
Omissions: Extra cable turns reduced to one open loop.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'e1427d2c-be06-40e8-b02b-6218ce9bc520'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__looped-cord-and-two-pin-plug/20260924T152540Z-thuan-mac/reference/cord_e1427d2c-be06-40e8-b02b-6218ce9bc520.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'looped-cord-and-two-pin-plug'
    keyshape = Keyshape.HRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/reference'
    aliases = ()
    keywords = ('cord',)
    def build(self):

        def path(n, start, steps, closed=False):
            ids=[]; p=start
            for i,step in enumerate(steps):
                k=f'{n}-{i}';kind=step[0];q=step[1]
                if kind=='L': self.add_line(k,p,q)
                elif kind=='A': self.add_arc(k,p,q,radius_x=step[2],radius_y=step[3],sweep=step[4])
                elif kind=='B': self.add_bezier(k,p,(step[2],step[3],q))
                ids.append(k);p=q
            self.add_contour(n,*ids,closed=closed)
        def circle(n,x,y,r):
            path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('cord',(36,8),[('L',(12,8)),('A',(12,24),8,8,False),('L',(20,24)),('B',(28,32),(24,24),(28,28))])
        path('plug',(28,32),[('A',(36,24),8,8,True),('L',(36,28)),('L',(36,36)),('L',(36,40)),('A',(28,32),8,8,True)],True)
        join('cord','plug')
        for y in (28,36): line(f'pin-{y}',(36,y),(44,y));join('plug',f'pin-{y}')
