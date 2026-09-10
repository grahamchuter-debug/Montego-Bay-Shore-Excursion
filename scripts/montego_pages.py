"""Montego Bay Shore Excursion — Phase 14B page content modules.

Each public page function returns:
  (hero_html, main_html, faq_list_or_None, meta)

meta keys: title, description, canonical_path, page_id, og_image
faq_list: list[tuple[str, str]] | None
"""
from __future__ import annotations

from montego_config import (
    ACCENT,
    COASTLINE,
    COASTLINE_ALT,
    CRUISE_PORT,
    CRUISE_PORT_ALT,
    DOCTORS_CAVE,
    DOCTORS_CAVE_ALT,
    DUNNS_RIVER,
    DUNNS_RIVER_ALT,
    EMAIL,
    EXCURSIONS_HERO,
    EXCURSIONS_HERO_ALT,
    GREEN_GROTTO_HERO,
    GREEN_GROTTO_HERO_ALT,
    HERO_HOME,
    HERO_HOME_ALT,
    ONE_DAY_HERO,
    ONE_DAY_HERO_ALT,
    PRIVATE_DRIVER,
    PRIVATE_DRIVER_ALT,
    ROSE_HALL,
    ROSE_HALL_ALT,
    SITE,
)
from montego_shell import (
    cruise_snapshot,
    faq_section,
    hero_band,
    related_links,
)

Meta = dict[str, str]
FaqList = list[tuple[str, str]]
PageTuple = tuple[str, str, FaqList | None, Meta]


def _cta(primary_href: str, primary_label: str, secondary_href: str = "", secondary_label: str = "") -> str:
    parts = [
        f'<a href="{primary_href}" class="btn-primary inline-flex items-center justify-center gap-2 '
        f'text-white font-semibold px-7 py-3 rounded-full text-sm shadow-xl">{primary_label}</a>'
    ]
    if secondary_href:
        parts.append(
            f'<a href="{secondary_href}" class="btn-outline inline-flex items-center justify-center gap-2 '
            f'text-white font-semibold px-7 py-3 rounded-full text-sm">{secondary_label}</a>'
        )
    return "".join(parts)


def _section(inner: str, *, bg: str = "bg-white", pad: str = "pt-8 pb-12") -> str:
    return f'<section class="{pad} {bg}"><div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">{inner}</div></section>\n'


def _prose(inner: str, *, bg: str = "bg-white", narrow: bool = True) -> str:
    wrap = "max-w-3xl" if narrow else "max-w-7xl"
    return (
        f'<section class="py-14 {bg}"><div class="{wrap} mx-auto px-4 sm:px-6 lg:px-8">'
        f"{inner}</div></section>\n"
    )


# ---------------------------------------------------------------------------
# HOME
# ---------------------------------------------------------------------------


