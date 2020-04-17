#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Int16
import cv2


def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        print ("Type something valid!")
        return False


def talker():

    pub_f = rospy.Publisher('/car/forward', Int16, queue_size=1)
    pub_b = rospy.Publisher('/car/backward', Int16, queue_size=1)
    pub_l = rospy.Publisher('/car/left', Int16, queue_size=1)
    pub_r = rospy.Publisher('/car/right', Int16, queue_size=1)

    rospy.init_node('talker', anonymous=True)
    # rate = rospy.Rate(10)  # 10hz

    pwm = 300

    print("Give direction...")
    while not rospy.is_shutdown():

        input_key = cv2.waitKey(250)

        if input_key == 2490368:
            print(u" \u2191 at " + str(pwm))
            pub_f.publish(pwm)
            pub_b.publish(0)
            pub_l.publish(0)
            pub_r.publish(0)

        elif input_key == 2621440:
            print(u" \u2193  at " + str(pwm))
            pub_f.publish(0)
            pub_b.publish(pwm)
            pub_l.publish(0)
            pub_r.publish(0)

        elif input_key == 2424832:
            print(u" \u2190  at " + str(pwm))
            pub_f.publish(0)
            pub_b.publish(0)
            pub_l.publish(pwm)
            pub_r.publish(0)

        elif input_key == 2555904:
            print(u" \u2192  at " + str(pwm))
            pub_f.publish(0)
            pub_b.publish(0)
            pub_l.publish(0)
            pub_r.publish(pwm)

        elif input_key == 't':
            print ("Terminating...")
            return

        elif input_key == 'p':
            pwm_input = raw_input("Type new PWM value...")
            if is_number(pwm_input):
                print("Changing PWM to " + pwm_input)
                pwm = int(pwm_input)

        else:
            pub_f.publish(0)
            pub_b.publish(0)
            pub_l.publish(0)
            pub_r.publish(0)


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
