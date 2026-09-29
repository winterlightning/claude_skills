"""Rejected single inner blob loses brain folds and the head has an oversized angular nose. Restore a rounded skull and chin, a compact profile and recognizable lobed brain with folds."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='0231a044-ecb1-470e-bcc3-8a45ccdc5d4a'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__right-profile-with-folded-brain/20260929T044747Z-thuan-mac/reference/neuropathologist_0231a044-ecb1-470e-bcc3-8a45ccdc5d4a.svg'
AUTHOR='gpt-6'
PLAN='Rejected single inner blob loses brain folds and the head has an oversized angular nose. Restore a rounded skull and chin, a compact profile and recognizable lobed brain with folds.'
CONSTRUCTION_REFERENCE='Lucide brain original and atomic-debug: lobed outline and a small number of connected internal folds.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='right-profile-with-folded-brain'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=()

    def circle(self,n,x,y,r):
        self.add_arc(n+'a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'a',n+'b',closed=True)
    def path(self,n,start,commands,closed=False):
        ids=[]; here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid); here=end
        self.add_contour(n,*ids,closed=closed)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        self.path('head',(12,44),[('L',(12,36)),('C',(8,22),(12,32),(8,30)),('C',(23,4),(8,11),(13,4)),('C',(36,20),(32,4),(36,10)),('L',(40,26)),('L',(35,26)),('L',(35,34)),('A',(31,38),4,4,True),('L',(25,38)),('L',(25,44))])
        self.path('brain',(17,26),[('C',(13,20),(11,26),(11,21)),('C',(19,13),(12,15),(15,12)),('C',(25,12),(19,8),(24,8)),('C',(31,17),(31,10),(33,13)),('C',(29,25),(36,20),(34,25)),('L',(24,25)),('C',(17,26),(22,29),(19,30))],True)
        self.path('fold',(25,12),[('L',(25,17)),('C',(20,20),(25,20),(22,20))])
        self.add_line('brainstem',(24,25),(27,30));self.relate('connect','brain','fold','brainstem')
