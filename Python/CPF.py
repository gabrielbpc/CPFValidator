from typing import List

class CPF():
    def validate(self, doc: str = ''):
        """Validar CPF."""
        doc = list(self._only_digits(doc))

        if len(doc) != 11:
            return False

        if self._check_repeated_digits(doc):
            return False

        return self._generate_first_digit(doc) == doc[9]\
               and self._generate_second_digit(doc) == doc[10]

    def _only_digits(self, doc: str = ''):
        return "".join([x for x in doc if x.isdigit()])

    def mask(self, doc: str = ''):
        return "{}.{}.{}-{}".format(doc[:3], doc[3:6], doc[6:9], doc[-2:])

    def _generate_first_digit(self, doc: list):
        sum = 0

        for i in range(10, 1, -1):
            sum += int(doc[10 - i]) * i

        sum = (sum * 10) % 11

        if sum == 10:
            sum = 0

        return str(sum)

    def _generate_second_digit(self, doc: list):
        sum = 0

        for i in range(11, 1, -1):
            sum += int(doc[11-i]) * i

        sum = (sum * 10) % 11

        if sum == 10:
            sum = 0

        return str(sum)

    def _check_repeated_digits(self, doc: List[str]):
        return len(set(doc)) == 1
