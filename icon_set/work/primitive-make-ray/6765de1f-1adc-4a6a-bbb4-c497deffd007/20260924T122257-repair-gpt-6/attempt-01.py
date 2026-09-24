"""Social webpage, header, circular portrait and broad semicircular shoulders. human_ref/user.svg owns the exact 4 ink-unit detached head gap; Lucide id-card informs paired text lines."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '6765de1f-1adc-4a6a-bbb4-c497deffd007'
SOURCE_PATH = 'pictographic-primitives/other/ui webpage social profile_6765de1f-1adc-4a6a-bbb4-c497deffd007.svg'
AUTHOR = 'gpt-6'
PLAN = 'Social webpage, header, circular portrait and broad semicircular shoulders. human_ref/user.svg owns the exact 4 ink-unit detached head gap; Lucide id-card informs paired text lines.'
OMISSIONS = ['Header dashes omitted to reserve space for portrait.']
class Drawing(Solo48):
    icon_id = 'ui-webpage-social-profile'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('ui', 'webpage', 'social', 'profile')
    def build(self):
        self.add_polyline('page',(6,14),(6,6),(42,6),(42,14),(42,42),(6,42),closed=True)
        self.add_line('header',(6,14),(42,14));self.relate('connect','page','header')
        self.circle('head',18,25,3)
        self.add_arc('shoulders',(13,41),(23,41),radius_x=5)
        for i,y in enumerate((25,33)):self.add_line(f'text-{i}',(32,y),(34,y))


    def circle(self,n,x,y,r):
        self.add_arc(n+'-top',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-bottom',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-top',n+'-bottom',closed=True)
    def box(self,n,l,t,r,b,rad=3):
        pts=[(l+rad,t),(r-rad,t),(r,t+rad),(r,b-rad),(r-rad,b),(l+rad,b),(l,b-rad),(l,t+rad)]
        members=[]
        for i,a in enumerate(pts):
            z=pts[(i+1)%8]; p=n+str(i)
            if i%2:self.add_arc(p,a,z,radius_x=rad)
            else:self.add_line(p,a,z)
            members.append(p)
        self.add_contour(n,*members,closed=True)
