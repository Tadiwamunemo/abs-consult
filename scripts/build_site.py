#!/usr/bin/env python3
"""Generate the static ABS Consult site."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NAV = [
    ("Consulting", "/consulting/", "consulting"),
    ("Planning", "/planning/", "planning"),
    ("Compliance", "/compliance/", "compliance"),
    ("Secretarial", "/secretarial/", "secretarial"),
    ("Contact Us", "/contact/", "contact"),
    ("About Us", "/about/", "about"),
]

POSTS = [
    {
        "slug": "vat-on-imported-services",
        "title": "VAT on Imported Services",
        "date": "December 4, 2024",
        "image": "/assets/images/blog-vat.jpg",
        "excerpt": "How Zimbabwe taxes services bought from foreign suppliers and used in the country.",
    },
    {
        "slug": "non-resident-shareholders-tax",
        "title": "Non-resident shareholders tax (NRST) treatment in Zimbabwe.",
        "date": "December 2, 2024",
        "image": "/assets/images/blog-nrst.jpg",
        "excerpt": "When dividend payments to non-residents attract NRST, and what the payer must withhold.",
    },
    {
        "slug": "finance-act-2024",
        "title": "Unraveling the Finance Act of 2024",
        "date": "December 2, 2024",
        "image": "/assets/images/blog-finance.jpg",
        "excerpt": "The changes that became law under the Finance Act No. 2 of 2024.",
    },
]


def icon_badge():
    return """<svg class="pillar-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M24 6l12 5v9c0 8.2-5.1 14.6-12 17-6.9-2.4-12-8.8-12-17V11l12-5z"/><path d="M17 23.5l4.2 4.2L31 18"/></svg>"""


def icon_people():
    return """<svg class="pillar-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><circle cx="17" cy="15" r="4.5"/><circle cx="31" cy="16.5" r="3.5"/><path d="M8 35.5c.8-6.2 4.4-9.5 9-9.5s8.2 3.3 9 9.5"/><path d="M26.5 27.2c2.6-.6 6.2.6 8.2 4.6"/></svg>"""


def icon_doc():
    return """<svg class="pillar-icon" viewBox="0 0 48 48" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><rect x="12" y="7" width="24" height="34" rx="3"/><circle cx="24" cy="18" r="4"/><path d="M17 30h14M17 35h9"/></svg>"""


def icon_chart():
    return """<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M6 26V14M13 26V8M20 26v-7M27 26V6"/><path d="M5 26h23"/></svg>"""


def icon_bulb():
    return """<svg viewBox="0 0 32 32" fill="none" stroke="currentColor" stroke-width="1.6" aria-hidden="true"><path d="M16 5a8 8 0 0 0-4 14.8V23h8v-3.2A8 8 0 0 0 16 5z"/><path d="M13 26h6M14 29h4"/></svg>"""


def icon_phone():
    return """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M7 3h3l1.5 4-2 1.5a12 12 0 0 0 6 6L17 13l4 1.5V18a2 2 0 0 1-2 2A15 15 0 0 1 4 5a2 2 0 0 1 2-2z"/></svg>"""


def icon_mail():
    return """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M4 7l8 6 8-6"/></svg>"""


def icon_down():
    return """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M6 9l6 6 6-6"/></svg>"""


def icon_up():
    return """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M6 15l6-6 6 6"/></svg>"""


def icon_wa():
    return """<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 3.2A8.7 8.7 0 0 0 4.7 16.3L3.5 20.5l4.3-1.1A8.8 8.8 0 1 0 12 3.2zm4.9 12.3c-.2.6-1.2 1.1-1.7 1.2-.4.1-.9.1-1.5-.1-.3-.1-.8-.3-1.4-.5-2.4-1-4-3.6-4.1-3.8-.1-.2-1-1.3-1-2.5s.6-1.8.9-2c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .5.4.2.6.7 2 .7 2.1.1.2 0 .3-.1.5l-.3.4c-.1.2-.3.3-.1.6.2.3.7 1.1 1.5 1.8 1 .9 1.9 1.2 2.2 1.3.3.1.4.1.6-.1l.5-.6c.2-.2.3-.2.6-.1.2.1 1.6.8 1.9.9.3.2.4.2.5.3.1.2 0 .7-.2 1.3z"/></svg>"""


def head(title, description):
    full = title if title == "ABS Consult" else f"{title} - ABS Consult"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{full}</title>
  <meta name="description" content="{description}">
  <meta name="theme-color" content="#141b2b">
  <link rel="icon" href="/assets/images/favicon.png" type="image/png">
  <link rel="apple-touch-icon" href="/assets/images/favicon.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Source+Sans+3:ital,wght@0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="/assets/css/styles.css?v=6">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
"""


def header(active):
    links = []
    for label, href, key in NAV:
        cls = ' class="is-active"' if key == active else ""
        links.append(f'<a href="{href}"{cls}>{label}</a>')
    return f"""<header class="site-header">
  <div class="container header-inner">
    <a class="logo" href="/" aria-label="ABS Consult home"><img src="/assets/images/logo.png" alt="ABS Consult"></a>
    <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="site-nav" aria-label="Menu"><span></span></button>
    <nav class="nav" id="site-nav" aria-label="Primary">
      {''.join(links)}
    </nav>
  </div>
