from fpdf import FPDF


class Resume:
    def __init__(self):
        self.personal_info = None
        self.educations = []
        self.experiences = []
        self.skills = None
        self.projects = []
        self.certificates = []
        self.pdf = None

    def add_education(self, education):
        self.educations.append(education)

    def remove_education_at(self, index):
        if len(self.educations) <= index:
            raise IndexError("Out of index")
        self.educations.pop(index)

    def add_experience(self, experience):
        self.experiences.append(experience)

    def remove_experience_at(self, index):
        if len(self.experiences) <= index:
            raise IndexError("Out of index")
        self.experiences.pop(index)

    def add_project(self, project):
        self.projects.append(project)

    def remove_project_at(self, index):
        if len(self.projects) <= index:
            raise IndexError("Out of index")
        self.projects.pop(index)

    def add_certificate(self, certificate):
        self.certificates.append(certificate)

    def remove_certificate_at(self, index):
        if len(self.certificates) <= index:
            raise IndexError("Out of index")
        self.certificates.pop(index)

    def clear_skills(self):
        self.skills = None

    def clear_personal_info(self):
        self.personal_info = None

    def clear_certificate(self):
        self.certificates = []

    def clear_projects(self):
        self.projects = []

    def clear_experiences(self):
        self.experiences = []

    def clear_educations(self):
        self.educations = []

    def clear(self):
        self.personal_info = None
        self.educations = []
        self.experiences = []
        self.skills = None
        self.projects = []
        self.certificates = []
        self.pdf = None
