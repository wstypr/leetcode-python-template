# pip install termcolor
# don't touch this
# it is for comparing the expected output of your solution
from solution import Solution
from termcolor import cprint
import testio

test_num = 0
header = f"==========  test {test_num} =========="
solution = Solution()

try:
    is_iterable = testio.inputs[0].__iter__()
except AttributeError:
    is_iterable = False

for input in testio.inputs:
    input_print = input
    output = solution.function(input)

    if is_iterable:
        if len(input) > 10:
            input_print = f"{input[:10]}".replace("]", "...]")

    print(header)
    print(f"input   : {input_print}")
    print(f"output  : {output}")
    print(f"expected: {testio.outputs[test_num]}")
    status = output == testio.outputs[test_num]
    background = "on_light_green" if status else "on_red"
    cprint(f"  {status}   ", "yellow", background, attrs=["bold"])
    test_num += 1
