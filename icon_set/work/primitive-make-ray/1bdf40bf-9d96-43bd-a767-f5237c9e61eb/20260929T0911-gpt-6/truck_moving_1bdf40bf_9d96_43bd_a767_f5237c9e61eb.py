from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '1bdf40bf-9d96-43bd-a767-f5237c9e61eb'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__truck-moving/20260929T090755Z-thuan-mac/reference/truck moving_1bdf40bf-9d96-43bd-a767-f5237c9e61eb.svg'
AUTHOR = "gpt-6"
# Plan: Restore a box truck with a house symbol above the cargo box and attached outlined wheels.
# Keyshape: HRECT_L; preserve reference arrangement.
# Construction reference: truck.

def _draw(icon, name, description):
    tokens=description.split(); pos=0; part=0; count=0; members=[]; start=None; point=None
    def finish(closed=False):
        nonlocal members,part
        if members: icon.add_contour(name if part==0 else f"{name}-part{part}",*members,closed=closed)
        members=[];part+=1
    while pos<len(tokens):
        op=tokens[pos];pos+=1
        if op=='M':
            if members: finish()
            point=tuple(map(int,tokens[pos:pos+2]));pos+=2;start=point
        elif op=='Z':
            if point!=start:
                count+=1;eid=f"{name}-{count}";icon.add_line(eid,point,start);members.append(eid);point=start
            finish(True)
        else:
            count+=1;eid=f"{name}-{count}";members.append(eid)
            if op=='L':
                end=tuple(map(int,tokens[pos:pos+2]));pos+=2;icon.add_line(eid,point,end)
            elif op=='C':
                values=list(map(int,tokens[pos:pos+6]));pos+=6;c1=tuple(values[:2]);c2=tuple(values[2:4]);end=tuple(values[4:]);icon.add_bezier(eid,point,(c1,c2,end))
            elif op=='A':
                rx,ry,sweep,x,y=map(int,tokens[pos:pos+5]);pos+=5;end=(x,y);icon.add_arc(eid,point,end,radius_x=rx,radius_y=ry,sweep=bool(sweep))
            point=end
    if members: finish()

class Revision(Solo48):
    icon_id = 'truck-moving'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'house', 'M 7 17 L 7 11 L 14 6 L 21 11 L 21 17 Z')
        _draw(self, 'door', 'M 14 17 L 14 13')
        _draw(self, 'box', 'M 4 21 L 28 21 L 28 34 L 18 34')
        _draw(self, 'back', 'M 4 21 L 4 34 L 7 34')
        _draw(self, 'cab', 'M 28 25 L 36 25 L 44 31 L 44 35 L 40 35')
        _draw(self, 'window', 'M 34 25 L 34 30 L 42 30')
        _draw(self, 'axle', 'M 17 36 L 30 36')
        _draw(self, 'rear', 'M 8 36 A 4 4 1 16 36 A 4 4 1 8 36 Z')
        _draw(self, 'front', 'M 31 36 A 4 4 1 39 36 A 4 4 1 31 36 Z')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
