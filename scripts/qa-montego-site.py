#!/usr/bin/env python3
"""QA checks for Montego Bay Shore Excursion Phase 14B static build."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "scripts" / "protected_routes.json"

QUARANTINE_NAMES = (
    "green-grotto-caves.jpg",
    "hero-excursions.jpg",
    "one-day.jpg",
    "river-tubing.jpg",
)

BANNED_SUBSTRINGS = (
    "cdn.tailwindcss.com",
    "shoreexcursionsgroup",
    "info@wowatour.com",
)

CAMB_RE = re.compile(r"\bCAMB[-_]?\d+\b", re.I)
SEG_CODE_RE = re.compile(r"\bSEG[-_]?\d{3,}\b", re.I)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)


def fail(msg: str, errors: list[str]) -> None:
    errors.append(msg)
    print(f"FAIL: {msg}")


def main() -> int:
    errors: list[str] = []
    print("QA Montego Bay Phase 14B…")

    if not MANIFEST.exists():
        fail(f"missing {MANIFEST.relative_to(ROOT)}", errors)
        print(f"{len(errors)} error(s)")
        return 1

    data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    routes = data.get("routes") or []
    if not routes:
        fail("protected_routes.json has no routes", errors)

    html_files: list[Path] = []
    for route in routes:
        rel = route.get("file")
        if not rel:
            fail(f"route missing file: {route}", errors)
            continue
        path = ROOT / rel
        if not path.exists():
            fail(f"protected route file missing: {rel}", errors)
        else:
            html_files.append(path)
            print(f"  ok file {rel}")

    titles: dict[str, str] = {}
    contact_ok = False

    # Only scan assembled protected-route HTML (not legacy content/partials fragments).
    for path in html_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        rel = str(path.relative_to(ROOT))

        for name in QUARANTINE_NAMES:
            if name in text:
                fail(f"quarantine image ref in {rel}: {name}", errors)

        if "/images/quarantine/" in text or "images/quarantine/" in text:
            fail(f"quarantine path ref in {rel}", errors)

        for banned in BANNED_SUBSTRINGS:
            if banned.lower() in text.lower():
                fail(f"banned string in {rel}: {banned}", errors)

        if CAMB_RE.search(text):
            fail(f"CAMB product code pattern in {rel}", errors)
        if SEG_CODE_RE.search(text):
            fail(f"SEG product code pattern in {rel}", errors)

        if "Return to Ship on Time" in text or "Return To Ship On Time" in text:
            fail(f"unsupported return-to-ship guarantee wording in {rel}", errors)

        m = TITLE_RE.search(text)
        if m:
            title = re.sub(r"\s+", " ", m.group(1)).strip()
            if title in titles:
                fail(f"duplicate title in {rel} and {titles[title]}: {title}", errors)
            else:
                titles[title] = rel

        if rel == "contact/index.html":
            if "hello@montegobayshoreexcursion.com" in text:
                contact_ok = True
            else:
                fail("contact page missing hello@montegobayshoreexcursion.com", errors)

    if (ROOT / "contact" / "index.html").exists() and not contact_ok:
        fail("contact page missing hello@montegobayshoreexcursion.com", errors)

    home = ROOT / "index.html"
    if home.exists():
        h = home.read_text(encoding="utf-8")
        for required in (
            "Cruise-aware timing",
            "Plan your return window",
            "Beach &amp; adventure options",
        ):
            if required not in h:
                fail(f"home missing trust-strip phrase: {required}", errors)

    if not errors:
        print(
            f"QA passed ({len(html_files)} protected files checked, "
            f"{len(titles)} unique titles)."
        )
        return 0

    print(f"{len(errors)} error(s)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
