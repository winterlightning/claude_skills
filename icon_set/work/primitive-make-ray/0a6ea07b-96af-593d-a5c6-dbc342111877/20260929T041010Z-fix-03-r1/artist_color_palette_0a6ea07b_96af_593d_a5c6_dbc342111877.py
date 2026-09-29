"""Reviewer explicitly requests replacing three dot-like wells with circles. Enlarge each well to a clearly open 6-unit centerline diameter."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='0a6ea07b-96af-593d-a5c6-dbc342111877'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__artist-color-palette/20260929T041010Z-thuan-mac/reference/color palette sample_0a6ea07b-96af-593d-a5c6-dbc342111877.svg'
AUTHOR='gpt-6'
PLAN='Reviewer explicitly requests replacing three dot-like wells with circles. Enlarge each well to a clearly open 6-unit centerline diameter.'
CONSTRUCTION_REFERENCE='Lucide palette original and atomic-debug: continuous outer contour and inward thumb turn.'
OMISSIONS='No paint wells omitted.'
class Drawing(Solo48):
    icon_id='artist-color-palette'
    keyshape=Keyshape.CIRCLE
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
        self.path('palette',(24,44),[('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(36,32),8,8,True),('C',(34,40),(30,32),(38,36)),('C',(24,44),(31,42),(28,44))],True)
        for n,(x,y) in enumerate(((17,16),(31,17),(15,30))): self.circle(f'well-{n}',x,y,3)
