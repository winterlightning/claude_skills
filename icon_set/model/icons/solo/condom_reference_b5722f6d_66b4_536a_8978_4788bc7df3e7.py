'Rounded the reservoir tip and smoothed its transition into the shoulders. Rolled rim uses equal semicircular ends, with an upright VRECT_L envelope. All defining parts retained. Construction references: No useful exact Lucide match; supplied reference plus coherent rounded contour construction.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='b5722f6d-66b4-536a-8978-4788bc7df3e7'
SOURCE_PATH='pictographic-primitives/health/condom_b5722f6d-66b4-536a-8978-4788bc7df3e7.svg'
AUTHOR='gpt-6'
PARENT_MODULE='icon_set/model/icons/solo/condom_reference_b5722f6d_66b4_536a_8978_4788bc7df3e7.py'
class Drawing(Solo48):
    icon_id='condom-reference'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'health'
    categories = ('health', 'primitives')
    aliases=()
    keywords=('condom',)

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
        self.path('body',(12,36),[('L',(12,20)),('C',(20,10),(12,14),(20,14)),('L',(20,8)),('A',(28,8),4,4,True),('L',(28,10)),('C',(36,20),(28,14),(36,14)),('L',(36,36))])
        self.path('rim',(12,36),[('L',(36,36)),('A',(36,44),4,4,True),('L',(12,44)),('A',(12,36),4,4,True)],True)
        self.relate('connect','rim','body')

    icon_id = 'condom-reference'
    category = 'health'
    categories = ('health', 'primitives')
    aliases = ()
    keywords = ('condom',)
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
