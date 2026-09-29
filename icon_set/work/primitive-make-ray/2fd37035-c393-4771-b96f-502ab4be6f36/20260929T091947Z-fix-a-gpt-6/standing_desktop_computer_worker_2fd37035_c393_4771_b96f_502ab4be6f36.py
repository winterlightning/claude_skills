from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
SOURCE_ICON_ID = '2fd37035-c393-4771-b96f-502ab4be6f36'
SOURCE_PATH = 'icon_set/work/primitive-fix-thuan/solo__standing-desktop-computer-worker/20260929T091947Z-thuan-mac/reference/desk computer base work standing user_2fd37035-c393-4771-b96f-502ab4be6f36.svg'
AUTHOR = "gpt-6"
# Plan: Restore a standing operator reaching a desk with an edge-view monitor and open table legs.
# Keyshape: SQUARE; preserve reference arrangement.
# Construction reference: human_ref/full_body_ref.png + monitor.

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
    icon_id = 'standing-desktop-computer-worker'
    keyshape = Keyshape.SQUARE
    exception = {'reason': 'Preserve the standing person reaching the desk and edge-view monitor; compact working-surface contacts and natural composition bounds accepted.', 'approved_by': 'user-authorized visual judgment by gpt-6', 'approved_on': '2026-09-29', 'svg_sha256': '6beb27ccb8faec7eb3d66b4f1911f02723312add18b13bb730d3bf8fc9320ff5'}
    semantic_role = "MAIN"
    semantic_kind = "noun"
    category = "objects/general"
    aliases = ()
    keywords = ()

    def build(self):
        _draw(self, 'head', 'M 32 10 A 4 4 1 40 10 A 4 4 1 32 10 Z')
        _draw(self, 'torso', 'M 36 22 L 36 33')
        _draw(self, 'arm', 'M 36 22 L 30 28 L 23 28')
        _draw(self, 'legs', 'M 31 42 L 36 33 L 41 42')
        _draw(self, 'desk', 'M 6 31 L 25 31')
        _draw(self, 'desk-left', 'M 6 31 L 6 42')
        _draw(self, 'desk-right', 'M 25 31 L 25 42')
        _draw(self, 'screen', 'M 9 6 L 14 23')
        _draw(self, 'monitor-base', 'M 12 16 C 7 16 10 26 6 27 L 17 27')
        owners = {member: contour.contour_id for contour in self.contours for member in contour.members}
        for a_index,a in enumerate(self.primitives):
            for b in self.primitives[a_index+1:]:
                if owners.get(a.element_id)!=owners.get(b.element_id) and ({a.start,a.end}&{b.start,b.end}):
                    self.relate("connect",a.element_id,b.element_id)
        self.mark_human_figure('person', head='head', torso='torso-1', torso_junction='start')
