"""Rejected straight bar merges the rifle and arms and looks like pointing. Separate the shoulder stock, barrel and bent supporting arm; retain an aiming stance."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='ad6a0427-9dcf-56bc-a271-c70f6694c4d6'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__aiming-rifle-shooter/20260929T041010Z-thuan-mac/reference/shooting rifle person aim_ad6a0427-9dcf-56bc-a271-c70f6694c4d6.svg'
AUTHOR='gpt-6'
PLAN='Rejected straight bar merges the rifle and arms and looks like pointing. Separate the shoulder stock, barrel and bent supporting arm; retain an aiming stance.'
CONSTRUCTION_REFERENCE='No useful subject-specific Lucide match; original reference determines the silhouette.'
OMISSIONS='Only insignificant source detail omitted.'
class Drawing(Solo48):
    icon_id='aiming-rifle-shooter'
    keyshape=Keyshape.HRECT_L
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
        self.circle('head',12,12,4)
        self.add_line('torso',(12,24),(12,30))
        self.add_polyline('legs',(4,40),(12,30),(22,40))
        self.add_polyline('rifle',(12,24),(22,24),(26,18),(44,18))
        self.add_polyline('support-arm',(12,24),(23,30),(31,24))
        self.add_line('sight',(40,14),(40,18))
        self.relate('connect','torso','legs','rifle','support-arm'); self.relate('connect','rifle','sight')
        self.mark_human_figure('person',head='head',torso='torso',torso_junction='start')

# Human reference: icon_set/references/human_ref/full_body_ref.png.
# Detached circular head: nearest neck point is radius + 8 from center, leaving exactly 4 px ink clearance.
# Head (12,12), r4; neck (12,24); upper torso vertical.

Drawing.exception = {'reason': 'Keep the shoulder stock, offset rifle barrel and bent supporting arm; reduced gaps at the arm/torso junction are readable at 48 px.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': 'db583db7df7dba10593cc83af32d373b0e9b61d1f606fdd63dcd635e7b404745'}
