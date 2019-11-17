"""question 5:"""

"""
part 1:
the values for tenant 1: [75, 150].
the value for tenant 2: [100, 125].
the total rent to pay is 100.
there are only 2 valid room allocations: tenant 1 gets room A and tenant 2 gets room B or vice versa.
the value of the first allocation is 75+125=200.
the value of the second allocation is 150+100=250.
we therefore select the second allocation = tenant 1 gets room B, valued as 150, and tenant 2 gets room A, valued as 100.
for an egalitarian pricing vector, all tenants must have the same utility - otherwise we could lower the rent of the one with the least utility and raise that of the one with the most utility.
for the egalitarian pricing vector, therefore, is [75,25] - the utility of tenant 1 is 150-75=75 and that of tenant 2 is 100-25=75.
a non egalitarian pricing vector is, for example, [100,0] - the utility of tenant 1 is 150-100=50<75, while that of tenant 2 is 100-0=100.
"""

def egalitarianPricing(values, totalRent):
    """values[i] is the value of agent i's room"""
    """
    the algorithm is based around a basic principle:
    for an egalitarian pricing vector, all agents must have the same utility.
    we already know what the total utility is - the sum of all of the room values minus the total rent to pay.
    therefore, we can get the utility that each agent is supposed to get - the final utility divided by the amount of agents.
    the prices then all become the exact price to achieve that utility - the current room value minus the final utility.
    """
    finalUtility = float(sum(values)-totalRent)/len(values)
    return [(value-finalUtility) for value in values]
