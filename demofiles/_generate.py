"""Generate realistic sample CSVs for the AI Business Guide manual demos."""
import csv
import random
from datetime import date, datetime, timedelta

random.seed(42)  # reproducible

OUT = "/home/claude/samples"

# =====================================================================
# 1. RETAIL SALES - 90 days, ~30 SKUs, women's boutique
# =====================================================================
def gen_retail_sales():
    skus = [
        # name, category, price, base_velocity (units/day), pattern
        ("Linen Blouse - White",       "Tops",       58, 2.8, "weekend"),
        ("Linen Blouse - Black",       "Tops",       58, 2.1, "weekend"),
        ("Cotton Tee - Cream",         "Tops",       28, 4.5, "steady"),
        ("Silk Camisole",              "Tops",       72, 0.8, "slow"),
        ("Wrap Sweater - Sage",        "Tops",       96, 1.2, "trending_up"),
        ("Wrap Sweater - Navy",        "Tops",       96, 0.9, "trending_up"),
        ("Vintage Denim Jacket",       "Outerwear", 145, 0.6, "weekend"),
        ("Wool Coat - Camel",          "Outerwear", 285, 0.4, "weekend"),
        ("Trench Coat",                "Outerwear", 220, 0.3, "weekend"),
        ("High-Waist Jeans",           "Bottoms",   118, 1.8, "weekend"),
        ("Wide-Leg Trousers",          "Bottoms",    98, 1.4, "trending_up"),
        ("Midi Skirt - Floral",        "Bottoms",    74, 1.1, "trending_down"),
        ("Linen Shorts",               "Bottoms",    52, 2.2, "trending_down"),
        ("Pleated Mini Skirt",         "Bottoms",    68, 0.4, "dog"),
        ("Slip Dress - Black",         "Dresses",   124, 1.3, "weekend"),
        ("Floral Maxi Dress",          "Dresses",   142, 1.7, "weekend"),
        ("Wrap Dress - Emerald",       "Dresses",   118, 0.7, "trending_up"),
        ("Cocktail Dress",             "Dresses",   168, 0.5, "weekend"),
        ("Leather Crossbody Bag",      "Accessories", 134, 1.5, "steady"),
        ("Canvas Tote",                "Accessories",  44, 3.2, "steady"),
        ("Silk Scarf",                 "Accessories",  38, 1.8, "steady"),
        ("Gold Hoop Earrings",         "Accessories",  32, 2.6, "steady"),
        ("Pearl Necklace",             "Accessories",  78, 0.9, "steady"),
        ("Wide-Brim Straw Hat",        "Accessories",  48, 1.4, "trending_down"),
        ("Cashmere Beanie",            "Accessories",  62, 0.3, "trending_up"),
        ("Leather Loafers - Black",    "Shoes",     168, 0.8, "trending_up"),
        ("Suede Ankle Boots",          "Shoes",     185, 0.5, "trending_up"),
        ("White Sneakers",             "Shoes",     128, 1.6, "steady"),
        ("Strappy Sandals",            "Shoes",      88, 1.3, "trending_down"),
        ("New Arrival: Cropped Cardigan", "Tops",    82, 2.1, "new"),  # only sells last 30 days
    ]

    rows = []
    today = date(2025, 4, 30)
    start = today - timedelta(days=89)  # 90 day window

    for day_offset in range(90):
        d = start + timedelta(days=day_offset)
        weekday = d.weekday()  # 0=Mon ... 6=Sun
        is_weekend = weekday >= 5

        # General store traffic noise
        traffic_mult = random.uniform(0.6, 1.4)
        if is_weekend:
            traffic_mult *= 1.6
        if weekday == 4:  # Friday
            traffic_mult *= 1.2
        if weekday == 0:  # Monday slow
            traffic_mult *= 0.7

        for name, cat, price, vel, pattern in skus:
            # Pattern adjustments
            mult = 1.0
            if pattern == "weekend" and is_weekend:
                mult = 1.8
            elif pattern == "weekend" and not is_weekend:
                mult = 0.6
            elif pattern == "trending_up":
                mult = 0.5 + (day_offset / 90) * 1.2  # 0.5 -> 1.7
            elif pattern == "trending_down":
                mult = 1.5 - (day_offset / 90) * 1.0  # 1.5 -> 0.5
            elif pattern == "slow":
                mult = 0.6
            elif pattern == "dog":
                mult = 0.2
            elif pattern == "new":
                if day_offset < 60:
                    mult = 0  # didn't exist yet
                else:
                    mult = (day_offset - 60) / 30 * 1.5  # ramp up

            expected = vel * traffic_mult * mult
            # Poisson-ish: round with some noise
            units = max(0, int(expected + random.gauss(0, expected * 0.3)))

            for _ in range(units):
                rows.append({
                    "date": d.isoformat(),
                    "sku": name,
                    "category": cat,
                    "unit_price": f"{price:.2f}",
                    "units_sold": 1,
                    "revenue": f"{price:.2f}",
                })

    # Aggregate per (date, sku)
    agg = {}
    for r in rows:
        k = (r["date"], r["sku"])
        if k not in agg:
            agg[k] = {**r, "units_sold": 0, "revenue": 0.0}
        agg[k]["units_sold"] += 1
        agg[k]["revenue"] += float(r["unit_price"])

    final = sorted(agg.values(), key=lambda x: (x["date"], x["sku"]))
    for f in final:
        f["revenue"] = f"{f['revenue']:.2f}"

    with open(f"{OUT}/retail-sales-90days.csv", "w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=["date", "sku", "category", "unit_price", "units_sold", "revenue"])
        w.writeheader()
        w.writerows(final)
    print(f"retail-sales-90days.csv: {len(final)} rows")

# =====================================================================
# 2. ECOMMERCE ORDERS - for product recommendations
# =====================================================================
def gen_ecommerce_orders():
    products = [
        "Yoga Mat - Cork",
        "Yoga Mat - Standard",
        "Yoga Block (pair)",
        "Yoga Strap",
        "Resistance Bands Set",
        "Foam Roller",
        "Massage Ball",
        "Water Bottle 32oz",
        "Workout Towel",
        "Gym Bag - Black",
        "Tank Top - Black",
        "Tank Top - Heather",
        "Leggings - Black",
        "Leggings - Olive",
        "Sports Bra",
        "Headband Set",
        "Wireless Earbuds",
        "Phone Armband",
        "Protein Powder - Vanilla",
        "Protein Powder - Chocolate",
        "Pre-Workout",
        "BCAA Powder",
        "Recovery Drink Mix",
        "Adjustable Dumbbells",
        "Kettlebell 20lb",
    ]

    # Common pairings (these will appear together more often)
    pairings = {
        "Yoga Mat - Cork":   ["Yoga Block (pair)", "Yoga Strap", "Workout Towel"],
        "Yoga Mat - Standard": ["Yoga Block (pair)", "Yoga Strap"],
        "Resistance Bands Set": ["Foam Roller", "Workout Towel"],
        "Leggings - Black":  ["Sports Bra", "Tank Top - Black"],
        "Leggings - Olive":  ["Sports Bra", "Tank Top - Heather"],
        "Protein Powder - Vanilla": ["Pre-Workout", "BCAA Powder", "Recovery Drink Mix"],
        "Protein Powder - Chocolate": ["Pre-Workout", "BCAA Powder"],
        "Adjustable Dumbbells": ["Workout Towel", "Water Bottle 32oz"],
        "Wireless Earbuds": ["Phone Armband", "Headband Set"],
    }
    prices = {p: round(random.uniform(15, 95), 2) for p in products}
    prices["Adjustable Dumbbells"] = 189.00
    prices["Yoga Mat - Cork"] = 78.00
    prices["Yoga Mat - Standard"] = 32.00
    prices["Wireless Earbuds"] = 64.99
    prices["Protein Powder - Vanilla"] = 42.00
    prices["Protein Powder - Chocolate"] = 42.00

    rows = []
    today = date(2025, 4, 30)
    order_id = 10001

    for d_offset in range(120):
        d = today - timedelta(days=119 - d_offset)
        n_orders = random.randint(8, 25)

        for _ in range(n_orders):
            customer_id = f"C{random.randint(1000, 1400):04d}"
            cart_size = random.choices([1, 2, 3, 4, 5], weights=[40, 30, 15, 10, 5])[0]

            # Pick the first item, then bias toward pairings
            seed = random.choice(products)
            cart = [seed]
            for _ in range(cart_size - 1):
                if seed in pairings and random.random() < 0.5:
                    pair_options = [p for p in pairings[seed] if p not in cart]
                    if pair_options:
                        cart.append(random.choice(pair_options))
                        continue
                # Otherwise random
                candidate = random.choice(products)
                if candidate not in cart:
                    cart.append(candidate)

            for item in cart:
                rows.append({
                    "order_id": f"O{order_id}",
                    "order_date": d.isoformat(),
                    "customer_id": customer_id,
                    "product": item,
                    "quantity": random.choices([1, 2, 3], weights=[80, 15, 5])[0],
                    "unit_price": f"{prices[item]:.2f}",
                })
            order_id += 1

    with open(f"{OUT}/ecommerce-order-history.csv", "w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=["order_id", "order_date", "customer_id", "product", "quantity", "unit_price"])
        w.writeheader()
        w.writerows(rows)
    print(f"ecommerce-order-history.csv: {len(rows)} rows")

# =====================================================================
# 3. RESTAURANT MENU SALES - 30 days, item-level with costs
# =====================================================================
def gen_restaurant_menu_sales():
    items = [
        # name, category, price, food_cost, base_qty_per_day, pattern
        ("Caesar Salad",        "Appetizer", 12.00, 2.80, 18, "steady"),
        ("Burrata & Tomato",    "Appetizer", 16.00, 5.20, 14, "trending_up"),
        ("Calamari Fritti",     "Appetizer", 14.00, 4.10, 9,  "steady"),
        ("Mushroom Bruschetta", "Appetizer", 11.00, 2.20, 4,  "puzzle"),  # high margin, low pop
        ("Soup of the Day",     "Appetizer",  8.00, 1.40, 3,  "dog"),
        ("Margherita Pizza",    "Entree",    18.00, 3.60, 32, "star"),
        ("Pepperoni Pizza",     "Entree",    20.00, 4.40, 28, "star"),
        ("Truffle Pizza",       "Entree",    28.00, 8.20, 8,  "puzzle"),
        ("Cacio e Pepe",        "Entree",    22.00, 3.80, 24, "star"),
        ("Spaghetti Carbonara", "Entree",    24.00, 5.10, 21, "steady"),
        ("Lasagna Bolognese",   "Entree",    26.00, 6.30, 18, "steady"),
        ("Mushroom Risotto",    "Entree",    25.00, 5.40, 11, "steady"),
        ("Branzino",            "Entree",    38.00, 14.20, 9, "plowhorse"),
        ("Osso Buco",           "Entree",    42.00, 16.80, 7, "plowhorse"),
        ("Veal Parmesan",       "Entree",    32.00, 9.20, 14, "steady"),
        ("Eggplant Parmesan",   "Entree",    22.00, 4.40, 6,  "trending_down"),
        ("Caprese Sandwich",    "Lunch",     14.00, 3.20, 5,  "dog"),
        ("Tiramisu",            "Dessert",    9.00, 1.80, 22, "star"),
        ("Cannoli (2pc)",       "Dessert",    8.00, 1.60, 12, "steady"),
        ("Panna Cotta",         "Dessert",    8.50, 1.40, 7,  "puzzle"),
        ("Gelato",              "Dessert",    7.00, 1.30, 16, "steady"),
        ("House Wine - Glass",  "Beverage",  11.00, 1.80, 38, "star"),
        ("Espresso",            "Beverage",   3.50, 0.40, 24, "steady"),
        ("Cappuccino",          "Beverage",   4.50, 0.55, 18, "steady"),
        ("San Pellegrino",      "Beverage",   5.00, 0.80, 11, "steady"),
    ]

    rows = []
    today = date(2025, 4, 30)
    start = today - timedelta(days=29)

    for d_offset in range(30):
        d = start + timedelta(days=d_offset)
        weekday = d.weekday()
        # busy: Fri Sat. medium: Wed Thu Sun. slow: Mon Tue
        day_mult = {0: 0.7, 1: 0.75, 2: 1.0, 3: 1.1, 4: 1.6, 5: 1.8, 6: 1.2}[weekday]
        weather_mult = random.uniform(0.85, 1.15)
        traffic = day_mult * weather_mult

        for name, cat, price, cost, base, pattern in items:
            mult = 1.0
            if pattern == "star":         mult = 1.0
            elif pattern == "plowhorse":  mult = 1.0
            elif pattern == "puzzle":     mult = 0.8
            elif pattern == "dog":        mult = 0.5
            elif pattern == "trending_up":   mult = 0.7 + (d_offset/30) * 0.7
            elif pattern == "trending_down": mult = 1.4 - (d_offset/30) * 0.8

            qty = max(0, int(base * traffic * mult + random.gauss(0, base * 0.18)))
            if qty == 0:
                continue
            rows.append({
                "date": d.isoformat(),
                "day_of_week": d.strftime("%A"),
                "item": name,
                "category": cat,
                "qty_sold": qty,
                "unit_price": f"{price:.2f}",
                "food_cost_per_unit": f"{cost:.2f}",
                "revenue": f"{qty * price:.2f}",
                "food_cost_total": f"{qty * cost:.2f}",
            })

    with open(f"{OUT}/restaurant-menu-sales.csv", "w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=[
            "date", "day_of_week", "item", "category",
            "qty_sold", "unit_price", "food_cost_per_unit", "revenue", "food_cost_total"
        ])
        w.writeheader()
        w.writerows(rows)
    print(f"restaurant-menu-sales.csv: {len(rows)} rows")

# =====================================================================
# 4. RESTAURANT DAILY COVERS - 365 days
# =====================================================================
def gen_restaurant_covers():
    rows = []
    today = date(2025, 4, 30)
    start = today - timedelta(days=364)

    holidays = {
        date(2024, 5, 12): ("Mother's Day", 1.7),
        date(2024, 6, 16): ("Father's Day", 1.4),
        date(2024, 7,  4): ("July 4th", 1.5),
        date(2024, 11, 28):("Thanksgiving", 0.6),  # closed-ish
        date(2024, 12, 24):("Christmas Eve", 1.3),
        date(2024, 12, 25):("Christmas Day", 0.2),
        date(2024, 12, 31):("New Year's Eve", 1.9),
        date(2025, 2, 14): ("Valentine's Day", 1.9),
        date(2025, 3, 17): ("St. Patrick's Day", 1.3),
    }

    weather_options = ["clear", "clear", "clear", "cloudy", "cloudy", "rain", "snow", "hot"]

    for d_offset in range(365):
        d = start + timedelta(days=d_offset)
        weekday = d.weekday()
        # base covers
        base = {0: 70, 1: 80, 2: 95, 3: 110, 4: 165, 5: 185, 6: 130}[weekday]
        # season effect
        month = d.month
        season_mult = {
            1: 0.85, 2: 0.95, 3: 1.0, 4: 1.05, 5: 1.1, 6: 1.05,
            7: 1.0, 8: 0.95, 9: 1.05, 10: 1.1, 11: 1.05, 12: 1.15
        }[month]

        weather = random.choice(weather_options)
        weather_mult = {"clear": 1.05, "cloudy": 1.0, "rain": 0.85, "snow": 0.65, "hot": 0.95}[weather]

        mult = season_mult * weather_mult
        notes = ""
        if d in holidays:
            name, h_mult = holidays[d]
            mult *= h_mult
            notes = name

        covers = max(0, int(base * mult + random.gauss(0, base * 0.08)))
        rows.append({
            "date": d.isoformat(),
            "day_of_week": d.strftime("%A"),
            "covers": covers,
            "weather": weather,
            "notes": notes,
        })

    with open(f"{OUT}/restaurant-covers-1year.csv", "w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=["date", "day_of_week", "covers", "weather", "notes"])
        w.writeheader()
        w.writerows(rows)
    print(f"restaurant-covers-1year.csv: {len(rows)} rows")

# =====================================================================
# 5. SALON CLIENT LIST - 200 clients
# =====================================================================
def gen_salon_clients():
    first_names = ["Emma", "Olivia", "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn",
                   "Abigail", "Ella", "Elizabeth", "Camila", "Luna", "Sofia", "Avery", "Mila",
                   "Aria", "Scarlett", "Penelope", "Layla", "Riley", "Nora", "Hazel", "Chloe",
                   "Liam", "Noah", "Oliver", "Ethan", "Mason", "James", "Daniel"]
    last_names = ["Smith", "Johnson", "Brown", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
                  "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor",
                  "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris",
                  "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young"]

    services = {
        "Haircut": 65,
        "Haircut + Color": 165,
        "Haircut + Highlights": 220,
        "Balayage": 280,
        "Blowout": 55,
        "Color Touch-up": 95,
        "Deep Conditioning": 45,
        "Keratin Treatment": 320,
        "Bridal Updo": 145,
    }

    rows = []
    today = date(2025, 4, 30)
    used_names = set()

    for cid in range(1001, 1201):  # 200 clients
        while True:
            name = f"{random.choice(first_names)} {random.choice(last_names)}"
            if name not in used_names:
                used_names.add(name)
                break

        # Decide segment
        segment = random.choices(
            ["VIP", "Regular", "Occasional", "Lapsed", "New"],
            weights=[15, 35, 25, 15, 10]
        )[0]

        if segment == "VIP":
            visits = random.randint(15, 30)
            last_visit_days_ago = random.randint(7, 35)
        elif segment == "Regular":
            visits = random.randint(6, 14)
            last_visit_days_ago = random.randint(15, 70)
        elif segment == "Occasional":
            visits = random.randint(3, 5)
            last_visit_days_ago = random.randint(40, 110)
        elif segment == "Lapsed":
            visits = random.randint(3, 12)
            last_visit_days_ago = random.randint(95, 280)
        else:  # New
            visits = random.randint(1, 2)
            last_visit_days_ago = random.randint(7, 60)

        # Generate spend/services pattern
        client_services = []
        total_spend = 0
        for _ in range(visits):
            svc = random.choice(list(services.keys()))
            client_services.append(svc)
            total_spend += services[svc]

        last_visit = today - timedelta(days=last_visit_days_ago)
        most_common_service = max(set(client_services), key=client_services.count)
        first_visit = today - timedelta(days=random.randint(last_visit_days_ago + 60, last_visit_days_ago + 730))

        rows.append({
            "client_id": f"C{cid}",
            "first_name": name.split()[0],
            "last_name": name.split()[1],
            "phone": f"555-{random.randint(100,999)}-{random.randint(1000,9999)}",
            "email": f"{name.split()[0].lower()}.{name.split()[1].lower()}@example.com",
            "first_visit": first_visit.isoformat(),
            "last_visit": last_visit.isoformat(),
            "total_visits": visits,
            "total_spend": f"{total_spend:.2f}",
            "avg_spend_per_visit": f"{total_spend/visits:.2f}",
            "most_common_service": most_common_service,
            "preferred_stylist": random.choice(["Maria", "Jasmine", "Ana", "Brittany", "Taylor"]),
        })

    with open(f"{OUT}/salon-client-list.csv", "w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"salon-client-list.csv: {len(rows)} rows")

# =====================================================================
# 6. SALON APPOINTMENT HISTORY - 6 months, ~800 appts, with no-shows
# =====================================================================
def gen_salon_appointments():
    today = date(2025, 4, 30)
    rows = []
    appt_id = 5001

    # Some clients are habitual no-shows
    no_show_clients = set([f"C{i}" for i in random.sample(range(1001, 1201), 25)])

    for d_offset in range(180):
        d = today - timedelta(days=180 - d_offset)
        weekday = d.weekday()
        # Sun closed
        if weekday == 6:
            continue
        n_appts = {0: 4, 1: 5, 2: 7, 3: 8, 4: 11, 5: 13}[weekday]

        for _ in range(n_appts):
            cid = f"C{random.randint(1001, 1200)}"
            booked_days_ago = random.choices([1, 2, 3, 7, 14, 21, 30], weights=[15, 15, 20, 25, 15, 7, 3])[0]
            booked_on = d - timedelta(days=booked_days_ago)
            if booked_on > today:
                booked_on = today
            time_slot = random.choice(["9:00 AM", "10:30 AM", "12:00 PM", "1:30 PM", "3:00 PM", "4:30 PM", "6:00 PM"])
            service = random.choice(["Haircut", "Color", "Highlights", "Balayage", "Blowout"])

            # No-show probability
            ns_prob = 0.05  # baseline 5%
            if cid in no_show_clients:
                ns_prob = 0.35
            if booked_days_ago == 1:
                ns_prob *= 1.8  # last-minute books no-show more
            if weekday == 0:  # Mondays
                ns_prob *= 1.3
            if time_slot in ["12:00 PM", "1:30 PM"]:
                ns_prob *= 1.2  # lunch hour

            outcome = "no-show" if random.random() < ns_prob else "showed"
            # Some late-cancels
            if outcome == "showed" and random.random() < 0.04:
                outcome = "late-cancel"

            rows.append({
                "appointment_id": f"A{appt_id}",
                "client_id": cid,
                "appointment_date": d.isoformat(),
                "day_of_week": d.strftime("%A"),
                "time_slot": time_slot,
                "service": service,
                "booked_on": booked_on.isoformat(),
                "days_booked_ahead": booked_days_ago,
                "outcome": outcome,
            })
            appt_id += 1

    with open(f"{OUT}/salon-appointment-history.csv", "w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"salon-appointment-history.csv: {len(rows)} rows")

# =====================================================================
# 7. AUTO SHOP CUSTOMER LIST - 100 customers, due/overdue/recent
# =====================================================================
def gen_auto_customers():
    first_names = ["Mike", "John", "David", "Robert", "Jennifer", "Lisa", "Michael", "Sarah",
                   "Chris", "Andrew", "Jessica", "Ashley", "Brian", "Kevin", "Amanda", "Daniel",
                   "Stephanie", "Brandon", "Rachel", "Eric", "Patricia", "Steven", "Nicole",
                   "Anthony", "Rebecca", "Mark", "Heather", "Paul", "Laura", "Matthew"]
    last_names = ["Anderson", "Thompson", "Wright", "Hill", "Green", "Adams", "Baker", "Nelson",
                  "Carter", "Mitchell", "Roberts", "Turner", "Phillips", "Campbell", "Parker",
                  "Evans", "Edwards", "Collins", "Stewart", "Morris", "Murphy", "Cook", "Rogers",
                  "Reed", "Bailey", "Cooper", "Peterson", "Howard", "Ward", "Foster"]

    vehicles = [
        ("Toyota", "Camry"), ("Toyota", "Corolla"), ("Toyota", "RAV4"), ("Honda", "Civic"),
        ("Honda", "Accord"), ("Honda", "CR-V"), ("Ford", "F-150"), ("Ford", "Explorer"),
        ("Chevrolet", "Silverado"), ("Chevrolet", "Equinox"), ("Nissan", "Altima"),
        ("Nissan", "Rogue"), ("Hyundai", "Sonata"), ("Hyundai", "Elantra"), ("Subaru", "Outback"),
        ("Mazda", "CX-5"), ("Jeep", "Grand Cherokee"), ("Jeep", "Wrangler"), ("Ram", "1500"),
        ("Volkswagen", "Jetta"), ("Lexus", "RX 350"), ("BMW", "X3"),
    ]

    services_freq_months = {
        "Oil Change": 4,
        "Tire Rotation": 6,
        "Brake Inspection": 12,
        "Air Filter": 12,
        "Transmission Fluid": 30,
        "Coolant Flush": 30,
        "Battery Check": 6,
        "Alignment": 12,
    }

    rows = []
    today = date(2025, 4, 30)

    for cid in range(2001, 2101):
        first = random.choice(first_names)
        last = random.choice(last_names)
        make, model = random.choice(vehicles)
        year = random.randint(2014, 2023)

        # Pick most recent service type and date
        last_service = random.choice(list(services_freq_months.keys()))
        freq = services_freq_months[last_service]
        # Distribute: some overdue, some on time, some recent
        bucket = random.choices(["overdue", "due_soon", "on_time", "recent"], weights=[20, 30, 30, 20])[0]
        if bucket == "overdue":
            # Last service was longer than freq ago
            days_ago = random.randint(int(freq * 30 * 1.2), int(freq * 30 * 1.8))
        elif bucket == "due_soon":
            days_ago = random.randint(int(freq * 30 * 0.85), int(freq * 30 * 1.05))
        elif bucket == "on_time":
            days_ago = random.randint(int(freq * 30 * 0.5), int(freq * 30 * 0.85))
        else:  # recent
            days_ago = random.randint(7, int(freq * 30 * 0.5))

        last_service_date = today - timedelta(days=days_ago)
        next_due_date = last_service_date + timedelta(days=freq * 30)
        mileage = random.randint(15000, 150000)

        rows.append({
            "customer_id": f"AC{cid}",
            "first_name": first,
            "last_name": last,
            "phone": f"555-{random.randint(100,999)}-{random.randint(1000,9999)}",
            "email": f"{first.lower()}.{last.lower()}@example.com",
            "vehicle_year": year,
            "vehicle_make": make,
            "vehicle_model": model,
            "vehicle_mileage": mileage,
            "last_service_type": last_service,
            "last_service_date": last_service_date.isoformat(),
            "service_interval_months": freq,
            "next_due_date": next_due_date.isoformat(),
            "lifetime_spend": f"{random.uniform(450, 8500):.2f}",
        })

    with open(f"{OUT}/auto-shop-customer-list.csv", "w", newline="") as fp:
        w = csv.DictWriter(fp, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"auto-shop-customer-list.csv: {len(rows)} rows")


if __name__ == "__main__":
    gen_retail_sales()
    gen_ecommerce_orders()
    gen_restaurant_menu_sales()
    gen_restaurant_covers()
    gen_salon_clients()
    gen_salon_appointments()
    gen_auto_customers()
    print("\nAll CSVs generated.")
