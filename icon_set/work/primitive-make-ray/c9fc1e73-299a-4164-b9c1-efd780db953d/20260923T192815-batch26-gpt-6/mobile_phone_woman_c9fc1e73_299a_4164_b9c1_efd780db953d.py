"""A mobile phone displaying woman icon.
Construction reference: human_ref/user.svg.
"""
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48
SOURCE_ICON_ID = 'c9fc1e73-299a-4164-b9c1-efd780db953d'
SOURCE_PATH = 'icon_set/work/todo-references/mobile phone woman_c9fc1e73-299a-4164-b9c1-efd780db953d.svg'
AUTHOR = 'gpt-6'
class Drawing(Solo48):
    icon_id = 'mobile-phone-woman'
    keyshape = Keyshape.VRECT_L
    # Visible ink extrema: (6, 2, 42, 46).
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    aliases = ()
    keywords = ('mobile', 'phone', 'woman')

    def circle(self,name,cx,cy,r):
        self.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
        self.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
        self.add_contour(name,name+'-a',name+'-b',closed=True)
    def rect(self,name,x,y,w,h,r=2):
        pts=[(x+r,y),(x+w-r,y),(x+w,y+r),(x+w,y+h-r),(x+w-r,y+h),(x+r,y+h),(x,y+h-r),(x,y+r)]
        names=[]
        for i,a in enumerate(pts):
            n=f'{name}-{i}';b=pts[(i+1)%8]
            if i%2:self.add_arc(n,a,b,radius_x=r)
            else:self.add_line(n,a,b)
            names.append(n)
        self.add_contour(name,*names,closed=True)

    def build(self):

        # Plan: rounded upright phone and lower band; content owns its own geometry.
        self.rect('phone',8,4,32,40)
        self.add_line('separator',(8,36),(40,36))
        self.relate('connect','phone','separator')

        # Human reference: icon_set/references/human_ref/user.svg.
        # Head center (24,19), radius 5; nearest shoulders (19,31)/(29,31).
        # Distance sqrt(5^2+12^2)-5=8 centerline, exactly 4 ink units.
        self.circle('head',24,19,5)
        self.add_bezier('hair',(18,25),((21,21),(15,13),(24,13)),((33,13),(27,21),(30,25)))
        self.add_bezier('shoulders',(16,36),((17,32),(18,31),(19,31)))
        self.add_polyline('collar',(19,31),(24,35),(29,31))
        self.add_bezier('shoulders-right',(29,31),((30,31),(31,32),(32,36)))
        self.relate('connect','shoulders','collar')
        self.relate('connect','shoulders-right','collar')
        self.relate('connect','shoulders','separator')
        self.relate('connect','shoulders-right','separator')
