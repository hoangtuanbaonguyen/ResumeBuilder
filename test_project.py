import resume
from project import get_intro_layout
from project import save_pdf_resume
from project import get_user_input_resume
from resume_builder import ResumeBuilder
from unittest.mock import patch
import unittest
import os


def test_get_intro_layout():
    assert get_intro_layout().startswith("Welcome to Easy Resume Builder - Your Terminal Resume Builder")


def test_save_pdf_resume():
    # Prepare sample resume
    resume_builder = ResumeBuilder()
    file_name = "example_file.pdf"

    save_pdf_resume(resume_builder, file_name)
    assert os.path.exists(file_name)
    # Remove the file to avoid conflict
    os.remove(file_name)


class test_get_user_input_resume(unittest.TestCase):
    SAMPLE_RESUME = resume.sample_resume()

    @patch("builtins.input", side_effect=["2", "Alice", "", "q"])
    def test_prompt_when_add_summary_then_get_correct_summary(self, mock_input):
        resume_builder = get_user_input_resume()
        self.assertIsInstance(resume_builder, ResumeBuilder)
        self.assertIn("Alice", resume_builder.resume.summary.content)

    @patch("builtins.input",
           side_effect=["1", "Tuan", "Bao", "example@lol.com", "123-123-123", "Ho Chi Minh", "Freelancer", "0", "q"])
    def test_prompt_when_add_personal_info_then_get_correct_personal_info(self, mock_input):
        personal_info = get_user_input_resume().resume.personal_info
        self.assertIn("Tuan", personal_info.first_name)
        self.assertIn("Bao", personal_info.last_name)
        self.assertIn("example@lol.com", personal_info.email)
        self.assertIn("123-123", personal_info.phone)
        self.assertIn("Ho Chi Minh", personal_info.address)
        self.assertIn("Freelancer", personal_info.job_title)

    @patch("builtins.input",
           side_effect=["3", "1", "line1", "line2", "line3", "line4", "line5", "line6", "line7", "line8", "q"])
    def test_prompt_when_add_educations_then_get_the_correct_education(self, mock_input):
        education = get_user_input_resume().resume.educations[0]
        self.assertEqual("line1", education.institute_name)
        self.assertEqual("line2", education.location)
        self.assertEqual("line3", education.degree_type)
        self.assertEqual("line4", education.field_of_study)
        self.assertEqual("line5", education.start_date)
        self.assertEqual("line6", education.graduated_date)
        self.assertEqual("line7", education.score_type)
        self.assertEqual("line8", education.scores)

    @patch("builtins.input",
           side_effect=["4", "1", "line1", "line2", "line3", "line4", "line5", "line6", "line7", "", "q"])
    def test_prompt_when_add_experience_then_get_correct_experience(self, mock_input):
        exps = get_user_input_resume().resume.experiences[0]
        self.assertEqual("line1", exps.company_name)
        self.assertEqual("line2", exps.job_title)
        self.assertEqual("line3", exps.start_date)
        self.assertEqual("line4", exps.graduated_date)
        self.assertEqual("line5", exps.location)
        self.assertEqual("line6\nline7", exps.description)

    @patch("builtins.input",
           side_effect=["5", "1", "line1", "line2", "line3", "line4", "line5", "line6", "line7", "", "q"])
    def test_prompt_when_add_projects_then_get_correct_projects(self, mock_input):
        projects = get_user_input_resume().resume.projects
        self.assertEqual("line1", projects[0].name)
        self.assertEqual("line2", projects[0].technologies)
        self.assertEqual("line3", projects[0].link)
        self.assertEqual("line4\nline5\nline6\nline7", projects[0].description)

    @patch("builtins.input",
           side_effect=["6", "line0", "line1", "line2", "line3", "line4", "q"])
    def test_prompt_when_add_skills_then_get_correct_skill_set(self, mock_input):
        skills = get_user_input_resume().resume.skills
        self.assertEqual("line0", skills.languages)
        self.assertEqual("line1", skills.frameworks)
        self.assertEqual("line2", skills.tools)
        self.assertEqual("line3", skills.platforms)
        self.assertEqual("line4", skills.databases)

    @patch("builtins.input",
           side_effect=["7", "1", "line0", "line1", "line2", "line3", "q"])
    def test_prompt_when_add_certificates_then_get_correct_certificates(self, mock_input):
        certs = get_user_input_resume().resume.certificates
        self.assertEqual("line0", certs[0].name)
        self.assertEqual("line1", certs[0].title)
        self.assertEqual("line2", certs[0].link)
        self.assertEqual("line3", certs[0].issued_by)
