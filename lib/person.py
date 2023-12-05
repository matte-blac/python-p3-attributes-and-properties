#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name, job):
# initializes a Person object with specified name and job
        self.name = name
        self.job = job

    @property
    def name(self):
# retrieves the name of the person
        return self._name
    
    @name.setter
    def name(self, value):
# sets the name of the person
        if not isinstance(value, str) or len(value) > 25:
# validates the condition
            print("Name must be string under 25 characters.")
            return
        self._name = value.title()

    @property
    def job(self):
# retrieves the job of the person
        return self._job
    
    @job.setter
    def job(self, value):
# sets the job of the person
        if value not in APPROVED_JOBS:
# validates the condition
            print("Job must be in list of approved jobs.")
            return
        self._job = value
    pass
