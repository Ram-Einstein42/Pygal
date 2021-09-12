from die import Die
import pygal

die = Die()
die2 = Die()

# roll and store in list
results = []
for roll_num in range(1000):
    result = die.roll() + die2.roll()
    results.append(result)

# analyze results
frequencies = []
max_result = die.num_sides + die2.num_sides

for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)


# visual results


hist = pygal.Bar()

hist.title = "Result Of Rolling 2 Dice 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6x2',frequencies)
hist.render_to_file('die_visual.svg')
