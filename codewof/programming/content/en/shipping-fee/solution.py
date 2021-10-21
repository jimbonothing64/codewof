def shipping(individual_costs):
    if individual_costs == []:
        return 0.00
    else:
        return max(individual_costs) + 2.50 * (len(individual_costs) - 1)


print(shipping([2.50, 5.00, 3.90]))
print(shipping([2.50, 5.00, 3.90, 10.00]))
print(shipping([]))
