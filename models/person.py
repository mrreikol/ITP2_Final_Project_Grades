class Person:

    def __init__(self, person_id, name):
        self._person_id = str(person_id)
        self._name = name

    def get_id(self):
        return self._person_id

    def get_name(self):
        return self._name

    def short_info(self):
        return self._person_id + " - " + self._name

    def __str__(self):
        return self.short_info()
