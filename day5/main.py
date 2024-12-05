import os
from typing import Dict, Set, List


def split_topage_ordering_rules_and_update_instructions(data: str) -> List[str]:
    data = data.split("\n")
    index_of_split = data.index("")
    return data[:index_of_split], data[index_of_split + 1 :]


def yield_rules(page_ordering_rules: List[str]):
    for rule in page_ordering_rules:
        page_before, page_after = rule.split("|")
        yield int(page_before), int(page_after)


def prepere_ordering_rules(page_ordering_rules: List[str]) -> Dict[int, Set[int]]:
    rules = {}
    for page_before, page_after in yield_rules(page_ordering_rules):
        rules.setdefault(page_before, set())
        rules.get(page_before).add(page_after)
    return rules


def prepere_update_instructions(update_instructions: List[str]) -> List[List[int]]:
    return [
        [int(page_number) for page_number in line]
        for line in [line.split(",") for line in update_instructions]
    ]


def give_incorrect_update_information(
    page_ordering_rules: Dict[int, Set[int]], update_instructions: List[List[int]]
) -> List[List[int]]:
    incorrect_update_instructions = []
    for update_instruction in update_instructions:
        for idx, page_number in enumerate(update_instruction):
            before, page_number, after = (
                set(update_instruction[:idx]),
                page_number,
                set(update_instruction[idx + 1 :]),
            )
            if (
                len(before.intersection(page_ordering_rules.get(page_number, set())))
                > 0
            ):
                incorrect_update_instructions.append(update_instruction)
                break

    return incorrect_update_instructions


def give_correct_update_information(
    update_instructions: List[List[int]], incorrect_update_instructions: List[List[int]]
) -> List[List[int]]:
    return [
        instruction
        for instruction in update_instructions
        if instruction not in incorrect_update_instructions
    ]


def get_middle_page(page_ordering_rules: list[int]) -> int:
    return page_ordering_rules[len(page_ordering_rules) // 2]


def solution1(data: str) -> int:
    ordering_rules, update_instructions = (
        split_topage_ordering_rules_and_update_instructions(data)
    )
    ordering_rules = prepere_ordering_rules(ordering_rules)
    update_instructions = prepere_update_instructions(update_instructions)
    incorrect_update_instructions = give_incorrect_update_information(
        ordering_rules, update_instructions
    )
    correct_update_instructions = give_correct_update_information(
        update_instructions, incorrect_update_instructions
    )
    return sum(
        [get_middle_page(instruction) for instruction in correct_update_instructions]
    )


def fix_incorrect_update_instruction(
    page_ordering_rules: Dict[int, Set[int]], incorrect_update_instruction: List[int]
) -> List[int]:
    for idx, page_number in enumerate(incorrect_update_instruction):
        before, page_number, after = (
            set(incorrect_update_instruction[:idx]),
            page_number,
            set(incorrect_update_instruction[idx + 1 :]),
        )
        if len(before.intersection(page_ordering_rules.get(page_number, set()))) > 0:
            incorrect_set = before.intersection(
                page_ordering_rules.get(page_number, set())
            )
            incorrect_page = list(incorrect_set)[0]
            (
                incorrect_update_instruction[idx],
                incorrect_update_instruction[
                    incorrect_update_instruction.index(incorrect_page)
                ],
            ) = (incorrect_page, page_number)
            fix_incorrect_update_instruction(
                page_ordering_rules, incorrect_update_instruction
            )
    return incorrect_update_instruction


def fix_incorrect_update_instructions(
    page_ordering_rules: Dict[int, Set[int]],
    incorrect_update_instructions: List[List[int]],
) -> List[List[int]]:
    fixed_update_instructions = []
    for incorrect_update_instruction in incorrect_update_instructions:
        fixed_update_instruction = fix_incorrect_update_instruction(
            page_ordering_rules, incorrect_update_instruction
        )
        fixed_update_instructions.append(fixed_update_instruction)
    return fixed_update_instructions


def solution2(data: str) -> int:
    ordering_rules, update_instructions = (
        split_topage_ordering_rules_and_update_instructions(data)
    )
    ordering_rules = prepere_ordering_rules(ordering_rules)
    update_instructions = prepere_update_instructions(update_instructions)
    incorrect_update_instructions = give_incorrect_update_information(
        ordering_rules, update_instructions
    )
    correct_update_instructions = fix_incorrect_update_instructions(
        ordering_rules, incorrect_update_instructions
    )
    return sum(
        [get_middle_page(instruction) for instruction in correct_update_instructions]
    )


def main():
    files = os.listdir(os.path.dirname(__file__))
    solutions_data = []
    for file in files:
        if file.endswith(".aoc"):
            data = open(os.path.join(os.path.dirname(__file__), file)).read()
            solutions_data += "task1_" + file, solution1(data)
            solutions_data += "task2_" + file, solution2(data)

    return solutions_data


if __name__ == "__main__":
    # TODO Clean the code
    print(main())
