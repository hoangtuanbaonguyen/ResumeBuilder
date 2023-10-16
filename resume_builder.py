from typing import List
from fpdf import FPDF
from resume_components import PersonalInfo, Experience, Education, SkillSets, Project, Certificate, Summary


class ResumeBuilder(FPDF):
    def __init__(self):
        super().__init__()
        self.default_setting()

    def default_setting(self):
        """
        Setting up the pdf by default spec
        :return:
        """
        self.add_page(orientation="P", format="A4")
        self.set_margins(left=10, right=10, top=0)
        self.set_author("Resume Builder")

    def add_personal_info(self, personal_info: PersonalInfo):
        """
        Add personal info component into the pdf file
        :param personal_info: given PersonalInfo
        :return:
        """
        if personal_info is None:
            return

        # Attach full name as title of the resume
        self.ln(10)
        fullname = f"{personal_info.first_name} {personal_info.last_name}"
        self._add_text_at_position(font="Times",
                                   literal="B",
                                   font_size=16,
                                   position="c",
                                   text=fullname.strip())

        # Attach headline
        self.ln(5)
        self.set_font('Times', 'B', 10)
        self._add_text_at_position(font="Times",
                                   literal="B",
                                   font_size=10,
                                   position="c",
                                   text=personal_info.job_title.strip())

        # Attach address
        self.ln(5)
        color = (128, 128, 128)  # Grey
        self._add_text_at_position(font="Times",
                                   literal="B",
                                   font_size=10,
                                   position="c",
                                   text=personal_info.address.strip(),
                                   text_color=color)

        # Attach contacts
        self.ln(5)
        contacts = [personal_info.phone, personal_info.email, *personal_info.links]
        # Filter contact list
        for contact in contacts:
            if len(contact.strip()) == 0:
                contacts.remove(contact)
        # Construct contacts str
        contacts_str = (" | ".join(contacts))
        self._add_text_at_position(font="Times",
                                   literal="B",
                                   font_size=10,
                                   position="c",
                                   text=contacts_str)

    def add_summary(self, summary: Summary):
        """
        Add Summary portion into the pdf file
        :param text: input summary
        :return:
        """
        if summary.content == "":
            return

        # Attach summary title + line
        self._add_liner("Summary")
        self._add_text_box(text=summary.content)

    def add_work_experiences(self, work_experience: List[Experience]):
        """
        Add work experience component into the pdf file
        :param work_experience:
        :return:
        """
        if work_experience is None:
            return

        # Attach Experiences line
        self._add_liner("Work Experience")

        # Attach work experiences
        for exp in work_experience:
            self._add_experience(exp)
            self.ln(5)

        self.ln(-5)

    def _add_experience(self, experience: Experience):
        """
        Add an experience portion into pdf file
        :param experience:
        :return:
        """
        if experience is None:
            return

        # Attach company name - company's location
        # Attach company name at the left most
        self._add_text_at_position(literal="B", position="left", text=experience.company_name)
        # Attach company's location at the right most
        self._add_text_at_position(literal="I",
                                   position="right",
                                   text=experience.location,
                                   text_color=(128, 128, 128))

        # Attach job-title - start-date - graduated-date
        start_grad_date = f"{experience.start_date} - {experience.graduated_date}"
        self.ln(4)
        # Attach job-title at the left most
        self._add_text_at_position(literal="B",
                                   position="left",
                                   font_size=8,
                                   text=experience.job_title.upper())
        # Attach start-date - graduated-date at the right most
        self._add_text_at_position(literal="I",
                                   position="right",
                                   font_size=8,
                                   text=start_grad_date,
                                   text_color=(128, 128, 128))

        # Attach job description
        self.ln(1)
        self._add_text_box(text=experience.description)

        # Change font back to normal
        self._set_default_font()

    def add_educations(self, educations: List[Education]):
        """
        Add educations into the pdf file
        :param educations:
        :return:
        """
        if educations is None:
            return

        self._add_liner("Education")
        for edu in educations:
            self._add_education(edu)
            self.ln(5)

        self.ln(-5)

    def _add_education(self, education: Education):
        """
        Add education portion into the pdf file
        :param education:
        :return:
        """
        if education is None:
            return

        text_color = (128, 128, 128)  # Grey

        # Attach institution - location
        self._add_text_at_position(literal="B", position="l", text=education.institute_name)
        self._add_text_at_position(literal="I", position="r", text=education.location, text_color=text_color)

        # Attach degree type | field of study
        self.ln(4)
        self._add_text_at_position(position="l", text=" | ".join((education.degree_type, education.field_of_study)))
        start_grad_str = " - ".join([education.start_date, education.graduated_date])

        self._add_text_at_position(literal="I", position="r", font_size=8, text=start_grad_str, text_color=text_color)

        # Attach score
        self.ln(4)
        scores_str = ": ".join([education.score_type.upper(), education.scores])
        self._add_text_at_position(position="l", text=scores_str)

    def add_skill_set(self, skill_set: SkillSets):
        """
        Add skill-sets into the pdf file
        :param skill_set:
        :return:
        """
        if skill_set is None:
            return

        self._add_liner("Skills")

        # Get skill_set dictionary from given skill-set
        skills_dict = skill_set.__dict__

        # Attach skill-sets
        for set_name in skills_dict:
            skills_str = skills_dict.get(set_name)
            if skills_str != "":
                self._add_text_at_position(font_size=8, literal="B",
                                           position="l", text=set_name.upper())
                self.ln(4)
                self._add_text_at_position(font_size=8, position="l", text=skills_str)
                self.ln(4)
        self.ln(-4)

    def add_projects(self, projects: List[Project]):
        """
        Add projects into pdf file
        :param projects:
        :return:
        """
        if projects is None:
            return

        self._add_liner("Projects")
        # Attach projects into the pdf
        for project in projects:
            self._add_project(project)
            self.ln(6)
        self.ln(-6)

    def _add_project(self, project: Project):
        """
        Add a project into pdf file
        :param project:
        :return:
        """
        if project is None:
            return

        # Attach project title
        self._add_text_at_position(position="l", literal="B", font_size=10, text=project.title)
        # Attach project link
        if project.link != "":
            self._add_text_at_position(position="r", font_size=8,
                                       text=f"[{project.link}]", text_color=(128, 128, 128))
        # Attach used techniques
        self.ln(4)
        self._add_text_at_position(position="l", font_size=8, text=project.technologies)

        # Attach project description
        self.ln(2)
        self._add_text_box(text=project.description)

    def add_certificates(self, certificates: List[Certificate], vertical_order=False):
        """
        Add certificates into the pdf file
        :param vertical_order: True if arrange certificate by vertical, otherwise by horizontal
        :param certificates:
        :return:
        """
        if certificates is None:
            return

        # Add liner to the certificates component
        self._add_liner("Certificates")

        # Iterate through certificates iterator to add certificate
        self.ln(-3)
        if vertical_order:
            for cert in certificates:
                self._add_certificate(cert, -1)
        else:
            for index, cert in enumerate(certificates):
                self._add_certificate(cert, index)
        self.ln(-5)

    def _add_certificate(self, certificate: Certificate, index=0, vertical_order=False):
        """
        Add certificate into certificates portion
        :param certificate:
        :return: Y coordinate after add certificate portion
        """
        if certificate is None:
            return
        base_y = self.get_y()
        position = "l"
        if not vertical_order and (index % 2 == 0):
            position = "r"

        line_h = 1  # ln

        # Attach name
        self._add_text_box_small(text=certificate.name, literal="B", font_size=10, position=position)
        self.ln(line_h)

        # Attach title
        self._add_text_box_small(text=certificate.title, position=position, font_size=8, text_color=(128, 128, 128))
        self.ln(line_h)
        # Attach issued by
        self._add_text_box_small(text=certificate.issued_by.upper(), font_size=8, position=position)
        self.ln(line_h)

        # Attach issued by
        self._add_text_box_small(text=certificate.link, font_size=8, position=position)

        if not vertical_order:
            if index % 2 == 0:
                self.set_y(base_y)
            else:
                self.ln(5)

    # Utility methods
    def _add_text_box_small(self,
                            font="Times",
                            literal="",
                            font_size=10,
                            ln=4,
                            text="",
                            position="left",
                            text_color=None):
        """
        Add small text box into pdf file include [half left, half right]
        Position including [left, l, right, r]
        :param font:
        :param literal:
        :param font_size:
        :param ln:
        :param text:
        :param text_color:
        :return:
        """
        # Validate input
        if text == "":
            return

        if text_color is None:
            text_color = (0, 0, 0)  # Black

        # Setting up font
        self.set_font(font, literal, font_size)
        self.set_text_color(text_color)
        position = position.lower()
        width = (self.w - self.l_margin * 2) / 2

        if position in ["left", "l"]:
            self.set_x(self.l_margin)
            self.multi_cell(w=width, h=ln, align="L", text=text)

        if position in ["right", "r"]:
            self.set_x(self.w / 2)
            self.multi_cell(w=width, h=ln, align="L", text=text)
            self.set_x(self.l_margin)

        # Change font back to normal
        self._set_default_font()

    def _add_text_box(self, font="Times", literal="", font_size=10, ln=4, text="", text_color=None):
        """
        Add a text box into pdf file
        :param ln:
        :param text_color:
        :param literal:
        :param font_size:
        :param font:
        :param text:
        :return:
        """
        if text == "":
            return

        if text_color is None:
            text_color = [0, 0, 0]

        text = self.multilines_text(text, "+")

        # Attach a multi cell, which is a text box
        self.set_x(self.l_margin - 1)
        self.set_font(font, literal, font_size)
        self.set_text_color(*text_color)
        self.multi_cell(w=0, h=ln, text=text, align="L", border=0)

        # Change font back to normal
        self._set_default_font()
        self.set_x(self.l_margin + 1)

    def _add_text_at_position(self,
                              font="Times",
                              literal="",
                              font_size=10,
                              position="center",
                              text="",
                              text_color=None):
        """
        Add text on specific position
        :param position:
        :param font:
        :param literal:
        :param font_size:
        :param text:
        :param text_color:
        :return:
        """
        if text == "":
            return

        if text_color is None:
            text_color = [0, 0, 0]

        self.set_font(font, literal, font_size)
        self.set_text_color(*text_color)
        position = position.lower()

        # Add Text in case position is left
        if position in ["left", "l"]:
            self.text(x=self.l_margin, y=self.get_y(), text=text)

        # Add Text in case position is right
        elif position in ["right", "r"]:
            x_coordinate = self.w - self.get_string_width(text) - self.r_margin
            self.text(x=x_coordinate, y=self.get_y(), text=text)

        # Add Text in case position is center
        elif position in ["center", "c"]:
            x_coordinate = (self.w - self.get_string_width(text)) / 2
            self.text(x=x_coordinate, y=self.get_y(), text=text)

        self._set_default_font()  # Change font back to normal

    def _add_liner(self, title: str):
        """
        Add a line into the pdf file
        :param title: The title of the line
        :return:
        """
        self.set_y(self.get_y() + 10)
        self.set_font('Times', 'B', 14)
        self.text(x=self.l_margin, y=self.get_y(), text=title)
        title_width = self.get_string_width(title) + self.l_margin
        self.line(x1=title_width, x2=self.w - self.r_margin, y1=self.get_y(), y2=self.get_y())
        self.ln(6)
        self._set_default_font()  # Change font back to normal

    def _set_default_font(self):
        # Change font back to normal
        self.set_font('Times', '', 10)
        self.set_text_color(0, 0, 0)

    def save_pdf(self, file_name: str):
        """
        Save pdf using given name {file_name}.pdf
        :param file_name:
        :return:
        """
        self.output(file_name + ".pdf")

    @staticmethod
    def multilines_text(text: str, sign: str) -> str:
        """
        Convert text with multiple lines, with a sign at the left most at each line
        :param sign:
        :param text:
        :return:
        """
        text = text.strip()
        lines = text.split("\n")
        if len(lines) > 1:
            lines = [f"{sign} {line}" for line in lines]
            return "\n".join(lines)
        else:
            return text
