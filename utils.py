#!/usr/bin/env python

import logging
import sys

def is_ascii(s):
    return all(ord(c) < 128 and ord(c) > 0 for c in s)

def is_string(s):
    try:
        return isinstance(s, basestring)
    except NameError:  # Silence Pyflakes warning
        raise

def str_to_bytes(s):
    return s

def bytes_to_str(s, errors='strict'):
    return s

def write_str(f, msg):
    f.write(msg)

def read_line(f):
    return f.readline()

def next(it):
    return it.next()

class Logger(object):
    def parse_verbose(self, verbose):
        if verbose > 0:
            return logging.DEBUG
        else:
            return logging.INFO

    def create_log_file(self, environment, name, path, verbosity):
        log_file = logging.getLogger(name)
        file_handler = logging.FileHandler(path)
        log_fmt = logging.Formatter("%(asctime)s [%(levelname)-5.5s]  %(message)s")
        file_handler.setFormatter(log_fmt)
        log_file.addHandler(file_handler)
        log_file.setLevel(verbosity)
        return log_file

    def __init__(self, environment):
        self.environment = environment
        self.loggers = []
        stderr_log = logging.getLogger('git_multimail.stderr')

        class EncodedStderr():
            def write(self, x):
                write_str(sys.stderr, x)

        stderr_handler = logging.StreamHandler(EncodedStderr())
        stderr_log.addHandler(stderr_handler)
        stderr_log.setLevel(self.parse_verbose(environment.verbose))
        self.loggers.append(stderr_log)

        if environment.debug_log_file is not None:
            debug_log_file = self.create_log_file(
                environment, 'git_multimail.debug', environment.debug_log_file, logging.DEBUG)
            self.loggers.append(debug_log_file)

        if environment.log_file is not None:
            log_file = self.create_log_file(
                environment, 'git_multimail.file', environment.log_file, logging.INFO)
            self.loggers.append(log_file)

        if environment.error_log_file is not None:
            error_log_file = self.create_log_file(
                environment, 'git_multimail.error', environment.error_log_file, logging.ERROR)
            self.loggers.append(error_log_file)

    def info(self, msg):
        for l in self.loggers:
            l.info(msg)

    def debug(self, msg):
        for l in self.loggers:
            l.debug(msg)

    def warning(self, msg):
        for l in self.loggers:
            l.warning(msg)

    def error(self, msg):
        for l in self.loggers:
            l.error(msg)
