#!/usr/bin/env python3
"""Build Montego Bay Shore Excursion World 2.0 static HTML (Phase 14B)."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from montego_config import APEX, PROTECTED_ROUTES, ROOT as SITE_ROOT  # noqa: E402
from montego_pages import (  # noqa: E402
    about,
    contact,
    doctors_cave,
    dunns_river,
    excursions,
    green_grotto,
    home,
    methodology,
    not_found,
    one_day,
    port_guide,
    privacy,
    private_driver,
    rose_hall,
    terms,
)
from montego_shell import page_shell  # noqa: E402


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    print(f"  wrote {path.relative_to(SITE_ROOT)}")


def render(builder, *, robots: str | None = None, include_trust: bool = True) -> str:
    hero, main, faqs, meta = builder()
    return page_shell(
        meta["title"],
        meta["description"],
        meta["canonical_path"],
        meta["page_id"],
        hero,
        main,
        meta["og_image"],
        faq_entities=faqs,
        robots=robots,
        include_trust=include_trust,
    )


PAGES: list[tuple[str, object, dict]] = [
    ("index.html", home, {}),
    ("excursions/index.html", excursions, {}),
    ("montego-bay-cruise-port-guide/index.html", port_guide, {}),
    ("one-day-in-montego-bay-from-cruise-ship/index.html", one_day, {}),
    ("doctors-cave-beach-montego-bay/index.html", doctors_cave, {}),
    ("dunns-river-falls-from-montego-bay/index.html", dunns_river, {}),
    ("rose-hall-great-house-montego-bay/index.html", rose_hall, {}),
    ("green-grotto-caves-montego-bay/index.html", green_grotto, {}),
    ("private-driver-montego-bay/index.html", private_driver, {}),
    ("contact/index.html", contact, {}),
    ("about/index.html", about, {}),
    ("privacy/index.html", privacy, {}),
    ("terms/index.html", terms, {}),
    ("methodology/index.html", methodology, {}),
]


def build_pages() -> None:
    for rel, builder, opts in PAGES:
        write(SITE_ROOT / rel, render(builder, **opts))
    write(
        SITE_ROOT / "404.html",
        render(not_found, robots="noindex, follow", include_trust=False),
    )


def build_sitemap() -> None:
    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for route in PROTECTED_ROUTES:
        if route.get("sitemap") is False:
            continue
        path = route["path"]
        loc = f"{APEX}/" if path == "/" else f"{APEX}{path}"
        kind = route.get("kind", "")
        if path == "/":
            pri, freq = "1.0", "weekly"
        elif kind in {"hub", "guide", "attraction", "decision"}:
            pri, freq = "0.9", "monthly"
        else:
            pri, freq = "0.5", "yearly"
        lines.extend(
            [
                "  <url>",
                f"    <loc>{loc}</loc>",
                f"    <changefreq>{freq}</changefreq>",
                f"    <priority>{pri}</priority>",
                "  </url>",
            ]
        )
    lines.append("</urlset>")
    lines.append("")
    write(SITE_ROOT / "sitemap.xml", "\n".join(lines))


def build_robots() -> None:
    write(
        SITE_ROOT / "robots.txt",
        f"""User-agent: *
Allow: /

Sitemap: {APEX}/sitemap.xml
""",
    )


def build_protected_manifest() -> None:
    manifest = {
        "domain": APEX,
        "phase": "14B",
        "routes": PROTECTED_ROUTES,
    }
    write(
        SITE_ROOT / "scripts" / "protected_routes.json",
        json.dumps(manifest, indent=2) + "\n",
    )


def main() -> None:
    print("Building Montego Bay Shore Excursion World 2.0 (Phase 14B)…")
    build_pages()
    build_sitemap()
    build_robots()
    build_protected_manifest()
    print("Build complete.")


if __name__ == "__main__":
    main()
