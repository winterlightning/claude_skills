from icon_set.model.icons.solo._base import Solo48, HEAD_BODY_CENTERLINE_GAP
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='3bfeb607-fee8-43a8-8a4a-88f605a7b761'
SOURCE_PATH='pictographic-primitives/design/fill adjustment layer_3bfeb607-fee8-43a8-8a4a-88f605a7b761.svg'
AUTHOR='gpt-6'
PLAN = 'Two diamond layers with broader tangent-continuous corner curves, mirrored around the center axis.'
CONSTRUCTION_REFERENCES='Lucide layers: repeated rhombus proportions and open lower layer.'
OMISSIONS = []
class Drawing(Solo48):
    icon_id='two-stacked-design-layers'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'design'
    categories = ('design', 'primitives')
    aliases=()
    keywords=('fill', 'adjustment', 'layer')
    def path(self,n,start,commands,closed=False):
        here=start;members=[]
        for i,(kind,end,*a) in enumerate(commands):
            k=f'{n}-{i}';members.append(k)
            if kind=='L':self.add_line(k,here,end)
            elif kind=='A':self.add_arc(k,here,end,radius_x=a[0],radius_y=a[1],sweep=a[2])
            elif kind=='C':self.add_bezier(k,here,(a[0],a[1],end))
            here=end
        self.add_contour(n,*members,closed=closed)
    def build(self):
        self.path('top-layer',(24,6),[
            ('C',(30,8),(26,6),(27,6)),('L',(39,14)),
            ('C',(42,18),(42,16),(42,16)),('C',(39,22),(42,20),(42,20)),
            ('L',(36,24)),('L',(30,28)),('C',(24,30),(27,30),(26,30)),
            ('C',(18,28),(22,30),(21,30)),('L',(12,24)),('L',(9,22)),
            ('C',(6,18),(6,20),(6,20)),('C',(9,14),(6,16),(6,16)),
            ('L',(18,8)),('C',(24,6),(21,6),(22,6))],True)
        self.path('lower-layer',(12,24),[
            ('L',(9,26)),('C',(6,30),(6,28),(6,28)),
            ('C',(9,34),(6,32),(6,32)),('L',(18,40)),
            ('C',(24,42),(21,42),(22,42)),('C',(30,40),(26,42),(27,42)),
            ('L',(39,34)),('C',(42,30),(42,32),(42,32)),
            ('C',(39,26),(42,28),(42,28)),('L',(36,24))])
        self.relate('connect','top-layer','lower-layer')

    icon_id = 'fill-adjustment-layer'
    category = 'design'
    categories = ('design', 'primitives')
    aliases = ()
    keywords = ('fill', 'adjustment', 'layer', 'design')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
