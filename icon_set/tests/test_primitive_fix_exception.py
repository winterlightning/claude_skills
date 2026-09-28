"""The fix upload honors verified visual approvals without accepting structural failures."""
import hashlib
from pathlib import Path
import tempfile
import unittest

from icon_set.scripts import build_gate, primitive_fix


class PrimitiveFixExceptionTests(unittest.TestCase):
    def test_drawing_bound_approval_retains_findings_and_rejects_stale_hash(self):
        source = '''from icon_set.model.icons.solo._base import Solo48
from icon_set.model.keyshapes import Keyshape
class Candidate(Solo48):
    icon_id = 'exception-test'
    keyshape = Keyshape.SQUARE
    semantic_role = 'MAIN'
    semantic_kind = 'noun'
    category = 'objects'
    def build(self):
        self.add_polyline('box',(6,6),(42,6),(42,42),(6,42),closed=True)
        self.add_line('detail',(12,16),(12,32))
'''
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'candidate.py'
            path.write_text(source)
            icon = primitive_fix.load_icon(path)
            report = icon.validate_icon()
            self.assertEqual(report.status, 'invalid')
            self.assertFalse(primitive_fix.approved_visual_exception(report, build_gate.gate(path)))
            sha = hashlib.sha256(icon.to_svg().encode()).hexdigest()
            approval = {'reason': 'User accepts this exact visible spacing', 'approved_by': 'user', 'svg_sha256': sha}
            path.write_text(source + f'\nCandidate.exception = {approval!r}\n')
            gate = build_gate.gate(path)
            self.assertTrue(primitive_fix.approved_visual_exception(report, gate))
            self.assertEqual(gate['automatic_status'], 'fail')
            self.assertTrue(gate['errors'])
            path.write_text(source + f'\nCandidate.exception = {dict(approval, svg_sha256="stale")!r}\n')
            self.assertFalse(primitive_fix.approved_visual_exception(report, build_gate.gate(path)))

    def test_structural_failure_cannot_be_approved(self):
        from types import SimpleNamespace
        gate = {'status': 'pass', 'automatic_status': 'fail', 'exception': {'reason': 'visual'}}
        for error in ('schema/profile: invalid role', 'style/grid: stroke must be 4',
                      'svg round-trip: mismatch', 'reproducibility: changed'):
            report = SimpleNamespace(status='invalid', errors=[error], warnings=[])
            self.assertFalse(primitive_fix.approved_visual_exception(report, gate))


if __name__ == '__main__':
    unittest.main()
