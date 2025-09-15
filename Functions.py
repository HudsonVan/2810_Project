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

def tiered(tiers, usage, fixed_fee):
    total_cost = fixed_fee
    remaining = usage
    previous_threshold = 0

    print(f"\nUsage: {usage} kWh")
    print(f"Fixed fee: ${fixed_fee:.2f}")

    for threshold, rate in tiers:
        # how much fits in this tier
        tier_usage = min(remaining, threshold - previous_threshold)
        cost = tier_usage * rate
        total_cost += cost
        
        #Print if not 0, otherwise prints final tier at 0 and looks gross
        if tier_usage > 0:
            print(f"{tier_usage} kWh @ ${rate:.2f}/kWh = ${cost:.2f}")

        remaining -= tier_usage
        previous_threshold = threshold

        if remaining <= 0:
            break

    #If still usage left
    if remaining > 0:
        last_rate = tiers[-1][1]  #Use last tiers rate
        cost = remaining * last_rate
        total_cost += cost
        print(f"{remaining} kWh @ ${last_rate:.2f}/kWh = ${cost:.2f}")

    print(f"Total bill = ${total_cost:.2f}")
    return total_cost
    

def tariffCompare(bills_dict):
    cheapest_tariff = min(bills_dict, key=bills_dict.get)
    cheapest_bill = bills_dict[cheapest_tariff]
    return cheapest_tariff, cheapest_bill