</header>
"""


def footer(active=""):
    links = "".join(f'<a href="{href}">{label}</a>' for label, href, _ in NAV)
    list_links = "".join(
        f'<li><a href="{href}"{" class=\"is-active\"" if key == active else ""}>{label}</a></li>'
        for label, href, key in NAV
    )
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="reveal">
        <a class="logo" href="/"><img src="/assets/images/logo.png" alt="ABS Consult"></a>
        <p>Empowering our clients by reducing tax burdens, eliminating business inefficiencies, and unlocking capital for investment, growth, and success.</p>
        <p>Through our expertise and personalized approach, we help businesses optimize their financial strategies, streamline operations, and navigate complex regulatory environments.</p>
      </div>
      <div class="reveal" style="--d:.12s">
        <h2>Quick links</h2>
        <ul class="footer-links">{list_links}</ul>
      </div>
      <div class="reveal" style="--d:.2s">
        <h2>Contact us</h2>
        <ul class="contact-list">
          <li><a href="mailto:tax@absconsult.co.zw">{icon_mail()}tax@absconsult.co.zw</a></li>
          <li><a href="tel:+263773751230">{icon_phone()}+263 77 375 1230</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bar">
      <nav aria-label="Footer">{links}</nav>
      <p>© Copyright 2026. All rights reserved, ABS Consult</p>
    </div>
  </div>
</footer>
<a class="wa" href="https://wa.me/263773751230" target="_blank" rel="noopener noreferrer"><span class="wa-icon">{icon_wa()}</span><span>Contact us</span></a>
<button class="to-top" type="button" aria-label="Back to top">{icon_up()}</button>
<script src="/assets/js/main.js"></script>
</body>
</html>
"""


def page(path, title, description, active, main):
    html = head(title, description) + header(active) + main + footer(active)
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html)
    print(path)


def hero_home():
    return f"""<section class="hero">
  <div class="hero-media"></div>
  <div class="hero-shade"></div>
  <div class="container hero-copy">
    <p class="eyebrow light">Tax liberation</p>
    <h1>Empowering Growth Through Tax Knowledge, Tax Relief &amp; Efficiency.</h1>
    <p class="lead">Empowering our clients by relieving them from excessive taxes, business inefficiencies, and capital constraints, allowing them to reinvest, expand, and flourish.</p>
    <a class="btn" href="#services">Learn more {icon_down()}</a>
  </div>
</section>"""


def pillars():
    return f"""<section class="pillars" id="services">
  <div class="container pillar-grid">
    <article class="pillar reveal">
      {icon_badge()}
      <h2>Compliance</h2>
      <p>We offer a full range of tax compliance services, ensuring accuracy, timely filings, and adherence to all regulatory requirements.</p>
      <a class="link-more" href="/compliance/">Learn more</a>
    </article>
    <article class="pillar reveal" style="--d:.1s">
      {icon_people()}
      <h2>Advisory &amp; Consulting</h2>
      <p>We provide consulting services, helping businesses navigate complex tax regulations, optimize tax strategies, and achieve their financial goals.</p>
      <a class="link-more" href="/consulting/">Learn more</a>
    </article>
    <article class="pillar reveal" style="--d:.2s">
      {icon_doc()}
      <h2>Secretarial</h2>
      <p>We provide secretarial services to ensure compliance, maintain records, and support effective corporate governance.</p>
      <a class="link-more" href="/secretarial/">Learn more</a>
    </article>
  </div>
</section>"""


def expertise():
    return f"""<section class="expertise" id="about">
  <div class="container">
    <div class="section-head reveal">
      <div>
        <p class="eyebrow">About us</p>
        <h2>Experience and Expertise: Your Trusted Tax Consulting Team</h2>
      </div>
      <a class="btn btn-navy" href="/contact/">{icon_phone()} Get in touch</a>
    </div>
    <div class="expertise-grid">
      <div class="expertise-visual reveal">
        <img src="/assets/images/hands.jpg" alt="Advisor working through figures with a calculator and notes">
        <article class="float-card expertise-card">
          <h3>Tax Expertise</h3>
          <p>With 15 years of expertise, our tax company has earned a reputation as a trusted partner in tax compliance and strategy.</p>
        </article>
      </div>
      <div class="reveal" style="--d:.12s">
        <article class="feature">
          <div class="feature-title">{icon_chart()}<h3>Effective Solutions</h3></div>
          <p>At ABS Consult, we provide tailored tax solutions that drive real results. Our strategies help clients enhance profitability, optimize cash flow, and navigate complex tax challenges effectively.</p>
        </article>
        <img class="chart-art" src="/assets/images/chart.png" alt="">
        <article class="feature">
          <div class="feature-title">{icon_bulb()}<h3>Innovative Strategies</h3></div>
          <p>Innovation is central to our approach at ABS Consult. We craft smarter, forward-thinking tax strategies that help clients manage obligations, maximize savings, and achieve their financial goals.</p>
        </article>
      </div>
    </div>
  </div>
</section>"""


def spectrum():
    return f"""<section class="spectrum" id="full-services">
  <div class="container">
    <p class="eyebrow reveal">Our services</p>
    <h2 class="reveal">Full-Spectrum Tax Advisory Services</h2>
    <div class="spectrum-stage">
      <figure class="spectrum-photo reveal">
        <img src="/assets/images/building.jpg" alt="Modern glass office building">
        <figcaption>
          <h3>15 Years of Experience</h3>
          <p>With 15 years of experience, we are reliable. Our integrated tax services enhance overall tax performance, providing greater opportunities to measure and improve your efficiency. We adopt a more strategic approach to tax and deliver exceptional value to your shareholders.</p>
        </figcaption>
      </figure>
      <aside class="float-card spectrum-card reveal" style="--d:.15s">
        <div class="check" aria-hidden="true"><svg width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="1.7"><path d="M5 12.5l4.2 4.2L19 7"/></svg></div>
        <h3>Complete Tax Services</h3>
        <ul>
          <li>* Compliance</li>
          <li>* Advisory</li>
          <li>* Consulting</li>
          <li>* Planning</li>
        </ul>
        <a class="btn" href="/consulting/">Learn more</a>
      </aside>
    </div>
  </div>
</section>"""


