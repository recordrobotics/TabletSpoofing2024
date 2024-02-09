import vgamepad as vg

import time

gamepad = vg.VX360Gamepad()




def setLeftJoystickXY(x, y):
    '''
    Spoof joystick input for x, y (float from -1 to 1)
    ??? is this true: Unfortunately, driverstation rounds to nearest hundreth, meaning less precision. This means a tolerance of about 3 inches
    '''
    gamepad.left_joystick_float(x, -y) # negative is intentional, I think it is reversed in driverstation
    gamepad.update()  # send the updated state to the computer


def press_A():
    '''
    Spoof joystick A button press
    '''
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()  # send the updated state to the computer


def release_A():
    '''
    Spoof joystick A button release
    '''
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()  # send the updated state to the computer



if __name__ == "__main__":

    input()

    time.sleep(3)
    gamepad.left_joystick_float(-0.75, 0.75)
    gamepad.update()  # send the updated state to the computer

    input()
    exit()

    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # press the A button
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # press the left hat button

    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # press the left hat button
    gamepad.update()  # send the updated state to the computer

    # (...) A and left hat are pressed...

    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # release the A button
    gamepad.update()  # send the updated state to the computer

    # (...) left hat is still pressed...

    input()


    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT)  # press the left hat button

    gamepad.left_joystick_float(-0.75, 0.75)
    gamepad.update()  # send the updated state to the computer

    # (...) A and left hat are pressed...

    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)  # release the A button

    gamepad.update()  # send the updated state to the computer


