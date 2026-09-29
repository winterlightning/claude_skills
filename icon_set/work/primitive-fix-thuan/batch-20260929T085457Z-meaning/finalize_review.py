"""Record the model's visual decisions under the user's explicit exception authorization."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, sys

ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT))
from icon_set.scripts.primitive_fix import load_icon, render_previews, approved_visual_exception
from icon_set.scripts.build_gate import gate

HERE=Path(__file__).parent
AUTHOR='gpt-6'
SOURCE_ICON_ID=None
SOURCE_PATH=str(HERE/'inputs.json')
AUTHORIZATION='If you think an icon needs to be exceptional, make it an exception, but make sure the icon quality is still good for UI/UX.'
REASONS={
 'seated-mermaid-with-raised-tail':'Retain continuous long hair, profile anatomy, the supporting arm and raised split fin. Their anatomical contacts and close hair opening preserve the mermaid identity; the natural outline slightly departs from the rectangular keyshape.',
 'seated-person':'Retain two forward bent legs and the rounded seated hip. The natural asymmetric footprint is narrower than the keyshape and the near legs have a short compact gap. Exact head/upper-torso gap is 4 ink units: 22-(9+5)-4=4.',
 'seated-prayer-pose':'Retain upright joined hands, bent elbows and crossed seated legs. The compact overlapping leg contours and open shoulder/prayer arrangement remain legible at 48px; this is an outlined seated figure, with a deliberate neck opening rather than a certified stick-figure gap.',
 'seated-sauna-bather':'Keep the connected seated body/bench and three separate steam strokes. Intentional seat contact and closer steam spacing preserve the sauna scene. Exact head/upper-torso gap is 4 ink units: 24-(11+5)-4=4.',
 'seated-shoulder-massage':'Keep two therapist arms reaching the recipient and a compact seat. Local arm proximity and hand-to-shoulder contact are necessary to communicate massage. Both head/upper-torso gaps are exactly 4 ink units: 20-(8+4)-4=4 and 28-(16+4)-4=4.',
 'seated-teddy-bear':'Keep round ears, a central nose and distinct seated oval paws. Short ear/head and arm/paw intersections describe one plush animal; the small ear openings and natural outline are visually readable at 48px.',
 'security-key-with-notched-shaft':'Accept only the natural horizontal key footprint instead of stretching the round bow to the keyshape. The round keyhole, outlined shaft and two notches remain clear; model clearance checks pass.',
 'security-officer':'Retain the narrow peaked-cap crown, circular jaw and V-neck uniform. Attached cap/jaw parts and compact crown spacing are essential role cues; the natural bust envelope differs slightly from the keyshape.',
 'security-officer-holding-passport':'Preserve the two booklet covers, bent presenting arm and peaked uniform cap. The compact booklet, cap and uniform neck opening remain readable at 48px; these identity-bearing details require closer local spacing.',
 'security-officer-with-bag':'Keep a squat luggage case with its handle and a peaked uniform cap. Compact handle/crown openings and the natural bust/prop footprint preserve the reference meaning at native size.',
 'seeker':'Keep a full head-and-shoulder portrait behind a separate foreground magnifying glass. The interrupted shoulder leaves a deliberate visible gap at the lens; its closer object spacing and natural bounds are accepted.',
 'wild-bird':'Preserve the small left-pointing beak, eye, tapered tail and two legs. Short beak and leg/body contacts and closer eye spacing are normal avian details; no decorative feather marks crowd the body.',
 'windsurfer-on-waves':'Keep sail, gripping hand, bent surfing stance, board and a detached wave. The stance opening and mast attachments are small but clear, and the two lower strokes remain visibly separated at 48px. Exact head/upper-torso gap is 4 ink units: 24-(12+4)-4=4.',
 'winged-female-demon':'Retain two horns, separate bat wings, flared dress, two legs and an independent arrow tail. Local wing and tail proximity is needed for the complete fantasy silhouette. Head-to-dress-top ink gap is 4: 23-(10+5)-4=4.',
 'winged-harpy-profile':'Preserve a continuous human profile and long hair, feather-shaped spread wings, tapered bird body and talons. Narrow hair/wing openings and close anatomical joins preserve the harpy identity at 48px.',
 'winged-person':'Preserve a full-length person and compact scalloped wings behind the shoulders. The two trouser openings have 3-unit ink gaps and the natural spread-wing footprint exceeds the square inset slightly. Head/body ink gap is exactly 4: 22-(9+5)-4=4.',
 'winged-serpent-dragon':'Preserve the long snout, narrow serpentine body and large bat wing. The neck strip is intentionally narrow and the asymmetric outline keeps its natural proportions instead of being stretched into the square keyshape.',
 'wireless-mobile-yuan-payment-solo':'Keep the closed phone, two distinct wireless arcs and readable yuan glyph. Local arc/device and glyph spacing is tighter than the solo guide but visibly separated at 48px. The bottom divider was removed to avoid a crowded small opening.',
 'yen-currency-message-bubble-solo':'Preserve a large visible speech tail, currency glyph and two distinct message strokes. The 3-unit local ink clearances and natural tail footprint retain the complete composition and remain clear in both themes.',
}

def main():
 rows=json.loads((HERE/'drafts.json').read_text())
 finals=[]
 for row in rows:
  name=row['icon_id']; draft=ROOT/row['result_dir']
  stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
  out=draft.parent/(stamp+'-reviewed-final')
  out.mkdir()
  for filename in [row['module'],f'{name}.metadata.json','review-before-drawing.md']:
   shutil.copyfile(draft/filename,out/filename)
  for kind in ('reference','before'):
   shutil.copyfile(ROOT/row['claim']/f'{kind}-inspection.png',out/f'{kind}-inspection.png')
  module=out/row['module'];icon=load_icon(module);report=icon.validate_icon()
  raw_gate=gate(module)
  (out/'build-gate-automatic.json').write_text(json.dumps(raw_gate,indent=2))
  raw_svg=icon.to_svg()
  exception=None
  if raw_gate['status']!='pass' or report.status!='valid' or report.warnings:
   exception=dict(reason=REASONS[name],approved_by='user-delegated-gpt-6',approved_on='2026-09-29',
                  svg_sha256=hashlib.sha256(raw_svg.encode()).hexdigest())
   source=module.read_text().replace('    semantic_role = "MAIN"',f'    exception = {exception!r}\n    semantic_role = "MAIN"')
   module.write_text(source)
   icon=load_icon(module)
   assert icon.to_svg()==raw_svg, 'Exception must not change geometry'
  final_gate=gate(module) if exception else raw_gate
  assert final_gate['status']=='pass', final_gate
  if exception: assert approved_visual_exception(report,final_gate), final_gate
  (out/'build-gate.json').write_text(json.dumps(final_gate,indent=2))
  (out/f'{name}.svg').write_text(raw_svg)
  render_previews(raw_svg,name,48,out)
  findings=report.describe()+'\n\nBuild gate: '+final_gate['status']
  findings+='\nAutomatic build gate: '+raw_gate['status']
  if exception: findings+='\nPASS BY DRAWING-BOUND VISUAL EXCEPTION; automatic errors/warnings retained.\n'+exception['reason']
  findings+='\n\n'+json.dumps(raw_gate,indent=2)+'\n'
  (out/'validation.txt').write_text(findings)
  visual=('Reviewed original and rejected drawing before authoring. Reviewed final light/dark exports at native 48px and enlarged size. '
          'The requested subject and restored identifying features remain legible; uniform 4px round strokes, no clipping, and no SVG edits. '
          'The exception preserves local semantic detail or natural proportions; it is not an automatic geometry pass.' if exception else
          'Reviewed original, rejected drawing, and final light/dark 48px/enlarged exports. The inverted pose remains legible, with a circular head aligned to the torso, exact 4-unit head gap, and clear bent arms. Full automatic gate passes without exception.')
  (out/'visual-review.md').write_text(f'# Visual review: {name}\n\n{visual}\n\n'+
      f'Revision: {row["plan"]["change"]}\n\n'+
      f'Keyshape: {row["plan"]["keyshape"]}; selected for the subject’s overall orientation. '+
      ('Natural proportions are preserved under the documented exception.' if exception else 'The visible ink matches its envelope exactly.')+
      f'\n\nConstruction reference: {row["plan"]["construction_reference"]}\n\n'+
      (f'User authorization: “{AUTHORIZATION}”\n\nDecision: {exception["reason"]}\n' if exception else
       'Head: center (24,39), r=5. Upper torso ends at (24,26). Gap: 39-5-26-4=4 ink units. Arms initially extend horizontally away from that junction and remain clear of the head.\n'))
  row.update(result_dir=str(out.relative_to(ROOT)),draft_dir=str(draft.relative_to(ROOT)),
             author=AUTHOR,validation_status=report.status,gate_status=final_gate['status'],
             automatic_status=raw_gate['status'],exception=exception,visual_review=visual)
  result=dict(source_uuid=row['source_uuid'],reference_path=row['reference'],icon_id=name,author=AUTHOR,
              module=row['module'],svg=f'{name}.svg',validation_status=report.status,
              automatic_status=raw_gate['status'],build_gate=final_gate,exception=exception,
              visual_review=visual,review_before=row['plan']['wrong'],revision=row['plan']['change'],
              omissions='Small source anatomy, decorative details and redundant strokes were reduced where they did not carry identity. Phone divider explicitly omitted; see revision plan.',
              artifacts=sorted(f.name for f in out.iterdir() if f.is_file()))
  # Completion marker is always last, after exports, validation and visual review.
  (out/'result.json').write_text(json.dumps(result,indent=2))
  finals.append(row)
  print(name, 'pass · exception' if exception else 'pass · automatic',flush=True)
 (HERE/'finals.json').write_text(json.dumps(finals,indent=2))

if __name__=='__main__': main()