def insight_cards(heading=True):
    cards = []
    for i, post in enumerate(POSTS):
        cards.append(f"""<a class="insight-card reveal" style="--d:{i * 0.08}s" href="/insights/{post['slug']}/">
        <img src="{post['image']}" alt="">
        <h3>{post['title']}</h3>
        <p class="meta">{post['date']}</p>
      </a>""")
    head_html = """<div class="center-head reveal">
      <p class="eyebrow">Our blog</p>
      <h2>Tax Insights, Updates and Trends</h2>
    </div>""" if heading else ""
    return f"""<section class="insights" id="insights">
  <div class="container">
    {head_html}
    <div class="insight-grid">{''.join(cards)}</div>
  </div>
</section>"""


def icon_arrow():
    return """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>"""


def cta():
    return f"""<section class="page-cta">
  <div class="container">
    <p class="eyebrow light">We're here to help</p>
    <div class="page-cta-row">
      <h2>Get in touch with us</h2>
      <a class="btn" href="/contact/">Contact {icon_arrow()}</a>
    </div>
  </div>
</section>"""


def page_hero(image, eyebrow, title, lead, extra="", cta_href=""):
    lead_html = f'\n    <p class="lead">{lead}</p>' if lead else ""
    btn = f'\n    <a class="btn" href="{cta_href}">Learn more {icon_down()}</a>' if cta_href else ""
    klass = f"page-hero {extra}".strip()
    return f"""<section class="{klass}" style="--image:url('{image}')">
  <div class="container">
    <p class="eyebrow light">{eyebrow}</p>
    <h1>{title}</h1>{lead_html}{btn}
  </div>
</section>"""


def flip_grid(items):
    blocks = []
    for title, body, span in items:
        blocks.append(f"""<button class="flip {span}" type="button" aria-pressed="false">
        <span class="flip-inner">
          <span class="flip-face flip-front"><span>{title}</span></span>
          <span class="flip-face flip-back"><span>{body}</span></span>
        </span>
      </button>""")
    return f'<div class="flip-grid">{"".join(blocks)}</div>'


def cards(items, columns_class="card-grid"):
    blocks = []
    for i, (title, body) in enumerate(items):
        blocks.append(f"""<article class="service-card reveal" style="--d:{(i % 3) * 0.08}s"><h3>{title}</h3><p>{body}</p></article>""")
    return f'<div class="{columns_class}">{"".join(blocks)}</div>'


def home():
    main = f"""<main id="main">
{hero_home()}
{pillars()}
{expertise()}
{spectrum()}
{insight_cards()}
</main>"""
    page(
        "index.html",
        "ABS Consult",
        "ABS Consult helps Zimbabwean businesses with tax compliance, planning, consulting, and company secretarial services.",
        "home",
        main,
    )


def consulting():
    main = f"""<main id="main">
{page_hero("/assets/images/hero-plain.jpg", "Tax consulting", "Tax Consulting, Specialization &amp; Insight", "The greatest long-term value we offer is sharing our knowledge. We believe that educating our clients strengthens our relationships and fosters trust.", "is-center", "#next")}
<section class="section" id="next">
  <div class="container split">
    <div class="reveal prose">
      <h2>What does tax consulting involve?</h2>
      <p>Tax consulting offers expert guidance on navigating tax laws, optimizing financial decisions, and minimizing liabilities. It provides strategic, tailored solutions to ensure compliance and maximize tax savings for individuals and businesses.</p>
      <p>Our tax consulting services include:</p>
      <ul class="check-list">
        <li>Entity structure planning for your business (per your situation).</li>
        <li>Tax planning or strategising.</li>
        <li>Business operations and documentation, and what is needed.</li>
        <li>What is truly a business expense, and how to maximize your deductions.</li>
        <li>Cash flow planning using incentives available in legislation.</li>
        <li>What is your why. Most people do not really know — together let’s figure it out.</li>
      </ul>
    </div>
    <img class="reveal frame" style="--d:.12s" src="/assets/images/consult.jpg" alt="Team in a strategy session">
  </div>
</section>
<section class="section alt">
  <div class="container narrow reveal">
    <p class="kicker">Our approach</p>
    <h2>Success lies in effective planning and preparation.</h2>
    <p>If you’re ready to take your business to the next level or start a new venture, it can feel overwhelming — but it doesn’t have to be. At ABS Consult, we’re here to help you focus on what you do best, while we handle the rest.</p>
    <p>You have a unique financial vision, and it’s time to embrace the next chapter of growth. Your financial journey is unlike anyone else’s, and stepping out with purpose means you’re heading toward greater financial success. There are opportunities waiting for you to achieve your financial goals. We believe that with the right financial support, you can navigate any challenges and realize your goals. At ABS Consult, we’re here to guide you through each step, ensuring you have the confidence and clarity to make informed financial decisions for a prosperous future.</p>
    <p>Being tax advisors has provided us with valuable exposure to a wide range of industries, giving us unique insights that we’re eager to share with our valued clients. This diverse experience allows us to offer tailored solutions to meet the specific needs of each client. By getting to know you and your business, we can better understand the challenges you face and create the most effective strategies for managing your financial and tax affairs, ensuring that every decision aligns with your goals and circumstances.</p>
  </div>
</section>
{insight_cards()}
{cta()}
</main>"""
    page("consulting/index.html", "Consulting", "Tax consulting, entity structure, deductions, and cash-flow planning from ABS Consult in Zimbabwe.", "consulting", main)


