"""A nectar bottle bears a five-petalled flower.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: Bottle cap rounding simplified; all five petals retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='74f05c03-957b-4b86-b062-d7cbbb568098'
SOURCE_PATH='icon_set/work/todo-references/nectar_74f05c03-957b-4b86-b062-d7cbbb568098.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='nectar'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('nectar',)

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):
        # Bottle and five-petal flower are separate, sharing the full square envelope.
        self.add_polyline('cap',(10,6),(18,6),(18,14),(10,14),closed=True)
        self.add_polyline('bottle',(10,14),(6,22),(6,42),(22,42),(22,22),(18,14))
        self.relate('connect','cap','bottle')
        # Open radial petals keep all five lobes without microscopic counters.
        ends=((36,12),(42,17),(40,26),(32,26),(30,17))
        names=[]
        for i,end in enumerate(ends):
            name=f'petal-{i}'
            self.add_line(name,(36,20),end)
            names.append(name)
        self.relate('connect',*names)
