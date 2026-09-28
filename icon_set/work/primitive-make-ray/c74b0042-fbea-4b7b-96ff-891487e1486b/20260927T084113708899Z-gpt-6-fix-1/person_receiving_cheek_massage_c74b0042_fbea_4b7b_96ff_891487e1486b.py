"""Revision from the inspected source: The rejected face showed two dot eyes and a hand escaping the face; the original closes its eyes during a cheek massage.

Changes: Shaped the eyelids as relaxed curves, pulled the fingers into the circular silhouette, and used the fitted circle keyshape.
Full-body or bust construction follows icon_set/references/human_ref.
"""
'person-receiving-cheek-massage: Relaxed circular face with gently closed eyes and a curved palm, thumb and wrist pressing the cheek. Original redrawn in place after the nine-icon meaning review.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'c74b0042-fbea-4b7b-96ff-891487e1486b'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__person-receiving-cheek-massage/20260927T083143Z-thuan-mac-1/reference/facial cleansing massage_c74b0042-fbea-4b7b-96ff-891487e1486b.svg'
AUTHOR = "gpt-6"

class PersonReceivingCheekMassage(Solo48):
    icon_id = 'person-receiving-cheek-massage'
    keyshape = Keyshape.CIRCLE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'beauty'
    categories = ('primitives', 'beauty')
    aliases = ()
    keywords = ('massage', 'therapy', 'person', 'wellness', 'relaxation', 'treatment', 'body', 'spa')

    def build(self):
        # Symbol plan: Relaxed circular face with gently closed eyes and a curved palm, thumb and wrist pressing the cheek.

        def path(name,start,commands,closed=False):
            members=[];here=start
            for i,(kind,end,*args) in enumerate(commands):
                ident=f'{name}-{i}'
                if kind=='L': self.add_line(ident,here,end)
                elif kind=='A': self.add_arc(ident,here,end,radius_x=args[0],radius_y=args[1],sweep=args[2])
                elif kind=='C': self.add_bezier(ident,here,(args[0],args[1],end))
                members.append(ident);here=end
            self.add_contour(name,*members,closed=closed)
        def ellipse(name,x,y,rx,ry):
            path(name,(x-rx,y),[('A',(x,y-ry),rx,ry,True),('A',(x+rx,y),rx,ry,True),('A',(x,y+ry),rx,ry,True),('A',(x-rx,y),rx,ry,True)],True)
        def circle(name,x,y,r): ellipse(name,x,y,r,r)
        def rounded(name,x0,y0,x1,y1,r):
            path(name,(x0+r,y0),[('L',(x1-r,y0)),('A',(x1,y0+r),r,r,True),('L',(x1,y1-r)),('A',(x1-r,y1),r,r,True),('L',(x0+r,y1)),('A',(x0,y1-r),r,r,True),('L',(x0,y0+r)),('A',(x0+r,y0),r,r,True)],True)
        line=self.add_line;poly=self.add_polyline;dot=self.add_dot
        join=lambda a,b:self.relate('connect',a,b)
        path('face',(24,44),[('A',(4,24),20,20,True),('A',(24,4),20,20,True),('A',(44,24),20,20,True),('A',(40,36),20,20,True)])
        path('hand',(30,42),[('L',(32,40)),('C',(26,34),(32,38),(28,36)),('C',(26,28),(22,32),(22,28)),('C',(33,27),(28,28),(31,25)),('C',(40,36),(35,29),(38,33)),('C',(40,36),(40,38),(40,37))])
        join('face','hand')
        for n,x in [('eye-left',15),('eye-right',29)]:path(n,(x,17),[('C',(x+4,17),(x+1,19),(x+3,19))])
