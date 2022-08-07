#!/usr/bin/python3




from jk_version import *
from jk_testing import *




#
# Successes
#


@TestCase()
def test_0(ctx):
	vA = Version("1.2.3")
	vB = Version("1.2.3")

	Assert.isEqual(vA, vB)
	Assert.isEqual(vA.__hash__(), vB.__hash__())
#

@TestCase()
def test_1(ctx):
	vA = Version("1.2.3")
	vB = Version("1.2.4")

	Assert.isNotEqual(vA, vB)
	Assert.isInstance(vA.__hash__(), int)
	Assert.isInstance(vB.__hash__(), int)
	Assert.isNotEqual(vA.__hash__(), vB.__hash__())
#



################################################################################################################################



testDriver = TestDriver()

results = testDriver.runTests([
	test_0,
	test_1,
])

#reporter = TestReporterHTML()
#reporter.report(results)
#reporter.report(results, webbrowserType="chromium")











