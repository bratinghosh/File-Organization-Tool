import yaml

from task import Task

def load_yaml_data(filepath="tasks.yaml"):
    with open(filepath, "r") as file_descriptor:
        data = yaml.safe_load(file_descriptor)
    return data


def main():
    data = load_yaml_data("tasks.yaml")

    for task in data["tasks"]:
        taskData = task["task"]

        task = Task(taskData["source"], taskData["destination"])

        for rule in taskData["rules"]:
            ruleData = rule["rule"]

            if ruleData["type"] == "keyword":
                keywords = ruleData["keyword"].split()
                task.add_keyword_rule(keywords)
            if ruleData["type"] == "extension":
                extensions = ruleData["extension"].split()
                task.add_extension_rule(extensions)
            if ruleData["type"] == "size_greater":
                pass
            if ruleData["type"] == "size_less":
                pass
            if ruleData["type"] == "created_time_on":
                pass
            if ruleData["type"] == "created_time_before":
                pass
            if ruleData["type"] == "created_time_after":
                pass
            if ruleData["type"] == "created_time_between":
                pass
            if ruleData["type"] == "modified_time_on":
                pass
            if ruleData["type"] == "modified_time_before":
                pass
            if ruleData["type"] == "modified_time_after":
                pass
            if ruleData["type"] == "modified_time_between":
                pass
        
        task.run()

    
main()