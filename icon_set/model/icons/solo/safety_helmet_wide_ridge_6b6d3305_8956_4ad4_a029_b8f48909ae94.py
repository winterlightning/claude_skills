"""Safety helmet with a wide raised rounded central crest, equal side arches and a deep rounded brim."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='6b6d3305-8956-4ad4-a029-b8f48909ae94'
SOURCE_PATH='pictographic-primitives/protection/helmet_6b6d3305-8956-4ad4-a029-b8f48909ae94.svg'
AUTHOR='gpt-6'
PLAN='Safety helmet with a wide raised rounded central crest, equal side arches and a deep rounded brim.'
CONSTRUCTION_REFERENCE='hard-hat original and atomic-debug: raised ridge and symmetric rounded silhouette.'
OMISSIONS='No omissions.'
class Drawing(Solo48):
    icon_id='safety-helmet-wide-ridge'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'protection'
    aliases=()
    keywords=('helmet',)

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
        self.path('ridge',(18,28),[('L',(18,14)),('L',(18,12)),('A',(22,8),4,4,True),('L',(26,8)),('A',(30,12),4,4,True),('L',(30,14)),('L',(30,28))])
        self.add_arc('dome-l',(8,28),(18,14),radius_x=10,radius_y=14);self.add_arc('dome-r',(30,14),(40,28),radius_x=10,radius_y=14)
        self.box('brim',4,28,44,40,4)
        for a,b in [('ridge','dome-l'),('ridge','dome-r'),('ridge','brim'),('dome-l','brim'),('dome-r','brim')]:self.relate('connect',a,b)

# Keyshape rationale: HRECT_L accommodates a wide raised ridge and deep rounded brim.
# Visual review: Symmetric wide rounded ridge and deep rounded brim replace uneven crest.
