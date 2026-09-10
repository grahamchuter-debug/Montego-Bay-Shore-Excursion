"""Montego Bay Shore Excursion — World 2.0 Phase 14B site configuration."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOMAIN = "montegobayshoreexcursion.com"
APEX = f"https://{DOMAIN}"
SITE = "Montego Bay Shore Excursion"
EMAIL = "hello@montegobayshoreexcursion.com"
DATE = "2026-09-10"
ACCENT = "text-pr-400"

FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)

HERO_GRADIENT = (
    "linear-gradient(140deg, rgba(15, 23, 42, 0.78) 0%, "
    "rgba(30, 64, 175, 0.62) 42%, rgba(249, 115, 22, 0.38) 72%, "
    "rgba(0, 0, 0, 0.22) 100%)"
)

# Seven real images under /images/ (quarantined 1×1 placeholders must not be referenced)
HERO_HOME = "/images/hero-home.jpg"
HERO_HOME_ALT = (
    "Montego Bay Jamaica coastline with turquoise Caribbean water and "
    "tropical shoreline for cruise passengers planning shore excursions"
)

CRUISE_PORT = "/images/cruise-port.jpg"
CRUISE_PORT_ALT = (
    "Montego Bay cruise port area with ships and pier infrastructure "
    "for cruise passenger arrivals at Montego Freeport"
)

DOCTORS_CAVE = "/images/doctors-cave-beach.jpg"
DOCTORS_CAVE_ALT = (
    "Doctor's Cave Beach in Montego Bay Jamaica with clear turquoise water "
    "and palm-lined shoreline near the cruise port"
)

DUNNS_RIVER = "/images/dunns-river-falls.jpg"
DUNNS_RIVER_ALT = (
    "Terraced limestone steps of Dunn's River Falls in Jamaica — a longer "
    "transfer option for cruise passengers sailing from Montego Bay"
)

ROSE_HALL = "/images/rose-hall.jpg"
ROSE_HALL_ALT = (
    "Rose Hall Great House near Montego Bay Jamaica with hilltop views "
    "visited on culture-focused cruise shore excursions"
)

PRIVATE_DRIVER = "/images/private-driver.jpg"
PRIVATE_DRIVER_ALT = (
    "Private driver vehicle on a scenic Montego Bay Jamaica route for "
    "cruise passengers building a flexible port-day itinerary"
)

COASTLINE = "/images/montego-bay-coastline.jpg"
COASTLINE_ALT = (
    "Montego Bay Jamaica coastline with Caribbean water and green hills "
    "used for general cruise port-day planning imagery"
)

# Honest stand-ins where dedicated photos are quarantined
EXCURSIONS_HERO = COASTLINE
EXCURSIONS_HERO_ALT = (
    "Montego Bay Jamaica coastline representing beach, culture and "
    "adventure shore excursion choices from the cruise port"
)
ONE_DAY_HERO = HERO_HOME
ONE_DAY_HERO_ALT = (
    "Montego Bay Jamaica shoreline for planning one day ashore "
    "from a cruise ship without inventing a single perfect itinerary"
)
GREEN_GROTTO_HERO = COASTLINE
GREEN_GROTTO_HERO_ALT = (
    "Montego Bay Jamaica north-coast scenery for Green Grotto Caves "
    "travel planning — not a photograph of the cave interior"
)

PROTECTED_ROUTES = [
    {"path": "/", "file": "index.html", "kind": "home"},
    {"path": "/excursions/", "file": "excursions/index.html", "kind": "hub"},
    {
        "path": "/montego-bay-cruise-port-guide/",
        "file": "montego-bay-cruise-port-guide/index.html",
        "kind": "guide",
    },
    {
        "path": "/one-day-in-montego-bay-from-cruise-ship/",
        "file": "one-day-in-montego-bay-from-cruise-ship/index.html",
        "kind": "guide",
    },
    {
        "path": "/doctors-cave-beach-montego-bay/",
        "file": "doctors-cave-beach-montego-bay/index.html",
        "kind": "attraction",
    },
    {
        "path": "/dunns-river-falls-from-montego-bay/",
        "file": "dunns-river-falls-from-montego-bay/index.html",
        "kind": "attraction",
    },
    {
        "path": "/rose-hall-great-house-montego-bay/",
        "file": "rose-hall-great-house-montego-bay/index.html",
        "kind": "attraction",
    },
    {
        "path": "/green-grotto-caves-montego-bay/",
        "file": "green-grotto-caves-montego-bay/index.html",
        "kind": "attraction",
    },
    {
        "path": "/private-driver-montego-bay/",
        "file": "private-driver-montego-bay/index.html",
        "kind": "decision",
    },
    {"path": "/contact/", "file": "contact/index.html", "kind": "trust"},
    {"path": "/about/", "file": "about/index.html", "kind": "trust"},
    {"path": "/privacy/", "file": "privacy/index.html", "kind": "trust"},
    {"path": "/terms/", "file": "terms/index.html", "kind": "trust"},
    {"path": "/methodology/", "file": "methodology/index.html", "kind": "trust"},
    {"path": "/404.html", "file": "404.html", "kind": "error", "sitemap": False},
]
