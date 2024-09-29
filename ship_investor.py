import game
import agents

def play(n, agent, initial_wealth = 100, debug = False):
	wealth = initial_wealth
	straits = game.initial_straits()

	wealths = [wealth]
	for _ in range(n):
		if debug:
			print("")
			print(f"Current wealth: {wealth}.")

		shipment = game.create_shipment(straits)
		options = game.investment_options(wealth, shipment, straits)
		
		if debug:
			print(f"Possible shipments to {shipment['strait']}: (traversed {straits[shipment['strait']]['traversals']} times, {round(straits[shipment['strait']]['successes'] / straits[shipment['strait']]['traversals'] * 100)} % success rate)")
			for o in options:
				print(f"Invest {o} ducats.")

		chosen_option = options[agent(options, shipment, wealth, straits)]
		value = round(chosen_option * (1 + shipment["odds"]))

		wealth, straits = game.investment_result(
			chosen_option,
			value,
			straits,
			straits[shipment["strait"]],
			wealth
		)
		wealths += [wealth]

	return wealths

if __name__ == "__main__":
	# Let the agent play N times
	N = 1000

	# The starting wealth
	initial_wealth = 100 # ducats

	play(N, agents.kelly_agent, initial_wealth=initial_wealth, debug=True)