from typing import List, Tuple

from utils.parser import get_input_as_list_of_strings


def main():
    filename = 'input.txt'

    instructions_as_strings = get_input_as_list_of_strings(filename)
    instructions = list(map(
        instruction_string_to_tuple, instructions_as_strings))
    accumulator_value = get_accumulator_value(instructions)
    print(f'The value in the accumulator before any instruction is executed a '
          f'second time: {accumulator_value}')


def instruction_string_to_tuple(instruction_string: str) -> Tuple[str, int]:
    instruction_type, instruction_value = instruction_string.split()
    return instruction_type, int(instruction_value)


def get_accumulator_value(instructions: List[Tuple[str, int]]) -> int:
    accumulator = 0
    idx = 0
    seen = set()
    while idx not in seen:
        seen.add(idx)
        instruction_type, instruction_value = instructions[idx]
        if instruction_type == 'jmp':
            idx += instruction_value
        elif instruction_type == 'acc':
            accumulator += instruction_value
            idx += 1
        else:  # if 'nop'
            idx += 1
    return accumulator


if __name__ == '__main__':
    main()
