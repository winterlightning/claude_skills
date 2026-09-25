'A side-view domed infant bonnet with broad curved opening band and two tied ribbons. VRECT_L gives height for the ties. Source supplies domed crown, sweeping opening and tied lower edge. Lucide hard-hat informs coherent crown curve; no bonnet-specific match. Band thickness retained; reduce bow to two tied ribbon runs if loops cannot fit.'
from ...keyshapes import Keyshape
from ._base import Solo48
SOURCE_ICON_ID = '83e67aec-5937-46a8-b003-935e44c13b02'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_07/bonnet_83e67aec-5937-46a8-b003-935e44c13b02.svg'
AUTHOR = "gpt-6-astra"
class Drawing(Solo48):
    icon_id = 'tied-infant-bonnet'
    keyshape = Keyshape.VRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    aliases = ['Tied Infant Bonnet']
    keywords = ['bonnet', 'baby', 'hat', 'infant', 'bow', 'ribbon', 'clothing']
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
        self.add_bezier('crown',(8,14),((10,7),(16,4),(24,4)),((33,4),(40,11),(40,20)),((40,26),(36,30),(32,32)))
        self.add_bezier('opening',(32,32),((20,33),(8,28),(8,18)),((8,16),(8,15),(8,14)))
        self.add_contour('bonnet','crown','opening',closed=True)
        self.add_bezier('band',(8,14),((22,10),(31,23),(32,32)))
        self.relate('connect','band','bonnet')
        self.add_bezier('tie-left',(32,32),((24,34),(18,36),(22,44)))
        self.add_bezier('tie-right',(32,32),((32,38),(36,42),(40,44)))
        self.relate('connect','tie-left','tie-right')
        self.relate('connect','tie-left','bonnet')
        self.relate('connect','tie-right','bonnet')
        self.relate('connect','tie-left','band')
        self.relate('connect','tie-right','band')