def home() -> PageTuple:
    hero = hero_band(
        eyebrow="Montego Bay · Jamaica",
        title_html=(
            f'Montego Bay Shore<br/><span class="{ACCENT}">Excursions</span><br/>'
            "for Cruise Passengers"
        ),
        lead=(
            "A practical guide to what works from Montego Freeport: near-port beaches "
            "and culture, longer north-coast adventures, and when a flexible private day "
            "makes more sense than stacking too many stops."
        ),
        image=HERO_HOME,
        aria_label=HERO_HOME_ALT,
        actions=_cta(
            "/excursions/",
            "Compare excursion styles",
            "/montego-bay-cruise-port-guide/",
            "Read the port guide",
        ),
        tags=["Doctor's Cave", "Rose Hall", "Dunn's from MoBay", "Private driver"],
    )

    snap = cruise_snapshot(
        [
            ("Typical time ashore", "Often around 5–8 hours — confirm your ship"),
            ("Near-port strengths", "Beach days, Hip Strip, Rose Hall"),
            ("Longer transfers", "Dunn's River Falls and some cave routes"),
            ("Planning focus", "One coherent theme beats over-stacking"),
            ("Return window", "Build a conservative buffer before all aboard"),
            ("This site", "Editorial planning — no booking checkout here"),
        ],
        label="Montego Bay cruise passenger snapshot",
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 lg:gap-20 items-center">
  <div>
    <div class="section-label">Jamaica cruise port</div>
    <h2 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 leading-snug mb-5">
      What Montego Bay is<br/><span class="text-ocean-600">actually good for</span>
    </h2>
    <p class="text-gray-600 leading-relaxed mb-5">
      Montego Bay rewards passengers who match ambition to geography. Doctor's Cave Beach,
      the Hip Strip and Rose Hall sit in the local orbit of the cruise area. Dunn's River Falls
      sits near Ocho Rios — reachable, but it consumes a large share of a typical call in road time.
      Green Grotto is a mid-distance option that still needs honest scheduling.
    </p>
    <p class="text-gray-600 leading-relaxed mb-8">
      Use this site to choose a style for the day: easy beach, culture close to port, a longer
      adventure, or a private driver who can adapt. Confirm live ship times and operator details
      before you commit — we do not publish fees, product codes or booking checkouts here.
    </p>
    <a href="/excursions/" class="btn-ocean inline-flex items-center gap-2 text-white font-semibold px-7 py-3.5 rounded-full text-sm shadow-lg">
      Explore decision groups
    </a>
  </div>
  <div class="info-image rounded-3xl aspect-[4/3] shadow-2xl overflow-hidden">
    <img src="{COASTLINE}" alt="{COASTLINE_ALT}" width="800" height="600" loading="eager" decoding="async" />
  </div>
</div>
''')}
{_section(f'''
<div class="text-center mb-12">
  <div class="section-label justify-center">Start here</div>
  <h2 class="text-3xl font-display font-bold text-gray-900">Four useful starting points</h2>
  <p class="mt-4 text-gray-500 max-w-2xl mx-auto">Pick the page that matches your question — not a ranking of “bestsellers”.</p>
</div>
<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">
  <a href="/doctors-cave-beach-montego-bay/" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col">
    <div class="card-media h-44"><img src="{DOCTORS_CAVE}" alt="{DOCTORS_CAVE_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
    <div class="p-5 flex flex-col flex-1">
      <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">Doctor's Cave Beach</h3>
      <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">Near-port beach day when you want water time without a long inland drive.</p>
      <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">Beach guide →</span>
    </div>
  </a>
  <a href="/rose-hall-great-house-montego-bay/" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col">
    <div class="card-media h-44"><img src="{ROSE_HALL}" alt="{ROSE_HALL_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
    <div class="p-5 flex flex-col flex-1">
      <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">Rose Hall Great House</h3>
      <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">One of the more practical culture stops in the Montego Bay orbit.</p>
      <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">Rose Hall guide →</span>
    </div>
  </a>
  <a href="/dunns-river-falls-from-montego-bay/" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col">
    <div class="card-media h-44"><img src="{DUNNS_RIVER}" alt="{DUNNS_RIVER_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
    <div class="p-5 flex flex-col flex-1">
      <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">Dunn's River from MoBay</h3>
      <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">Iconic falls — framed honestly as a long transfer, not a local stroll.</p>
      <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">Falls guide →</span>
    </div>
  </a>
  <a href="/private-driver-montego-bay/" class="card-hover bg-white rounded-2xl overflow-hidden border border-gray-100 shadow-sm group block flex flex-col">
    <div class="card-media h-44"><img src="{PRIVATE_DRIVER}" alt="{PRIVATE_DRIVER_ALT}" width="600" height="352" loading="lazy" decoding="async" /></div>
    <div class="p-5 flex flex-col flex-1">
      <h3 class="text-lg font-display font-semibold text-gray-900 group-hover:text-ocean-600 transition-colors">Private driver</h3>
      <p class="text-sm text-gray-500 mt-2 leading-relaxed flex-1">Decision guide for flexible pacing — not a bookable product on this site.</p>
      <span class="inline-flex mt-4 text-ocean-600 text-sm font-semibold">Private day guide →</span>
    </div>
  </a>
</div>
''', bg="bg-pr-50", pad="py-16")}
{_section(snap + related_links([
    ("/montego-bay-cruise-port-guide/", "Port guide"),
    ("/one-day-in-montego-bay-from-cruise-ship/", "One day ashore"),
    ("/excursions/", "Excursion styles"),
    ("/contact/", "Contact"),
]), pad="pb-16 pt-4")}
"""

    faqs: FaqList = [
        (
            "Is Montego Bay a good cruise stop?",
            "Yes for passengers who choose one coherent theme. Near-port beach and culture work well; "
            "longer transfers to Dunn's River need a longer call and disciplined timing.",
        ),
        (
            "Where do ships usually call in Montego Bay?",
            "Cruise calls are commonly associated with the Montego Freeport / cruise pier area. "
            "Confirm your ship's berth notes and terminal instructions for your sailing.",
        ),
        (
            "Should I try Dunn's River from Montego Bay?",
            "Only if your call is long enough and you accept significant road time. Passengers docking "
            "closer to Ocho Rios have a shorter approach — see our dedicated Dunn's-from-MoBay guide.",
        ),
    ]

    meta: Meta = {
        "title": "Montego Bay Shore Excursion | Cruise Passenger Planning Guide",
        "description": (
            "Plan Montego Bay shore excursions from the cruise port — Doctor's Cave, Rose Hall, "
            "Dunn's River transfers, Green Grotto and private-driver decision guidance."
        ),
        "canonical_path": "/",
        "page_id": "home",
        "og_image": HERO_HOME,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# EXCURSIONS
# ---------------------------------------------------------------------------


def excursions() -> PageTuple:
    hero = hero_band(
        eyebrow="Decision hub",
        title_html=f'Compare Montego Bay<br/><span class="{ACCENT}">excursion styles</span>',
        lead=(
            "Beach, culture, adventure, private/flexible and longer-distance Jamaica — "
            "grouped by how they fit a cruise call, not by invented popularity rankings."
        ),
        image=EXCURSIONS_HERO,
        aria_label=EXCURSIONS_HERO_ALT,
        breadcrumb="Excursions",
        actions=_cta("/montego-bay-cruise-port-guide/", "Port logistics first", "/one-day-in-montego-bay-from-cruise-ship/", "One-day scenarios"),
    )

    snap = cruise_snapshot(
        [
            ("How to use this page", "Choose a style, then open the matching guide"),
            ("Near-port", "Doctor's Cave, Hip Strip, Rose Hall"),
            ("Longer distance", "Dunn's River; plan carefully"),
            ("Orphan themes", "River tubing covered editorially below — no dedicated page yet"),
            ("Commerce", "No prices, SEG codes or checkout on this site"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Montego Bay shore days split cleanly once you decide how far you are willing to travel.
  Stay close for beach and plantation culture; commit the day if you want Jamaica's headline waterfall.
  Mixing both on a short call usually produces rushed photography and a tense return window.
</p>
''' + snap)}
{_section('''
<div class="mb-10">
  <div class="section-label">Beach</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Near-port water time</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Beach days suit shorter calls, mixed-age groups and anyone who wants swimming ahead of inland roads.
    Doctor's Cave is the clearest named beach option in our equity set; combine lightly with Hip Strip time if pacing allows.
  </p>
  <p><a href="/doctors-cave-beach-montego-bay/" class="text-ocean-600 font-semibold">Doctor's Cave Beach guide →</a></p>
</div>
<div class="mb-10">
  <div class="section-label">Culture</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Plantation history without a marathon drive</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Rose Hall is one of Montego Bay's more practical culture stops — close enough to pair with a beach afternoon
    when you keep the wish list short. Treat ghost-story marketing as colour, not as a substitute for cruise timing.
  </p>
  <p><a href="/rose-hall-great-house-montego-bay/" class="text-ocean-600 font-semibold">Rose Hall guide →</a></p>
</div>
<div class="mb-10">
  <div class="section-label">Adventure</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Caves and waterfall climbs</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Green Grotto offers a change of pace from beaches; Dunn's River is the signature climb — but from Montego Bay
    it is a transfer day, not a neighbourhood outing. Read both guides before stacking caves and falls.
  </p>
  <p class="space-x-4">
    <a href="/green-grotto-caves-montego-bay/" class="text-ocean-600 font-semibold">Green Grotto →</a>
    <a href="/dunns-river-falls-from-montego-bay/" class="text-ocean-600 font-semibold">Dunn's from MoBay →</a>
  </p>
</div>
<div class="mb-10">
  <div class="section-label">Private / flexible</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">When a private day helps</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Private driver days are useful for couples, small groups and passengers who want to adapt pace —
    not because they magically shrink Jamaica's roads. Our private-driver page is a decision guide only in this phase.
  </p>
  <p><a href="/private-driver-montego-bay/" class="text-ocean-600 font-semibold">Private driver decision page →</a></p>
</div>
<div class="mb-4">
  <div class="section-label">Longer-distance Jamaica</div>
  <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-3">Commit the day — or do not go</h2>
  <p class="text-gray-600 leading-relaxed max-w-3xl mb-6">
    Dunn's River Falls near Ocho Rios is the main longer-distance choice passengers ask about from Montego Bay.
    Falmouth and Ocho Rios calls sit differently on the same north coast; if your ship docks elsewhere,
    start with those ports' own guides rather than forcing a MoBay itinerary.
  </p>
  <p class="text-sm text-gray-500">
    Sister editorial sites (external):
    <a href="https://ochoriosshoreexcursion.com/" class="text-ocean-600" rel="noopener">Ocho Rios Shore Excursion</a>
    ·
    <a href="https://falmouthshoreexcursion.com/" class="text-ocean-600" rel="noopener">Falmouth Shore Excursion</a>
  </p>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<div class="section-label">Family D · editorial only</div>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">River tubing from Montego Bay</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  River tubing appears in many Jamaica cruise conversations, but this site does not yet carry a dedicated
  tubing URL. Treat it as an adventure-style option that still needs operator-confirmed duration, pickup
  logistics and a realistic return buffer — the same discipline as any inland water activity.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  If tubing is your priority, ask providers how the route sits relative to Montego Freeport, what the wet
  sections involve, and whether the product is designed around cruise all-aboard times. Do not assume
  Falmouth or Ocho Rios tubing marketing applies unchanged to a Montego Bay call.
</p>
<p class="text-sm text-gray-500">
  Imagery note: we do not show a fake tubing photograph. Use the
  <a href="/excursions/" class="text-ocean-600 font-medium">decision groups above</a>
  and the <a href="/one-day-in-montego-bay-from-cruise-ship/" class="text-ocean-600 font-medium">one-day guide</a>
  to keep the rest of the call realistic.
</p>
''' + related_links([
    ("/one-day-in-montego-bay-from-cruise-ship/", "One day scenarios"),
    ("/montego-bay-cruise-port-guide/", "Port guide"),
    ("/private-driver-montego-bay/", "Private driver"),
    ("/contact/", "Contact"),
]), bg="bg-white")}
"""

    faqs: FaqList = [
        (
            "How should I choose between beach and adventure?",
            "Choose beach for shorter calls and lower transfer risk. Choose adventure only when "
            "road time plus activity still leaves a conservative return window.",
        ),
        (
            "Is there a dedicated river tubing page?",
            "Not in this phase. Tubing is covered as an editorial section on this hub until a "
            "standalone guide is justified and approved.",
        ),
        (
            "Do you sell tours here?",
            "No. This is an independent planning guide. Use /contact/ for editorial questions only.",
        ),
    ]

    meta: Meta = {
        "title": "Best Montego Bay Shore Excursions | Compare Cruise Day Styles",
        "description": (
            "Compare Montego Bay cruise excursion styles — beach, culture, adventure, "
            "private/flexible and longer-distance options including Dunn's River transfers."
        ),
        "canonical_path": "/excursions/",
        "page_id": "excursions",
        "og_image": EXCURSIONS_HERO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# PORT GUIDE
# ---------------------------------------------------------------------------


def port_guide() -> PageTuple:
    hero = hero_band(
        eyebrow="Port logistics",
        title_html=f'Montego Bay<br/><span class="{ACCENT}">cruise port guide</span>',
        lead=(
            "What cruise passengers should know about Montego Freeport logistics, "
            "near-port choices and how far popular sights really sit from the pier."
        ),
        image=CRUISE_PORT,
        aria_label=CRUISE_PORT_ALT,
        breadcrumb="Port guide",
        actions=_cta("/excursions/", "Compare excursion styles", "/one-day-in-montego-bay-from-cruise-ship/", "One day ashore"),
    )

    snap = cruise_snapshot(
        [
            ("Port area", "Montego Freeport / cruise pier context"),
            ("Near-port", "Beach, Hip Strip, Rose Hall"),
            ("Mid / long", "Green Grotto; Dunn's River near Ocho Rios"),
            ("Berth notes", "Confirm live ship instructions — do not assume tender vs berth"),
            ("Return planning", "Leave buffer; traffic and queues vary"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Montego Bay is one of Jamaica's primary cruise gateways. Passengers usually organise the day around
  the Freeport / cruise pier area, then choose between staying local or committing road time along the north coast.
  Exact berth and gangway instructions belong to your cruise line for that sailing — treat pier anecdotes as orientation, not gospel.
</p>
''' + snap)}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Getting ashore and moving on</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Once you clear the terminal flow, decisions arrive quickly: organised tour pickup, licensed taxi, or a short local plan.
  If you are heading to Doctor's Cave or the Hip Strip, keep the plan compact and watch the clock.
  If you are heading toward Dunn's River, you are effectively buying a transfer-heavy day — see the dedicated guide before adding shopping stops.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Transport prices and “official” taxi rates change; we do not invent figures here. Ask for a clear quote, confirm currency,
  and agree whether attraction entry is included. Keep small notes of what you agreed for the return.
</p>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4 mt-10">What fits different call lengths</h2>
<ul class="space-y-3 text-gray-600 leading-relaxed">
  <li><strong class="text-gray-800">Shorter calls:</strong> beach or Rose Hall — not Dunn's River plus caves plus shopping.</li>
  <li><strong class="text-gray-800">Typical mid-length calls:</strong> one main theme with a light secondary stop nearby.</li>
  <li><strong class="text-gray-800">Longer calls:</strong> Dunn's-from-MoBay becomes more realistic if you depart early and avoid over-stacking.</li>
</ul>
''', bg="bg-sand-50")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Near-port practicality</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  <a href="/doctors-cave-beach-montego-bay/" class="text-ocean-600 font-medium">Doctor's Cave Beach</a>
  is the named beach passengers ask about most. The Hip Strip offers shops and a walkable tourist corridor —
  useful after a swim, less useful as a third stop after a long inland drive.
  <a href="/rose-hall-great-house-montego-bay/" class="text-ocean-600 font-medium">Rose Hall</a>
  sits in the Montego Bay cultural orbit and often pairs better with beach time than with Dunn's River.
</p>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4 mt-10">Planning the return window</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Build a conservative buffer before all aboard. Queues, weather and road slowdowns are normal Caribbean variables.
  This site talks about cruise-aware timing and return windows — not unsupported “back on ship guarantees.”
</p>
''' + related_links([
    ("/one-day-in-montego-bay-from-cruise-ship/", "One day in Montego Bay"),
    ("/excursions/", "Excursion styles"),
    ("/dunns-river-falls-from-montego-bay/", "Dunn's from MoBay"),
    ("/private-driver-montego-bay/", "Private driver"),
]))}
"""

    faqs: FaqList = [
        (
            "Is Montego Bay a tender port?",
            "Do not assume. Confirm your sailing's berth or tender notes with the cruise line. "
            "Local conditions and ship assignments can differ.",
        ),
        (
            "What is realistic near the port?",
            "Beach time, Hip Strip browsing and Rose Hall are the practical near-port themes. "
            "Dunn's River is a longer-distance commitment.",
        ),
        (
            "How much buffer should I leave?",
            "Leave more than you think you need — especially after inland drives. Confirm all-aboard "
            "time on the day and treat published schedules as live documents.",
        ),
    ]

    meta: Meta = {
        "title": "Montego Bay Cruise Port Guide | Freeport Logistics & Shore Days",
        "description": (
            "Practical Montego Bay cruise port guide — Freeport orientation, near-port choices, "
            "excursion distances and return-window planning for cruise passengers."
        ),
        "canonical_path": "/montego-bay-cruise-port-guide/",
        "page_id": "port",
        "og_image": CRUISE_PORT,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# ONE DAY
# ---------------------------------------------------------------------------


def one_day() -> PageTuple:
    hero = hero_band(
        eyebrow="Port-day planning",
        title_html=f'One day in Montego Bay<br/><span class="{ACCENT}">from a cruise ship</span>',
        lead=(
            "Choose a style for the hours you actually have — beach, culture + beach, "
            "private/flexible, or a longer adventure — instead of inventing one perfect itinerary."
        ),
        image=ONE_DAY_HERO,
        aria_label=ONE_DAY_HERO_ALT,
        breadcrumb="One day",
        actions=_cta("/excursions/", "Compare styles", "/montego-bay-cruise-port-guide/", "Port guide"),
    )

    snap = cruise_snapshot(
        [
            ("Anti-stacking rule", "One theme + optional light nearby stop"),
            ("Easy day", "Doctor's Cave / Hip Strip"),
            ("Culture + beach", "Rose Hall then water time"),
            ("Flexible day", "Private driver decision guide"),
            ("Long adventure", "Dunn's River from MoBay — only on longer calls"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  A Montego Bay cruise day is long enough to do something memorable and short enough to ruin itself
  with optimistic stacking. Start with your all-aboard time, then pick one of the styles below.
</p>
''' + snap)}
{_section('''
<div class="grid md:grid-cols-2 gap-6">
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Easy beach day</h2>
    <p class="text-sm text-gray-600 leading-relaxed mb-4">
      Swim and decompress near port. Use
      <a href="/doctors-cave-beach-montego-bay/" class="text-ocean-600 font-medium">Doctor's Cave</a>
      as the named beach reference, keep shopping light, and protect the return window.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Culture + beach</h2>
    <p class="text-sm text-gray-600 leading-relaxed mb-4">
      <a href="/rose-hall-great-house-montego-bay/" class="text-ocean-600 font-medium">Rose Hall</a>
      in the cooler part of the day, then water time if the clock still looks generous.
      Skip Dunn's River on the same call.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Private / flexible day</h2>
    <p class="text-sm text-gray-600 leading-relaxed mb-4">
      Useful when your group wants control of pace. Read the
      <a href="/private-driver-montego-bay/" class="text-ocean-600 font-medium">private driver decision page</a>
      — it is not a bookable product listing on this site.
    </p>
  </article>
  <article class="rounded-2xl border border-ocean-100 bg-white p-6">
    <h2 class="text-xl font-display font-bold text-gray-900 mb-3">Longer adventure day</h2>
    <p class="text-sm text-gray-600 leading-relaxed mb-4">
      Commit to
      <a href="/dunns-river-falls-from-montego-bay/" class="text-ocean-600 font-medium">Dunn's River from Montego Bay</a>
      or a mid-distance cave visit — not both plus Rose Hall plus beach.
      Short calls should think carefully before leaving the local orbit.
    </p>
  </article>
</div>
''', bg="bg-sand-50", pad="py-16")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">What not to do</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Do not treat Jamaica's north coast as a checklist. Dunn's River, Green Grotto, Rose Hall and a long beach lunch
  rarely fit a single cruise call from Montego Bay without stress. Passengers calling at
  <a href="https://ochoriosshoreexcursion.com/" class="text-ocean-600" rel="noopener">Ocho Rios</a>
  or
  <a href="https://falmouthshoreexcursion.com/" class="text-ocean-600" rel="noopener">Falmouth</a>
  face different drive times to the same landmarks — use the guide that matches your berth.
</p>
''' + related_links([
    ("/excursions/", "Excursion hub"),
    ("/montego-bay-cruise-port-guide/", "Port guide"),
    ("/green-grotto-caves-montego-bay/", "Green Grotto"),
    ("/contact/", "Contact"),
]))}
"""

    faqs: FaqList = [
        (
            "Is there one best day in Montego Bay?",
            "No. Match beach, culture, private pacing or a longer adventure to your call length "
            "and fitness — then stop adding stops.",
        ),
        (
            "Can I see Dunn's River and Doctor's Cave in one call?",
            "Usually a poor trade. The falls consume significant transfer time from Montego Bay; "
            "beach time then becomes rushed.",
        ),
    ]

    meta: Meta = {
        "title": "One Day in Montego Bay from a Cruise Ship | Realistic Port Plans",
        "description": (
            "Plan one day in Montego Bay from a cruise ship — beach, culture + beach, "
            "private/flexible and longer adventure scenarios without over-stacking."
        ),
        "canonical_path": "/one-day-in-montego-bay-from-cruise-ship/",
        "page_id": "one-day",
        "og_image": ONE_DAY_HERO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# DOCTOR'S CAVE
# ---------------------------------------------------------------------------


def doctors_cave() -> PageTuple:
    hero = hero_band(
        eyebrow="Beach day",
        title_html=f'Doctor\'s Cave Beach<br/><span class="{ACCENT}">from Montego Bay</span>',
        lead=(
            "A cruise-passenger decision guide to Montego Bay's best-known beach stop — "
            "practical questions, not invented entrance fees or opening hours."
        ),
        image=DOCTORS_CAVE,
        aria_label=DOCTORS_CAVE_ALT,
        breadcrumb="Doctor's Cave Beach",
        actions=_cta("/excursions/", "Compare styles", "/one-day-in-montego-bay-from-cruise-ship/", "One-day plans"),
    )

    snap = cruise_snapshot(
        [
            ("Role", "Near-port beach option"),
            ("Best for", "Swimming, relaxed pacing, mixed ages"),
            ("Pairing", "Light Hip Strip time or Rose Hall — not Dunn's"),
            ("Fees / hours", "Confirm live locally — not published here"),
            ("Return window", "Still plan a buffer; popular beaches get busy"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Why cruise passengers ask</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Clear water without a marathon transfer</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Doctor's Cave Beach is the named Montego Bay beach most cruise passengers recognise.
      It sits in the local resort corridor rather than hours inland, which makes it a strong answer
      when your priority is swimming and shade rather than chasing Jamaica's headline waterfall.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      We do not invent current entrance fees, locker prices, opening hours or facility guarantees.
      Those change. Confirm on the day with the beach operator or your tour provider.
    </p>
    <ul class="space-y-2 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Strong fit for shorter and mid-length calls</li>
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Easier pacing than Dunn's River from MoBay</li>
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Still needs a planned return window</li>
    </ul>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{DOCTORS_CAVE}" alt="{DOCTORS_CAVE_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Decision questions</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  <strong>Do you want swimming more than sightseeing?</strong> Choose the beach.
  <strong>Do you want plantation history the same day?</strong> Rose Hall can pair if you keep lunch and shopping short.
  <strong>Do you want Dunn's River?</strong> That is a different day shape — see the Dunn's-from-MoBay guide instead of forcing both.
</p>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4 mt-10">Who it suits</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Families, first-time Caribbean cruisers and anyone protecting mobility or heat tolerance.
  If your group thrives on climbing wet limestone for an hour after a long coach ride, look at adventure options instead.
</p>
''' + related_links([
    ("/rose-hall-great-house-montego-bay/", "Rose Hall"),
    ("/one-day-in-montego-bay-from-cruise-ship/", "One day"),
    ("/montego-bay-cruise-port-guide/", "Port guide"),
    ("/private-driver-montego-bay/", "Private driver"),
]), bg="bg-sand-50")}
"""

    faqs: FaqList = [
        (
            "Is Doctor's Cave good for cruise passengers?",
            "Yes when you want a near-port beach day. Confirm access details live; we do not invent fees or hours.",
        ),
        (
            "Can I combine Doctor's Cave with Rose Hall?",
            "Often more realistic than combining the beach with Dunn's River from Montego Bay — keep the secondary stop light.",
        ),
    ]

    meta: Meta = {
        "title": "Doctor's Cave Beach Montego Bay | Cruise Passenger Beach Guide",
        "description": (
            "Cruise passenger guide to Doctor's Cave Beach in Montego Bay — who it suits, "
            "how it fits a port day, and how it compares with longer Jamaica transfers."
        ),
        "canonical_path": "/doctors-cave-beach-montego-bay/",
        "page_id": "doctors-cave",
        "og_image": DOCTORS_CAVE,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# DUNN'S RIVER
# ---------------------------------------------------------------------------


def dunns_river() -> PageTuple:
    hero = hero_band(
        eyebrow="Longer transfer · not a MoBay local",
        title_html=f'Dunn\'s River Falls<br/><span class="{ACCENT}">from Montego Bay</span>',
        lead=(
            "Possible on the right call — but this is a long transfer toward the Ocho Rios side of the north coast, "
            "not a neighbourhood attraction. Short calls should think carefully."
        ),
        image=DUNNS_RIVER,
        aria_label=DUNNS_RIVER_ALT,
        breadcrumb="Dunn's River from Montego Bay",
        actions=_cta("/excursions/", "Other styles", "/doctors-cave-beach-montego-bay/", "Near-port beach instead"),
    )

    snap = cruise_snapshot(
        [
            ("Geography", "Falls near Ocho Rios — not beside Montego Freeport"),
            ("Road time", "Often around an hour or more each way — confirm live"),
            ("Day shape", "Transfer-heavy; protect the return window"),
            ("Short calls", "Think carefully — beach/culture may fit better"),
            ("Stacking", "Do not add caves + Rose Hall + long beach lunch"),
            ("Sister ports", "Ocho Rios calls are closer to the falls"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Honest framing</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Iconic falls, significant road commitment</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Dunn's River Falls is Jamaica's signature terraced waterfall climb. From Montego Bay it is absolutely
      reachable — and it will use a large share of a typical cruise call in transit alone.
      Road time is often around an hour or more each way; confirm live with your operator because traffic,
      construction and pickup logistics vary.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      This page does not compete with Ocho Rios guides by pretending the geography is equivalent.
      If your ship docks closer to the falls, start with
      <a href="https://ochoriosshoreexcursion.com/" class="text-ocean-600 font-medium" rel="noopener">Ocho Rios Shore Excursion</a>
      instead of forcing a Montego Bay transfer narrative.
    </p>
    <ul class="space-y-2 text-sm text-gray-600">
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Worth considering on longer calls with an early start</li>
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Water shoes and a change of clothes help</li>
      <li class="flex gap-2"><span class="text-ocean-600">✔</span> Viewing options exist if you skip the full climb</li>
    </ul>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{DUNNS_RIVER}" alt="{DUNNS_RIVER_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Who it suits from Montego Bay</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Active travellers who accept coach time for a headline experience, and first-time Jamaica visitors
  unlikely to return soon. It is a weaker fit for very short calls, tight mobility limits, or groups
  who mainly want swimming near port — choose
  <a href="/doctors-cave-beach-montego-bay/" class="text-ocean-600 font-medium">Doctor's Cave</a>
  or
  <a href="/rose-hall-great-house-montego-bay/" class="text-ocean-600 font-medium">Rose Hall</a>
  instead.
</p>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4 mt-10">What not to over-stack</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Resist adding Green Grotto, a long Hip Strip lunch and multiple shopping stops to the same Dunn's day
  from Montego Bay. The falls plus transfers are already the day. Falmouth passengers face yet another
  geography — see
  <a href="https://falmouthshoreexcursion.com/" class="text-ocean-600 font-medium" rel="noopener">Falmouth Shore Excursion</a>
  if that is your berth.
</p>
''' + related_links([
    ("/one-day-in-montego-bay-from-cruise-ship/", "One day scenarios"),
    ("/green-grotto-caves-montego-bay/", "Green Grotto"),
    ("/excursions/", "Excursion hub"),
    ("/montego-bay-cruise-port-guide/", "Port guide"),
]), bg="bg-sand-50")}
"""

    faqs: FaqList = [
        (
            "Can you visit Dunn's River Falls from Montego Bay?",
            "Yes on a dedicated, cruise-timed plan. Expect significant road time — often around an hour "
            "or more each way; confirm live — and protect your return window.",
        ),
        (
            "Is it worth it on a short call?",
            "Often no. Short calls usually fit beach or near-port culture better than a long eastbound transfer.",
        ),
        (
            "Is this the same as an Ocho Rios Dunn's River day?",
            "The attraction is the same geography; the transfer burden from Montego Bay is not. "
            "Do not treat the ports as interchangeable.",
        ),
    ]

    meta: Meta = {
        "title": "Dunn's River Falls from Montego Bay | Long Transfer Cruise Guide",
        "description": (
            "Honest guide to Dunn's River Falls from Montego Bay cruise port — long transfer realities, "
            "who it suits, and why short calls should think carefully."
        ),
        "canonical_path": "/dunns-river-falls-from-montego-bay/",
        "page_id": "dunns-river",
        "og_image": DUNNS_RIVER,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# ROSE HALL
# ---------------------------------------------------------------------------


def rose_hall() -> PageTuple:
    hero = hero_band(
        eyebrow="Culture near MoBay",
        title_html=f'Rose Hall Great House<br/><span class="{ACCENT}">Montego Bay</span>',
        lead=(
            "Plantation history and hilltop context in the Montego Bay orbit — "
            "one of the more practical culture choices for cruise passengers who want more than a beach."
        ),
        image=ROSE_HALL,
        aria_label=ROSE_HALL_ALT,
        breadcrumb="Rose Hall Great House",
        actions=_cta("/doctors-cave-beach-montego-bay/", "Pair with beach?", "/excursions/", "Compare styles"),
    )

    snap = cruise_snapshot(
        [
            ("Role", "Near-port culture / history stop"),
            ("Pairing", "Often beach — rarely Dunn's same day"),
            ("Tone", "Guided house tour; legend marketing is optional colour"),
            ("Fees", "Confirm live — not listed here"),
            ("Mobility", "Expect stairs/uneven areas — ask providers"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Montego Bay culture</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">A practical history stop in the local orbit</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      Rose Hall Great House is one of the easiest named culture experiences for Montego Bay cruise passengers.
      It sits closer to the MoBay resort corridor than Dunn's River does, which is why it pairs more naturally
      with a beach afternoon than with a waterfall transfer day.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      Keep the Montego framing: this is not a Falmouth port-day article with names swapped.
      If you are sailing into Falmouth, use that port's own guides for drive-time expectations.
    </p>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{ROSE_HALL}" alt="{ROSE_HALL_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">How it fits a cruise day</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Morning house tour, afternoon
  <a href="/doctors-cave-beach-montego-bay/" class="text-ocean-600 font-medium">Doctor's Cave</a>
  is a common shape when the call is mid-length. Adding Dunn's River on top usually breaks the day.
  A
  <a href="/private-driver-montego-bay/" class="text-ocean-600 font-medium">private driver day</a>
  can help with pacing between nearby stops — still without treating this site as a booking desk.
</p>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4 mt-10">Who it suits</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Travellers who want narrative and architecture, older children who can stay engaged on a guided tour,
  and passengers skipping wet-rock climbs. Very young children may prefer beach time only.
</p>
''' + related_links([
    ("/one-day-in-montego-bay-from-cruise-ship/", "One day"),
    ("/excursions/", "Excursion hub"),
    ("/montego-bay-cruise-port-guide/", "Port guide"),
    ("/green-grotto-caves-montego-bay/", "Green Grotto"),
]), bg="bg-sand-50")}
"""

    faqs: FaqList = [
        (
            "Is Rose Hall worth it from the cruise port?",
            "Yes as a practical culture stop in the Montego Bay orbit — especially if you want history without a Dunn's-length transfer.",
        ),
        (
            "Can Rose Hall combine with a beach?",
            "Often more realistic than combining Rose Hall with Dunn's River from Montego Bay on the same call.",
        ),
    ]

    meta: Meta = {
        "title": "Rose Hall Great House Montego Bay | Cruise Culture Guide",
        "description": (
            "Visit Rose Hall Great House from Montego Bay cruise port — practical culture pairing "
            "with beach days and honest advice on what not to stack."
        ),
        "canonical_path": "/rose-hall-great-house-montego-bay/",
        "page_id": "rose-hall",
        "og_image": ROSE_HALL,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# GREEN GROTTO
# ---------------------------------------------------------------------------


def green_grotto() -> PageTuple:
    hero = hero_band(
        eyebrow="Mid-distance option",
        title_html=f'Green Grotto Caves<br/><span class="{ACCENT}">from Montego Bay</span>',
        lead=(
            "A cave day with real travel implications from Montego Bay — framed with honest imagery "
            "(no fake grotto photograph) and careful timing."
        ),
        image=GREEN_GROTTO_HERO,
        aria_label=GREEN_GROTTO_HERO_ALT,
        breadcrumb="Green Grotto Caves",
        actions=_cta("/excursions/", "Compare styles", "/dunns-river-falls-from-montego-bay/", "Vs Dunn's River"),
        # Could also use css_only=True; coastline stand-in is preferred per brief
    )

    snap = cruise_snapshot(
        [
            ("Role", "Change-of-pace cave visit"),
            ("Transfer", "Mid-distance from MoBay — confirm live duration"),
            ("Vs Dunn's", "Different experience; still do not casually stack both"),
            ("Imagery", "No cave interior photo on this page"),
            ("Fees / hours", "Confirm live — not invented here"),
        ]
    )

    main = f"""
{_prose('''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Green Grotto Caves appeal to cruise passengers who want limestone chambers and a guided underground walk
  instead of a beach morning. From Montego Bay the visit still includes meaningful road time —
  less of a headline transfer than Dunn's River for many sailings, but not a five-minute hop from the gangway.
</p>
<p class="text-sm text-gray-500 mb-8">
  Photo note: we do not have a verified Green Grotto interior image in the live asset set.
  The hero uses Montego Bay coastline imagery with honest alt text rather than a quarantine 1×1 placeholder.
</p>
''' + snap)}
{_prose('''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Travel implications from MoBay</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Ask operators for pickup point, expected round-trip duration and how they handle cruise all-aboard buffers.
  Do not copy Falmouth or Ocho Rios cave timing assumptions wholesale — your berth changes the maths.
</p>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4 mt-10">Who it suits</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Curious walkers comfortable with humid enclosed spaces and moderate walking. Guests who mainly want swimming
  should prefer
  <a href="/doctors-cave-beach-montego-bay/" class="text-ocean-600 font-medium">Doctor's Cave</a>.
  Guests chasing the iconic climb should read
  <a href="/dunns-river-falls-from-montego-bay/" class="text-ocean-600 font-medium">Dunn's from Montego Bay</a>
  and pick one primary adventure theme.
</p>
''' + related_links([
    ("/one-day-in-montego-bay-from-cruise-ship/", "One day"),
    ("/rose-hall-great-house-montego-bay/", "Rose Hall"),
    ("/excursions/", "Excursion hub"),
    ("/montego-bay-cruise-port-guide/", "Port guide"),
]), bg="bg-sand-50")}
"""

    faqs: FaqList = [
        (
            "Is Green Grotto worth it from Montego Bay?",
            "Yes if you want a cave experience and accept mid-distance travel time. Confirm duration live; "
            "do not casually stack it with Dunn's River on a short call.",
        ),
        (
            "Why is there no grotto photo?",
            "The previous grotto asset was a broken placeholder. We use honest coastline imagery or a CSS hero instead.",
        ),
    ]

    meta: Meta = {
        "title": "Green Grotto Caves from Montego Bay | Cruise Timing Guide",
        "description": (
            "Green Grotto Caves from Montego Bay cruise port — travel implications, who it suits, "
            "and honest imagery without fake cave photographs."
        ),
        "canonical_path": "/green-grotto-caves-montego-bay/",
        "page_id": "green-grotto",
        "og_image": GREEN_GROTTO_HERO,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# PRIVATE DRIVER
# ---------------------------------------------------------------------------


def private_driver() -> PageTuple:
    hero = hero_band(
        eyebrow="Decision guide · not bookable here",
        title_html=f'Private driver in<br/><span class="{ACCENT}">Montego Bay</span>',
        lead=(
            "When a flexible vehicle day helps — and when it does not. "
            "Editorial decision page only: no prices, product codes or checkout."
        ),
        image=PRIVATE_DRIVER,
        aria_label=PRIVATE_DRIVER_ALT,
        breadcrumb="Private driver",
        actions=_cta("/excursions/", "Compare group styles", "/contact/", "Editorial contact"),
    )

    snap = cruise_snapshot(
        [
            ("Status on this site", "Decision page — not a bookable product"),
            ("Useful for", "Pacing, nearby combos, small groups"),
            ("Not magic", "Does not shrink Dunn's River road time"),
            ("Ask providers", "Licensing, buffer policy, what is excluded"),
            ("Avoid here", "Invented prices, SEG codes, capacity claims"),
        ]
    )

    main = f"""
{_section(f'''
<div class="grid lg:grid-cols-2 gap-12 items-start">
  <div>
    <div class="section-label">Flexible port days</div>
    <h2 class="text-2xl sm:text-3xl font-display font-bold text-gray-900 mb-4">Control of pace — not a shorter island</h2>
    <p class="text-gray-600 leading-relaxed mb-4">
      A private driver can help couples, families and small groups adapt a Montego Bay call:
      linger at Rose Hall, skip a crowded stop, or move to Doctor's Cave when energy dips.
      It does not erase north-coast distances. Dunn's River from MoBay remains a long transfer whether
      you travel by coach or car.
    </p>
    <p class="text-gray-600 leading-relaxed mb-4">
      This page intentionally omits prices, supplier names, vehicle capacity, age rules and product codes.
      Those belong to a future commercial phase — if approved — not this editorial rebuild.
    </p>
  </div>
  <div class="info-image rounded-3xl overflow-hidden aspect-[4/3] shadow-lg">
    <img src="{PRIVATE_DRIVER}" alt="{PRIVATE_DRIVER_ALT}" width="800" height="600" loading="lazy" decoding="async" />
  </div>
</div>
''')}
{_section(snap, pad="pb-8 pt-0")}
{_prose(f'''
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">When private pacing helps</h2>
<ul class="space-y-3 text-gray-600 leading-relaxed mb-8">
  <li>Combining nearby stops (for example Rose Hall + beach) without fixed group dwell times</li>
  <li>Mixed ages who need toilet stops, shade breaks or a quieter lunch</li>
  <li>Repeat visitors who have already done the headline waterfall elsewhere</li>
  <li>Passengers who want a clear conversation about the return window before leaving the pier</li>
</ul>
<h2 class="text-2xl font-display font-bold text-gray-900 mb-4">Questions to ask any provider</h2>
<p class="text-gray-600 leading-relaxed mb-4">
  Licensing, pickup point at the cruise area, what is included versus attraction entry, how they monitor
  all-aboard time, and what happens if traffic spikes. Get answers in writing where possible.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Next steps on this site:
  compare styles on the
  <a href="/excursions/" class="text-ocean-600 font-medium">excursions hub</a>
  or email
  <a href="mailto:{EMAIL}" class="text-ocean-600 font-medium">{EMAIL}</a>
  via
  <a href="/contact/" class="text-ocean-600 font-medium">contact</a>
  for editorial questions only.
</p>
''' + related_links([
    ("/excursions/", "Excursions"),
    ("/contact/", "Contact"),
    ("/rose-hall-great-house-montego-bay/", "Rose Hall"),
    ("/doctors-cave-beach-montego-bay/", "Doctor's Cave"),
]), bg="bg-sand-50")}
"""

    faqs: FaqList = [
        (
            "Can I book a private driver on this website?",
            "Not in this phase. This is a decision guide. Use /excursions/ to compare styles and /contact/ for editorial questions.",
        ),
        (
            "Can a private driver make Dunn's River a short trip?",
            "No. The falls still sit toward the Ocho Rios side of the coast. Private pacing helps stops and timing conversations — it does not delete road miles.",
        ),
    ]

    meta: Meta = {
        "title": "Private Driver Montego Bay | Cruise Day Decision Guide",
        "description": (
            "Private driver decision guide for Montego Bay cruise passengers — when flexibility helps, "
            "what to ask providers, and why this site does not publish prices or product codes."
        ),
        "canonical_path": "/private-driver-montego-bay/",
        "page_id": "private-driver",
        "og_image": PRIVATE_DRIVER,
    }
    return hero, main, faqs, meta


# ---------------------------------------------------------------------------
# TRUST PAGES
# ---------------------------------------------------------------------------


def contact() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'Contact<br/><span class="{ACCENT}">{SITE}</span>',
        lead="Editorial questions about this Montego Bay cruise planning guide.",
        image=HERO_HOME,
        aria_label=HERO_HOME_ALT,
        breadcrumb="Contact",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  Email <a href="mailto:{EMAIL}" class="text-ocean-600 font-semibold">{EMAIL}</a>
  for questions about this independent guide. We do not process bookings, payments or shore-excursion
  checkouts on this website in the current phase.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Please include your ship’s scheduled Montego Bay date if you are asking about planning logic —
  we still will not invent fees or guarantee operator inventory.
</p>
<p class="text-sm text-gray-500">Do not send payment card details by email.</p>
''')}
"""
    meta: Meta = {
        "title": f"Contact | {SITE}",
        "description": f"Contact {SITE} at {EMAIL} for editorial questions about this Montego Bay cruise planning guide.",
        "canonical_path": "/contact/",
        "page_id": "contact",
        "og_image": HERO_HOME,
    }
    return hero, main, None, meta


def about() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'About<br/><span class="{ACCENT}">{SITE}</span>',
        lead="Independent cruise-passenger planning for Montego Bay, Jamaica.",
        image=COASTLINE,
        aria_label=COASTLINE_ALT,
        breadcrumb="About",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed text-lg mb-6">
  {SITE} helps cruise passengers decide what is genuinely practical from a Montego Bay call —
  near-port beach and culture, mid-distance caves, and longer transfers such as Dunn's River —
  without pretending every highlight fits every ship schedule.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  We are not a cruise line, not a pier operator, and not a booking marketplace in this phase.
  Sister Jamaica guides for other berths include Ocho Rios and Falmouth; each keeps its own geography.
</p>
<p class="text-gray-600 leading-relaxed">
  Read our <a href="/methodology/" class="text-ocean-600 font-medium">methodology</a>
  and <a href="/contact/" class="text-ocean-600 font-medium">contact</a> pages for how we work.
</p>
''')}
"""
    meta: Meta = {
        "title": f"About | {SITE}",
        "description": f"About {SITE} — an independent cruise passenger planning guide for Montego Bay, Jamaica.",
        "canonical_path": "/about/",
        "page_id": "about",
        "og_image": COASTLINE,
    }
    return hero, main, None, meta


def privacy() -> PageTuple:
    hero = hero_band(
        eyebrow="Legal",
        title_html=f'Privacy<br/><span class="{ACCENT}">policy</span>',
        lead="How this editorial website handles information.",
        image=HERO_HOME,
        aria_label=HERO_HOME_ALT,
        breadcrumb="Privacy",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  {SITE} is an editorial planning website. If you email us at
  <a href="mailto:{EMAIL}" class="text-ocean-600 font-medium">{EMAIL}</a>,
  we use your message only to respond. We do not sell personal information.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  Standard server and security logs may record technical data such as IP address, user agent and requested URLs.
  Analytics, if enabled by the hosting platform, may collect aggregated traffic statistics.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  This site does not operate a booking checkout in the current phase and does not ask for payment card details.
</p>
<p class="text-sm text-gray-500">Questions: <a href="mailto:{EMAIL}" class="text-ocean-600">{EMAIL}</a>.</p>
''')}
"""
    meta: Meta = {
        "title": f"Privacy Policy | {SITE}",
        "description": f"Privacy policy for {SITE} — how this Montego Bay cruise planning website handles information.",
        "canonical_path": "/privacy/",
        "page_id": "privacy",
        "og_image": HERO_HOME,
    }
    return hero, main, None, meta


def terms() -> PageTuple:
    hero = hero_band(
        eyebrow="Legal",
        title_html=f'Terms of<br/><span class="{ACCENT}">use</span>',
        lead="Editorial information only — not a booking contract.",
        image=HERO_HOME,
        aria_label=HERO_HOME_ALT,
        breadcrumb="Terms",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  Content on {SITE} is general planning information for cruise passengers. It is not a ticket,
  voucher, insurance policy or contract with any tour operator. Attraction access, road times and
  ship schedules change — confirm live details before you travel.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  We are not affiliated with cruise lines calling at Montego Bay. Mentions of beaches, houses, caves
  or falls do not imply partnership. External links to sister destination sites are editorial references.
</p>
<p class="text-gray-600 leading-relaxed mb-4">
  To the fullest extent permitted by law, we disclaim liability for decisions made solely on the basis
  of this website. Nothing here creates a consumer booking relationship.
</p>
<p class="text-sm text-gray-500">Contact: <a href="mailto:{EMAIL}" class="text-ocean-600">{EMAIL}</a>.</p>
''')}
"""
    meta: Meta = {
        "title": f"Terms of Use | {SITE}",
        "description": f"Terms of use for {SITE} — editorial cruise planning information, not a booking marketplace.",
        "canonical_path": "/terms/",
        "page_id": "terms",
        "og_image": HERO_HOME,
    }
    return hero, main, None, meta


def methodology() -> PageTuple:
    hero = hero_band(
        eyebrow="Trust",
        title_html=f'Methodology<br/><span class="{ACCENT}">&amp; sourcing</span>',
        lead="How we organise Montego Bay cruise-day guidance without inventing commercial claims.",
        image=COASTLINE,
        aria_label=COASTLINE_ALT,
        breadcrumb="Methodology",
    )
    main = f"""
{_prose(f'''
<p class="text-gray-600 leading-relaxed mb-4">
  {SITE} prioritises cruise-passenger decisions: call length, transfer burden, and whether a stop
  sits in Montego Bay’s local orbit or requires a longer north-coast commitment.
</p>
<ul class="space-y-3 text-gray-600 leading-relaxed mb-6">
  <li>Preserve equity URLs that already attract search interest.</li>
  <li>Separate near-port options from longer transfers such as Dunn's River from MoBay.</li>
  <li>Avoid unsupported guarantees, star ratings, inventing fees/hours, and public product codes.</li>
  <li>Use only live image assets; quarantine broken 1×1 placeholders.</li>
  <li>Defer schedules imports and commerce activation to later approved phases.</li>
</ul>
<p class="text-gray-600 leading-relaxed">
  Softened wording (“often”, “confirm live”) marks uncertainty on minutes and berth details.
  See <a href="/about/" class="text-ocean-600 font-medium">about</a> and
  <a href="/contact/" class="text-ocean-600 font-medium">contact</a>.
</p>
''')}
"""
    meta: Meta = {
        "title": f"Methodology | {SITE}",
        "description": f"How {SITE} researches and organises Montego Bay cruise shore excursion planning guides.",
        "canonical_path": "/methodology/",
        "page_id": "methodology",
        "og_image": COASTLINE,
    }
    return hero, main, None, meta


def not_found() -> PageTuple:
    hero = ""
    main = f"""
<section class="pt-28 pb-24 bg-white">
  <div class="max-w-xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
    <p class="section-label justify-center">404</p>
    <h1 class="text-3xl sm:text-4xl font-display font-bold text-gray-900 mb-4">Page not found</h1>
    <p class="text-gray-600 leading-relaxed mb-8">
      That URL is not part of the {SITE} guide. Try the excursions hub or port guide.
    </p>
    <div class="flex flex-col sm:flex-row gap-3 justify-center">
      <a href="/" class="btn-ocean inline-flex items-center justify-center text-white font-semibold px-7 py-3 rounded-full text-sm">Home</a>
      <a href="/excursions/" class="inline-flex items-center justify-center font-semibold px-7 py-3 rounded-full text-sm border border-ocean-200 text-ocean-700">Excursions</a>
      <a href="/montego-bay-cruise-port-guide/" class="inline-flex items-center justify-center font-semibold px-7 py-3 rounded-full text-sm border border-ocean-200 text-ocean-700">Port guide</a>
    </div>
  </div>
</section>
"""
    meta: Meta = {
        "title": f"Page not found | {SITE}",
        "description": f"The requested page was not found on {SITE}.",
        "canonical_path": "/404.html",
        "page_id": "404",
        "og_image": HERO_HOME,
    }
    return hero, main, None, meta


PAGE_BUILDERS = {
    "home": home,
    "excursions": excursions,
    "port_guide": port_guide,
    "one_day": one_day,
    "doctors_cave": doctors_cave,
    "dunns_river": dunns_river,
    "rose_hall": rose_hall,
    "green_grotto": green_grotto,
    "private_driver": private_driver,
    "contact": contact,
    "about": about,
    "privacy": privacy,
    "terms": terms,
    "methodology": methodology,
    "not_found": not_found,
}
