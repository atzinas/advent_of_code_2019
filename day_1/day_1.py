def fuel(mass):
    fuel_mass = mass // 3 - 2
    if fuel_mass <= 0:
        return 0
    return fuel_mass + fuel(fuel_mass)

with open("in.txt", "r") as f:
    components = f.read().splitlines()

components = map(int, components)
fuel_per_component = map(fuel, components)

print(sum(fuel_per_component))
