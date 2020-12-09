from typing import List, Optional, Tuple

from utils.parser import get_input_as_list_of_strings


def main():
    filename = 'input.txt'

    instructions_as_strings = get_input_as_list_of_strings(filename)
    instructions = list(map(
        instruction_string_to_tuple, instructions_as_strings))
    accumulator_value, instruction_changed = get_accumulator_value(
        instructions)

    print(f'The value in the accumulator before any instruction is executed a '
          f'second time: {accumulator_value}')
    changed_from, instruction_changed_value = instructions[instruction_changed]
    changed_to = 'jmp' if changed_from == 'nop' else 'nop'
    print(f'(Instruction {instruction_changed} was changed from {changed_from}'
          f' {instruction_changed_value} to {changed_to} '
          f'{instruction_changed_value}.)')


def instruction_string_to_tuple(instruction_string: str) -> Tuple[str, int]:
    instruction_type, instruction_value = instruction_string.split()
    return instruction_type, int(instruction_value)


def get_accumulator_value(
        instructions: List[Tuple[str, int]]
) -> Optional[int]:
    idx = 0
    accumulator_value_at_idx = 0
    seen = set()
    while idx < len(instructions) and idx not in seen:
        seen.add(idx)
        instruction_type, instruction_value = instructions[idx]
        if instruction_type == 'acc':
            accumulator_value_at_idx += instruction_value
            idx += 1
            continue
        if instruction_type == 'jmp':
            start_idx = idx + 1
            idx += instruction_value
        else:  # if 'nop'
            start_idx = idx + instruction_value
            idx += 1
        program_terminated, accumulator_value = run_instructions_from_idx(
            instructions, start_idx, accumulator_value_at_idx)
        if program_terminated:
            return accumulator_value, idx
    return None


def run_instructions_from_idx(
        instructions: List[Tuple[str, int]],
        idx: int,
        accumulator: int
) -> Tuple[bool, int]:
    nbr_instructions = len(instructions)
    seen = set()
    while idx < nbr_instructions and idx not in seen:
        seen.add(idx)
        instruction_type, instruction_value = instructions[idx]
        if instruction_type == 'jmp':
            idx += instruction_value
        elif instruction_type == 'acc':
            accumulator += instruction_value
            idx += 1
        else:  # if 'nop'
            idx += 1
    program_terminated = idx == nbr_instructions
    return program_terminated, accumulator


if __name__ == '__main__':
    main()
