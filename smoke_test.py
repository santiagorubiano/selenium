from unittest import TestLoader, TestSuite, runner
from pyunitreport import HTMLTestRunner
from assertions import AssertionsTest
from searchtest import SearchTest

Assertions_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([Assertions_test,search_test])


kwargs = {
    "output":'smoke-repot'
    
}
runner= HTMLTestRunner(**kwargs)
runner.run(smoke_test)