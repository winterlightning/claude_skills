"""Use outlined heads and a separate curved balloon string.
Symbol plan: Shared full_body_ref.png: circular heads and coherent limbs; exact 4px detached head gap.
Keyshape SQUARE; exact contract bounds.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'bb01aec5-8d69-470f-9cde-ccfb72c0af02'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__couple-beside-heart-shaped-balloon/20260929T104736Z-thuan-mac/reference/dating couple balloon_bb01aec5-8d69-470f-9cde-ccfb72c0af02.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'couple-beside-heart-shaped-balloon'
    keyshape = Keyshape.SQUARE
    category = "objects"
    human_construction = "bust"
    semantic_role = "MAIN"
    semantic_kind = "noun"
    aliases = ()
    keywords = ()
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def arc(n,a,b,r,ry=None,s=True): self.add_arc(n,a,b,radius_x=r,radius_y=ry or r,sweep=s)
        def poly(n,*p,closed=False): self.add_polyline(n,*p,closed=closed)
        def contour(n,*m,closed=False): self.add_contour(n,*m,closed=closed)
        def join(a,b): self.relate('connect',a,b)
        def bez(n,a,*segs): self.add_bezier(n,a,*segs)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            contour(n,n+'a',n+'b',closed=True)
        def box(n,l,t,r,b,k=2):
            pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k),(l+k,t)]
            names=[]
            for i,(a,z) in enumerate(zip(pts,pts[1:])):
                if a==z: continue
                m=n+str(i); names.append(m)
                if i%2: arc(m,a,z,k)
                else: line(m,a,z)
            contour(n,*names,closed=True)

        for n,x in [('left',10),('right',24)]:
            circle('head-'+n,x,24,3)
            line('torso-'+n,(x,35),(x,37))
            poly('legs-'+n,(x-4,42),(x,37),(x+4,42));join('torso-'+n,'legs-'+n)
            self.mark_human_figure(n,head='head-'+n,torso='torso-'+n,torso_junction='start')
        line('hands',(10,35),(24,35));join('hands','torso-left');join('hands','torso-right')
        bez('balloon',(36,20),((32,17),(30,14),(30,11)),((30,8),(31,6),(33,6)),((35,6),(36,8),(36,8)),((36,8),(37,6),(39,6)),((41,6),(42,8),(42,11)),((42,14),(40,17),(36,20)))
        bez('string',(36,20),((32,27),(42,31),(36,38)));join('string','balloon')
