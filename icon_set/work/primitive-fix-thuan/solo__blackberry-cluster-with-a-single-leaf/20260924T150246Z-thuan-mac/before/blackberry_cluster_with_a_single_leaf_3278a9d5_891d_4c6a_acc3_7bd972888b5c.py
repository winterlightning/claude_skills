"""Blackberry cluster with one upper-right leaf.
VRECT_L reaches (8,4)-(40,44). Berry and leaf share one outer contour and
an explicit attachment edge. Three broad drupelet regions keep the tapered
cluster readable; omit fine fruit lobes and the small stem curl. The source
supplies arrangement; Lucide grape supplies the repeated round-cell principle.
Internal seams attach at actual outer nodes. AUTHOR updated in this batch.
"""
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '3278a9d5-891d-4c6a-acc3-7bd972888b5c'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/blackberry_3278a9d5-891d-4c6a-acc3-7bd972888b5c.svg'
AUTHOR = 'gpt-6-astra'

class Drawing(Solo48):
    icon_id = 'blackberry-cluster-with-a-single-leaf'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "Uncategorized"
    aliases = ('Fresh Berry Fruit with Leaf',)
    keywords = ('blackberry','berry','fruit','leaf','cluster','drupelets','food')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            if name not in ('berry','leaf'): self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('berry',(32,16),[('C',(40,24),(38,16),(40,20)),('C',(34,34),(40,28),(38,32)),('C',(24,44),(34,42),(28,44)),('C',(14,34),(20,44),(14,42)),('C',(8,24),(10,32),(8,28)),('C',(24,16),(8,16),(14,12))])
        path('lobes',(8,24),[('C',(24,26),(12,32),(20,32)),('C',(40,24),(28,32),(36,32))]);join('lobes','outline')
        path('middle',(24,16),[('C',(24,26),(19,18),(19,23)),('L',(24,35))]);join('middle','outline');join('middle','lobes')
        path('leaf',(24,16),[('C',(38,4),(24,8),(30,4)),('C',(32,16),(38,10),(36,14))])
        self.add_contour('outline', 'berry-0','berry-1','berry-2','berry-3','berry-4','berry-5','leaf-0','leaf-1',closed=True)
        line('attachment',(24,16),(32,16));join('attachment','outline')
