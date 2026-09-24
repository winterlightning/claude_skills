"""Beveled price tag with a complete two-bar yuan sign. Bars share8-unit step.
Symbol plan: shared contour owners and attachment nodes; repeated marks share a spacing parameter.
Omissions: Small punch hole omitted to prioritize currency identity.
Construction: Lucide tag: clipped tag shoulder; supplied reference: two-bar yuan.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.profiles import Profile
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='280da1a2-f9bb-4c4f-8a82-4da931ec7064'
SOURCE_PATH='pictographic-primitives/_uncategorized_37/tag yuan_280da1a2-f9bb-4c4f-8a82-4da931ec7064.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='tag-yuan'
    keyshape=Keyshape.VRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects/general'
    aliases=()
    keywords=('tag', 'yuan')
    ink_extremes=keyshape.bounds_for(Profile.SOLO48)
    def build(self):
        self.add_polyline('tag',(8,16),(20,4),(40,4),(40,36),(32,44),(8,44),closed=True)
        self.add_polyline('yuan-fork',(18,18),(24,25),(30,18))
        self.add_polyline('yuan-stem',(24,25),(24,33),(24,35))
        for name,y in [('upper',25),('lower',33)]:
            self.add_polyline(name,(17,y),(24,y),(31,y));self.relate('connect',name,'yuan-stem')
        self.relate('connect','yuan-fork','yuan-stem','upper')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)
    def path(self,n,start,ops,closed=False):
        p=start;members=[]
        for i,op in enumerate(ops):
            name=f'{n}-{i}';end=op[1]
            if op[0]=='L':self.add_line(name,p,end)
            elif op[0]=='A':self.add_arc(name,p,end,radius_x=op[2],radius_y=op[3],sweep=op[4])
            elif op[0]=='B':self.add_bezier(name,p,(op[2],op[3],end))
            members.append(name);p=end
        if closed and p!=start:
            self.add_line(n+'-close',p,start);members.append(n+'-close')
        self.add_contour(n,*members,closed=closed)
