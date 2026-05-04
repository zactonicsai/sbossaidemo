# Sample Files for AI Business Guide — Manual Demos

These are realistic (but fictional) sample files designed to be uploaded into Claude.ai when running the **"Do it manually with Claude"** demos in the AI Business Guide. Each file matches a specific upload requirement in one or more use cases.

## How to use these

1. Open the AI Business Guide HTML page in your browser
2. Navigate to a use case (e.g., **Retail → Smart Inventory Tracking**)
3. Switch to the **"Do it manually with Claude"** tab
4. Open [claude.ai](https://claude.ai) in another tab
5. Upload the matching file from this folder
6. Copy the prompt from the guide, paste it into Claude, and send

---

## File-to-Use-Case Map

### 🛍️ Retail & E-commerce

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `retail-sales-90days.csv` | Smart Inventory Tracking · Sales Forecasting | 90 days of sales for a women's boutique. 30 SKUs across Tops, Outerwear, Bottoms, Dresses, Accessories, and Shoes. Includes realistic patterns: weekend bumps, trending-up items (Wrap Sweater), trending-down (Linen Shorts), a "dog" (Pleated Mini Skirt), a slow performer, and a new arrival from the last 30 days. Claude will find these patterns. |
| `ecommerce-order-history.csv` | Product Recommendations | 120 days of orders for a fitness/wellness e-commerce store. ~3,900 line items across 25 products. Has built-in pairings — yoga mats with blocks/straps, leggings with sports bras, protein with pre-workout — that Claude should detect as "frequently bought together." |

### 🍽️ Restaurants & Cafes

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `restaurant-menu-sales.csv` | Menu Optimization | 30 days of item-level sales for an Italian restaurant. 25 menu items with sale price AND food cost. Designed so Claude can correctly classify items into the menu engineering quadrants: stars (Margherita Pizza, Cacio e Pepe), plowhorses (Branzino, Osso Buco — popular but expensive ingredients), puzzles (Truffle Pizza, Mushroom Bruschetta — high margin but unloved), and dogs (Caprese Sandwich, Soup of the Day). |
| `restaurant-covers-1year.csv` | Demand Prediction | 365 days of daily covers for the same restaurant. Includes day-of-week patterns, seasonal effects, weather, and major holiday spikes (Mother's Day, Valentine's, NYE) and dips (Christmas Day, Thanksgiving). |
| `bakery-faq.md` | Customer Service Chatbot | A complete FAQ for a small bakery — hours, custom cake policy, allergens, payment, returns, etc. Use this to test how Claude would behave as a chatbot answering customer questions. |

### 💼 Professional Services (Consulting · Legal · Accounting)

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `legal-client-intake-email.txt` | Client Intake & Onboarding | A long, emotional client email from a freelance graphic designer who wasn't paid the final 40% on a $48K project. Has factual details, multiple legal questions, and signals about the client's financial pressure. Claude should produce a clean intake summary, key facts list, action plan, and draft welcome email. |
| `service-agreement-contract.md` | Contract & Document Review | A 13-section professional services agreement between a marketing agency and a real estate firm. Loaded with clauses worth flagging: 90-day non-renewal window, automatic 8% annual price increase, 7.5% surcharge on ad spend, $8,500 non-refundable setup fee, 50% early termination fee with 180-day notice, 24-month non-solicit, IP held until full payment, 3-month liability cap, mandatory arbitration in Delaware, class-action waiver. Lots for Claude to find. |
| `board-meeting-transcript.txt` | Meeting Notes & Summaries | A 47-minute Q3 strategy meeting transcript for a small coffee roastery. Four attendees, several decisions made, multiple action items with deadlines, some open questions. Tests Claude's ability to extract structure from prose. |

### 🔧 Cleaning, Handyman & Trades

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `handyman-lead-inquiry.txt` | Lead Follow-up · AI-Powered Quoting | An inbound customer email listing 6 different small jobs (drywall repair, cabinet hinges, sagging gate, ceiling fan, floating shelf, plus "maybe other things"). Customer has questions about pricing, scheduling, materials, and dog. Tests Claude's ability to ballpark a multi-item quote and draft a personalized first-reply. |

### 💇 Salons, Gyms & Fitness Studios

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `salon-client-list.csv` | Personalized Offers · Client Retention | 200 clients with first/last visit dates, total visits, lifetime spend, most-common service, preferred stylist. Pre-segmented behavior: VIPs, regulars, occasional, lapsed, and new. Claude should rebuild these segments and propose tailored offers. |
| `salon-appointment-history.csv` | No-Show Prediction | ~1,200 appointments over 6 months with showed/no-show/late-cancel outcomes. Built-in patterns Claude should find: 25 chronic no-show clients, last-minute bookings (1-day-ahead) no-show ~80% more often, Mondays are worse, lunch-hour slots are slightly worse. |

### 🚗 Auto Repair & Service

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `auto-shop-customer-list.csv` | Service Reminders | 100 customers with vehicle make/model/year/mileage, last service type, last service date, recommended interval, and next-due date. Mix of overdue (~20%), due-soon (~30%), on-time, and recently serviced. Lifetime spend included. Claude should identify who's due and draft personal reminder texts. |

### 🏠 Real Estate

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `property-listing-info.md` | AI Property Listings | A complete listing prep doc for a 4BR/3.5BA Asheville home. Specs, recent renovations, layout, outdoor features, smart-home upgrades, location, schools, owner's notes (sensitive — for the agent only). Claude should write the MLS description (fair-housing compliant), social posts, email blurb, and open-house promos. |
| `service-agreement-contract.md` | Contract & Document Review | Reuse this same contract — works for any contract review demo. |

### 🩺 Healthcare & Dental Practices

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `legal-client-intake-email.txt` | Client Intake | The intake demo works the same way for healthcare. Replace "law firm" with "practice" in the prompt and Claude will adapt. |
| `bakery-faq.md` | Chatbot test | Replace the FAQ with your practice's policies and the same prompt works. |

### 🎓 Education & Tutoring

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `student-essay-with-rubric.md` | Student Feedback & Grading | A 10th-grade argumentative essay on financial literacy education, with intentional small errors (its/it's, "alot", "to crowded", "shouldnt", run-ons). Rubric included with 4 categories. Notes for the grader specify the student is sensitive to critique — a great test of Claude's tone-management. |

### 📣 Marketing & Creative Agencies

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `past-marketing-emails.md` | AI Email Marketing · Social Media Content | 5 past emails from a small tea shop — distinct, lower-case, anti-corporate voice. Includes performance data and detailed voice notes. Use as the upload before asking Claude to draft new emails or social posts that "sound like us." |

### 🏗️ Construction & Contractors

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `handyman-lead-inquiry.txt` | Lead Follow-up · Quoting | The handyman lead works equally well for general contractors and remodelers. |

### 🧑‍💻 Freelancers & Solo Operators

| File | Matching Use Case(s) | What It Contains |
|------|----------------------|-------------------|
| `legal-client-intake-email.txt` | Client Intake | The legal intake demo is also a great template for any solo professional. |
| `past-marketing-emails.md` | Email Marketing | Voice samples work for any solopreneur. |
| `board-meeting-transcript.txt` | Meeting Notes | Even solo operators have client meetings — this works just the same. |

---

## Quick Start: Five Demos Worth Running First

If you only have 30 minutes to play with the guide, try these in order. Each takes ~5 minutes.

1. **Inventory analysis** — Upload `retail-sales-90days.csv`, run the inventory prompt. Watch Claude rank your bestsellers and flag the trending-up Wrap Sweater.
2. **Menu engineering** — Upload `restaurant-menu-sales.csv`, run the menu optimization prompt. Claude will correctly call out the Truffle Pizza as a "Puzzle" — high margin but underperforming.
3. **Contract review** — Upload `service-agreement-contract.md`, run the contract review prompt. Watch Claude flag the 8% annual increase, the 50% early termination fee, and the 24-month non-solicit.
4. **Meeting notes** — Upload `board-meeting-transcript.txt`, run the meeting summary prompt. Claude will produce action items with owners and deadlines.
5. **Property listing** — Upload `property-listing-info.md`, run the listings prompt. Claude will write a fair-housing-compliant MLS description plus 3 social variants.

---

## Notes

- **All names, addresses, and details are fictional.** Don't try to email anyone in these files.
- **CSVs use `\r\n` line endings** — they should open cleanly in Excel, Google Sheets, Numbers, or any text editor.
- **Markdown files render best on GitHub** but are also readable as plain text.
- **You can edit these freely** — change a name to your business, a product to one you sell, an address to your city. Localized examples make the demo more compelling.
- **The patterns are real but not the data.** Each CSV was generated programmatically with realistic patterns built in (weekend bumps, seasonality, no-show predictors, etc.) so Claude can find meaningful insights — not random noise.

## File generation

All CSVs were generated with `_generate.py` in this directory. You can re-run it (`python3 _generate.py`) to regenerate with different random seeds, more rows, or different products. The script is well-commented and easy to adapt for your real business.
