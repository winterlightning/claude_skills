"""Quail Bird with Topknot.

Plan: Quail bounds6,6,42,42. Plump profile, crest, wing and two legs. Source asymmetry is essential.
Construction reference: Lucide bird: continuous back/belly silhouette, simple wing and stick feet
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'f16c7aac-6428-480f-9ba6-4d2eab0942e5'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__quail-with-curved-crest/20260927T170540Z-thuan-mac-1/reference/quail_f16c7aac-6428-480f-9ba6-4d2eab0942e5.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'quail-with-curved-crest'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'primitives-generate'
    categories = ('primitives', 'primitives-generate')
    aliases = ()
    keywords = ('quail', 'with', 'curved', 'crest')

    def build(self):

        def path(name, start, commands, closed=False):
            here=start; members=[]
            for index,(kind,end,*args) in enumerate(commands):
                member=f"{name}-{index}"
                if kind=='L': self.add_line(member,here,end)
                elif kind=='A': self.add_arc(member,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(member,here,(args[0],args[1],end))
                here=end; members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
        def rect(name,x,y,w,h,r=4):
            path(name,(x+r,y),[('L',(x+w-r,y)),('A',(x+w,y+r),r,r,True),('L',(x+w,y+h-r)),('A',(x+w-r,y+h),r,r,True),('L',(x+r,y+h)),('A',(x,y+h-r),r,r,True),('L',(x,y+r)),('A',(x+r,y),r,r,True)],True)
        def line(name,a,b): self.add_line(name,a,b)
        def poly(name,*points,closed=False): self.add_polyline(name,*points,closed=closed)
        def join(a,b): self.relate('connect',a,b)

        path('bird',(6,34),[('C',(24,16),(12,24),(17,18)),('C',(30,10),(26,16),(24,10)),('C',(36,14),(34,10),(32,14)),('L',(42,18)),('L',(36,22)),('C',(20,34),(36,30),(30,34)),('L',(6,34))],True)
        self.add_arc('crest',(30,10),(38,10),radius_x=4,sweep=True);join('crest','bird')
        poly('leg-left',(20,34),(20,42),(24,42));poly('leg-right',(32,31),(34,42),(38,42));join('leg-left','bird');join('leg-right','bird')
