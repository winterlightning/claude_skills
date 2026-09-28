'Segmented Insect Larva.\nPlan and review: Retained curled larva silhouette and broad head. Reduced three segmentation bands to two; removed the tight tail band and rebuilt exact extrema.\nKeyshape: SQUARE, exact SOLO48 envelope.\nConstruction reference: Source render; no useful exact local Lucide match.'
from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = '26443253-e3d6-433d-8f28-747729ca34c3'
SOURCE_PATH = '/Applications/Workspaces/pictographic/claude_skills/pictographic-primitives/_uncategorized_24/larva_26443253-e3d6-433d-8f28-747729ca34c3.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'curved-larva'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('curved', 'larva')

    def build(self):

        def path(name, start, steps, closed=False):
            members=[]; point=start
            for index, step in enumerate(steps):
                member=f"{name}-{index}"
                if len(step)==2:
                    self.add_line(member,point,step); point=step
                else:
                    end,rx,ry,sweep=step
                    self.add_arc(member,point,end,radius_x=rx,radius_y=ry,sweep=sweep); point=end
                members.append(member)
            self.add_contour(name,*members,closed=closed)
        def circle(name,x,y,r):
            path(name,(x-r,y),[((x+r,y),r,r,True),((x-r,y),r,r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)
        def curve(name,start,*segments):
            self.add_bezier(name,start,*segments)

        curve('outer',(6,34),((6,24),(24,28),(24,14)),((24,8),(28,6),(32,6)),((38,6),(42,10),(42,16)),((42,30),(28,42),(14,42)),((8,42),(6,38),(6,34)))
        self.add_arc('band-top',(24,16),(42,16),radius_x=18,radius_y=8,sweep=False)
        self.add_arc('band-middle',(20,26),(36,32),radius_x=16,radius_y=8,sweep=False)
        
        for s in ('band-top','band-middle'):self.relate('connect',s,'outer')
