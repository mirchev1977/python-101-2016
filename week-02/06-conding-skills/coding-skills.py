import json
import sys

# coding skills


class Skill(object):
    skill = ''
    level = 0
    first_name = ''
    last_name = ''


def main():
    input_file = sys.argv[1]
    with open(input_file, 'r') as json_file:
        json_data = json.load(json_file)

        skills_dict = {}

        for person in json_data['people']:
            skills = person['skills']
            for skill in skills:
                skill_name = skill['name']
                skill_level = skill['level']
                skl = Skill()
                skl.first_name = person['first_name']
                skl.last_name = person['last_name']
                skl.skill_name = skill_name
                skl.skill_level = skill_level

                if skl.skill_name in skills_dict:
                    current_skill_level = skills_dict[
                        skl.skill_name].skill_level
                    if skl.skill_level > current_skill_level:
                        del skills_dict[skl.skill_name]
                        skills_dict[skl.skill_name] = skl
                else:
                    skills_dict[skl.skill_name] = skl

        for skill in skills_dict:
            current = skills_dict[skill]
            output = ''
            output = '{} - {} {}'.format(skill,
                                         current.first_name, current.last_name)
            print(output)


if __name__ == "__main__":
    main()