def planning():
    steps = [
        ("Return Review", "We carefully examine your latest tax returns, going through each item step by step."),
        ("Revenue Review", "We identify and consider every source of income and track how funds were allocated or used within the business."),
        ("Expenditure Review", "We evaluate your expenses to determine the optimal deductions for maximizing your profits."),
        ("Complete Solution", "We consolidate our approach, aiming to achieve objectives in the most tax-effective manner."),
    ]
    icons = [
        """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M7 3h7l5 5v13a1 1 0 0 1-1 1H7a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z"/><path d="M14 3v5h5M8 13h8M8 17h5"/></svg>""",
        """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 19V5M4 19h16"/><path d="M8 15v-3M12 15V8M16 15v-5"/></svg>""",
        """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h4"/></svg>""",
        """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="12" r="8"/><path d="M8.5 12.5l2.2 2.2 4.8-5"/></svg>""",
    ]
    step_html = []
    for i, ((title, body), icon) in enumerate(zip(steps, icons)):
        step_html.append(f'<article class="process-step reveal" style="--d:{i * 0.08}s"><span class="process-icon">{icon}</span><h3>{title}</h3><p>{body}</p></article>')
    main = f"""<main id="main">
{page_hero("/assets/images/notebook.jpg", "Tax planning", "Effortless Tax Planning, Expert Results", "Your earnings matter—let us help you keep more of them.", "is-center", "#next")}
<section class="section" id="next">
  <div class="container plan-layout">
    <div class="plan-visual reveal">
      <img src="/assets/images/planning.jpg" alt="Advisor reviewing returns at a desk">
      <aside class="plan-card">
        <h2>Our comprehensive tax planning includes:</h2>
        <ul>
          <li>Domestic and Indirect Tax Strategy</li>
          <li>Investment and Private Tax Advisory</li>
          <li>Transfer Pricing Solutions</li>
          <li>Sustainable Tax Planning</li>
          <li>Global Tax Strategy</li>
        </ul>
      </aside>
    </div>
    <div class="plan-why reveal" style="--d:.12s">
      <h2 class="with-icon"><span class="mini-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/></svg></span>Why You Need Tax Planning?</h2>
      <p>Traditional tax advice often looks back, focusing on last year’s expenses. Strategic tax planning, on the other hand, is forward-thinking—taking proactive steps to leverage legal opportunities, credits, and deductions.</p>
    </div>
  </div>
</section>
<section class="section tight">
  <div class="container">
    <div class="center-head mid reveal">
      <p class="eyebrow">Tax strategy</p>
      <h2>Our Process</h2>
    </div>
    <div class="process-grid">{''.join(step_html)}</div>
  </div>
</section>
<section class="navy-band">
  <img class="wide-photo reveal" src="/assets/images/office.jpg" alt="Business newspaper">
  <div class="container navy-grid reveal">
    <div>
      <h2>Business Tax Planning</h2>
      <p>As tax advisors, we’ve gained valuable insights and experience across a wide range of industries. These diverse exposures allow us to offer unique perspectives and strategies, which we are eager to share with our valued clients to help them thrive in their respective sectors.</p>
      <p>Getting to know our clients in depth is a crucial step that allows us to tailor our approach and develop the most effective strategies for managing your financial affairs. By taking the time to understand the specific goals, challenges, and dynamics of your business or personal situation, we are able to create a comprehensive plan that aligns with your needs. Our approach, rooted in years of expertise, involves a careful and strategic process designed to optimize your financial outcomes while minimizing tax liabilities.</p>
    </div>
    <ul class="band-list">
      <li>Strategic Planning for Entry</li>
      <li>Creating Ideal Business Structures</li>
      <li>Tax Risk Assessment and Due Diligence</li>
      <li>Legal Strategies for Reducing Taxable Income</li>
      <li>Optimizing Deductions</li>
      <li>Leveraging Tax Losses</li>
      <li>Recovering Overpaid Taxes</li>
    </ul>
  </div>
</section>
{insight_cards()}
{cta()}
</main>"""
    page("planning/index.html", "Planning", "Forward-looking tax planning for Zimbabwean businesses, from return review to structure and deductions.", "planning", main)


