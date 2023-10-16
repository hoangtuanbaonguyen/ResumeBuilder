import sys
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from resume import Resume
from typing import List
from resume_builder import ResumeBuilder
from resume import sample_resume
from resume_components import PersonalInfo, Experience, Education, SkillSets, Project, Certificate


class DynamicPrompt:
    def __init__(self, class_instance):
        self.class_instance = class_instance
        self.style = Style.from_dict({"prompt": "bold"})
        self.session = PromptSession()

    @staticmethod
    def input_instance(instance, message=""):
        """
        Create prompt get input values of a class instance
        :param message:
        :param instance: an instance of a class
        :return:
        """
        print(message)
        DynamicPrompt(instance).create_prompts()

    def create_prompts(self):
        for key, value in self.class_instance.__dict__.items():
            if not key.startswith("__"):  # Exclude special attributes
                if isinstance(value, list):
                    prompt_text = f"Enter number of {key.replace('_', ' ').capitalize()}: "
                    numbers = 0

                    # Get number of input
                    while True:
                        try:
                            numbers = int(self.session.prompt(prompt_text, style=self.style))
                            break
                        except ValueError:
                            pass

                    # Get inputs
                    inputs = []
                    for index in range(numbers):
                        try:
                            prompt_text = f"Enter {key[:-1].replace('_', ' ').capitalize()} {index + 1}: "
                            user_input = self.session.prompt(prompt_text, style=self.style).strip()
                            if len(user_input) > 0:
                                inputs.append(user_input)
                        except IOError or KeyboardInterrupt:
                            break
                    # Store inputs into class-instance
                    setattr(self.class_instance, key, inputs)

                else:
                    prompt_text = f"Enter {key.replace('_', ' ').capitalize()}: "
                    user_input = self.session.prompt(prompt_text, style=self.style)
                    setattr(self.class_instance, key, user_input)


def prompt_personal_info():
    instance = PersonalInfo()
    message = "Fill your personal info below: "
    DynamicPrompt.input_instance(instance, message)
    return instance


def prompt_summary() -> str:
    session = PromptSession()
    message = "Fill your summary: "
    return session.prompt(message)


def prompt_skill_set() -> SkillSets:
    instance = SkillSets()
    message = "Fill your skill set below: "
    DynamicPrompt.input_instance(instance, message)
    return instance


def prompt_experience() -> List[Experience]:
    numbers = get_user_input_int("Number of work experiences: ")
    experiences = []
    for index in range(numbers):
        try:
            instance = Experience()
            message = f"Fill your work experience {index + 1}: "
            DynamicPrompt.input_instance(instance, message)
            experiences.append(instance)
        except IOError or KeyboardInterrupt:
            break
    return experiences


def get_user_input_int(message: str) -> int:
    while True:
        try:
            num = int(input(message))
            if num > 0:
                return num
        except ValueError:
            pass


def prompt_education() -> List[Education]:
    numbers = get_user_input_int("Number of educations: ")
    educations = []
    for index in range(numbers):
        try:
            instance = Education()
            message = f"Fill your education {index + 1}: "
            DynamicPrompt.input_instance(instance, message)
            educations.append(instance)
        except IOError or KeyboardInterrupt:
            break
    return educations


def prompt_project() -> List[Project]:
    numbers = get_user_input_int("Number of projects: ")
    projects = []
    for index in range(numbers):
        try:
            instance = Project()
            message = f"Fill your project {index + 1}: "
            DynamicPrompt.input_instance(instance, message)
            projects.append(instance)
        except IOError or KeyboardInterrupt:
            break
    return projects


def prompt_certificate() -> List[Certificate]:
    numbers = get_user_input_int("Number of certificates: ")
    certificates = []
    for index in range(numbers):
        try:
            instance = Certificate()
            message = f"Fill your certificate {index + 1}: "
            DynamicPrompt.input_instance(instance, message)
            certificates.append(instance)
        except IOError or KeyboardInterrupt:
            break
    return certificates


def create_menu_layout(component_names: List[str]) -> str:
    menu_layout = "Pick a number to attach a resume component to your resume\n" \
                  "Instructions: Choose a number and press 'Enter'\n" \
                  "              Type 'quit' or 'q' to save and exit\n" \
                  "              Type 'reset' or 'r' to reset\n" \
                  "              Type 'sample' to output a sample resume\n"

    for index, name in enumerate(component_names):
        menu_layout += "\n{}. Add {} component.".format(index + 1, name.replace("_", " "))
    return menu_layout


def resume_program():
    resume_instance = Resume()
    resume_builder = ResumeBuilder()
    # Extract component names from resume instance
    component_names = [key for key in resume_instance.__dict__.keys()]
    # Show introduction
    print("Welcome to Easy Resume Builder - Your Terminal Resume Builder!\n"
          "Create professional resumes instantly. Easy commands, custom templates.\n"
          "[https://github.com/hoangtuanbaonguyen/ResumeBuilder]\n")

    # Prompt menu
    while True:
        menu_layout = create_menu_layout(component_names)
        print(menu_layout)
        try:
            user_input = input(f"Enter your choice: ").strip().lower()
            index = int(user_input) - 1
            if 0 <= index < len(component_names):
                # Get component name from name list
                component_name = component_names[index]

                if component_name == "personal_info":
                    personal_info = prompt_personal_info()
                    resume_builder.add_personal_info(personal_info)
                elif component_name == "experiences":
                    exps = prompt_experience()
                    resume_builder.add_work_experiences(exps)
                elif component_name == "summary":
                    summary = prompt_summary()
                    resume_builder.add_summary(summary)
                elif component_name == "projects":
                    projects = prompt_project()
                    resume_builder.add_projects(projects)
                elif component_name == "educations":
                    educations = prompt_education()
                    resume_builder.add_educations(educations)
                elif component_name == "certificates":
                    certs = prompt_certificate()
                    resume_builder.add_certificates(certs)
                elif component_name == "skills":
                    skills = prompt_skill_set()
                    resume_builder.add_skill_set(skills)
                component_names.pop(index)
        except ValueError:
            if user_input in ["quit", "q"]:
                # Save PDF file
                output_file = "MyResume.pdf"
                print("Perform save your resume and exit.")
                print(f"Resume file: {output_file}")
                resume_builder.output(output_file)
                sys.exit()
            elif user_input in ["reset", "r"]:
                # Refresh resume_builder and component names
                resume_builder = ResumeBuilder()
                component_names = [key for key in resume_instance.__dict__.keys()]
            elif user_input == "sample":
                # Save sample resume
                file_name = "SampleResume.pdf"
                print("Perform create sample resume and exit.")
                print(f"Resume file: {file_name}")
                create_sample_resume().output(file_name)
                sys.exit()


def create_sample_resume() -> ResumeBuilder:
    resume = sample_resume()
    resume.projects.pop(0)
    resume_builder = ResumeBuilder()
    resume_builder.add_personal_info(resume.personal_info)
    resume_builder.add_summary(resume.summary)
    resume_builder.add_work_experiences(resume.experiences)
    resume_builder.add_skill_set(resume.skills)
    resume_builder.add_projects(resume.projects)
    resume_builder.add_educations(resume.educations)
    return resume_builder
