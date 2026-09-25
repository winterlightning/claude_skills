"""Organic circular kidney palette with a thumb indentation and three paint wells."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='0a6ea07b-96af-593d-a5c6-dbc342111877'
SOURCE_PATH='pictographic-primitives/design/color palette sample_0a6ea07b-96af-593d-a5c6-dbc342111877.svg'
AUTHOR='gpt-6'
PLAN='Organic circular kidney palette with a thumb indentation and three paint wells.'
CONSTRUCTION_REFERENCE='palette original and atomic-debug: circular outer contour and smooth inward thumb turn.'
OMISSIONS='Outlined wells reduced to small circular paint dots.'
class Drawing(Solo48):
    icon_id='artist-color-palette'
    keyshape=Keyshape.CIRCLE
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('color', 'palette', 'sample')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)

    def path(self,n,start,commands,closed=False):
        ids=[];here=start
        for i,c in enumerate(commands):
            tag,end,*args=c; eid=f'{n}-{i}'
            if tag=='L': self.add_line(eid,here,end)
            elif tag=='A': self.add_arc(eid,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
            elif tag=='C': self.add_bezier(eid,here,(args[0],args[1],end))
            ids.append(eid);here=end
        self.add_contour(n,*ids,closed=closed)

    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def file(self,l=8,t=4,r=40,b=44):
        self.path('page',(l+4,t),[('L',(r-10,t)),('L',(r,t+10)),('L',(r,b-4)),('A',(r-4,b),4,4,True),('L',(l+4,b)),('A',(l,b-4),4,4,True),('L',(l,t+4)),('A',(l+4,t),4,4,True)],True)

    def build(self):
        self.path('palette',(24,44),[('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(36,32),8,8,True),('C',(34,40),(30,32),(38,36)),('C',(24,44),(31,42),(28,44))],True)
        for n,(x,y) in enumerate(((17,17),(31,17),(17,30))):self.circle(f'well-{n}',x,y,2)

# Keyshape rationale: CIRCLE keeps the organic palette broad and round.
# Visual review: Organic silhouette and three readable paint dots; deliberate thumb-side asymmetry.
