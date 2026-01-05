'''
USING PYTHON 3.11.9
'''

from src.crew import AIVerseCrew


"""Run the Crew"""

inputs = {
    "query": "how many 'r' are there in the word 'strawberry'",
}

AIVerseCrew().crew().kickoff(inputs=inputs)
