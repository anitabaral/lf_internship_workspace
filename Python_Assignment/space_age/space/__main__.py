
# class SpaceAge:
#
#     def __init__(self):
#         seconds = 0
#         planet = ''

def take_input():
    seconds = int(input('Enter the value of your age in earth(years): '))
    planet = input('Enter the name of the planet where you want to know your age: ')
    print('Calculating your age in {}............ '.format(planet))
    return (planet, seconds)

def calculation():
    planet, seconds = take_input()
        # return round(seconds/(60 * 60 * 24 * 365.25 * factor), 2)
    if planet == 'earth':
        return (round(seconds/(1), 2), planet)
    if planet == 'mercury':
        return (round(seconds/(0.2408467), 2), planet)
    if planet == 'venus':
        return (round(seconds/(0.61519726), 2), planet)
    if planet == 'mars':
        return (round(seconds/(1.8808158), 2), planet)
    if planet == 'jupiter':
        return (round(seconds/(11.862615), 2), planet)
    if planet == 'saturn':
        return (round(seconds/(29.447498), 2), planet)
    if planet == 'uranus':
        return (round(seconds/(84.016846), 2), planet)
    if planet == 'neptune':
        return (round(seconds/(164.79132), 2), planet)

def main():
    age, planet = calculation()
    print('Your age in {} is {} years.'.format(planet, age))

if __name__=="__main__":
    main()
