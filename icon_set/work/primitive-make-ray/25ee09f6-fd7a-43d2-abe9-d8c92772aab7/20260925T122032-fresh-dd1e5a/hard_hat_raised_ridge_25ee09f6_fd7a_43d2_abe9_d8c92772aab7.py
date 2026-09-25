"""Front-facing hard hat with a raised narrow central ridge and rounded rectangular brim."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='25ee09f6-fd7a-43d2-abe9-d8c92772aab7'
SOURCE_PATH='pictographic-primitives/protection/helmet_25ee09f6-fd7a-43d2-abe9-d8c92772aab7.svg'
AUTHOR='gpt-6'
PLAN='Front-facing hard hat with a raised narrow central ridge and rounded rectangular brim.'
CONSTRUCTION_REFERENCE='hard-hat original and atomic-debug: raised U-shaped ridge, curved side shell and rounded brim.'
OMISSIONS='No omissions.'
class Drawing(Solo48):
    icon_id='hard-hat-raised-ridge'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
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
        self.path('ridge',(20,30),[('L',(20,14)),('L',(20,11)),('A',(23,8),3,3,True),('L',(25,8)),('A',(28,11),3,3,True),('L',(28,14)),('L',(28,30))])
        self.path('dome-l',(8,30),[('C',(20,14),(8,21),(13,16))]);self.path('dome-r',(28,14),[('C',(40,30),(35,16),(40,21))])
        self.box('brim',4,30,44,40,3)
        for a,b in [('ridge','dome-l'),('ridge','dome-r'),('ridge','brim'),('dome-l','brim'),('dome-r','brim')]:self.relate('connect',a,b)

# Keyshape rationale: HRECT_L fits a raised narrow ridge above the broad brim.
# Visual review: Symmetric shell with narrow rounded ridge raised above the shoulders.
