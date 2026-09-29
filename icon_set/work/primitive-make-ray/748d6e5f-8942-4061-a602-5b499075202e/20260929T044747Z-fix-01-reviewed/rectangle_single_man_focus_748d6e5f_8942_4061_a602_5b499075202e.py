"""Rejected diagonal marks merge into the frame and the person becomes two small marks. Restore four independent right-angle focus brackets around a head and shoulder bust."""
from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID='748d6e5f-8942-4061-a602-5b499075202e'
SOURCE_PATH='icon_set/work/primitive-fix-thuan/solo__rectangle-single-man-focus/20260929T044747Z-thuan-mac/reference/rectangle single man focus_748d6e5f-8942-4061-a602-5b499075202e.svg'
AUTHOR='gpt-6'
PLAN='Rejected diagonal marks merge into the frame and the person becomes two small marks. Restore four independent right-angle focus brackets around a head and shoulder bust.'
CONSTRUCTION_REFERENCE='No useful Lucide subject match; original reference establishes silhouette and arrangement.'
OMISSIONS='Secondary source detail simplified only where needed for 48 px legibility.'
class Drawing(Solo48):
    icon_id='rectangle-single-man-focus'
    keyshape=Keyshape.VRECT_L
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
        self.box('frame',8,4,40,44,4)
        self.circle('head',24,18,3)
        self.path('shoulders',(20,33),[('L',(20,32)),('C',(24,29),(20,30),(22,29)),('C',(28,32),(26,29),(28,30)),('L',(28,33))])
        for n,points in enumerate((((14,16),(14,11),(19,11)),((29,11),(34,11),(34,16)),((14,32),(14,37),(19,37)),((29,37),(34,37),(34,32)))):self.add_polyline(f'focus-{n}',*points)

# Human reference: icon_set/references/human_ref/full_body_ref.png.
# Bust: head center (24,18), radius 3; shoulders reach y29. Centerline gap 8, visible ink gap 4.

Drawing.exception = {'reason': 'Four independent focus brackets, a person and a surrounding panel are all essential. The narrow but visible gaps preserve the complete composition with 4 px strokes.', 'approved_by': 'user-authorized gpt-6 visual review', 'approved_on': '2026-09-29', 'svg_sha256': '6ad94eddfadcbfa6c088bc0301928d2659190b01f14e41be2bdfe754a9139109'}
