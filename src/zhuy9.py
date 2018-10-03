"""
  Capstone Project.  Code written by Yuchen Zhu.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs tests. """
    run_tests()


def run_tests():
    """ Runs various tests. """
    run_test_go_stop()
    run_test_turn_for_N_seconds()

def run_test_go_stop():
    """ Tests the   go   and   stop   Snatch3rRobot methods. """
    robot = rb.Snatch3rRobot()

    robot.go(50, 25)
    time.sleep(2)
    robot.stop()

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())
    robot.left_wheel.reset_degrees_spun(0)

    time.sleep(2)

    robot.go(100, 100)
    time.sleep(3)
    robot.stop(rb.StopAction.COAST.value)

    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())

def run_test_turn_for_N_seconds():
    robot = rb.Snatch3rRobot()
    robot.right_wheel.turn("clockwise",10, 5)
    print(robot.right_wheel.get_degrees_spun())
    print(robot.left_wheel.get_degrees_spun())

main()
