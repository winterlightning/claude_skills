'A brimmed-hat archaeologist bust beside an upright spade.\nPlan: SQUARE fits the bust and separate spade side by side.\nReduction: Enlarged the circular jaw and replaced the shoulder curve with a centered ellipse. Omitted sleeve lines and the lower spade handle outline.\nConstruction: Shared human user.svg: circular face and broad smooth shoulders.'
from icon_set.model.keyshapes import Keyshape
from icon_set.model.icons.solo._base import Solo48

SOURCE_ICON_ID = '434aebe0-5637-41b2-ba5b-e41942db8485'
SOURCE_PATH = 'pictographic-primitives/_uncategorized_04/archaeologist_434aebe0-5637-41b2-ba5b-e41942db8485.svg'
AUTHOR = 'gpt-6'

class Drawing(Solo48):
    icon_id = 'archaeologist-beside-a-spade'
    keyshape = Keyshape.SQUARE
    human_construction = "bust"
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects"
    keywords = ('archaeologist', 'beside', 'a', 'spade')

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

        # Human user.svg proportions: circular jaw and centered broad shoulders.
        # Jaw bottom 26, shoulder top 30: four centerline units, touching ink.
        self.add_arc('hat',(7,17),(25,17),radius_x=9,radius_y=11)
        self.add_polyline('brim',(6,17),(7,17),(25,17),(26,17))
        self.relate('connect','hat','brim')
        self.add_arc('jaw',(7,17),(25,17),radius_x=9,sweep=False)
        self.relate('connect','jaw','brim');self.relate('connect','jaw','hat')
        self.add_arc('shoulders',(6,42),(26,42),radius_x=10,radius_y=12)
        self.relate('connect','jaw','shoulders')
        self.add_polyline('spade',(34,28),(34,20),(38,16),(42,20),(42,28),(38,28),closed=True)
        self.add_line('shaft',(38,28),(38,42));self.relate('connect','shaft','spade')
