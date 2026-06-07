#!/usr/bin/env python3
"""Generate index.html page shells for montegobayshoreexcursion.com."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOMAIN = "https://montegobayshoreexcursion.com"
KEYWORDS = "Montego Bay shore excursions, Montego Bay cruise port, Jamaica cruise excursions, Montego Bay cruise tours, things to do in Montego Bay from a cruise ship"

HOME_FAQS = [
    ("Is Montego Bay good for cruise passengers?", "Yes. Montego Bay works well for cruise passengers who want either a low-effort beach day or a fuller Jamaica experience. Doctor's Cave Beach and Rose Hall are close; Dunn's River Falls and Green Grotto Caves are reachable on well-timed Montego Bay cruise tours."),
    ("Where do cruise ships dock in Montego Bay?", "Most ships berth at the Montego Bay cruise port at Montego Freeport. The terminal area connects to taxis, tour pickups and the main resort corridor."),
    ("Can you visit Dunn's River Falls from Montego Bay cruise port?", "Yes, on a dedicated shore excursion. Dunn's River Falls sits near Ocho Rios, roughly 60–90 minutes east of Montego Bay. It requires a cruise-friendly tour with realistic timing."),
    ("Is Doctor's Cave Beach good for cruise passengers?", "Doctor's Cave Beach is one of the best beach options for Montego Bay cruise passengers — famous clear water, facilities and a short drive from the port."),
    ("Are Montego Bay shore excursions suitable for families?", "Yes. Beach days, Rose Hall tours and many river adventures work for families. Dunn's River Falls suits older children who can handle moderate climbing."),
    ("Do Montego Bay tours return to the ship on time?", "Reputable Montego Bay shore excursion operators track ship schedules and build buffer time. Always confirm your all aboard time at booking."),
    ("Should I book a beach day or an adventure tour?", "Choose a beach day if you want maximum relaxation with minimal travel. Choose an adventure tour if Dunn's River Falls, caves or river tubing are priorities — and your port time allows for longer drives."),
    ("Is Montego Bay safe for cruise passengers?", "Cruise passengers on organised Montego Bay shore excursions and in tourist areas generally have straightforward visits. Stick with licensed operators and standard travel awareness."),
    ("Can you hire a private driver in Montego Bay?", "Yes. Private driver tours are popular with cruise passengers who want a custom route — Rose Hall, beaches, shopping and a waterfall if timing allows."),
]

EXCURSIONS_FAQS = [
    ("Should I book a beach day or an adventure tour?", "Beach days suit short port calls and relaxed travellers. Adventure tours to Dunn's River Falls or Green Grotto need longer drives — book only when your ship schedule allows a 5–6 hour excursion plus buffer time."),
    ("Do Montego Bay tours return to the ship on time?", "Licensed operators running Montego Bay cruise port tours track ship schedules. Confirm your all aboard time when booking."),
    ("Are Montego Bay shore excursions suitable for families?", "Beach breaks and Rose Hall work well for families. Dunn's River Falls suits older children who can handle moderate climbing."),
    ("Can you visit Dunn's River Falls from Montego Bay cruise port?", "Yes, on a dedicated shore excursion. Expect 60–90 minutes driving each way on a long port day with an early tour departure."),
    ("Can you hire a private driver in Montego Bay?", "Yes. Private driver tours let you customise your Jamaica cruise excursion — popular for couples and small groups."),
]

PORT_FAQS = [
    ("Where do cruise ships dock in Montego Bay?", "At the Montego Bay cruise port (Montego Freeport). The terminal connects to taxis, tour pickups and the main resort area."),
    ("Is Montego Bay good for cruise passengers?", "Yes. Montego Bay offers both easy beach days and bigger Jamaica adventures within reach on Montego Bay cruise tours."),
    ("Is Montego Bay safe for cruise passengers?", "Cruise passengers on organised shore excursions and in tourist corridors generally have straightforward visits. Use licensed operators and standard travel awareness."),
]

ONE_DAY_FAQS = [
    ("Should I book a beach day or an adventure tour?", "Beach days fit shorter port calls and relaxed pacing. Adventure tours to Dunn's River need 5–6 hours minimum — choose based on your ship's arrival and departure times."),
    ("Is Montego Bay good for cruise passengers?", "Yes — few Caribbean ports offer both an easy beach day and access to Jamaica's biggest sights."),
    ("Do Montego Bay tours return to the ship on time?", "Reputable Montego Bay shore excursion operators track ship schedules. Avoid over-ambitious DIY itineraries that stack too many distant sights."),
]

DUNNS_RIVER_FAQS = [
    ("Can you visit Dunn's River Falls from Montego Bay cruise port?", "Yes, on a dedicated shore excursion. The falls are near Ocho Rios, roughly 60–90 minutes east of Montego Bay. It requires a cruise-friendly tour with realistic timing."),
    ("Is Dunn's River Falls worth it from Montego Bay?", "On a long port day with an early departure, yes — it is one of Jamaica's unmissable experiences. On a short call, a beach day or Rose Hall tour may be more realistic."),
    ("Do Montego Bay tours return to the ship on time?", "Licensed operators running Dunn's River excursions from Montego Bay track ship schedules and build buffer time."),
]

DOCTORS_CAVE_FAQS = [
    ("Is Doctor's Cave Beach good for cruise passengers?", "Yes — it is one of the best beach options for Montego Bay cruise passengers. Clear water, facilities and a short drive from the port."),
    ("Should I book a beach day or an adventure tour?", "Choose Doctor's Cave if you want maximum relaxation and schedule flexibility. Choose an adventure tour if Dunn's River Falls or caves are your priority."),
    ("Are Montego Bay shore excursions suitable for families?", "Doctor's Cave Beach is among the most family-friendly Montego Bay shore excursions — calm water, facilities and easy pacing for all ages."),
]

GREEN_GROTTO_FAQS = [
    ("Is Green Grotto Caves worth visiting from Montego Bay?", "Yes, if you want something beyond beaches and waterfalls. The drive is shorter than Dunn's River, and the cave experience is distinctive."),
    ("Are Montego Bay shore excursions suitable for families?", "Green Grotto suits families with older children who enjoy exploring. Very young children may prefer a beach day at Doctor's Cave."),
    ("Do Montego Bay tours return to the ship on time?", "Licensed operators running Green Grotto excursions track ship schedules. Standalone cave tours typically offer good return-to-ship confidence."),
]

ROSE_HALL_FAQS = [
    ("Is Rose Hall worth visiting from Montego Bay cruise port?", "Yes — Rose Hall is one of the easiest cultural Montego Bay shore excursions. Short drive, engaging guided tour, and hilltop views."),
    ("Can you combine Rose Hall with a beach day?", "Yes. Rose Hall's proximity to Doctor's Cave Beach makes this a popular half-day combination on Montego Bay cruise tours."),
    ("Are Montego Bay shore excursions suitable for families?", "Rose Hall suits families with older children interested in history. Younger children may find the ghost-story elements unsettling."),
]

PRIVATE_DRIVER_FAQS = [
    ("Can you hire a private driver in Montego Bay?", "Yes. Private driver tours are widely available for Montego Bay cruise passengers. Book ahead for busy port days and confirm pickup at the cruise terminal."),
    ("Do private drivers return to the ship on time?", "Reputable licensed drivers track ship schedules and build buffer time. Share your all aboard time at the start of the day."),
    ("Can a private driver take you to Dunn's River Falls?", "Yes, on a long port day. The drive is 60–90 minutes each way — your driver should advise whether timing allows a falls visit plus other stops."),
]


def faq_schema(faqs):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a},
            }
            for q, a in faqs
        ],
    }


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Montego Bay Shore Excursions",
        "url": f"{DOMAIN}/",
        "description": "Planning guide for Montego Bay cruise shore excursions in Jamaica",
    }


def local_business_schema():
    return {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": "Montego Bay Shore Excursions",
        "url": f"{DOMAIN}/",
        "description": "Independent cruise passenger guide to Montego Bay shore excursions and Jamaica port day planning",
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Montego Bay",
            "addressRegion": "St. James",
            "addressCountry": "JM",
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": "18.4762",
            "longitude": "-77.8939",
        },
    }


PAGES = [
    {
        "path": "index.html",
        "depth": 0,
        "page": "home",
        "hero": "partials/hero-home.html",
        "content": "content/home.html",
        "trust": True,
        "title": "Montego Bay Shore Excursions | Jamaica Cruise Tours",
        "description": "Discover the best Montego Bay shore excursions for cruise passengers, including beach breaks, Dunn's River Falls, Green Grotto Caves, Rose Hall, river adventures and private Jamaica tours.",
        "canonical": "/",
        "preload": "images/hero-home.jpg",
        "og_image": "/images/hero-home.jpg",
        "geo_region": "JM",
        "geo_placename": "Montego Bay, Jamaica",
        "schemas": [website_schema(), local_business_schema(), faq_schema(HOME_FAQS)],
    },
    {
        "path": "excursions/index.html",
        "depth": 1,
        "page": "excursions",
        "hero": "partials/hero-excursions.html",
        "content": "content/excursions.html",
        "trust": True,
        "title": "Best Montego Bay Shore Excursions",
        "description": "Compare the best Montego Bay shore excursions, from beach days and river tubing to Dunn's River Falls, Green Grotto Caves, Rose Hall and private driver tours.",
        "canonical": "/excursions/",
        "preload": "images/hero-excursions.jpg",
        "og_image": "/images/hero-excursions.jpg",
        "schemas": [faq_schema(EXCURSIONS_FAQS)],
    },
    {
        "path": "montego-bay-cruise-port-guide/index.html",
        "depth": 1,
        "page": "port",
        "hero": "partials/hero-port-guide.html",
        "content": "content/montego-bay-cruise-port-guide.html",
        "trust": True,
        "title": "Montego Bay Cruise Port Guide",
        "description": "A practical guide to Montego Bay cruise port, including what to expect, how to choose a shore excursion and what cruise passengers can see in one day.",
        "canonical": "/montego-bay-cruise-port-guide/",
        "preload": "images/cruise-port.jpg",
        "og_image": "/images/cruise-port.jpg",
        "schemas": [faq_schema(PORT_FAQS)],
    },
    {
        "path": "one-day-in-montego-bay-from-cruise-ship/index.html",
        "depth": 1,
        "page": "one-day",
        "hero": "partials/hero-one-day.html",
        "content": "content/one-day-in-montego-bay-from-cruise-ship.html",
        "trust": True,
        "title": "One Day in Montego Bay From a Cruise Ship",
        "description": "Plan one day in Montego Bay from a cruise ship with beach, waterfall, river, cave, shopping and sightseeing ideas for cruise passengers.",
        "canonical": "/one-day-in-montego-bay-from-cruise-ship/",
        "preload": "images/one-day.jpg",
        "og_image": "/images/one-day.jpg",
        "schemas": [faq_schema(ONE_DAY_FAQS)],
    },
    {
        "path": "dunns-river-falls-from-montego-bay/index.html",
        "depth": 1,
        "page": "dunns-river",
        "hero": "partials/hero-dunns-river.html",
        "content": "content/dunns-river-falls-from-montego-bay.html",
        "trust": True,
        "title": "Dunn's River Falls From Montego Bay Cruise Port",
        "description": "Find out whether Dunn's River Falls is worth visiting from Montego Bay cruise port, including travel time, tour tips and cruise passenger advice.",
        "canonical": "/dunns-river-falls-from-montego-bay/",
        "preload": "images/dunns-river-falls.jpg",
        "og_image": "/images/dunns-river-falls.jpg",
        "schemas": [faq_schema(DUNNS_RIVER_FAQS)],
    },
    {
        "path": "doctors-cave-beach-montego-bay/index.html",
        "depth": 1,
        "page": "doctors-cave",
        "hero": "partials/hero-doctors-cave.html",
        "content": "content/doctors-cave-beach-montego-bay.html",
        "trust": True,
        "title": "Doctor's Cave Beach From Montego Bay Cruise Port",
        "description": "A cruise passenger guide to Doctor's Cave Beach in Montego Bay, including why it is popular, who it suits and how it fits into a Jamaica cruise stop.",
        "canonical": "/doctors-cave-beach-montego-bay/",
        "preload": "images/doctors-cave-beach.jpg",
        "og_image": "/images/doctors-cave-beach.jpg",
        "schemas": [faq_schema(DOCTORS_CAVE_FAQS)],
    },
    {
        "path": "green-grotto-caves-montego-bay/index.html",
        "depth": 1,
        "page": "green-grotto",
        "hero": "partials/hero-green-grotto.html",
        "content": "content/green-grotto-caves-montego-bay.html",
        "trust": True,
        "title": "Green Grotto Caves From Montego Bay Cruise Port",
        "description": "Discover Green Grotto Caves from Montego Bay cruise port, including what to expect, who it suits and why it works well for Jamaica cruise passengers.",
        "canonical": "/green-grotto-caves-montego-bay/",
        "preload": "images/green-grotto-caves.jpg",
        "og_image": "/images/green-grotto-caves.jpg",
        "schemas": [faq_schema(GREEN_GROTTO_FAQS)],
    },
    {
        "path": "rose-hall-great-house-montego-bay/index.html",
        "depth": 1,
        "page": "rose-hall",
        "hero": "partials/hero-rose-hall.html",
        "content": "content/rose-hall-great-house-montego-bay.html",
        "trust": True,
        "title": "Rose Hall Great House From Montego Bay Cruise Port",
        "description": "Learn about visiting Rose Hall Great House from Montego Bay cruise port, including history, views, tour options and cruise timing advice.",
        "canonical": "/rose-hall-great-house-montego-bay/",
        "preload": "images/rose-hall.jpg",
        "og_image": "/images/rose-hall.jpg",
        "schemas": [faq_schema(ROSE_HALL_FAQS)],
    },
    {
        "path": "private-driver-montego-bay/index.html",
        "depth": 1,
        "page": "private-driver",
        "hero": "partials/hero-private-driver.html",
        "content": "content/private-driver-montego-bay.html",
        "trust": True,
        "title": "Private Driver in Montego Bay for Cruise Passengers",
        "description": "Explore Montego Bay and nearby Jamaica highlights with a private driver tour designed for cruise passengers who want flexibility and comfort.",
        "canonical": "/private-driver-montego-bay/",
        "preload": "images/montego-bay-coastline.jpg",
        "og_image": "/images/montego-bay-coastline.jpg",
        "schemas": [faq_schema(PRIVATE_DRIVER_FAQS)],
    },
]


def rel(depth, asset):
    if depth == 0:
        return asset
    prefix = "../" * depth
    return f"{prefix}{asset}"


def render_page(p):
    depth = p["depth"]
    base = "../" * depth
    data_base = base.rstrip("/") if depth else ""
    data_base_attr = f'  data-base="{data_base}"\n' if depth else '  data-base=""\n'

    schema_blocks = "\n".join(
        f'  <script type="application/ld+json">\n{json.dumps(s, indent=2)}\n  </script>'
        for s in p["schemas"]
    )

    trust_attr = ""
    if p["trust"]:
        trust_attr = '  data-trust-strip="partials/trust-strip.html"\n'

    canonical_url = DOMAIN + (p["canonical"] if p["canonical"] != "/" else "/")
    og_image_url = DOMAIN + p["og_image"]

    geo_tags = ""
    if p.get("geo_region"):
        geo_tags = f'  <meta name="geo.region" content="{p["geo_region"]}" />\n  <meta name="geo.placename" content="{p["geo_placename"]}" />\n'

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>{p['title']}</title>
  <meta name="description" content="{p['description']}" />
  <meta name="keywords" content="{KEYWORDS}" />
  <link rel="canonical" href="{canonical_url}" />
  <link rel="preload" as="image" href="{rel(depth, p['preload'])}" fetchpriority="high" />

  <meta property="og:type" content="website" />
  <meta property="og:url" content="{canonical_url}" />
  <meta property="og:title" content="{p['title']}" />
  <meta property="og:description" content="{p['description']}" />
  <meta property="og:image" content="{og_image_url}" />
  <meta property="og:site_name" content="Montego Bay Shore Excursions" />
  <meta name="twitter:card" content="summary_large_image" />
{geo_tags}
{schema_blocks}

  <script src="https://cdn.tailwindcss.com"></script>
  <script src="{rel(depth, 'js/tailwind-config.js')}"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700&family=Source+Sans+3:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="{rel(depth, 'css/site.css')}" />
</head>
<body
  class="bg-white text-gray-800 antialiased"
  data-page="{p['page']}"
{data_base_attr}  data-hero="{p['hero']}"
{trust_attr}  data-content="{p['content']}"
>
  <div id="site-nav"></div>
  <div id="page-hero"></div>
  <div id="page-trust-strip"></div>
  <main id="page-content"></main>
  <div id="site-footer"></div>
  <script src="{rel(depth, 'js/site.js')}"></script>
</body>
</html>
"""


def main():
    for p in PAGES:
        out = ROOT / p["path"]
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_page(p), encoding="utf-8")
        print(f"Created {p['path']}")


if __name__ == "__main__":
    main()
