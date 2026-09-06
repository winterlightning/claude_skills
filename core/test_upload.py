#!/usr/bin/env python3
"""Offline regression coverage for the production SVG uploader's HTTP contract."""
from __future__ import annotations

from contextlib import redirect_stdout
import importlib.util
import io
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import MagicMock, patch
from urllib.parse import parse_qs, urlsplit


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location("production_svg_upload", ROOT / "upload.py")
uploader = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(uploader)


class UploadHttpContractTests(unittest.TestCase):
    def setUp(self):
        temporary = TemporaryDirectory(prefix="offline-upload-test-")
        self.addCleanup(temporary.cleanup)
        self.batch = Path(temporary.name)
        (self.batch / "output").mkdir()
        self.svg_bytes = (
            '<svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" '
            'viewBox="0 0 48 48"><title>Café &amp; tea</title>'
            '<path d="M8 24H40" fill="none" stroke="currentColor" stroke-width="4"/></svg>\n'
        ).encode("utf-8")
        (self.batch / "output/sym-000123-test.svg").write_bytes(self.svg_bytes)
        self.route = "/test-symbol-upload/sym_000123"
        self.label = "reviewed variant"
        manifest = {
            "api": {"base": "https://symlib.example.invalid/", "label": self.label},
            "symbols": [{"sid": "sym_000123", "upload": "output/sym-000123-test.svg",
                         "upload_url": self.route}],
        }
        (self.batch / "manifest.json").write_text(json.dumps(manifest), encoding="utf-8")

    def invoke(self, *arguments):
        response = MagicMock()
        response.__enter__.return_value = response
        response.read.return_value = b'{"added":[{"file":"sym_000123_reviewed.svg"}]}'
        with (patch.object(uploader, "HERE", self.batch),
              patch.object(sys, "argv", ["upload.py", *arguments]),
              patch.object(uploader.urllib.request, "urlopen", return_value=response) as request,
              redirect_stdout(io.StringIO()) as output):
            status = uploader.main()
        return status, request, output.getvalue()

    def assert_svg_post(self, request, *, force):
        request.assert_called_once()
        outgoing = request.call_args.args[0]
        headers = {name.lower(): value for name, value in outgoing.header_items()}
        self.assertEqual(outgoing.get_method(), "POST")
        self.assertEqual(headers["user-agent"], "symlib-rework-upload/1.0")
        self.assertEqual(headers["content-type"], "image/svg+xml; charset=utf-8")
        self.assertEqual(outgoing.data, self.svg_bytes)
        address = urlsplit(outgoing.full_url)
        self.assertEqual((address.scheme, address.netloc, address.path),
                         ("https", "symlib.example.invalid", self.route))
        expected = {"name": [self.label]}
        if force:
            expected["force"] = ["1"]
        self.assertEqual(parse_qs(address.query), expected)

    def test_normal_post_uses_production_user_agent_and_raw_svg_body(self):
        status, request, _ = self.invoke()
        self.assertEqual(status, 0)
        self.assert_svg_post(request, force=False)

    def test_force_post_keeps_http_contract_and_adds_force_query(self):
        status, request, _ = self.invoke("--force")
        self.assertEqual(status, 0)
        self.assert_svg_post(request, force=True)

    def test_dry_run_never_opens_a_request_even_with_force(self):
        for arguments in (("--dry-run",), ("--dry-run", "--force")):
            with self.subTest(arguments=arguments):
                status, request, output = self.invoke(*arguments)
                self.assertEqual(status, 0)
                request.assert_not_called()
                self.assertIn("would send 1, skipped 0, failed 0", output)
                self.assertEqual((self.batch / "output/sym-000123-test.svg").read_bytes(), self.svg_bytes)


if __name__ == "__main__":
    unittest.main()
