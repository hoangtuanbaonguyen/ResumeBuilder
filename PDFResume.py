from fpdf import FPDF
from components import PersonalInfo
from components import Certificate


class PDFResume(FPDF):
    def default_setting(self):
        """
        Setting up the pdf by default spec
        :return:
        """
        self.set_margins(left=10, right=10, top=5)
        self.set_author("Resume Builder")

    def add_personal_info(self, personal_info: PersonalInfo) -> None:
        """
        Add personal info component into the pdf file
        :param personal_info: given PersonalInfo
        :return:
        """

        pass

    def calculate_center_coordinate(self, text: str) -> float:
        """
        Calculate the start coordinate to align the text into the center of a statement
        :param text: given string to be calculated
        :return:
        """
        width = self.get_string_width(text)
        return (self.w - width) / 2


pdf = PDFResume()
pdf.add_page(orientation="P", format="A4")
pdf.add_personal_info(None)
pdf.output("abc.pdf")