def compliance():
    items = [
        ("Income Tax Return (ITF12C)", "Calculating and submitting your ITF12C return annually on time to prevent penalties.", ""),
        ("ZIMRA VAT Registration", "A taxpayer is liable to register for VAT once their taxable supply exceeds USD 25,000.00.", ""),
        ("Tax Clearance", "We provide comprehensive assistance in processing Tax Clearances, ensuring that all necessary documentation is accurately prepared and submitted to facilitate a smooth and timely clearance process.", ""),
        ("ZIMRA TIN Registration", "We assist in registering with ZIMRA to obtain your Taxpayer Identification Number (TIN), ensuring that all required forms are completed accurately and submitted.", ""),
        ("TaRMS Registration", "Returns are submitted via e-filing services to prevent penalties.", ""),
        ("Company Returns", "We help companies file tax returns on time, ensuring compliance and avoiding penalties or tax issues.", ""),
        ("Transfer Pricing Return (ITF12C2)", "We handle the computation and timely filing of your ITF12C2 return annually, ensuring compliance and avoiding penalties.", ""),
        ("Provisional Tax (ITF12B)", "We assist with the accurate computation and timely quarterly filing of your QPDs, helping you avoid penalties.", ""),
        ("Statutory Obligations", "We assist with the computation and filing of NEC, NSSA, SDF, and ZIMDEF returns, ensuring compliance and avoiding penalties.", ""),
        ("Tax Audits and Representations", "We are here to support you with ZIMRA representations during all your tax audits.", ""),
        ("Pay As You Earn (P2) Returns", "Ensuring the accurate computation and timely monthly filing of your P2 returns to help you avoid penalties.", ""),
        ("Single Account Change", "If you’re planning to switch from one bank to another, we’re here to assist you every step of the way.", ""),
        ("ITF16", "We assist with the accurate computation and timely annual filing of your ITF16 return, ensuring compliance and helping you avoid penalties.", ""),
        ("CGT 1", "We assist with the computation and filing of your CGT1 return whenever you sell a specified asset.", ""),
        ("REV5", "We assist with the timely computation and filing of your REV5 form for Withholding Tax to help you avoid penalties.", ""),
        ("REV 2", "We assist with filling out and submitting your changes, updating your status with ZIMRA.", ""),
        ("VAT 7 Return", "We provide comprehensive assistance with accurately computing and filing your VAT7 return on time, so deadlines are met and penalties are avoided.", "span-2"),
        ("VAT 10 Return", "Let us take care of processing your VAT refunds the correct way, ensuring that all procedures are followed accurately to prevent penalties.", "span-2"),
    ]
    main = f"""<main id="main">
{page_hero("/assets/images/notebook.jpg", "Tax compliance", "All-Inclusive Tax Compliance Services", "We make it a priority to stay current with evolving tax laws to offer our clients timely guidance and enhanced solutions.", "is-center", "#next")}
<section class="section" id="next">
  <div class="container">
    <div class="center-head compact reveal">
      <h2>ZIMRA Compliance</h2>
      <p class="intro">We fully recognize the complexities of the current business landscape and regulatory challenges. Our compliance services are designed to address our clients’ pressing needs, offering support in areas such as registrations, consulting, advisory, planning, calculations, and the timely submission of various tax categories, including Value Added Tax, Income Tax, Withholding Tax, Capital Gains, and Transfer Pricing.</p>
    </div>
    {flip_grid(items)}
  </div>
</section>
<section class="section tight">
  <div class="container why-layout">
    <img class="reveal" src="/assets/images/compliance.jpg" alt="Signing tax documents">
    <div class="reveal" style="--d:.1s">
      <p class="kicker">Why us?</p>
      <h2>ABS Compliance Services</h2>
      <article class="why-item">
        <h3 class="with-icon"><span class="mini-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M6 9a6 6 0 0 1 12 0c0 7 3 7 3 9H3c0-2 3-2 3-9"/><path d="M10 20a2 2 0 0 0 4 0"/></svg></span>The Growing Importance of Tax Compliance</h3>
        <p>Ignoring tax liabilities can have serious consequences, and demonstrating compliance offers significant advantages. With businesses facing budget shortfalls, ZIMRA is increasing efforts to identify those neglecting their tax responsibilities. It’s time to rethink how taxes are approached—not as something to avoid, but as a necessary obligation.</p>
      </article>
      <article class="why-item">
        <h3 class="with-icon"><span class="mini-icon" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="5"/><path d="m9.4 8.1 1.6 1.6 3.4-3.4"/><path d="M7 13.2 5.2 21l6.8-2.5L18.8 21 17 13.2"/></svg></span>Efficient Tax Compliance and Advisory Services</h3>
        <p>Our tax compliance and advisory services help businesses efficiently manage their tax obligations and meet deadlines. We integrate these services with finance and accounting for a complete compliance solution. Our experts prepare monthly tax returns, address inquiries promptly, and provide necessary management reports to support business operations.</p>
      </article>
    </div>
  </div>
</section>
{cta()}
</main>"""
    page("compliance/index.html", "Compliance", "ZIMRA compliance support from ABS Consult, including VAT, income tax, PAYE, withholding tax, and tax clearance.", "compliance", main)


def secretarial():
    reqs = [
        ("Company Objective", "Defines the primary goal or purpose a business aims to achieve through its activities.", """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>"""),
        ("Proposed Business Names", "Five creative and original business name suggestions, arranged by preference.", """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="9" cy="9" r="3"/><circle cx="16" cy="10" r="2.4"/><path d="M4 19c.6-3 2.6-4.5 5-4.5s4.4 1.5 5 4.5"/><path d="M14 15.2c1.4-.3 3 .2 4 2"/></svg>"""),
        ("Directors and Shareholders", "Names, surnames, ID or passport numbers, addresses and nationalities.", """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><circle cx="12" cy="8" r="3"/><path d="M6 19c1-3.2 3-4.8 6-4.8s5 1.6 6 4.8"/></svg>"""),
        ("Company addresses", "Physical, postal, and email contact details for the company in Zimbabwe.", """<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 10.5 12 4l8 6.5V20a1 1 0 0 1-1 1h-5v-6H10v6H5a1 1 0 0 1-1-1v-9.5z"/></svg>"""),
    ]
    tiles = [
        ("Company Formation", ""),
        ("Name Search", ""),
        ("Share Allotments", ""),
        ("Company Annual Return", ""),
        ("Company Conversion", "span-2"),
        ("Change of Directors", "span-2"),
    ]
    req_html = []
    for title, body, icon in reqs:
        req_html.append(f'<article class="req reveal"><span class="process-icon">{icon}</span><h3>{title}</h3><p>{body}</p></article>')
    tile_html = []
    for title, span in tiles:
        tile_html.append(f'<article class="tile {span}"><h3>{title}</h3></article>')
    main = f"""<main id="main">
{page_hero("/assets/images/notebook.jpg", "Secretarial services", "Zimbabwe Company Registration", "Transform your business ideas into profit. With our expertise, we meticulously assess your startup needs, ensuring a cost-effective business launch. Whether you’re looking to register a Private Limited Company or a Private Business Corporation, we’re here to help.", "is-center", "#next")}
<section class="section" id="next">
  <div class="container split">
    <div class="reveal prose">
      <p>Turn your business dreams into reality by registering a Private Limited Company (PLC) or a Private Business Corporation (PBC). Both are governed by the Companies Act but differ in documentation.</p>
      <p>A PLC is a popular choice in Zimbabwe, offering limited liability and comprehensive documentation, ideal for simplicity and protection. PBCs, on the other hand, are favored by professionals like web developers, lawyers, and consultants, especially post-pandemic.</p>
      <p>We not only assist with business registration but also provide startup advice and integrated tax and accounting services, ensuring a smooth, cost-effective launch and ongoing growth.</p>
    </div>
    <img class="reveal shot" style="--d:.1s" src="/assets/images/office.jpg" alt="Business newspaper">
  </div>
</section>
<section class="section tight">
  <div class="container">
    <div class="center-head mid reveal">
      <p class="eyebrow">Company registration</p>
      <h2>Requirements to Registering a company</h2>
    </div>
    <div class="req-grid">{''.join(req_html)}</div>
  </div>
</section>
<section class="services-banner">
  <div class="container reveal">
    <p class="eyebrow light">More services</p>
    <h2>Additional Secretarial Services We Provide.</h2>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="tile-grid">{''.join(tile_html)}</div>
  </div>
</section>
{cta()}
</main>"""
    page("secretarial/index.html", "Secretarial", "Company registration and secretarial services in Zimbabwe, including PLCs, PBCs, annual returns, and director changes.", "secretarial", main)


