'An oval brooch has a small central gem and a horizontal pin ending in a round clasp. HRECT_M spans the ornament and extended pin. One oval owns its concentric gem; shared y24 axis owns pin and clasp. Source supplies ornament and fastening; Lucide pin suggests a single simple shaft, not its pushpin silhouette. Omit decoration absent from source.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'da8e4b4b-2941-4694-9449-49cdee922e25'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_08/brooch_da8e4b4b-2941-4694-9449-49cdee922e25.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'oval-brooch-with-extended-pin'
    keyshape = Keyshape.HRECT_M
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ('Decorative Round Jewelry Brooch',)
    keywords = ('decorative', 'round', 'jewelry', 'brooch')
    def build(self):
        def path(name,start,steps,closed=False):
            members=[]; point=start
            for j,step in enumerate(steps):
                member=f'{name}-{j}'
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep);point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        path('face',(28,24),[((4,24),12,14,True),((28,24),12,14,True)],True)
        circle('gem',16,24,3)
        circle('clasp',41,24,3)
        self.add_line('pin',(28,24),(38,24))
        self.relate('connect','pin','face');self.relate('connect','pin','clasp')
