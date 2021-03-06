def readInputs(file_name: str) -> list[int]:
    with open(file_name) as f:
        lineInput = f.readlines()
    return [int(x) for x in lineInput]


def do_we_have_a_twenty_twenty_pair(input_one: int, remaining_numbers: list[int]) -> tuple(bool, int):
    for x in remaining_numbers:
        if x + input_one == 2020:
            return True, x
    return False, None


# numbers=[1721, 979, 366, 299, 675, 1456]
numbers=readInputs("/Users/ciaran.whyte/dev/aoc2020/day1/input.txt")

found_result=False
for idx, num in enumerate(numbers):        
    for idx_two, num_two in enumerate(numbers[idx:]):
        match, paired_num = do_we_have_a_twenty_twenty_pair(num + num_two, numbers[idx_two:])
        if match:
            print(f"{num} + {num_two} + {paired_num} == 2020")
            print(f"{num} * {num_two} * {paired_num} == {num * num_two * paired_num}")
            found_result=True
            break
    if found_result:
        break
            
            

