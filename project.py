from resume_builder_prompt import resume_program
from resume_builder import ResumeBuilder


def get_intro_layout():
    return "Welcome to Easy Resume Builder - Your Terminal Resume Builder!\n" \
           "Create professional resumes instantly. Easy commands, custom templates.\n" \
           "[https://github.com/hoangtuanbaonguyen/ResumeBuilder]\n"


def save_pdf_resume(resume: ResumeBuilder, file_name: str):
    # Perform save resume
    resume.output(file_name)


def get_user_input_resume() -> ResumeBuilder:
    return resume_program()


def main():
    # Print introduction
    print(get_intro_layout())
    # Call resume builder prompt
    resume = resume_program()
    # Save the pdf resume by file_name
    file_name = "MyResume.pdf"
    save_pdf_resume(resume, file_name)
    # Show output file to help user find the outcome
    print(f"Output file: {file_name}")


if __name__ == "__main__":
    main()
