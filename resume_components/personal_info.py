from typing import List


class PersonalInfo:
    def __init__(self,
                 first_name="",
                 last_name="",
                 email="",
                 phone="",
                 address="",
                 job_title="",
                 links: List[str] = []):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.job_title = job_title
        self.links = links
