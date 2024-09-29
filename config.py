# Random number generator's seed
global rstate
r_state = 1

# Set the different straits characteristics
base_straits = [
	# Malacca, rate: 0.65–0.75. Fair odds: 0.33–0.54.
	{ "name": 'Malacca', "rate": 0.7, "odds_low": 0.4, "odds_high": 0.7, },
	# Bering, rate: 0.45–0.55. Fair odds: 0.82–1.22.
	{ "name": 'Bering', "rate": 0.50, "odds_low": 0.8, "odds_high": 1.6, },
	# Gibraltar, rate: 0.89–0.99. Fair odds: 0.01–0.12.
	{ "name": 'Gibraltar', "rate": 0.94, "odds_low": 0, "odds_high": 0.2, },
]