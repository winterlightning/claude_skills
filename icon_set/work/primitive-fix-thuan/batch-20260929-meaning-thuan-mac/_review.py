"""Export and verify standalone primitive-make-ray runs, keeping all automatic findings."""
from pathlib import Path
import sys,json
ROOT=Path(__file__).resolve().parents[4];sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon,run_module,render_previews
from icon_set.scripts.build_gate import gate
from PIL import Image,ImageDraw
import cairosvg
AUTHOR='gpt-6'
SOURCE_ICON_ID = {'acro-yoga-folded-balance': '672c58c9-cf49-5d74-ba11-e6398667c047', 'adult-child-high-five-hands': 'b88757c2-b1ab-49df-9283-b755a2874066', 'airplane-rising-above-ground-line': '28bc625b-2596-540d-91c3-fb5e36336a56', 'baby-bottle-with-handles': '46fff59c-84bf-4526-bd9b-33201133c81c', 'box-delivery-truck': '0070eae2-79f7-4131-b3be-164ea822745d', 'briefcase-carrying-hailing-person': '459ca9bc-41c3-44a7-bd18-4322e40df660', 'broccoli-and-carrot': '1833535f-220e-490a-9e51-7058a14ac9db', 'browser-user-profile': '3a3e4d85-115c-4ccb-82d1-46fd45222b3a', 'canoe': '2f08daf6-071b-5ac7-9717-2239ffbb2925', 'hand-holding-wrench': '80b7765d-72c2-4b01-b0bf-6a084aa9bc97', 'hand-massaging-foot-8ab52d55': '8ab52d55-ae52-4c12-82e0-c8e7e2dc8409', 'hand-massaging-scalp-17e8bc26': '17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec', 'hand-over-heat': 'e2391138-4aaf-4587-83d5-f636e7ba5379', 'hand-playing-pad-controller': '2e9ddede-2e59-4491-8fa8-b1f79514c010', 'hand-playing-yoyo': '28a605e6-a545-47ed-ae21-f45557bb8374', 'hand-pointing-down-batch-024-04': '5a80cb54-e04f-5e41-ba53-6892a6852f05', 'hand-stealing-identity-card-solo-b005-06': '3ba267b5-9ca9-4999-a24d-b73d45e0c937', 'handcuffs-with-arched-connector': '404190ff-389e-4a15-a7fe-4b448b432ffd', 'handcuffs-with-curved-link': 'ad5f17ec-d6f2-402a-8907-dbd8532598e6', 'handled-comb-on-diagonal': 'dafdca17-4d27-4cd9-935d-01a08f4e53e2'}
SOURCE_PATH = {'acro-yoga-folded-balance': 'icon_set/work/primitive-fix-thuan/solo__acro-yoga-folded-balance/20260929T025914Z-thuan-mac/reference/acro yoga pose_672c58c9-cf49-5d74-ba11-e6398667c047.svg', 'adult-child-high-five-hands': 'icon_set/work/primitive-fix-thuan/solo__adult-child-high-five-hands/20260929T025914Z-thuan-mac/reference/play together_b88757c2-b1ab-49df-9283-b755a2874066.svg', 'airplane-rising-above-ground-line': 'icon_set/work/primitive-fix-thuan/solo__airplane-rising-above-ground-line/20260929T025914Z-thuan-mac/reference/plane land_28bc625b-2596-540d-91c3-fb5e36336a56.svg', 'baby-bottle-with-handles': 'icon_set/work/primitive-fix-thuan/solo__baby-bottle-with-handles/20260929T025914Z-thuan-mac/reference/milk bottle handle_46fff59c-84bf-4526-bd9b-33201133c81c.svg', 'box-delivery-truck': 'icon_set/work/primitive-fix-thuan/solo__box-delivery-truck/20260929T025914Z-thuan-mac/reference/carrier_0070eae2-79f7-4131-b3be-164ea822745d.svg', 'briefcase-carrying-hailing-person': 'icon_set/work/primitive-fix-thuan/solo__briefcase-carrying-hailing-person/20260929T025914Z-thuan-mac/reference/taxi wave businessman_459ca9bc-41c3-44a7-bd18-4322e40df660.svg', 'broccoli-and-carrot': 'icon_set/work/primitive-fix-thuan/solo__broccoli-and-carrot/20260929T025914Z-thuan-mac/reference/broccoli carrot_1833535f-220e-490a-9e51-7058a14ac9db.svg', 'browser-user-profile': 'icon_set/work/primitive-fix-thuan/solo__browser-user-profile/20260929T025914Z-thuan-mac/reference/browser person_3a3e4d85-115c-4ccb-82d1-46fd45222b3a.svg', 'canoe': 'icon_set/work/primitive-fix-thuan/solo__canoe/20260929T025914Z-thuan-mac/reference/canoe_2f08daf6-071b-5ac7-9717-2239ffbb2925.svg', 'hand-holding-wrench': 'icon_set/work/primitive-fix-thuan/solo__hand-holding-wrench/20260929T025914Z-thuan-mac/reference/tools wrench hold_80b7765d-72c2-4b01-b0bf-6a084aa9bc97.svg', 'hand-massaging-foot-8ab52d55': 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-foot-8ab52d55/20260929T025914Z-thuan-mac/reference/massage foot_8ab52d55-ae52-4c12-82e0-c8e7e2dc8409.svg', 'hand-massaging-scalp-17e8bc26': 'icon_set/work/primitive-fix-thuan/solo__hand-massaging-scalp-17e8bc26/20260929T025914Z-thuan-mac/reference/massage head_17e8bc26-5dd7-4e47-b8f2-9a09c357e6ec.svg', 'hand-over-heat': 'icon_set/work/primitive-fix-thuan/solo__hand-over-heat/20260929T025914Z-thuan-mac/reference/hand with flame_e2391138-4aaf-4587-83d5-f636e7ba5379.svg', 'hand-playing-pad-controller': 'icon_set/work/primitive-fix-thuan/solo__hand-playing-pad-controller/20260929T025914Z-thuan-mac/reference/modern music mix touch_2e9ddede-2e59-4491-8fa8-b1f79514c010.svg', 'hand-playing-yoyo': 'icon_set/work/primitive-fix-thuan/solo__hand-playing-yoyo/20260929T025914Z-thuan-mac/reference/playing yoyo_28a605e6-a545-47ed-ae21-f45557bb8374.svg', 'hand-pointing-down-batch-024-04': 'icon_set/work/primitive-fix-thuan/solo__hand-pointing-down-batch-024-04/20260929T025914Z-thuan-mac/reference/hand pointer bottom_5a80cb54-e04f-5e41-ba53-6892a6852f05.svg', 'hand-stealing-identity-card-solo-b005-06': 'icon_set/work/primitive-fix-thuan/solo__hand-stealing-identity-card-solo-b005-06/20260929T025914Z-thuan-mac/reference/identity stolen id card_3ba267b5-9ca9-4999-a24d-b73d45e0c937.svg', 'handcuffs-with-arched-connector': 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-arched-connector/20260929T025914Z-thuan-mac/reference/handcuffs_404190ff-389e-4a15-a7fe-4b448b432ffd.svg', 'handcuffs-with-curved-link': 'icon_set/work/primitive-fix-thuan/solo__handcuffs-with-curved-link/20260929T025914Z-thuan-mac/reference/tools shackle_ad5f17ec-d6f2-402a-8907-dbd8532598e6.svg', 'handled-comb-on-diagonal': 'icon_set/work/primitive-fix-thuan/solo__handled-comb-on-diagonal/20260929T025914Z-thuan-mac/reference/hair dress comb_dafdca17-4d27-4cd9-935d-01a08f4e53e2.svg'}
BATCH=Path(__file__).parent

