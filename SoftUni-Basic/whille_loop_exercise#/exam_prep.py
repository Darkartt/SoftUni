failed_threshold = int(input())

failed_times = 0
solved_problems = 0
grades_sum = 0
last_problem = ''
has_failed = True

while failed_times < failed_threshold:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
        grades_sum += grade
        solved_problems += 1
        last_problem = problem_name
    if grade > 4:
        grades_sum += grade
        solved_problems += 1
        last_problem = problem_name
average_score = grades_sum / solved_problems
if has_failed:
    print(f"You need a break, {failed_threshold} poor grades.")
if not  has_failed:
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {solved_problems}')
    print(f'Last problem: {last_problem}')