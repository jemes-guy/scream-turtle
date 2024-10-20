import turtle, random

why = input('What do you want to scream into the endless matrix? > ')
turtle.penup()
turtle.speed(0)
for alpha in range(50):
  turtle.goto(random.randint(-500, 500), random.randint(-500, 500))
  turtle.write("%s" % '_______________________________________________________________________________________________________________________________________________________________________________________________')
for beta in range(500):
  turtle.goto(random.randint(-768, 768), random.randint(-500, 500))
  turtle.write("%s" % '-          -     -                     -    - - - - - -')
for delta in range(1500):
  turtle.goto(random.randint(-768, 768), random.randint(-500, 500))
  turtle.write("%s" % why)
turtle.exitonclick()