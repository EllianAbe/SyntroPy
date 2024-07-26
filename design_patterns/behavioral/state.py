from abc import ABC, abstractmethod


class UnderstandingState(ABC):
    @abstractmethod
    def study(self, student):
        pass


class NotUnderstoodState(UnderstandingState):
    def study(self, student):
        print(f"Studying the subject... Still not understood.")
        student.state = PartiallyUnderstoodState()


class PartiallyUnderstoodState(UnderstandingState):
    def study(self, student):
        print("Studying the subject... Partially understood.")
        student.state = FullyUnderstoodState()


class FullyUnderstoodState(UnderstandingState):
    def study(self, student):
        print("Subject fully understood! Moving to next subject.")
        student.next_subject()


class Student:
    def __init__(self, subjects):
        self.subjects = subjects
        self.subject_generator = self._next_subject()
        self.next_subject()

    def study(self):
        print(f"Current Subject: {self._current_subject}")
        self.state.study(self)

    def next_subject(self):
        try:
            self._current_subject = next(self.subject_generator)
            self.state = NotUnderstoodState()
        except StopIteration:
            self._current_subject = None
            print("All subjects completed!")

    def _next_subject(self):
        yield from self.subjects


# Example usage
subjects = ["Math", "Physics", "Chemistry"]
student = Student(subjects)

while student._current_subject:
    student.study()
