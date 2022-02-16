import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushroom', 'green peppers', 'extra cheese')

# module_name.name of the function()
# if you want to import a specific function from a module you use the following
# syntax : from module_name import function_name

from pizza import make_pizza

pizza.make_pizza(16, 'mushrooms', 'sweetcorn', 'tomato', 'tuna')
pizza.make_pizza(12, ' red pepper', 'sweetcorn', 'extra cheese', 'beef')

# You can give a function from a given module a nick name using mp()
# This can be done by using the following syntax
# from module_name import function_name as mp()

from pizza import make_pizza as mp

mp(21, 'cheese', 'beef', 'chicken', 'smoke ham')
mp(17, 'beef', 'sweetcorn', 'tuna', 'tomato')

# using the syntax above the function make_pizza from the module: pizza is convert to mp().
# now the function make_pizza can be substitute for mp() when called upon.

import pizza as p

p.make_pizza(12, 'extra cheese', 'onion', 'fresh garlic', 'green pepper', 'tuna')
p.make_pizza(13, 'smoked chicken', 'tomatoes', 'black olives', 'pepperoni')

# if you a * when importing a module, it will import all the function within the module
# Using this approach means you no longer need to use the dot notation

from pizza import *

make_pizza(21, 'beef', 'extra cheese', 'mushrooms', 'onion')
make_pizza(15, 'sweetcorn', 'no cheese', 'thai chicken')