def export():
    records=[]
    for p in map(Path,json.loads((BATCH/'runs.json').read_text())):
        m=run_module(p);icon=load_icon(m);svg=icon.to_svg()
        (p/(icon.icon_id+'.svg')).write_text(svg)
        render_previews(svg,icon.icon_id,48,p)
        report=icon.validate_icon();g=gate(m)
        (p/'validation.txt').write_text(report.describe()+'\n\nBuild gate:\n'+json.dumps(g,indent=2)+'\n')
        (p/'gate.json').write_text(json.dumps(g,indent=2)+'\n')
        meta=json.loads((p/(icon.icon_id+'.metadata.json')).read_text())
        for name,source in [('reference',ROOT/meta['reference_path']),('before',ROOT/meta['fix_run']/'before'/(icon.icon_id+'.svg'))]:
            for size in (48,192):cairosvg.svg2png(url=str(source),write_to=str(p/f'{name}-{size}.png'),output_width=size,output_height=size,background_color='white')
        records.append(dict(meta,run=str(p.relative_to(ROOT)),module=m.name,svg=icon.icon_id+'.svg',validation_status=report.status,build_gate=g))
        print(icon.icon_id,g['status'],len(g['errors']),len(g['warnings']),flush=True)
    (BATCH/'review-records.json').write_text(json.dumps(records,indent=2)+'\n')
    for n in range(4):
        sheet=Image.new('RGB',(1000,1200),'#ededeb');d=ImageDraw.Draw(sheet)
        for i,r in enumerate(records[n*5:n*5+5]):
            p=ROOT/r['run'];d.text((5,i*240+4),r['icon_id'],fill='black')
            for j,name in enumerate(['reference-192.png','before-192.png','preview-light-384.png','preview-dark-384.png']):
                sheet.paste(Image.open(p/name).convert('RGB').resize((192,192)),(j*218,i*240+28))
            for j,t in enumerate(['light','dark']):sheet.paste(Image.open(p/f'preview-{t}-48.png').convert('RGB'),(910,i*240+40+j*80))
        sheet.save(BATCH/f'comparison-{n+1}.png')

if __name__=='__main__':export()
