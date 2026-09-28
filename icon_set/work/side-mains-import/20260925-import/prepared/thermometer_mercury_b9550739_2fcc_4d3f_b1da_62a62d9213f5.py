'thermometer. Taller tube and smaller smoothly joined bulb replace the oversized bowl. Separate mercury line and central dot match the supplied source. Construction reference: local Lucide thermometer.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'b9550739-2fcc-4d3f-b1da-62a62d9213f5'
SOURCE_PATH = 'pictographic-primitives/symbol/thermometer_b9550739-2fcc-4d3f-b1da-62a62d9213f5.svg'
AUTHOR = 'gpt-6'
PARENT_MODULE = 'icon_set/model/icons/solo/thermometer_mercury_b9550739_2fcc_4d3f_b1da_62a62d9213f5.py'
class Drawing(Solo48):
    icon_id = 'thermometer-mercury'
    keyshape = Keyshape.VRECT_M
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('thermometer',)

    def path(self,n,start,commands,closed=False):
        ids=[]
        for i,c in enumerate(commands):
            k=f'{n}-{i}';end=c[1]
            if c[0]=='L':self.add_line(k,start,end)
            elif c[0]=='A':self.add_arc(k,start,end,radius_x=c[2],radius_y=c[3],sweep=c[4])
            elif c[0]=='C':self.add_bezier(k,start,(c[2],c[3],end))
            ids.append(k);start=end
        self.add_contour(n,*ids,closed=closed)
    def circle(self,n,x,y,r):
        self.path(n,(x-r,y),[('A',(x+r,y),r,r,True),('A',(x-r,y),r,r,True)],True)
    def box(self,n,l,t,r,b,rad=4):
        self.path(n,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,rad,True)],True)

    def build(self):
        # Tall straight tube and smoothly swelling round bulb.
        self.path('outline',(15,13),[('A',(33,13),9,9,True),('L',(33,27)),('C',(38,34),(36,29),(38,31)),('C',(24,44),(38,41),(32,44)),('C',(10,34),(16,44),(10,41)),('C',(15,27),(10,31),(12,29)),('L',(15,13))],True)
        self.add_line('mercury',(24,14),(24,25));self.add_dot('bulb-dot',(24,35))

    icon_id = 'thermometer-mercury'
    category = 'objects/symbols'
    aliases = ()
    keywords = ('thermometer', 'temperature', 'weather', 'heat', 'fever', 'measure', 'climate', 'hot')
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
