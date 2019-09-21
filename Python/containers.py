### You can buy custom containers from a manufacturing company. They are expensive, but the manufacturer agrees to let you return
### a certain number of them for a new container. Assume that purchasing the containers is the only job you need to do. 
### Maximize the number of containers purchased.
### Input: amount_to_spend, cost_of_container, bonus_container_cost[in number of containers]
### Output: Total number of containers purchased.
### Perform this operation for n number of scenarios, wherein each scenario defines the input differently.

def handle_input(scenario):
    values = scenario.split(' ')
    currency = int(values[0])
    cost = int(values[1])
    bonus = int(values[2])

    return currency, cost, bonus

def containers(scenarios):
    for scenario in scenarios:

        currency, cost, bonus = handle_input(scenario)

        containers_bought = currency // cost ## Buy the initial boxes.
        containers_possessed = containers_bought

        while containers_possessed // bonus != 0:
            bought = containers_possessed // bonus
            containers_possessed -= (bought * bonus)
            containers_bought += bought
            containers_possessed += bought
        print(containers_bought)
    
if __name__ == "__main__":
    scenarios = ['6 2 2', '10 2 5']
    containers(scenarios)
        
