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
        self.add_arc('sun',(7,18),(19,18),radius_x=6,sweep=True)
        self.add_line('ray-top',(13,4),(13,6))
        self.add_line('ray-left',(4,8),(5,9))
        self.add_line('ray-right',(21,8),(22,7))
        self.add_line('horizon',(4,24),(20,24))
        self.circle('head',35,15,5)
        self.path('back',(35,28),[('C',(44,40),(41,28),(44,34)),('L',(37,40))])
        self.add_polyline('laptop',(4,32),(24,32),(29,44),(9,44),closed=True)
        self.add_dot('logo',(16,38))

        self.mark_human_figure('person',head='head',torso='back-0',torso_junction='start')

# Human reference: icon_set/references/human_ref/full_body_ref.png.
# Detached circular head: nearest neck point is radius + 8 from center, leaving exactly 4 px ink clearance.
# Head (35,15), r5; neck (35,28); reference shows a seated back with deliberate neck bend.

Drawing.exception = {'reason': 'Preserve the complete sun, rays, horizon, laptop and seated worker composition. Compact local spacing and a broader keyshape envelope keep all four visual cues legible.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': '0d47904f203a82387c647752902e04a87316f0a9608fb143fee149ce33048a02'}
