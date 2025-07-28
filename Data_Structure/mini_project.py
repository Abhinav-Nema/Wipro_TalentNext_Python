
'''
MINI PROJECT 1
Create a dictionary that contains a list of people and one interesting fact about each of them.Display each person and his or herinteresting fact to the screen. Next, change a fact about one ofthe people. Also add an additional person and corresponding fact. Display the new list of peopleand facts. Run the program multiple times and notice if the order changes
'''
people = {
    "Jason": "Can fly an airplane",
    "Jeff": "Is afraid of heights",
    "David": "Plays the piano",
    "Jill": "Can hula dance"
}


print("Original list of people and facts:")
for name, fact in people.items():
    print(f"{name}: {fact}")


people["Jeff"] = "Is afraid of dogs"


people["Anna"] = "Loves skydiving"


print("\nUpdated list of people and facts:")
for name, fact in people.items():
    print(f"{name}: {fact}")


'''
MINI PROJECT 2
Given the participant’sscore sheet for your University Sports Day, you are required to find the runner-up score. You have scores. Store them in a list and find the score of the runner-up.
Sample input:[2, 3, 6, 6, 5]
Sample output:5
Explanation:
Given list is [2, 3, 6, 6, 5]. 
The maximum score is 6, second maximum is 5. Hence, we print 5as the runner-up score
'''

def find_runner_up(scores):
    
    unique_scores = set(scores)

    
    max_score = max(unique_scores)
    unique_scores.remove(max_score)

    
    runner_up = max(unique_scores)

    return runner_up


scores = [2, 3, 6, 6, 5]
print(find_runner_up(scores))

