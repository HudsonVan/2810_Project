def flatRate(useage, rate):
    """
    User can input the flat rate value (e.g., $0.25/kWh).
    The system multiplies the total kWh consumed in the billing period by the flat rate.
    A fixed monthly supply fee (if specified) should also be included.
    """
    total = useage * rate
    
    return {"Flat-Rate" : total}

def TOU():
    """"
    User must define the time periods and their rates (e.g., Peak 6pm–10pm $0.40/kWh, Off-Peak 10pm–7am $0.15/kWh, Shoulder all other times $0.25/kWh).
    The system should parse each usage record’s timestamp and apply the correct rate.
    The bill should show a breakdown by tariff category (Peak/Off-Peak/Shoulder).
    """
    total = 0
    return {"Time-of-Use" : total}

def Tiered():
    """
    User defines tier thresholds and rates (e.g., Tier 1: first 100 kWh $0.20, Tier 2: 101–300 kWh $0.30, Tier 3: above 300 kWh $0.40).
    The system calculates cost progressively across tiers.
    The bill should show how much consumption fell into each tier.
    """
    total = 0
    return {"Tiered" : total}

def tariffCompare(bills_dict):
    cheapest_tariff = min(bills_dict, key=bills_dict.get)
    cheapest_bill = bills_dict[cheapest_tariff]
    return cheapest_tariff, cheapest_bill