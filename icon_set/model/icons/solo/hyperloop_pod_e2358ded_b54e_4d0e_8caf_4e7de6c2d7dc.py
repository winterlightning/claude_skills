'Restored both rear marks and a flat lower shell. Windshield follows a smooth inset curve into the front. HRECT_M provides enough vertical space for two separated marks; the result is deliberately taller than the slender source. Right-facing asymmetry preserved. Construction references: train-front (coherent vehicle shell).'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='e2358ded-b54e-4d0e-8caf-4e7de6c2d7dc'
SOURCE_PATH='pictographic-primitives/technology/hyperloop_e2358ded-b54e-4d0e-8caf-4e7de6c2d7dc.svg'
AUTHOR='gpt-6'
PARENT_MODULE='icon_set/model/icons/solo/hyperloop_pod_e2358ded_b54e_4d0e_8caf_4e7de6c2d7dc.py'
class Drawing(Solo48):
    icon_id='hyperloop-pod'
    keyshape=Keyshape.HRECT_M
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases=()
    keywords=('hyperloop',)

    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';end=c[1]
            if c[0]=='L':self.add_line(k,start,end)
            elif c[0]=='A':self.add_arc(k,start,end,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,start,(c[2],c[3],end))
            ids.append(k);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.path('pod',(18,10),[('L',(26,10)),('C',(44,26),(32,10),(44,20)),('C',(38,38),(44,32),(44,38)),('L',(18,38)),('A',(18,10),14,14,True)],True)
        self.path('windshield',(26,10),[('C',(34,26),(26,20),(28,26)),('L',(44,26))]);self.relate('connect','pod','windshield')
        self.add_line('mark-top',(14,20),(17,20));self.add_line('mark-bottom',(14,28),(16,28))

    icon_id = 'hyperloop-pod'
    category = 'technology'
    categories = ('primitives', 'technology')
    aliases = ()
    keywords = ('hyperloop', 'pod', 'train', 'capsule', 'transport', 'vehicle', 'travel')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
