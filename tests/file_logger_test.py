#!/usr/bin/python3
""" file_logger_test.py:   
""" 

# Import Required Libraries (Standard, Third Party, Local) ****************************************
import logging
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath('..'))
from file_logger.file_logger import setup_log_files, setup_log_handlers, setup_logging


# Define test class *******************************************************************************
class TestFileLogger(unittest.TestCase):
    def setUp(self):
        pass


    def test_setup_log_files(self):
        self.debug_file, self.info_file = setup_log_files(__file__)
        self.assertEqual(self.debug_file, "c:/python_logs/file_logger_test_debug.log")
        self.assertEqual(self.info_file, "c:/python_logs/file_logger_test_info.log")


    def test_setup_log_handlers(self):
        self.debug_file, self.info_file = setup_log_files(__file__)
        self.logger = setup_log_handlers(__file__, self.debug_file, self.info_file)
        self.assertEqual(len(self.logger.handlers), 3)


    def test_setup_logging(self):
        self.logger = setup_logging(__file__)
        self.assertEqual(len(self.logger.handlers), 3)



if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout)
    logger = logging.getLogger(__name__)
    logger.level = logging.DEBUG
    unittest.main() 
