from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = 'c14f0462-1a4f-4fce-8591-b63fddf2fa6d'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__truck-medical/20260929T090755Z-thuan-mac/reference/truck medical_c14f0462-1a4f-4fce-8591-b63fddf2fa6d.svg'
AUTHOR = "gpt-6"
# Plan: Restore a tall medical box, windshield and two round wheels.
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
    icon_id = 'truck-medical'
    keyshape = Keyshape.HRECT_L
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'box', 'M 4 32 L 4 8 L 27 8 L 27 32')
        _draw(self, 'cross-h', 'M 11 19 L 20 19')
        _draw(self, 'cross-v', 'M 15 15 L 15 24')
        _draw(self, 'cab', 'M 27 16 L 36 16 L 44 26 L 44 33 L 40 33')
        _draw(self, 'window', 'M 33 17 L 33 25 L 43 25')
        _draw(self, 'axle', 'M 17 35 L 30 35')
        _draw(self, 'rear', 'M 7 35 A 5 5 1 17 35 A 5 5 1 7 35 Z')
        _draw(self, 'front', 'M 30 35 A 5 5 1 40 35 A 5 5 1 30 35 Z')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
