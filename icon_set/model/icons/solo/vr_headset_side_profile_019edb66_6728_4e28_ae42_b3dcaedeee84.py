'Left-facing continuous head profile with visor, horizontal strap, nose, chin and neck.'
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='019edb66-6728-4e28-ae42-b3dcaedeee84'
SOURCE_PATH='pictographic-primitives/other/vr headset 1_019edb66-6728-4e28-ae42-b3dcaedeee84.svg'
AUTHOR='gpt-6'
PLAN='Left-facing continuous head profile with visor, horizontal strap, nose, chin and neck.'
CONSTRUCTION_REFERENCE='human_ref/user.svg: head proportion; source owns continuous side profile and visor.'
class Drawing(Solo48):
    icon_id='vr-headset-side-profile'
    keyshape=Keyshape.SQUARE
    semantic_role='MAIN'
    semantic_kind='noun'
    category = 'primitives-generate'
    categories = ('other', 'primitives-generate')
    aliases=()
    keywords=('vr', 'headset', '1')
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
        self.path('head',(18,14),[('C',(27,6),(20,8),(23,6)),('C',(42,20),(35,6),(42,12)),('L',(42,24)),('C',(34,36),(42,30),(34,32)),('L',(34,42))])
        self.path('visor',(10,14),[('L',(18,14)),('L',(22,14)),('A',(26,18),4,4,True),('L',(26,20)),('L',(26,22)),('A',(22,26),4,4,True),('L',(14,26)),('L',(10,26)),('A',(6,22),4,4,True),('L',(6,18)),('A',(10,14),4,4,True)],True)
        self.add_line('strap',(26,20),(42,20))
        self.path('face',(14,26),[('L',(11,34)),('L',(18,34)),('L',(18,36)),('A',(22,40),4,4,False),('L',(22,42))])
        for a,b in [('head','visor'),('head','strap'),('visor','strap'),('face','visor')]:self.relate('connect',a,b)

# Keyshape: SQUARE gives the visor room beside the rounded skull and continuous neck.
# Visual review: Continuous profile now includes a rounded chin below the nose; visor and strap retain their orientation.
OMISSIONS='Small mouth/ear detail omitted; supplied continuous neck retained.'
HUMAN_REVIEW={'reference': 'icon_set/references/human_ref/user.svg', 'construction': 'Continuous source profile and neck; detached head rule does not apply.'}
