from cv_operations import take_photo
from ui_interface import invok_ui

if '__main__' == __name__:
    callback = lambda name: take_photo(name)
    invok_ui(callback)