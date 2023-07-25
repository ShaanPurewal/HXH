class Profile:
    title: str = "Title"
    description: str = "Description"
    location: str = "location (remote|in-person)"
    salary: int = -1

    def __init__(self, title: str = "Title",
                 description: str = "Description",
                 location: str = "location (remote|in-person)",
                 salary: int = -1):
        self.title = title
        self.description = description
        self.location = location
        self.salary = salary

    def get_title(self) -> str:
        return self.title

    def get_description(self) -> str:
        return self.description

    def get_location(self) -> str:
        return self.location

    def get_salary(self) -> int:
        return self.salary

    def __str__(self):
        return f"{self.title}\n" \
               f"\n" \
               f"Location: {self.location}\n" \
               f"Salary: {self.salary}\n" \
               f"\n" \
               f"{self.description}"
