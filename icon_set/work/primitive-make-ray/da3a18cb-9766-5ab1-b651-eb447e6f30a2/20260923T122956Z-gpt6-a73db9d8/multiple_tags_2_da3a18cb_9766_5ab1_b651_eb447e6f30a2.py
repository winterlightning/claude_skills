from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = 'da3a18cb-9766-5ab1-b651-eb447e6f30a2'
SOURCE_PATH = 'icon_set/work/todo-references/multiple tags 2_da3a18cb-9766-5ab1-b651-eb447e6f30a2.svg'
AUTHOR = 'gpt-6'
SUBJECT = 'Two overlapping price tags, with a circular hole in the foreground tag.'
CONSTRUCTION_PLAN = 'Front diagonal tag and partially hidden upright rear tag share actual overlap boundary endpoints; retain the round hole and diagonal orientation.'
KEYSHAPE_CENTERLINE_BOUNDS = [6, 6, 42, 42]

def circle(icon,name,cx,cy,r):
    icon.add_arc(name+'-a',(cx-r,cy),(cx+r,cy),radius_x=r)
    icon.add_arc(name+'-b',(cx+r,cy),(cx-r,cy),radius_x=r)
    icon.add_contour(name,name+'-a',name+'-b',closed=True)

def rounded_rect(icon,name,left,top,right,bottom,r=4,bottom_split=None):
    points=[(left+r,top),(right-r,top),(right,top+r),(right,bottom-r),(right-r,bottom)]
    if bottom_split is not None:points.append((bottom_split,bottom))
    points += [(left+r,bottom),(left,bottom-r),(left,top+r)]
    members=[]
    for i,start in enumerate(points):
        end=points[(i+1)%len(points)];n=f'{name}-{i}';members.append(n)
        if start[0]!=end[0] and start[1]!=end[1]:icon.add_arc(n,start,end,radius_x=r)
        else:icon.add_line(n,start,end)
    icon.add_contour(name,*members,closed=True)

def monitor(icon):
    # Shared screen, central attachment and two base halves, drawn on SOLO48.
    rounded_rect(icon,'screen',6,6,42,34,bottom_split=24)
    icon.add_line('stand',(24,34),(24,42))
    icon.add_line('base-left',(16,42),(24,42))
    icon.add_line('base-right',(24,42),(32,42))
    icon.relate('connect','screen','stand')
    icon.relate('connect','stand','base-left','base-right')

class Drawing(Solo48):
    icon_id = 'multiple-tags-2'
    keyshape = Keyshape.SQUARE
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ('multiple', 'tags', '2')

    def build(self):
        self.add_line('front-upper',(6,28),(26,8))
        self.add_bezier('front-shoulder',(26,8),((28,6),(28,6),(30,6)))
        self.add_line('front-top',(30,6),(36,6))
        self.add_arc('front-corner',(36,6),(40,10),radius_x=4)
        self.add_line('front-right-1',(40, 10),(40, 12))
        self.add_line('front-right-2',(40, 12),(40, 20))
        self.add_line('front-right-3',(40, 20),(24, 36))
        self.add_line('front-right-4',(24, 36),(20, 40))
        self.add_bezier('front-bottom',(20,40),((18,42),(16,42),(14,40)))
        self.add_line('front-lower',(14,40),(8,34))
        self.add_bezier('front-left',(8,34),((6,32),(6,30),(6,28)))
        self.add_contour('front','front-upper','front-shoulder','front-top','front-corner',*[f'front-right-{i}' for i in range(1,5)],'front-bottom','front-lower','front-left',closed=True)
        self.add_line('rear-upper-1',(40, 12),(42, 16))
        self.add_line('rear-upper-2',(42, 16),(42, 38))
        self.add_arc('rear-br',(42,38),(38,42),radius_x=4)
        self.add_line('rear-bottom',(38,42),(28,42))
        self.add_arc('rear-bl',(28,42),(24,38),radius_x=4)
        self.add_line('rear-left',(24,38),(24,36))
        self.add_contour('rear','rear-upper-1','rear-upper-2','rear-br','rear-bottom','rear-bl','rear-left')
        self.relate('connect','front','rear')
        circle(self,'hole',30,16,2)
