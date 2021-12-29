# This is a sample Python script.
from checker.internet.TwoHundredResponseChecker import TwoHundredResponseChecker
from consequence.powersocket.FourThreeThreeMhzSocketOffOn import FourThreeThreeMhzSocketOffOn
from checkerwithconsequence.CheckerWithConsequence import CheckerWithConsequence
from scheduler.TimeDelayScheduler import TimeDelayScheduler

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    checker = TwoHundredResponseChecker(['8.8.8.8', '8.8.4.4', '1.1.1.1'])
    consequence = FourThreeThreeMhzSocketOffOn('someSocket', 5)
    checker_with_consequence = CheckerWithConsequence(checker, consequence)
    scheduler = TimeDelayScheduler(checker_with_consequence, delay=30)
    scheduler.run()
