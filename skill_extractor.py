def load_skills():

    with open("skills.txt", "r") as file:
        skills = [line.strip().lower() for line in file]

    return skills


def extract_skills(text, skills_db):

    text = text.lower()

    found_skills = []

    for skill in skills_db:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))