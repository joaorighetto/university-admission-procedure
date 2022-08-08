# check if there's still vacancy for given department
def check_vacancies(dep):
    if len(dep) < department_vacancies:
        return True
    else:
        return False


# fill final department list with applicants from sorted list and add them to approved applicants list
def fill_vacancies(stage, final, removed):
    for dep_sorted, final_dep in zip(stage, final):
        temp_list = dep_sorted.copy()
        for j in range(len(temp_list)):
            if check_vacancies(final_dep):
                if temp_list[j] not in removed:
                    final_dep.append(temp_list[j])
                    removed_item = dep_sorted.pop(dep_sorted.index(temp_list[j]))
                    removed.append(removed_item)
            else:
                break


# create a sorted list by criteria from a candidate list for each priority stage of the procedure
def sort(gen_list, dep_list, crit_list, priority):
    sorted_lists = list()
    for department, crit in zip(dep_list, crit_list):
        sorted_lists.append(sorted([x for x in gen_list if x[priority] == department],
                                   key=crit))
    return sorted_lists


# define sorting criteria for approval
def bio_criteria(candidate): return ((-max((candidate["chem_score"] + candidate["phys_score"]) / 2, candidate["special_score"])),
                                     candidate["first_name"],
                                     candidate["last_name"])


def eng_criteria(candidate): return ((-max((candidate["math_score"] + candidate["cs_score"]) / 2, candidate["special_score"])),
                                     candidate["first_name"],
                                     candidate["last_name"])


def phys_criteria(candidate): return ((-max((candidate["math_score"] + candidate["phys_score"]) / 2, candidate["special_score"])),
                                      candidate["first_name"],
                                      candidate["last_name"])


def chem_criteria(candidate): return ((-max(candidate["chem_score"], candidate["special_score"])),
                                      candidate["first_name"],
                                      candidate["last_name"])


def math_criteria(candidate): return ((-max(candidate["math_score"], candidate["special_score"])),
                                      candidate["first_name"],
                                      candidate["last_name"])


department_vacancies = int(input("Enter maximum number of students a department can have: "))  # input max amount of students allowed in each department
applicants_list = list(dict())
keys = ["first_name", "last_name", "phys_score", "chem_score", "math_score", "cs_score", "special_score",
        "first_priority", "second_priority", "third_priority"]

# read file and stores applicants' data in a list of dictionaries
with open(r"applicant_list_7.txt", "r") as file:
    for line in file:
        applicant = list(line.split())
        for i in range(2, 7):  # convert score strings to floats
            applicant[i] = float(applicant[i])
        applicants_list.append(dict(zip(keys, applicant)))

approved_applicants = list()
bio_final = list()
chem_final = list()
eng_final = list()
math_final = list()
phys_final = list()

department_list = ["Biotech", "Engineering", "Physics", "Chemistry", "Mathematics"]
final_lists = [bio_final, eng_final, phys_final, chem_final, math_final]  # create a list of final lists
criteria_list = [bio_criteria, eng_criteria, phys_criteria, chem_criteria, math_criteria]

# first round
first_round = sort(applicants_list, department_list, criteria_list, "first_priority")  # sort all departments for first priorities
fill_vacancies(first_round, final_lists, approved_applicants)

# second round
second_round = sort(applicants_list, department_list, criteria_list, "second_priority")  # sort all departments for second priorities
fill_vacancies(second_round, final_lists, approved_applicants)

# third round
third_round = sort(applicants_list, department_list, criteria_list, "third_priority")  # sort all departments for third priorities
fill_vacancies(third_round, final_lists, approved_applicants)

# final sort
final_sorted_list = list()
for final_list, criteria in zip(final_lists, criteria_list):
    final_sorted_list.append(sorted(final_list, key=criteria))

# write approval results files
for final_list, criteria, dep_name in zip(final_sorted_list, criteria_list, department_list):
    with open(f"{dep_name.casefold()}.txt", "w") as file:
        for applicant in final_list:
            final_score = str(-criteria(applicant)[0])
            first_name = applicant["first_name"]
            last_name = applicant["last_name"]
            file.write(f"{first_name} {last_name} {final_score}\n")
