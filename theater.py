def calculate_ticket_revenue(show_type, tickets_sold, time_slot):
    price = 0
    if show_type =="blukbuster":
        if time_slot == "morning":
            price = 12
        elif time_slot == "afternoon":
            price = 18
        elif time_slot == "evening":
            price = 25
        else:
            price= 0
    elif show_type == "standard":
        if time_slot == "morning":
           price = 8
        elif time_slot == "afternoon":
            price = 12
        elif time_slot == "evening":
            price = 16
        else :
            price = 0
    elif show_type == "classic":
        if time_slot == "morning":
            price = 5
        elif time_slot == "afternoon":
            price =  8
        elif time_slot == "evening":
            price = 10
        else:
            price = 0
    ticket_prices  = price * tickets_sold
    return ticket_prices
def calculate_occupancy_rate(theater_years, baseline_seats, filled_seats):
    expected_capacity = 1000+(theater_years * 100)
    seat_availability = expected_capacity - baseline_seats
    occupancy_percent = ((filled_seats-baseline_seats)/ seat_availability)* 100
    return round(occupancy_percent, 1)
def determine_popularity_status(occupancy_percent):
    if occupancy_percent < 50:
        return "Low Demand"
    elif 50 <= occupancy_percent < 60:
        return "Moderate Demand"
    elif 60<= occupancy_percent < 70:
        return "Good Demand"
    elif 70 <= occupancy_percent < 85:
        return "High Demand"
    else:
        return "Sold Out Status"
        return "high demand"
def calculate_total_profit(revenue, tickets,status_multiplier): # status-multiplier = 'low' or 'moderate'
    # calculate base profit
    # if-elif-else where you check status multipliers
    # when you find current status multiplier, then multiply base profit by this status multiplier
#      occupancy_percent = tickets / status_multiplier
#      profit = revenue * (occupancy_percent/100)*0.4
#      return round(profit, 1)
    base_profit = revenue* 0.05 + tickets *2
    if status_multiplier == 'Low':
       return base_profit * 0.5
    elif status_multiplier == 'moderate':
       return base_profit * 1
    elif status_multiplier =='good':
       return base_profit * 1.2
    elif status_multiplier == 'high':
       return base_profit * 1.5
    elif status_multiplier == 'sold out':
       return base_profit * 1.8
def needs_prommotion(screening_days, total_tickets, avg_occupancy):
     if screening_days >=6 and avg_occupancy < 50:
         return True
     if total_tickets < 100 and avg_occupancy < 60:
         return True
     if screening_days >= 4 and avg_occupancy < 40:
         return True
     return False
def generate_theater_report(movie_title, show_type, tickets, time_slot, theater_years, baseline_seats, filled_seats, screening_days):
    revenue=calculate_ticket_revenue(show_type, tickets, time_slot)
    occupancy=calculate_occupancy_rate(theater_years, baseline_seats, filled_seats ) 
    popularity = determine_popularity_status(occupancy)
# status multiplier based on popularity
    multipliers = {"Low Demand": 0.5, "Moderate Demand": 1.0, "Good Demand":1.2, "High Demand":1.5, "Sold Out Status": 1.8}
    profit=calculate_total_profit(revenue, tickets, multipliers[popularity]) 
    promo_needed=needs_prommotion(screening_days, tickets, occupancy)
    print(f'='*40)
    print(f"Theater Report for:{movie_title}")
    print(f"-"*40)
    print(f"Show Type: {show_type}")
    print(f"Tickets Sold: {tickets}")
    print(f"Time Slot: {time_slot}")
    print(f"Ticket Revenue:$ {revenue}")
    print(f"Occupancy Analysis:")
    print(f"Experience: {theater_years} years, Baseline: {baseline_seats}, Filled Seats: {filled_seats}")
    print(f"Occupancy: {occupancy}%")
    print(f"Popularity Status:{popularity}")
    print(f"Total Profit: $ {profit}")
    print(f"Screening Days:{screening_days}")
    print(f"Promotion Needed: {'Yes'if promo_needed else 'No'}")
    print("MOVIE THEATER MANAGMENT SYSTEM")
    print("======================================")
generate_theater_report("Space Adventure", "blukbuster", 45, "evening", 3,800, 1150, 3)
generate_theater_report("Comedy Night", "standard", 60, "afternoon", 5, 900, 1300, 5)
generate_theater_report("Old Classic", "classic", 30, "morning", 8, 850, 950,7)
