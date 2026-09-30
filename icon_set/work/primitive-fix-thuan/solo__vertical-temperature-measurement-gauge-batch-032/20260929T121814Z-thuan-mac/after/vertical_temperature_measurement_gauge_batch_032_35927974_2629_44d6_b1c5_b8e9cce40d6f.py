"""The rejected thermometer has a flattened broad bulb and a heavy interior bar; restore a round bulb and shorter temperature column. No written reviewer feedback.
Restored a round bulb and a slimmer stem, with a shorter temperature column.
Construction: Lucide thermometer original and atomic-debug; circular lower bulb and upright stem.
Omissions: Tiny bulb-center point omitted.
Keyshape: CIRCLE. Radial centerline limit 20 around (24,24), preserving the natural circular or slender subject proportions.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='35927974-2629-44d6-b1c5-b8e9cce40d6f'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__vertical-temperature-measurement-gauge-batch-032/20260929T121814Z-thuan-mac/reference/thermometer_35927974-2629-44d6-b1c5-b8e9cce40d6f.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='vertical-temperature-measurement-gauge-batch-032'
    keyshape=Keyshape.CIRCLE
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

        self.path('outline',(15,13),[('A',(33,13),9,9,True),('L',(33,24)),('C',(36,32),(35,27),(36,29)),('A',(24,44),12,12,True),('A',(12,32),12,12,True),('C',(15,24),(12,29),(13,27)),('L',(15,13))],True)
        self.add_line('column',(24,14),(24,27))

