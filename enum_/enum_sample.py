#!/usr/bin/env python

from enum import Enum

class TaskState(Enum):
    NOT_STARTED = 1
    ON_GOING = 2
    DONE = 3

def check_state(state):
    if state == TaskState.NOT_STARTED:
        print(f'Task: Not started. {state}')
    elif state == TaskState.ON_GOING:
        print(f'Task: On-going. {state}')
    elif state == TaskState.DONE:
        print(f'Task: one. {state}')
    else:
        print(f'Out of definition')

def check_enum_behavior():
    print(f'***{check_enum_behavior.__name__}')
    check_state(1)
    print(TaskState)
    print(TaskState(1))
    print(TaskState.NOT_STARTED == TaskState.ON_GOING)
    for state in TaskState:
        print(state)


if __name__ == '__main__':
    check_enum_behavior()
