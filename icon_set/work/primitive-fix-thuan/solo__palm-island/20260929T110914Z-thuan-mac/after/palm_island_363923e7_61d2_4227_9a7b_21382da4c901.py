"""The current palm is mechanically symmetric and crowded against a flattened island. No written feedback. Rebuilt an asymmetric curved trunk and three flowing fronds over a broad island arc and water line.
Construction: No local palm-tree original found; source informs intentional leaning trunk and irregular fronds.
Plan: SQUARE SOLO48; shared shape parameters and scoped real joins.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '363923e7-61d2-4227-9a7b-21382da4c901'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__palm-island/20260929T110914Z-thuan-mac/reference/island_363923e7-61d2-4227-9a7b-21382da4c901.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'palm-island'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'primitives-generate'
    aliases = ()
    keywords = ('palm', 'island')
    
    def build(self):

        def line(n,a,b): self.add_line(n,a,b)
        def poly(n,*ps,closed=False): self.add_polyline(n,*ps,closed=closed)
        def bez(n,a,*ss): self.add_bezier(n,a,*ss)
        def arc(n,a,b,rx,ry=None,s=True): self.add_arc(n,a,b,radius_x=rx,radius_y=ry,sweep=s)
        def circle(n,x,y,r):
            arc(n+'a',(x-r,y),(x+r,y),r);arc(n+'b',(x+r,y),(x-r,y),r)
            self.add_contour(n,n+'a',n+'b',closed=True)
        def path(n,a,commands,closed=False):
            members=[]
            for j,c in enumerate(commands):
                k,b,*args=c; name=n+str(j)
                if k=='L': line(name,a,b)
                elif k=='A': arc(name,a,b,*args)
                elif k=='C': bez(name,a,(args[0],args[1],b))
                members.append(name);a=b
            self.add_contour(n,*members,closed=closed)
        def rect(n,x,y,w,h,r=0):
            if not r: poly(n,(x,y),(x+w,y),(x+w,y+h),(x,y+h),closed=True);return
            path(n,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r),('L',(x+r,y+h)),('A',(x,y+h-r),r),('L',(x,y+r)),('A',(x+r,y),r)],True)
        def join(*ns): self.relate('connect',*ns)

        bez('trunk',(25,15),((26,23),(25,28),(22,34)))
        bez('upper-left',(25,15),((19,6),(13,6),(8,6)))
        bez('upper-right',(25,15),((29,6),(34,6),(40,6)))
        bez('lower-left',(25,15),((14,13),(6,18),(6,23)))
        bez('lower-right',(25,15),((33,15),(42,18),(42,23)))
        join('trunk','upper-left','upper-right','lower-left','lower-right')
        bez('island',(6,42),((9,37),(15,34),(22,34)),((30,34),(37,37),(42,42)));join('trunk','island')
