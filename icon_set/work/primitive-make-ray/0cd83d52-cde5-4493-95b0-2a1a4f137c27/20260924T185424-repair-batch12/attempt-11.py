"""A car emits jagged noise marks beneath a lightning bolt.
Plan: complete reference composition, coherent strokes and parameterized repeat definitions.
SOLO48 SQUARE; omissions: Fine body rounding and window divider omitted; wheels and sound marks retained.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID='0cd83d52-cde5-4493-95b0-2a1a4f137c27'
SOURCE_PATH = 'pictographic-primitives/ecology/noise pollution car_0cd83d52-cde5-4493-95b0-2a1a4f137c27.svg'
AUTHOR='gpt-6'
class Drawing(Solo48):
    icon_id='noise-pollution-car'
    keyshape=Keyshape.HRECT_L
    semantic_role='MAIN'
    semantic_kind='noun'
    category='objects'
    aliases=()
    keywords=('noise', 'pollution', 'car')

    def circle(self,n,x,y,r):
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def box(self,n,x,y,w,h,r=2):
        p=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        ids=[]
        for i in range(8):
            k=n+'-'+str(i);ids.append(k)
            if i%2:self.add_arc(k,p[i],p[(i+1)%8],radius_x=r)
            else:self.add_line(k,p[i],p[(i+1)%8])
        self.add_contour(n,*ids,closed=True)

    def build(self):
        # One car silhouette owns its rounded wheel bulges; wheel/body seams
        # are omitted so the fenders have no narrow enclosed pockets.
        self.add_polyline('bolt',(28,8),(18,14),(28,14),(26,18))
        self.add_polyline('noise-left',(6,8),(8,12),(6,16))
        self.add_polyline('noise-right',(42,8),(40,12),(42,16))
        self.add_polyline('body',(12,36),(4,36),(4,28),(12,28),(18,26),(30,26),(36,28),(44,28),(44,36),(36,36))
        self.add_arc('wheel-right',(36,36),(28,36),radius_x=4)
        self.add_line('chassis',(28,36),(20,36))
        self.add_arc('wheel-left',(20,36),(12,36),radius_x=4)
        self.add_contour('car',*(f'body-{j}' for j in range(1,10)),'wheel-right','chassis','wheel-left',closed=True)
        self.contours=[c for c in self.contours if c.contour_id!='body']
