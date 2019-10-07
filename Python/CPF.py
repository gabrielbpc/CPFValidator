from typing import List

class CPF():
    def mask(self, document: str = ''):
        return "{}.{}.{}-{}".format(document[:3], document[3:6], document[6:9], document[-2:])

    def validate(self, document: str = ''):
        document = list(self._hasOnlyDigits(document))

        if len(document) != 11:
            return False

        if self._hasRepeatedDigits(document):
            return False

        return self._getFirstDigit(document) == document[9]\
               and self._getSecondDigit(document) == document[10]

    def _hasOnlyDigits(self, document: str = ''):
        return "".join([x for x in document if x.isdigit()])

    def _hasRepeatedDigits(self, document: List[str]):
        return len(set(document)) == 1

    def _getFirstDigit(self, document: list):
        sum = 0

        for i in range(10, 1, -1):
            sum += int(document[10 - i]) * i

        sum = (sum * 10) % 11

        if sum == 10:
            sum = 0

        return str(sum)

    def _getSecondDigit(self, document: list):
        sum = 0

        for i in range(11, 1, -1):
            sum += int(document[11-i]) * i

        sum = (sum * 10) % 11

        if sum == 10:
            sum = 0

        return str(sum)
