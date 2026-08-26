from constraint import *

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    papersubjects = {
        'AI':[],
        'NLP':[],
        'ML':[]
    }

    subjectcount = {
        'AI':0,
        'NLP':0,
        'ML':0
    }

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        subjectcount[topic] = subjectcount[topic] + 1
        var_name = f'{title} ({topic})'
        papers[title] = topic
        papersubjects[topic].append(var_name)
        paper_info = input()

    # Define the variables
    variables = []

    for key, value in papers.items():
        variables.append(f'{key} ({value})')

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Change this section if necessary
    problem.addVariables(variables, domain)

    # Add the constraints

    def najmnogu4(*vals):
        for i in range(1, num + 1):
            if vals.count(f"T{i}") > 4:
                return False
        return True

    problem.addConstraint(najmnogu4, variables)

    def sameterm(*vals):
        return len(set(vals)) == 1

    for subject, titles in papersubjects.items():
        if 0 < len(titles) <= 4:
            problem.addConstraint(sameterm, papersubjects[subject])


    result = problem.getSolution()

    # Add the required print section

    carry = ""
    sorted_results = sorted(result.items(), key=lambda x: x[0])
    for key, value in sorted_results:
        if key[6] == '0':
            carry = f'{key}: {value}'
        else:
            print(f'{key}: {value}')
    print(carry)

    print(papersubjects)

