# coding=utf-8
import unittest
import testsuites
from testsuites.test_baidu_search import BaiduSearch
from testsuites.test_get_page_title import GetPageTitle

suite = unittest.TestSuite()
suite.addTest(BaiduSearch('test_baidu_search'))
#suite.addTest(BaiduSearch('test_search2'))
suite.addTest(GetPageTitle('test_get_title'))

if __name__ == '__main__':
    # 执行用例
    runner = unittest.TextTestRunner()
    runner.run(suite)