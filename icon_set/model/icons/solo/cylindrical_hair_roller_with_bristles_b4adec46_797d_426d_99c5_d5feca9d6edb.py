"""An upright cylindrical roller has an oval top, curved lower edge and two curved horizontal divisions. Short bristles project from both sides, and a vertical seam runs down the front.
Symbol plan: Symmetric roller with elliptical end caps, one curved division and three paired bristles. Omit the top interior ellipse and vertical seam to retain generous openings.
Keyshape: VRECT_L; centerline extremes (8,4)-(40,44).
Construction reference: cylinder; local original and atomic geometry inspected for Lucide.
"""
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = 'b4adec46-797d-426d-99c5-d5feca9d6edb'
SOURCE_PATH = 'pictographic-primitives/beauty/hair dress round brush_b4adec46-797d-426d-99c5-d5feca9d6edb.svg'
AUTHOR = 'gpt-6'

class BatchSolo(Solo48):
    icon_id = 'cylindrical-hair-roller-with-bristles'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = 'beauty'
    aliases = ()
    keywords = ('cylindrical', 'hair', 'roller', 'with', 'bristles')

    def build(self):

        def segments(name,*points):
            for j,(a,b) in enumerate(zip(points,points[1:]),1):
                self.add_line(f'{name}-{j}',a,b)

        def circle(name,cx,cy,r):
            self.add_arc(name+'-top',(cx-r,cy),(cx+r,cy),radius_x=r)
            self.add_arc(name+'-bottom',(cx+r,cy),(cx-r,cy),radius_x=r)
            self.add_contour(name,name+'-top',name+'-bottom',closed=True)

        def rect(name,l,t,r,b,q=0):
            if not q:
                self.add_polyline(name,(l,t),(r,t),(r,b),(l,b),closed=True)
                return
            points=[(l+q,t),(r-q,t),(r,t+q),(r,b-q),(r-q,b),(l+q,b),(l,b-q),(l,t+q),(l+q,t)]
            ids=[]
            for j,(a,z) in enumerate(zip(points,points[1:])):
                if a==z:continue
                n=f'{name}-{j}'
                if j%2:self.add_arc(n,a,z,radius_x=q)
                else:self.add_line(n,a,z)
                ids.append(n)
            self.add_contour(name,*ids,closed=True)

        self.add_arc('cap',(15,9),(33,9),radius_x=9,radius_y=5)
        segments('side-right',(33,9),(33,14),(33,24),(33,34),(33,39))
        self.add_arc('base',(33,39),(15,39),radius_x=9,radius_y=5)
        segments('side-left',(15,39),(15,34),(15,24),(15,14),(15,9))
        self.add_contour('roller','cap','side-right-1','side-right-2','side-right-3','side-right-4','base','side-left-1','side-left-2','side-left-3','side-left-4',closed=True)
        self.add_arc('division',(15,24),(33,24),radius_x=9,radius_y=3,sweep=False)
        self.relate('connect','division','roller')
        for x,end in [(15,8),(33,40)]:
         for y in (14,24,34):
          n=f'bristle-{x}-{y}'
          self.add_line(n,(x,y),(end,y))
          self.relate('connect',n,'roller')
          if y==24:self.relate('connect',n,'division')
