"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ['100'],
            "answer": 0,
        },
        {
            "input": ['001'],
            "answer": 2,
        },
        {
            "input": ['100100'],
            "answer": 0,
        },
        {
            "input": ['001001'],
            "answer": 2,
        },
        {
            "input": ['012345679'],
            "answer": 1,
        },
        {
            "input": ['0000'],
            "answer": 4,
        },
    ],
    "Extra": [
        {
            "input": ['734'],
            "answer": 0,
        },
        {
            "input": ['110'],
            "answer": 0,
        },
        {
            "input": ['567'],
            "answer": 0,
        },
        {
            "input": ['0'],
            "answer": 1,
        },
        {
            "input": ['1'],
            "answer": 0,
        },
    ]
}
