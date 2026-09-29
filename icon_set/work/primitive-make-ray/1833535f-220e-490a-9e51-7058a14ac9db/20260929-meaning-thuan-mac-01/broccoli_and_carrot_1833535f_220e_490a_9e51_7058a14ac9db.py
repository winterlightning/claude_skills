"""Restored a tilted carrot with a short surface notch, a three-stroke leafy top, and a branching broccoli stalk below rounded florets.
Symbol plan: coherent named contours; repeated shapes use shared helpers.
Construction: Lucide carrot: tapered diagonal root and top leaves; supplied reference defines broccoli lobes and arrangement.
Keyshape: SQUARE; bounds checked and any deliberate optical deviation recorded.
Reduction: Fine floret bumps reduced to four lobes and carrot grooves to one notch."""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = '1833535f-220e-490a-9e51-7058a14ac9db'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__broccoli-and-carrot/20260929T025914Z-thuan-mac/reference/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'broccoli-and-carrot'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects/general'
    aliases = ()
    keywords = ('broccoli', 'and', 'carrot')

    def build(self):

        def curve(name,start,c1,c2,end): self.add_bezier(name,start,(c1,c2,end))
        def path(name,start,steps,closed=False):
            point=start;ids=[]
            for j,(kind,end,*args) in enumerate(steps):
                part=f'{name}-{j}'
                if kind=='L':self.add_line(part,point,end)
                elif kind=='C':curve(part,point,args[0],args[1],end)
                elif kind=='A':self.add_arc(part,point,end,radius_x=args[0],sweep=args[1])
                ids.append(part);point=end
            self.add_contour(name,*ids,closed=closed)
        def circle(name,x,y,r):path(name,(x-r,y),[('A',(x+r,y),r,True),('A',(x-r,y),r,True)],True)
        def box(name,l,t,r,b,rad):
            path(name,(l+rad,t),[('L',(r-rad,t)),('A',(r,t+rad),rad,True),('L',(r,b-rad)),('A',(r-rad,b),rad,True),('L',(l+rad,b)),('A',(l,b-rad),rad,True),('L',(l,t+rad)),('A',(l+rad,t),rad,True)],True)

        path('florets',(8,23),[('C',(6,14),(3,23),(3,17)),('C',(13,10),(6,10),(9,9)),('C',(23,10),(15,3),(21,3)),('C',(29,16),(27,9),(30,12)),('C',(23,22),(31,21),(26,23)),('C',(15,24),(21,26),(18,25)),('C',(8,23),(12,27),(9,26))],True)
        path('stalk',(10,25),[('L',(15,35)),('L',(22,35)),('L',(22,24))])
        self.add_line('branch',(17,29),(22,24))
        path('carrot',(27,24),[('C',(40,32),(31,17),(42,22)),('C',(26,42),(36,37),(30,41)),('C',(23,38),(22,43),(22,40)),('C',(27,24),(23,33),(25,27))],True)
        self.add_line('carrot-mark',(27,27),(31,30))
        self.add_polyline('greens',(36,22),(36,15),(41,13))
        self.add_line('leaf',(36,22),(44,20))
        self.relate('connect','carrot-mark','carrot');self.relate('connect','greens','leaf')
 