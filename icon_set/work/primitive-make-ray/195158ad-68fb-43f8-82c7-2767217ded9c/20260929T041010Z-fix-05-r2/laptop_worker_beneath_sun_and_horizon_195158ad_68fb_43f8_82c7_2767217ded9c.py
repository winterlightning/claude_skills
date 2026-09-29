"""Rejected worker is a floating head and hook; the sun lost rays and horizon. Restore rays, horizon, laptop display and a continuous seated back."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='195158ad-68fb-43f8-82c7-2767217ded9c'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__laptop-worker-beneath-sun-and-horizon/20260929T041010Z-thuan-mac/reference/digital nomad sun_195158ad-68fb-43f8-82c7-2767217ded9c.svg'
AUTHOR='gpt-6'
PLAN='Rejected worker is a floating head and hook; the sun lost rays and horizon. Restore rays, horizon, laptop display and a continuous seated back.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='laptop-worker-beneath-sun-and-horizon'
    keyshape=Keyshape.SQUARE
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
        self.add_arc('sun',(6,16),(20,16),radius_x=7,sweep=True)
        self.add_line('ray-top',(13,2),(13,3))
        self.add_line('ray-left',(3,5),(4,6))
        self.add_line('ray-right',(22,5),(23,4))
        self.add_line('horizon',(4,22),(20,22))
        self.circle('head',35,15,5)
        self.path('back',(35,28),[('C',(44,40),(41,28),(44,34)),('L',(37,40))])
        self.add_polyline('laptop',(4,29),(24,29),(29,44),(9,44),closed=True)
        self.add_dot('logo',(16,36))
