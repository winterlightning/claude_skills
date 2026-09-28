# Final repair: Integrate ears into one outer contour; retain central round muzzle without crowded inner brow.
'Round Eared Chimpanzee Face\nPlan: Chimp face made of a broad skull and continuous muzzle; ears are open attached arcs.\nReference: No useful exact Lucide match; supplied reference governs the subject.\nReduction: Reduce inner heart muzzle to broad brow; visual identity review required.\nKeyshape: HRECT_L; exact SOLO48 contract envelope.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '8d911861-b769-4909-ac71-eb23683fc359'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__round-eared-chimpanzee-face/20260927T171905Z-thuan-mac-1/reference/chimpanzee_8d911861-b769-4909-ac71-eb23683fc359.svg'
AUTHOR = "gpt-6"

class Drawing(Solo48):
    icon_id = 'round-eared-chimpanzee-face'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "primitives-generate"
    categories = ("primitives", "primitives-generate")
    keywords = ('round', 'eared', 'chimpanzee', 'face')

    def build(self):

        def path(name, start, steps, closed=False):
            members, point = [], start
            for index, step in enumerate(steps):
                member = f"{name}-{index}"
                if len(step) == 2:
                    self.add_line(member, point, step)
                    point = step
                else:
                    end, rx, ry, sweep = step
                    self.add_arc(member, point, end, radius_x=rx, radius_y=ry, sweep=sweep)
                    point = end
                members.append(member)
            self.add_contour(name, *members, closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[((x+rx,y),rx,ry,True),((x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r):
            ellipse(name,x,y,r,r)
        def box(name,l,t,r,b,rad=4):
            path(name,(l+rad,t),[(r-rad,t),((r,t+rad),rad,rad,True),(r,b-rad),((r-rad,b),rad,rad,True),(l+rad,b),((l,b-rad),rad,rad,True),(l,t+rad),((l+rad,t),rad,rad,True)],True)

        path('head',(24,8),[((36,20),12,12,True),((44,24),8,4,True),((36,28),8,4,True),((24,40),12,12,True),((12,28),12,12,True),((4,24),8,4,True),((12,20),8,4,True),((24,8),12,12,True)],True)
        self.add_bezier('face-left-lower',(24,40),((20,36),(20,32),(21,28)))
        self.add_bezier('face-left-cheek',(21,28),((20,24),(20,18),(22,20)))
        self.add_bezier('face-left-brow',(22,20),((23,20),(24,21),(24,22)))
        self.add_bezier('face-right-brow',(24,22),((24,21),(25,20),(26,20)))
        self.add_bezier('face-right-cheek',(26,20),((28,18),(28,24),(27,28)))
        self.add_bezier('face-right-lower',(27,28),((28,32),(28,36),(24,40)))
        self.add_contour('face','face-left-lower','face-left-cheek','face-left-brow',
                         'face-right-brow','face-right-cheek','face-right-lower',closed=True)
        self.relate('connect','face','head')
