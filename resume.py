from typing import List
from resume_components import PersonalInfo, Experience, SkillSets, Certificate, Project, Education, Summary


class Resume:
    def __init__(self):
        self.summary: Summary = None
        self.personal_info: PersonalInfo = None
        self.educations: List[Education] = None
        self.experiences: List[Experience] = None
        self.skills: SkillSets = None
        self.projects: List[Project] = None
        self.certificates: List[Certificate] = None

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


def sample_resume() -> Resume:
    # Prepare personal info
    personal_info = PersonalInfo(
        first_name="Tuan",
        last_name="Bao",
        job_title="Software Engineer",
        address="123 Main St, Cityville, State, 12345",
        email="tuanbao@example.com",
        phone="(123) 456-7890",
        links=["linkedin.com/in/tuanbao", "twitter.com/tuanbao"]
    )
    # Prepare summary
    summary_str = "Dedicated and detail-oriented professional with a strong educational background and hands-on " \
                  "experience in software development. Seeking a challenging position in a progressive organization " \
                  "where " \
                  "my skills and expertise in programming and problem-solving will contribute to the company's success."
    summary = Summary(summary_str)
    # Prepare work experience
    work_experience = [Experience(
        company_name="Tech Solutions",
        job_title="Software Developer Intern",
        location="Cityville, State",
        start_date="May 2022",
        graduated_date="Auguest 2023",
        description='''
Collaborated with a team of developers to design and implement software solutions.
Assisted in debugging and resolving software defects.
Participated in code reviews and provided constructive feedback to peers.
        '''
    ), Experience(
        company_name="InnovateTech Solutions",
        job_title="Software Engineer",
        location="Cityville, State",
        start_date="June 2024",
        graduated_date="Present",
        description='''
Developed robust and scalable software solutions for clients, meeting strict deadlines and quality standards.
Collaborated with cross-functional teams, including designers and product managers, to translate project requirements into elegant and user-friendly interfaces.
Led the implementation of a critical feature set in a high-profile project, resulting in a 30% improvement in user engagement.
Conducted regular code reviews, ensuring adherence to best practices and identifying areas for optimization.
Assisted in the mentorship of junior developers, providing guidance and support in problem-solving and technical skills development.
Actively participated in the Agile development process, contributing innovative ideas during sprint planning sessions and retrospectives.
        '''
    )]
    # Job 1
    # Job 2

    # Prepare educations
    educations = []
    # University 1
    educations.append(Education(
        institute_name="University of Advanced Technology, TechCity",
        location="TechCity, State",
        start_date="September 20XX",
        graduated_date="May 20XX",
        degree_type="Master's Degree",
        field_of_study="Computer Science",
        score_type="Grade",
        scores="A+"
    ))
    # University 2
    educations.append(Education(
        institute_name="City University, Cityville",
        location="Cityville, State",
        start_date="August 20XX",
        graduated_date="May 20XX",
        degree_type="Bachelor's Degree",
        field_of_study="Computer Science",
        score_type="gpa",
        scores="3.9/4.0"
    ))

    # Prepare skill-sets
    skill_sets = SkillSets(
        languages="Python, JavaScript, Java",
        frameworks="Django, React, Spring",
        tools="Git, Visual Studio Code, Eclipse",
        platforms="Linux, Windows",
        databases="MySQL, SQLite"
    )

    # Prepare projects
    projects = []
    project1 = Project(
        name="Online Bookstore",
        title="Full Stack Web Development Project",
        technologies="Django, JavaScript, MySQL",
        link="https://example.com/bookstore",
        description="Developed a fully functional online bookstore with user authentication, product search, and online payment features."
    )

    project2 = Project(
        name="Task Manager App",
        title="Mobile App Development Project",
        technologies="React Native, Node.js, MongoDB",
        link="https://example.com/task-manager",
        description="Built a mobile task manager app for Android and iOS devices. Implemented user authentication and "
                    "real-time task updates."
    )

    project3 = Project(
        name="Data Visualization Dashboard",
        title="Data Science Project",
        technologies="Python, Pandas, Matplotlib, Tableau",
        link="https://example.com/data-dashboard",
        description="Created a data visualization dashboard for analyzing sales data. Used various Python libraries "
                    "and integrated with Tableau for interactive visualizations."
    )
    projects.append(project1)
    projects.append(project2)
    projects.append(project3)

    # Prepare certificates
    certificate1 = Certificate(
        name="Python Programming",
        title="Certificate of Completion",
        link="https://www.example.com/certificates/python",
        issued_by="Example Online Learning Platform"
    )

    certificate2 = Certificate(
        name="Web Development Fundamentals",
        title="Certificate of Achievement",
        link="https://www.example.com/certificates/webdev",
        issued_by="Web Development Institute"
    )

    certificate3 = Certificate(
        name="Data Analysis with Python",
        title="Professional Certificate",
        link="https://www.example.com/certificates/data-analysis",
        issued_by="Data Science Academy"
    )
    certificates = [certificate1, certificate2, certificate3]

    # Construct resume
    sample = Resume()
    sample.certificates = certificates
    sample.educations = educations
    sample.projects = projects
    sample.skills = skill_sets
    sample.personal_info = personal_info
    sample.experiences = work_experience
    sample.summary = summary
    # Return
    return sample
