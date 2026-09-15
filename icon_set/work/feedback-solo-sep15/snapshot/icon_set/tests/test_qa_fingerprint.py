"""Overlay caches must expire when the circle rules change, even for the same SVG."""
import hashlib
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import patch
from icon_set.scripts.qa_fingerprint import checker_fingerprint

class OverlayRuleCacheTests(unittest.TestCase):
    def test_rule_change_expires_an_otherwise_current_overlay(self):
        import qa_overlays
        with TemporaryDirectory() as folder:
            svg = Path(folder)/'circle.svg'
            svg.write_text('<svg/>')
            metrics = {'svg_sha256':hashlib.sha256(svg.read_bytes()).hexdigest(),
                       'checker_fingerprint':checker_fingerprint(), 'distance_gate':8}
            svg.with_suffix('.metrics.json').write_text(json.dumps(metrics))
            self.assertIsNotNone(qa_overlays.existing_metrics(str(svg),gate=8))
            read = Path.read_bytes
            with patch.object(Path,'read_bytes',lambda path:read(path)+(b' ' if path.name=='negative-space.v1.json' else b'')):
                self.assertIsNone(qa_overlays.existing_metrics(str(svg),gate=8))
            del metrics['checker_fingerprint']
            svg.with_suffix('.metrics.json').write_text(json.dumps(metrics))
            self.assertIsNone(qa_overlays.existing_metrics(str(svg),gate=8))
