def generate_checkpoint_plan(regular_checkpoint: list, programs: list, discipline: dict, final_checkpoint: dict,
                             course_project_checkpoint: dict, term: int, point_distribution: int,
                             additional_points: bool,
                             alternate_methods: bool,
                             has_course_project: bool):
    temp = {
        "additional_points": additional_points,
        "alternate_methods": alternate_methods,
        "has_course_project": has_course_project,
        "programs": programs,
        "status": "SAVED",
        "term": term,
        "regular_checkpoints": regular_checkpoint,
        "discipline": discipline,
        "final_checkpoint": final_checkpoint,
        "course_project_checkpoint": course_project_checkpoint,
        "point_distribution": point_distribution,
    }
    return temp


def generate_checkpoint(name, min, max, week, key, type_id):
    temp = {
        "name": name,
        "min_grade": min,
        "max_grade": max,
        "week": week,
        "key": key,
        "type_id": type_id,
    }
    return temp


def generate_discipline(bars_id, name, term, course_project):
    temp = {
        "id": bars_id,
        "name": name,
        "term": term,
        "course_project": course_project
    }
    return temp


def generate_program(bars_id, code, name):
    temp = {
        "id": bars_id,
        "code": code,
        "name": name
    }
    return temp

#TODO: Придумать как избавиться от этого хардкод-прикола
def get_checkpoints_type(type):
    types = [{
        "id": 27,
        "name": "Диф. зачет",
        "type": "final",
        "ordering": 1,
        "created_by": "None",
        "updated_by": "None",
        "created_at": "None",
        "updated_at": "None",
        "type_here": 2
    },
        {
            "id": 26,
            "name": "Зачет",
            "type": "final",
            "ordering": 1,
            "created_by": "None",
            "updated_by": "None",
            "created_at": "None",
            "updated_at": "None",
            "type_here": 3
        },
        {
            "id": 25,
            "name": "Экзамен",
            "type": "final",
            "ordering": 1,
            "created_by": "None",
            "updated_by": "None",
            "created_at": "None",
            "updated_at": "None",
            "type_here": 1
        }]
    for el in types:
        if el["type_here"] == type:
            return el["id"]