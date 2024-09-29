import math
from config import *

def lcg():
	global r_state
	
	# Generate a random number based on a seed
	r_state = (r_state * 1103515245 + 12345) % (2**31);
	return (r_state >> 16)/(2**15)

def initial_straits():
	straits = {}
	for strait in base_straits:
		# Calculate the straits characteristics
		chance = strait["rate"] + lcg() * 0.1 - 0.05
		traversals = round(lcg() * 10 + 6)
		successes = math.floor(traversals * strait["rate"] + lcg() * 0.3 - 0.15)

		straits[strait["name"]] = {
			"name": strait["name"],
			"chance": chance,
			"traversals": traversals,
			"successes": successes
		}

	return straits

def create_shipment(straits):
	# Choose which strait the shipments pass through
	strait_name = base_straits[math.floor(lcg() * len(base_straits))]["name"]
	strait = straits[strait_name]
	
	# Calculate fair payoff
	payoff_p = strait["chance"] + lcg() * 0.2 - 0.15
	almost_fair_odds = (1 - payoff_p) / payoff_p

	return {
		"strait": strait_name,
		"odds": almost_fair_odds
	}

def full_kelly(phat, odds, wealth):
	kelly = phat - (1 - phat) / odds
	return round(wealth * kelly)

def investment_options(wealth, shipment, straits):
    global base_straits
    
    options = []

    # Small bet.
    if wealth < 100:
        small = 1
    elif wealth < 1000:
        small = 10
    else:
        small = 100
    options.append(small)

    # Push two uniformly distributed random investment levels.
    for _ in range(2):
        options.append(math.floor(lcg() * (wealth - small) + small))

    # Going for broke.
    options.append(wealth)

    # Use for the Kelly computation the harmonic mean of the observed rate and the base rate for the strait.
    base_rate = next(s['rate'] for s in base_straits if s['name'] == shipment['strait'])
    strait = straits[shipment['strait']]
    adj_p = 2 / (strait['traversals'] / strait['successes'] + 1 / base_rate)
    kelly = full_kelly(adj_p, shipment['odds'], wealth)

    if kelly > wealth - 0.95:
        options.append(math.floor(kelly * 0.9))
    elif kelly > small * 2:
        # If any bet is close to Kelly, remove it so it is replaced with Kelly.
        for i in range(len(options)):
            lk = math.log(kelly)
            lo = math.log(options[i])
            if lo - 0.1 < lk < lo + 0.1:
                options[i] = None
        
        options = [opt for opt in options if opt is not None]
        options.append(kelly)

    return sorted(options)

def investment_result(amount, value, straits, strait, wealth):
	win = lcg() <= straits[strait["name"]]["chance"]
	nextWealth = max(0, wealth - amount + win * value)

	# Adjust traversals and successes for straits
	straits[strait["name"]]["traversals"] += 1
	straits[strait["name"]]["successes"] += win

	return nextWealth, straits