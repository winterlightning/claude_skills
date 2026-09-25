'Broad domed cycling helmet with a hanging chin strap and round fastener. The shell owns its split rim attachment nodes; buckle is a quarter-circle loop. HRECT_L preserves broad low shell with height for strap. Source contributes dome, single hanging tail and buckle. Lucide hard-hat contributes smooth dome and horizontal rim; omit its crown ridge because absent in source. Omit strap thickness.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '08152344-8f0e-4721-af0a-ec9f68eb4218'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_06/biking helmet_08152344-8f0e-4721-af0a-ec9f68eb4218.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'domed-cycling-helmet-with-chin-strap'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Domed Cycling Helmet with Chin Strap']
    keywords = ['helmet', 'cycling', 'strap', 'buckle', 'dome', 'safety', 'headwear']
    def build(self):
        def path(name,start,steps,closed=False):
            point=start; members=[]
            for i,step in enumerate(steps):
                pid=f'{name}-{i}'
                if len(step)==2:
                    self.add_line(pid,point,step);point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(pid,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(pid)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x,y-r),[((x+r,y),r,r,True),((x,y+r),r,r,True),((x-r,y),r,r,True),((x,y-r),r,r,True)],True)
        path('shell',(4,20),[((24,8),20,12,True),((44,20),20,12,True),(28,20),(12,20),(4,20)],True)
        self.add_polyline('strap',(12,20),(12,31),(25,31))
        self.add_line('buckle-stem',(28,20),(28,28))
        circle('buckle',28,31,3)
        self.add_line('tail',(28,34),(28,40))
        for a,b in [('shell','strap'),('shell','buckle-stem'),('buckle-stem','buckle'),('strap','buckle'),('buckle','tail')]:
            self.relate('connect',a,b)
