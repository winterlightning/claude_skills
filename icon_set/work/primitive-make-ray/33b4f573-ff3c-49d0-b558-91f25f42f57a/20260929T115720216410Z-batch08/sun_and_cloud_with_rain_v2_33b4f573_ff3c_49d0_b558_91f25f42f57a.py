"""The rejected cloud has a pinched upright lobe and very short rain marks; restore a broad smooth cloud and diagonal rainfall with exposed sun. No written feedback.
Symbol plan: Lucide cloud-sun-rain: coherent cloud lobes and detached rain. Two clear rays replace the finer ray series.
Keyshape SQUARE, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='33b4f573-ff3c-49d0-b558-91f25f42f57a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__sun-and-cloud-with-rain-v2/20260929T115301Z-thuan-mac/reference/cloud sun rain_33b4f573-ff3c-49d0-b558-91f25f42f57a.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='sun-and-cloud-with-rain-v2'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('sun', 'and', 'cloud', 'with', 'rain', 'v2')

    def path(self,n,start,ops,closed=False):
        here=start; members=[]
        for i,(kind,end,*args) in enumerate(ops):
            m=f'{n}-{i}'
            if kind=='L': self.add_line(m,here,end)
            elif kind=='A': self.add_arc(m,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif kind=='C': self.add_bezier(m,here,(args[0],args[1],end))
            members.append(m); here=end
        self.add_contour(n,*members,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x,y-r),[('A',(x+r,y),r,r,True),('A',(x,y+r),r,r,True),('A',(x-r,y),r,r,True),('A',(x,y-r),r,r,True)],True)

    def build(self):

        self.path('cloud',(14,30),[('A',(6,22),8,8,True),('C',(14,16),(6,18),(10,16)),('C',(24,16),(16,8),(22,8)),('C',(28,22),(27,16),(28,19)),('A',(28,30),4,4,True),('L',(14,30))],True)
        self.path('sun',(24,16),[('C',(40,22),(27,10),(40,10)),('A',(32,30),8,8,True),('L',(28,30))]);self.relate('connect','sun','cloud')
        self.add_dot('ray-top',(32,6))
        self.add_dot('ray-right',(42,6))
        for x in (14,24,34):self.add_line(f'rain-{x}',(x,38),(x-3,42))

