"""Square watch face encloses a euro glyph; top and bottom strap attachments share a central axis."""
from ._base import Solo48
from ...keyshapes import Keyshape
SOURCE_ICON_ID='ac5e07e4-9e24-406e-8500-ef19796d1933'
SOURCE_PATH='pictographic-primitives/other/smart watch square euro sign_ac5e07e4-9e24-406e-8500-ef19796d1933.svg'
AUTHOR='gpt-6'
PLAN='Restored the missing single-bar euro. Paired strap extensions are integrated into the outer contour, with matching rounded case corners.'
CONSTRUCTION_REFERENCE='watch original and atomic-debug: paired straps and central face; source supplies single-bar euro.'
OMISSIONS='The source strap/face dividing rails are omitted; short outlined top and bottom extensions preserve the wristwatch silhouette.'
class Drawing(Solo48):
    icon_id='smartwatch-euro'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    aliases=()
    keywords=('smart', 'watch', 'square', 'euro', 'sign')
    category = 'primitives-generate'

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
        self.path('watch',(11,7),[('L',(16,7)),('L',(16,4)),('L',(32,4)),('L',(32,7)),('L',(37,7)),('A',(40,10),3,3,True),('L',(40,38)),('A',(37,41),3,3,True),('L',(32,41)),('L',(32,44)),('L',(16,44)),('L',(16,41)),('L',(11,41)),('A',(8,38),3,3,True),('L',(8,10)),('A',(11,7),3,3,True)],True)
        self.path('euro',(31,16),[('L',(24,16)),('A',(20,20),4,4,False),('L',(20,24)),('L',(20,28)),('A',(24,32),4,4,False),('L',(31,32))])
        self.add_line('euro-bar',(17,24),(26,24));self.relate('connect','euro','euro-bar')
