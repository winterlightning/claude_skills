from ...keyshapes import Keyshape
from ._base import Solo48

SOURCE_ICON_ID = 'cd870bf9-9544-4c9b-a2dd-608effb82774'
SOURCE_PATH = 'icon_set/work/todo-references/people arrows_cd870bf9-9544-4c9b-a2dd-608effb82774.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    """Two people with a bidirectional arrow between them.
    Plan: Two identical circular heads and broad shoulder arcs, plus a centered horizontal double arrow.
    Reference: user-search: simple circular head; shared human_ref/user.svg owns head and shoulder proportions.
    """
    icon_id = 'people-arrows'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    aliases = ()
    keywords = ('people', 'arrows')
    # Two heads r=5 at y=13 end at y=18. Shoulder arcs have apex y=26: exact centerline gap 8, ink gap 4. Busts are not stick figures.

    def circle(self,n,x,y,r,ry=None):
        ry=r if ry is None else ry
        self.add_arc(n+'-a',(x-r,y),(x+r,y),radius_x=r,radius_y=ry)
        self.add_arc(n+'-b',(x+r,y),(x-r,y),radius_x=r,radius_y=ry)
        self.add_contour(n,n+'-a',n+'-b',closed=True)

    def rounded(self,n,l,t,r,b,k=4):
        pts=[(l+k,t),(r-k,t),(r,t+k),(r,b-k),(r-k,b),(l+k,b),(l,b-k),(l,t+k)]
        members=[]
        for i,p in enumerate(pts):
            q=pts[(i+1)%8];name=f'{n}-{i}';members.append(name)
            if i%2:self.add_arc(name,p,q,radius_x=k)
            else:self.add_line(name,p,q)
        self.add_contour(n,*members,closed=True)

    def dollar(self):
        self.add_line('s-top',(29,16),(24,16))
        self.add_arc('s-left',(24,16),(24,24),radius_x=4,sweep=False)
        self.add_arc('s-right',(24,24),(24,32),radius_x=4)
        self.add_line('s-bottom',(24,32),(19,32))
        self.add_contour('dollar','s-top','s-left','s-right','s-bottom')
        self.add_line('stem-top',(24,12),(24,16));self.relate('connect','stem-top','dollar')
        self.add_line('stem-bottom',(24,32),(24,36));self.relate('connect','stem-bottom','dollar')

    def bust(self,n,x,y,r,width,body_y,body_ry):
        # Detached head bottom = y+r; shoulder apex = body_y-body_ry.
        # Author parameters require their difference to be exactly eight.
        self.circle(n+'-head',x,y,r)
        self.add_arc(n+'-shoulders',(x-width,body_y),(x+width,body_y),radius_x=width,radius_y=body_ry)

    def build(self):

        for i,x in enumerate((12,36)):
            self.bust(f'person-{i}',x,13,5,8,32,6)
        self.add_polyline('arrow',(12,36),(24,36),(36,36))
        self.add_polyline('arrow-left',(16,32),(12,36),(16,40))
        self.add_polyline('arrow-right',(32,32),(36,36),(32,40))
        self.relate('connect','arrow','arrow-left');self.relate('connect','arrow','arrow-right')