def about():
    main = f"""<main id="main">
{page_hero("/assets/images/about-hero.jpg", "Get to know us", "About Us", "We are professional advisors offering business process outsourcing solutions. Our mission is to empower our clients by eliminating the burden of overtaxation and business inefficiencies, unlocking their capital to invest, grow, and succeed.", "is-center", "#next")}
<section class="section" id="next">
  <div class="container">
    {cards([
        ("Our mission", "We are dedicated to helping businesses navigate the complexities of taxation with ease. By offering innovative solutions and expert advice, we empower our clients to achieve compliance, minimize liabilities, and unlock resources for growth and success."),
        ("Our journey", "With over 15 years in tax advisory and compliance, we have built relationships by helping businesses stay compliant, reduce liabilities, and grow in a way that lasts."),
        ("Our values", "Excellence, collaboration, adaptability, passion, trust, and commitment guide the work. They shape how we show up, beyond the numbers on a return."),
    ])}
  </div>
</section>
<section class="section alt">
  <div class="container">
    <div class="reveal" style="margin-bottom:22px">
      <p class="kicker">Why choose</p>
      <h2>ABS Consult</h2>
    </div>
    {cards([
        ("Expertise you can trust", "We keep updating our reading of tax rules as they change. Business tax strategy or personal tax optimization, the advice is specific and checkable."),
        ("Personalized solutions", "We learn the financial landscape first, then build a strategy that increases what you keep and lowers what you should not be paying. Your outcome is the brief."),
        ("A year-round practice", "We stay engaged through the year, so tax changes and opportunities are raised with you. You should not have to chase your advisor for an update."),
    ])}
  </div>
</section>
{spectrum()}
{insight_cards()}
{cta()}
</main>"""
    page("about/index.html", "About Us", "ABS Consult is a Zimbabwean tax advisory practice with 15 years of experience in compliance, planning, and secretarial work.", "about", main)


def contact():
    main = f"""<main id="main">
{page_hero("/assets/images/hero-plain.jpg", "Contact us", "We're here to help", "Got a question? Whether it’s about Advisory, Tax, Audit, or anything else, our team of professionals is ready to assist you. Fill out the form below, and we’ll get back to you as soon as possible.", "is-center", "#next")}
<section class="section" id="next">
  <div class="container contact-grid">
    <div class="reveal">
      <p>We welcome inquiries about starting a business, careers, media, services, events, accounts, feedback, or advice.</p>
      <div class="info-stack">
        <article class="info-card">
          <h3>Email</h3>
          <p><a href="mailto:tax@absconsult.co.zw">tax@absconsult.co.zw</a></p>
        </article>
        <article class="info-card">
          <h3>Phone</h3>
          <p><a href="tel:+263773751230">+263 77 375 1230</a></p>
        </article>
        <article class="info-card">
          <h3>WhatsApp</h3>
          <p><a href="https://wa.me/263773751230" target="_blank" rel="noopener noreferrer">+263 77 375 1230</a></p>
        </article>
      </div>
    </div>
    <form class="form reveal" style="--d:.1s">
      <h2>Send us a message</h2>
      <div class="form-row">
        <label>Name<input name="name" type="text" autocomplete="name" required></label>
        <label>Email<input name="email" type="email" autocomplete="email" required></label>
      </div>
      <label>Subject<input name="subject" type="text"></label>
      <label>Message<textarea name="message" required></textarea></label>
      <button class="btn btn-navy" type="submit">Submit</button>
      <p class="form-note" role="status"></p>
    </form>
  </div>
</section>
</main>"""
    page("contact/index.html", "Contact Us", "Contact ABS Consult by email, phone, or WhatsApp for tax, advisory, and secretarial enquiries.", "contact", main)


def insights():
    main = f"""<main id="main">
{page_hero("/assets/images/blog-finance.jpg", "Our blog", "Tax Insights, Updates and Trends", "Notes on Zimbabwean tax rules, written for owners and finance teams who have to apply them.")}
{insight_cards(heading=False)}
</main>"""
    page("insights/index.html", "Insights", "Tax insights and updates from ABS Consult, including VAT on imported services, NRST, and the Finance Act of 2024.", "insights", main)


def article_shell(title, date, image, body):
    related = []
    for post in POSTS:
        if post["title"] == title:
            continue
        related.append(f"""<a href="/insights/{post['slug']}/"><img src="{post['image']}" alt=""><span>{post['title']}</span></a>""")
    main = f"""<main id="main">
{page_hero(image, date, title, "", "is-article")}
<section class="section">
  <div class="container">
    <article class="article prose reveal">{body}</article>
    <div style="margin-top:48px">
      <p class="kicker">More from the journal</p>
      <div class="related">{''.join(related)}</div>
    </div>
  </div>
</section>
</main>"""
    return main


