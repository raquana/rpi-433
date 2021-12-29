class CheckerWithConsequence:

    checker: None
    consequence: None

    def __init__(self, checker, consequence):
        self.checker = checker
        self.consequence = consequence

    def do_check(self, do_consequence=True):
        check_result = self.checker.check()
        consequence_result = None
        if (not check_result) & do_consequence:
            consequence_result = self.consequence.execute()

        return check_result, consequence_result
