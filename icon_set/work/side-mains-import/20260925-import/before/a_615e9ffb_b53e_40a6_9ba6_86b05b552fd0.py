'Replaced the symmetric oval with the reference’s asymmetric single-storey a: rising left curve, higher crown, straighter right side and a short baseline stem. VRECT_L; no omissions. Curved bowl now separates promptly from the descending stroke. Construction references: type inspected; no useful glyph match; supplied a controls the drawing.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID='615e9ffb-b53e-40a6-9ba6-86b05b552fd0'
SOURCE_PATH='pictographic-primitives/typeface/a_615e9ffb-b53e-40a6-9ba6-86b05b552fd0.svg'
AUTHOR='gpt-6'
PARENT_MODULE='icon_set/model/icons/solo/a_615e9ffb_b53e_40a6_9ba6_86b05b552fd0.py'
class Drawing(Solo48):
    icon_id='a'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('a',)

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
        self.path('bowl',(8,25),[('C',(25,4),(8,14),(18,4)),('C',(40,18),(32,4),(40,11)),('L',(40,32)),('C',(24,44),(34,40),(31,44)),('C',(8,25),(13,44),(8,38))],True)
        self.add_line('stem',(40,32),(40,44));self.relate('connect','bowl','stem')