def articles():
    vat = """
      <p>The Value Added Tax (VAT) on Imported Services (VIS) in Zimbabwe ensures that services purchased from foreign entities and used by residents are taxed similarly to those offered by local businesses. This note covers the background, the relevant rules, and the effect of VIS on businesses.</p>
      <h2>What VIS covers</h2>
      <p>VIS targets services brought into Zimbabwe and consumed by residents. The standard VAT rate stands at 15%. The tax obligation is triggered by the earliest of these events: the issuance of an invoice, payment to the foreign provider, or completion of the service. Taxpayers must pay the tax by the 25th of the month after the service is provided, and they can reclaim VIS if the services directly contribute to taxable outputs. Payment of VAT on imported services can be made in local currency.</p>
      <p>The value for imported services is determined by the greater of the payment made or the open market value. Typically, ZIMRA applies a 15% rate on the payment. Barter or donation transactions are priced at market value, and services given without payment are valued at zero unless involving connected individuals. Services that are usually zero-rated or exempt locally, such as actuarial, insurance, medical, financial guarantee, or suretyship services, are exempt from VAT.</p>
      <h2>Reclaiming the tax</h2>
      <p>Reclaiming VIS involves paperwork and compliance. Taxpayers can offset the tax paid against their VAT obligations if the imported services are used directly for producing taxable outputs.</p>
      <p>The requirement to pay VAT by the 25th of the next month imposes a strict timeline. Businesses need the funds and the documentation ready, or they risk penalties and interest. The option to pay VIS in local currency adds flexibility, especially where foreign currency is tight.</p>
      <h2>What it means in practice</h2>
      <p>The implementation of VIS significantly affects businesses that buy from international service providers. Although the ability to reclaim VIS offers some relief, the requirement to prepay the tax can pressure cash flow, especially for small and medium-sized enterprises. The conditions for claiming a refund call for detailed records. That administrative load is heavier for smaller teams that do not have a dedicated tax function. ABS Consult prepares the computation, the timing, and the reclaim so the rule is observed without becoming a monthly surprise.</p>
    """
    nrst = """
      <h2>What is non-resident shareholders tax?</h2>
      <p>Non-resident shareholders tax is tax levied on a dividend accruing to a person who is not resident in Zimbabwe.</p>
      <h2>Who is a non-resident?</h2>
      <p>A non-resident means a person, other than a company, who is not ordinarily resident in Zimbabwe, or a partnership or foreign company which is not ordinarily resident in Zimbabwe. The definition is met any time a resident taxpayer in Zimbabwe makes a payment to a foreign resident entity or individual.</p>
      <p>For NRST, a dividend is income distributed by a company to its members as a return on capital they have invested. Every company that distributes a dividend is required to withhold the tax when it is paid to:</p>
      <ul>
        <li>A person, other than a company, a pension fund, a benefit fund, or a medical aid society, who is not ordinarily resident in Zimbabwe;</li>
        <li>A partnership which is not ordinarily resident in Zimbabwe;</li>
        <li>A foreign company; or</li>
        <li>A foreign life insurance company, in respect of any shareholding the Commissioner determines was acquired from funds other than those arising from that company’s life insurance business in Zimbabwe.</li>
      </ul>
      <p>Non-resident shareholders tax is levied at 15% of the gross dividend paid by an unlisted company, and at 10% where the paying company is listed. A lower rate can apply where a double taxation agreement is in place between Zimbabwe and the non-resident’s country of residence.</p>
      <h2>Distributions that are not dividends for this tax</h2>
      <ul>
        <li>Certain amounts distributed by a building society that are not distributed as a dividend on the specified classes of shares for the Central Africa Building Society, the Founders Building Society, and the Beverley Building Society.</li>
        <li>Bonus shares.</li>
        <li>Any amount which, in the opinion of the Commissioner, is a return of the amount received by the company for its shares.</li>
        <li>Amounts distributed by the Industrial Development Corporation of Zimbabwe Limited in respect of its issued share capital.</li>
        <li>Amounts distributed by the Zimbabwe Development Bank, established by section 3 of the Zimbabwe Development Bank Act [Chapter 24:14].</li>
        <li>Amounts distributed to the International Finance Corporation referred to in the International Financial Organizations Act [Chapter 22:09].</li>
        <li>Amounts distributed by a licensed investor which arise from operations in an export processing zone.</li>
        <li>Any amount which, in the opinion of the Commissioner, is a return of an amount contributed to the capital of a private business corporation by a member.</li>
        <li>Amounts distributed by an industrial park developer which arise from the operation of that industrial park.</li>
      </ul>
      <h2>When the dividend is deemed distributed</h2>
      <p>A dividend is deemed to have been distributed when it is paid to the shareholder, credited to the shareholder’s account, or otherwise dealt with so that the shareholder becomes entitled to it — whichever comes first.</p>
      <h2>The withholding certificate</h2>
      <p>Once NRST is withheld, the payer must give the shareholder a withholding tax certificate showing the gross amount of the dividend, any reduction of the dividend for the purpose of computing NRST, and the amount of non-resident shareholders tax withheld.</p>
    """
    finance = """
      <p><strong>Examining the significant changes introduced by the Finance Act No. 2 of 2024.</strong></p>
      <p>The Finance Bill, H.B. 8, 2024, underwent minimal changes, with the exception of the introduction of fees on certain presumptive taxes. It appears that the House leadership prioritized the concerns of thousands of informal traders who were dissatisfied with the fees imposed in the Finance Bill. Consequently, these measures are now legally obligatory for businesses and individuals to comply with.</p>
      <h2>Corporate income tax</h2>
      <p><em>Now legal, under the Finance Act No. 2 of 2024. 1 August 2024 is the effective date.</em></p>
      <h2>Payment of provisional tax (QPDs) in foreign currency</h2>
      <p>Companies receiving income in foreign currency and projecting that 50% or more of their income will be in foreign currency must remit 50% of their Quarterly Provisional Payments (QPDs) in local currency and 50% in foreign currency.</p>
      <p>For companies whose revenue exceeds 50% in local currency, taxes must be paid in the currency of trade.</p>
      <h2>Employment tax</h2>
      <p><em>Now legal, under the Finance Act No. 2 of 2024.</em></p>
      <ul>
        <li>The bonus-free threshold is now <strong>$700</strong>, from $400.</li>
        <li>Two tax periods apply because the currency changed from RTGS to ZiG.
          <ul>
            <li>1 January 2024 to 4 April 2024 (RTGS era).</li>
            <li>5 April 2024 to 31 December 2024 (ZiG era).</li>
          </ul>
        </li>
      </ul>
      <h2>Intermediated Money Transfer Tax</h2>
      <p>IMTT rates below are as set out in the Finance Act No. 2 of 2024.</p>
      <div class="table-wrap"><table>
        <thead><tr><th>Tax</th><th>Amount</th><th>Rate</th></tr></thead>
        <tbody>
          <tr><td>Fees</td><td>$100</td><td>$0.05 USD</td></tr>
          <tr><td>IMTT (ZiG)</td><td>Any amount</td><td>2%</td></tr>
          <tr><td>IMTT (ZiG)</td><td>Transaction exceeds the equivalent of $500,000 USD</td><td>$10,150 USD (at the prevailing interbank rate)</td></tr>
          <tr><td>IMTT (USD)</td><td>$500,000 USD</td><td>$10,150 USD</td></tr>
          <tr><td>Outbound foreign payments</td><td></td><td>2%</td></tr>
          <tr><td>Zimbabwe gold-backed digital tokens</td><td></td><td>2%</td></tr>
        </tbody>
      </table></div>
      <h2>Presumptive taxes</h2>
      <p>This is where the Finance Act moved furthest from the Bill. Monthly amounts below are shown as published.</p>
      <div class="table-wrap"><table>
        <thead><tr><th>Description</th><th>Previous rate</th><th>Enacted rate</th></tr></thead>
        <tbody>
          <tr><td>Driving schools — class 4 vehicles only<br>Driving schools — class 1 and class 2</td><td>USD 300<br>USD 600</td><td>USD 50<br>USD 100</td></tr>
          <tr><td>Hairdressing salons</td><td>USD 300 per chair</td><td>USD 5 per chair</td></tr>
          <tr><td>Informal cross-border traders</td><td>20% of the value for duty purposes</td><td>20% of the value for duty purposes</td></tr>
          <tr><td>Informal traders</td><td>10% of the monthly rentals of the premises they operate from</td><td>10% of the monthly rentals of the premises they operate from</td></tr>
          <tr><td>Restaurants or bottle stores</td><td>USD 300</td><td>USD 35</td></tr>
          <tr><td>Cottage industry operators</td><td>USD 300</td><td>USD 100</td></tr>
          <tr><td>Commercial waterborne vessels, by passenger capacity<br>Fewer than 5<br>6 to 15<br>16 to 25<br>26 to 49<br>More than 49</td><td>USD 80<br>USD 100<br>USD 150<br>USD 200<br>USD 300</td><td>USD 30<br>USD 35<br>USD 50<br>USD 70<br>USD 100</td></tr>
          <tr><td>Fishing rigs (paragraph 2(b) of the definition of a commercial waterborne vessel in the 26th Schedule)</td><td>USD 250</td><td>USD 85</td></tr>
          <tr><td>Beauty and massage parlours</td><td>—</td><td>USD 100</td></tr>
          <tr><td>Gyms or fitness centres</td><td>—</td><td>USD 100</td></tr>
          <tr><td>Butcheries</td><td>—</td><td>USD 50</td></tr>
        </tbody>
      </table></div>
    """
    bodies = {
        "vat-on-imported-services": vat,
        "non-resident-shareholders-tax": nrst,
        "finance-act-2024": finance,
    }
    for post in POSTS:
        main = article_shell(post["title"], post["date"], post["image"], bodies[post["slug"]])
        page(
            f"insights/{post['slug']}/index.html",
            post["title"].rstrip("."),
            post["excerpt"],
            "insights",
            main,
        )


