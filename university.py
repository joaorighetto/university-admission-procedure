# check if there's still vacancy for given department
def check_vacancies(department_list):
    if len(department_list) < department_vacancies:
        return True
    else:
        return False


# fill final department list with applicants from sorted list and add them to approved applicants list
def fill_vacancies(sorted_applicants_list, final_department_list, approved_applicants_list):
    temp_list = sorted_applicants_list.copy()
    for j in range(len(temp_list)):
        if check_vacancies(final_department_list):
            if temp_list[j] not in approved_applicants_list:
                final_department_list.append(temp_list[j])
                removed_item = sorted_applicants_list.pop(sorted_applicants_list.index(temp_list[j]))
                approved_applicants_list.append(removed_item)
        else:
            break


# define sorting criteria for approval
def bio_criteria(candidate): return max((candidate["chem_score"] + candidate["phys_score"]) / 2, candidate["special_score"])
def eng_criteria(candidate): return max((candidate["math_score"] + candidate["cs_score"]) / 2, candidate["special_score"])
def phys_criteria(candidate): return max((candidate["math_score"] + candidate["phys_score"]) / 2, candidate["special_score"])
def chem_criteria(candidate): return max(candidate["chem_score"], candidate["special_score"])
def math_criteria(candidate): return max(candidate["math_score"], candidate["special_score"])


department_vacancies = int(input())  # select max amount of students allowed in each department
list_of_applicants = list(dict())
keys = ["first_name", "last_name", "phys_score", "chem_score", "math_score", "cs_score", "special_score",
        "first_priority", "second_priority", "third_priority"]

with open(r"applicant_list_7.txt", "r") as file:
    for line in file:
        applicant = list(line.split())
        for i in range(2, 7):  # convert score strings to floats
            applicant[i] = float(applicant[i])
        list_of_applicants.append(dict(zip(keys, applicant)))

list_of_applicants = sorted(list_of_applicants, key=lambda x: (x["first_name"], x["last_name"]))  # sort applicants list by name in alphabetical order

approved_applicants = list()
final_biotech_list = list()
final_chemistry_list = list()
final_engineering_list = list()
final_mathematics_list = list()
final_physics_list = list()


bio_first_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["first_priority"] == "Biotech"],
                                 key=lambda x: -bio_criteria(x))
eng_first_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["first_priority"] == "Engineering"],
                                 key=lambda x: -eng_criteria(x))
phys_first_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["first_priority"] == "Physics"],
                                  key=lambda x: -phys_criteria(x))
chem_first_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["first_priority"] == "Chemistry"],
                                  key=lambda x: -chem_criteria(x))
math_first_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["first_priority"] == "Mathematics"],
                                  key=lambda x: -math_criteria(x))

fill_vacancies(bio_first_priority_list, final_biotech_list, approved_applicants)
fill_vacancies(chem_first_priority_list, final_chemistry_list, approved_applicants)
fill_vacancies(eng_first_priority_list, final_engineering_list, approved_applicants)
fill_vacancies(math_first_priority_list, final_mathematics_list, approved_applicants)
fill_vacancies(phys_first_priority_list, final_physics_list, approved_applicants)

bio_second_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["second_priority"] == "Biotech"],
                                  key=lambda x: -bio_criteria(x))
eng_second_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["second_priority"] == "Engineering"],
                                  key=lambda x: -eng_criteria(x))
phys_second_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["second_priority"] == "Physics"],
                                   key=lambda x: -phys_criteria(x))
chem_second_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["second_priority"] == "Chemistry"],
                                   key=lambda x: -chem_criteria(x))
math_second_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["second_priority"] == "Mathematics"],
                                   key=lambda x: -math_criteria(x))

fill_vacancies(bio_second_priority_list, final_biotech_list, approved_applicants)
fill_vacancies(chem_second_priority_list, final_chemistry_list, approved_applicants)
fill_vacancies(eng_second_priority_list, final_engineering_list, approved_applicants)
fill_vacancies(math_second_priority_list, final_mathematics_list, approved_applicants)
fill_vacancies(phys_second_priority_list, final_physics_list, approved_applicants)

bio_third_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["third_priority"] == "Biotech"],
                                 key=lambda x: -bio_criteria(x))
eng_third_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["third_priority"] == "Engineering"],
                                 key=lambda x: -eng_criteria(x))
phys_third_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["third_priority"] == "Physics"],
                                  key=lambda x: -phys_criteria(x))
chem_third_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["third_priority"] == "Chemistry"],
                                  key=lambda x: -chem_criteria(x))
math_third_priority_list = sorted([applicant for applicant in list_of_applicants if applicant["third_priority"] == "Mathematics"],
                                  key=lambda x: -math_criteria(x))

fill_vacancies(bio_third_priority_list, final_biotech_list, approved_applicants)
fill_vacancies(chem_third_priority_list, final_chemistry_list, approved_applicants)
fill_vacancies(eng_third_priority_list, final_engineering_list, approved_applicants)
fill_vacancies(math_third_priority_list, final_mathematics_list, approved_applicants)
fill_vacancies(phys_third_priority_list, final_physics_list, approved_applicants)

final_biotech_list = sorted(final_biotech_list,
                            key=lambda x: (-bio_criteria(x), x["first_name"], x["last_name"]))
final_engineering_list = sorted(final_engineering_list,
                                key=lambda x: (-eng_criteria(x), x["first_name"], x["last_name"]))
final_physics_list = sorted(final_physics_list,
                            key=lambda x: (-phys_criteria(x), x["first_name"], x["last_name"]))
final_chemistry_list = sorted(final_chemistry_list,
                              key=lambda x: (-chem_criteria(x), x["first_name"], x["last_name"]))
final_mathematics_list = sorted(final_mathematics_list,
                                key=lambda x: (-math_criteria(x), x["first_name"], x["last_name"]))


with open("biotech.txt", "w") as file:
    for applicant in final_biotech_list:
        final_score = str(bio_criteria(applicant))
        first_name = applicant["first_name"]
        last_name = applicant["last_name"]
        file.write(f"{first_name} {last_name} {final_score}\n")

with open("engineering.txt", "w") as file:
    for applicant in final_engineering_list:
        final_score = str(eng_criteria(applicant))
        first_name = applicant["first_name"]
        last_name = applicant["last_name"]
        file.write(f"{first_name} {last_name} {final_score}\n")

with open("chemistry.txt", "w") as file:
    for applicant in final_chemistry_list:
        final_score = str(chem_criteria(applicant))
        first_name = applicant["first_name"]
        last_name = applicant["last_name"]
        file.write(f"{first_name} {last_name} {final_score}\n")

with open("mathematics.txt", "w") as file:
    for applicant in final_mathematics_list:
        final_score = str(math_criteria(applicant))
        first_name = applicant["first_name"]
        last_name = applicant["last_name"]
        file.write(f"{first_name} {last_name} {final_score}\n")

with open("physics.txt", "w") as file:
    for applicant in final_physics_list:
        final_score = str(phys_criteria(applicant))
        first_name = applicant["first_name"]
        last_name = applicant["last_name"]
        file.write(f"{first_name} {last_name} {final_score}\n")
