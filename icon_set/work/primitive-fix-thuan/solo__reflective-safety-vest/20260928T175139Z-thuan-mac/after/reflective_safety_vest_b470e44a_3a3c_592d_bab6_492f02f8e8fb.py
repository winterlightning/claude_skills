"""A symmetric vest outline owns shoulder radius, curved armholes, central seam and two band edges; x symmetry axis 24. Ink extremes (6,2)-(42,46).
Lucide shirt: rounded garment contours and intrinsic neckline. The original establishes the sleeveless armholes and reflective strip."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b470e44a-3a3c-592d-bab6-492f02f8e8fb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__reflective-safety-vest/20260928T175139Z-thuan-mac/reference/safety vest_b470e44a-3a3c-592d-bab6-492f02f8e8fb.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'reflective-safety-vest'
    keyshape = Keyshape.VRECT_L
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('reflective', 'safety', 'vest')

    def build(self):

        def curve(name,start,c1,c2,end):
            self.add_bezier(name,start,(c1,c2,end))
        def path(name,start,steps,closed=False):
            point=start
            ids=[]
            for j,(kind,end,*args) in enumerate(steps):
                part=f'{name}-{j}'
                if kind=='L': self.add_line(part,point,end)
                elif kind=='A': self.add_arc(part,point,end,radius_x=args[0],sweep=args[1])
                elif kind=='C': curve(part,point,args[0],args[1],end)
                ids.append(part)
                point=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)

        path('outline',(16,4),[
            ('L',(24,20)),('L',(32,4)),('L',(34,4)),
            ('A',(38,8),4,True),('L',(38,12)),
            ('C',(40,22),(38,17),(39,20)),
            ('L',(40,28)),('L',(40,36)),('L',(40,40)),
            ('A',(36,44),4,True),('L',(24,44)),('L',(12,44)),
            ('A',(8,40),4,True),('L',(8,36)),('L',(8,28)),('L',(8,22)),
            ('C',(10,12),(9,20),(10,17)),('L',(10,8)),
            ('A',(14,4),4,True),('L',(16,4))],True)
        self.add_polyline('seam',(24,20),(24,28),(24,36),(24,44))
        self.relate('connect','outline','seam')
        for j,y in enumerate((28,36)):
            name=f'band-{j}'
            self.add_polyline(name,(8,y),(24,y),(40,y))
            self.relate('connect',name,'outline')
            self.relate('connect',name,'seam')
