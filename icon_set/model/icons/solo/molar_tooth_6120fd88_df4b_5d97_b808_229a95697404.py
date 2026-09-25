'Restored the shallow crown groove and natural curved shoulders and long roots. Paired lobes and roots mirror about x=24. VRECT_L retains a tall dental silhouette; no defining detail omitted. Construction references: bone (smooth anatomical contours).'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='6120fd88-df4b-5d97-b808-229a95697404'
SOURCE_PATH='pictographic-primitives/health/tooth_6120fd88-df4b-5d97-b808-229a95697404.svg'
AUTHOR='gpt-6'
PARENT_MODULE='icon_set/model/icons/solo/molar_tooth_6120fd88_df4b_5d97_b808_229a95697404.py'
class Drawing(Solo48):
    icon_id='molar-tooth'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'health'
    aliases=()
    keywords=('tooth',)

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
        # Crown lobes and long rounded roots derive from a shared axis.
        self.path('tooth',(8,13),[('C',(16,4),(8,7),(10,4)),('C',(24,6),(20,4),(21,6)),('C',(32,4),(27,6),(28,4)),('C',(40,13),(38,4),(40,7)),('C',(36,30),(40,20),(36,24)),('C',(32,44),(36,37),(34,44)),('C',(28,34),(30,44),(29,38)),('C',(24,26),(27,29),(27,26)),('C',(20,34),(21,26),(21,29)),('C',(16,44),(19,38),(18,44)),('C',(12,30),(14,44),(12,37)),('C',(8,13),(12,24),(8,20))],True)
        self.path('groove',(17,16),[('C',(24,15),(19,12),(21,15)),('C',(31,13),(27,17),(30,16))])

    icon_id = 'molar-tooth-6120fd88'
    category = 'health'
    aliases = ('molar-tooth',)
    keywords = ('molar', 'tooth')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
