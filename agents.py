from game import full_kelly

# Model different kinds of agents that play the game
def kelly_agent(options, shipment, wealth, straits):
	probability = straits[shipment["strait"]]["successes"] / straits[shipment["strait"]]["traversals"]
	kelly = full_kelly(probability, shipment["odds"], wealth)
	# Get option closest to kelly bet
	return min(enumerate(options), key=lambda x: abs(x[1] - kelly))[0]

def greedy_agent(options, shipment, wealth, straits):
	return len(options) - 1

def cautious_agent(options, shipment, wealth, straits):
	return 0

def median_agent(options, shipment, wealth, straits):
	return len(options) // 2