def not_found():
    main = f"""<main id="main">
<section class="section">
  <div class="container prose">
    <p class="eyebrow">404</p>
    <h2>That page is not on this site.</h2>
    <p>The link may have changed. The services, the journal, and the contact form are all still here.</p>
    <p style="margin-top:22px"><a class="btn btn-navy" href="/">Back to the homepage</a></p>
  </div>
</section>
</main>"""
    page("404.html", "Page not found", "The page you requested is not available on the ABS Consult site.", "", main)


def extras():
    (ROOT / "_redirects").write_text("""/tax-consulting /consulting/ 301
/tax-consulting/ /consulting/ 301
/tax-planning /planning/ 301
/tax-planning/ /planning/ 301
/tax-compliance /compliance/ 301
/tax-compliance/ /compliance/ 301
/contact-us /contact/ 301
/contact-us/ /contact/ 301
/about-us /about/ 301
/about-us/ /about/ 301
/633-2 /insights/vat-on-imported-services/ 301
/633-2/ /insights/vat-on-imported-services/ 301
/non-resident-shareholders-tax-nrst-treatment-in-zimbabwe /insights/non-resident-shareholders-tax/ 301
/non-resident-shareholders-tax-nrst-treatment-in-zimbabwe/ /insights/non-resident-shareholders-tax/ 301
/unraveling-the-finance-act-of-2024 /insights/finance-act-2024/ 301
/unraveling-the-finance-act-of-2024/ /insights/finance-act-2024/ 301
""")
    (ROOT / "_headers").write_text("""/*
  X-Frame-Options: SAMEORIGIN
  X-Content-Type-Options: nosniff
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()

/assets/*
  Cache-Control: public, max-age=604800
""")
    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\n")
    (ROOT / ".gitignore").write_text(".DS_Store\n.src/\n.tmp-home.html\n")
    (ROOT / "wrangler.toml").write_text("""name = "abs-consult"
pages_build_output_dir = "."
compatibility_date = "2026-11-17"
""")


if __name__ == "__main__":
    home()
    consulting()
    planning()
    compliance()
    secretarial()
    about()
    contact()
    insights()
    articles()
    not_found()
    extras()
