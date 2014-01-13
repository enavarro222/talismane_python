#!/usr/bin/env python
#-*- coding:utf-8 -*-
""" This python module propose a simple wrapper to Talismane syntax analyzer.

Talismane is run in a different thread and the communication with python is
made through stdin/stdout.
"""
__author__ = "Emmanuel Navarro <enavarro222@gmail.com>"
__copyright__ = "Copyright (c) 2012 Emmanuel Navarro"
__license__ = "GNU Affero General Public License, version >= 3"
__version__ = "0.1"

import time
import sys, os
import logging
import subprocess
import threading
from Queue import Queue, Empty

def pipe_writer(pipe, text):
    try:
        pipe.write(text)
        if text[-1] != '\n':
            pipe.write("\n")
        pipe.write("\f\f\n")
        pipe.flush()
    except:
        raise

def pipe_reader(pipe, queue):
    for line in iter(pipe.readline, b''):
        queue.put(line)


class Talismane():
    """ Small Talismane wrapper.

    For more information about Talismane see:
    * https://github.com/urieli/talismane
    * http://redac.univ-tlse2.fr/applications/talismane.html
    """

    def __init__(self, talismane_jar):
        self.talismane_jar = talismane_jar
        self._logger = logging.getLogger("Talismane")
        # internal variables used to communicate with talismane
        self._tm_process = None
        self._tm_reader = None
        self._tm_output = None
        if not os.path.isfile(talismane_jar):
            raise ValueError("The indicated talismane jar file doesn't exist !")
        self._start_process()

    def _start_process(self):
        """ Start Talismane process.
        Internal use.
        """
        #cmd: $ java -Xmx1G -jar talismane.jar command=analyse
        talismane_cmd = ["java"]
        talismane_cmd.append("-Xmx1G") #TODO: add an option for Talismane available ram
        talismane_cmd.append("-jar")
        talismane_cmd.append(self.talismane_jar)
        talismane_cmd.append("command=analyse")
        try:
            self._tm_process = subprocess.Popen(
                talismane_cmd, # Use a list of params in place of a string.
                bufsize=0,     # Not buffered to retrieve data asap from Talismane
                stdin=subprocess.PIPE,  # Get a pipe to write input data
                stdout=subprocess.PIPE, # Get a pipe to read processing results
            )
            time.sleep(2)
            self._logger.info("Started Talismane from command: %r", " ".join(talismane_cmd))
            self._tm_output = Queue()
            # starts the reader of Talismane output
            self._tm_reader = threading.Thread(
                                target=pipe_reader,
                                args=(self._tm_process.stdout, self._tm_output)
                            )
            self._tm_reader.daemon = True # thread dies with the program
            self._tm_reader.start()
        except:
            self._logger.error("Failure to start Talismane with: %r", \
                                " ".join(talismane_cmd), exc_info=True)
            raise

    def __del__ (self) :
        """ Wrapper to be deleted.
        Cut links with Talismane process.
        """
        if self._tm_process:
            self._tm_process.terminate()

    def analyse(self, texte):
        """ Make the given text analyzed by Talismane
        """
        writer = threading.Thread(
                target=pipe_writer,
                args=(self._tm_process.stdin, texte)
              )
        writer.start()
        res = []
        get_results = False # True when the results starts to be read
        result_end = False  # True when all the results have been readed
        previous_line = None
        while not result_end:
            try:
                line = self._tm_output.get_nowait()
            except Empty:
                # Result not yet available, wait please
                time.sleep(0.2)
                continue
            if get_results and line == "\n" and previous_line == "\n":
                result_end = True
            else:
                previous_line = line
            line = line.strip()
            if line:
                get_results = True
                token = line.split("\t")
                res.append(token)
        # Synchronize to avoid possible problems.
        writer.join()
        return res


def main():
    from optparse import OptionParser
    usage = """usage: %prog [options]"""

    parser = OptionParser(usage=usage)
    # Wikipedia 
    parser.add_option("-t", "--talismane-jar", action="store", type=str,
        default='talismane.jar', dest="talismane_jar",  help="path to the Talismane jar")

    (options, args) = parser.parse_args()
    if len(args) != 0:
        parser.error("You should provide no arguments")

    # setup logging
    logging_level = logging.DEBUG
    logger = logging.getLogger('Talismane')
    logger.setLevel(logging_level)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging_level)
    # create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(name)s:%(message)s")
    ch.setFormatter(formatter)
    # add the handlers to the logger
    logger.addHandler(ch)

    # Run examples
    try:
        tm = Talismane(options.talismane_jar)
    except ValueError as e:
        print("Erreur: %s" % e)
        return 1
    print("--1--")
    res = tm.analyse("Je déguste du python.")
    for token in res:
        print("%s" % token)

    print("--2--")
    res = tm.analyse("Il danse la Java, mais le python ne vas pas lui offrir des perles ou des rubis pour noel. En voila une autre phrase !")
    for token in res:
        print("%s" % token)

    return 0

if __name__ == '__main__':
    sys.exit(main())
