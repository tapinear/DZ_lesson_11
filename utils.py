import json

from pprint import pprint as pp

path = "data/candidates.json"

def load_candidates_from_json():
    """ Возвращает список всех кандидатов"""

    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data


def ger_all_candidates():
    """ Делает копию списка всех кандидатов"""
    candidates = load_candidates_from_json()
    return candidates


def get_candidates_by_id(candidate_id):
    """ Возвращает одного кандидата по его id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate.get("id") == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name):
    """ Возвращает кандидатов по имени"""
    candidates = load_candidates_from_json()
    candidates_found = []

    for candidate in candidates:
        if candidate_name.lower() in candidate.get("name").lower():
            candidates_found.append(candidate)
    return candidates_found


def get_candidates_by_skill(skill_name):
    """ Возвращает кандидатов по навыку"""
    skill_name = skill_name.lower()
    candidates = load_candidates_from_json()
    candidates_found = []

    for candidate in candidates:
        skills = candidate.get("skills")
        list_of_skills = skills.lower().split(", ")
        if skill_name in list_of_skills:
            candidates_found.append(candidate)
    return candidates_found



# Проверка загрузки данных по кандидатам
#pp(load_candidates_from_json("data/candidates.json"))

# Проверка загрузки данных по кандидатам
#pp(get_candidate(33))

# Проверка загрузки данных по имени кандидата
#p(get_candidates_by_name("burt"))

# Проверка загрузки данных по скиллу
#pp(get_candidates_by_skill("python"))
