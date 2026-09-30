"""The rejected thermometer has a flattened broad bulb and a heavy interior bar; restore a round bulb and shorter temperature column. No written reviewer feedback.
Symbol plan: Lucide thermometer: narrow stem above a circular bulb. Symmetric vertical construction; tiny bulb point omitted.
Keyshape VRECT_M, authored on the SOLO48 integer grid with 4-unit strokes.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='35927974-2629-44d6-b1c5-b8e9cce40d6f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vertical-temperature-measurement-gauge-batch-032/20260929T121814Z-thuan-mac/reference/thermometer_35927974-2629-44d6-b1c5-b8e9cce40d6f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='vertical-temperature-measurement-gauge-batch-032'
    keyshape=Keyshape.VRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category='primitives-generate'
    aliases=()
    keywords=('vertical', 'temperature', 'measurement', 'gauge', 'batch', '032')

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

        self.path('outline',(16,12),[('A',(32,12),8,8,True),('L',(32,26)),('C',(38,34),(36,28),(38,30)),('A',(24,44),14,10,True),('A',(10,34),14,10,True),('C',(16,26),(10,30),(12,28)),('L',(16,12))],True)
        self.add_line('column',(24,14),(24,28))
